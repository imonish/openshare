import json
from pathlib import Path
from scanner import is_valid_image

BASE_DIR = Path(__file__).resolve().parent.parent
SCAN_QUEUE = BASE_DIR / "queues" / "scan_queue.json"
FACE_QUEUE = BASE_DIR / "queues" / "face_queue.json"

print("📸 PhotoScanner started")

# Load scan queue
with open(SCAN_QUEUE, "r") as f:
    scan_jobs = json.load(f)

face_jobs = []

for job in scan_jobs:
    print(f"🔍 Scanning job: {job.get('job_id')}")

    valid_images = []
    for img in job.get("images", []):
        if is_valid_image(img):
            valid_images.append(img)

    if valid_images:
        job["images"] = valid_images
        job["status"] = "SAFE"
        face_jobs.append(job)
        print(f"✅ Job marked SAFE ({len(valid_images)} images)")
    else:
        job["status"] = "FAILED"
        print("❌ No valid images found")

# Write to face queue
with open(FACE_QUEUE, "w") as f:
    json.dump(face_jobs, f, indent=2)

print("🚀 PhotoScanner finished")
