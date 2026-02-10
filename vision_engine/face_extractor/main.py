import json
import cv2
from pathlib import Path

from vision_engine.face_extractor.detector import detect_faces
from vision_engine.face_extractor.thumbnail import generate_thumbnail
from vision_engine.face_extractor.simple_embedding import get_simple_embedding
from vision_engine.face_extractor.distance import face_distance
from vision_engine.db_postgres import (
    insert_face,
    get_group_embeddings,
    get_or_create_group,
)

BASE_DIR = Path(__file__).resolve().parent.parent
FACE_QUEUE = BASE_DIR / "queues" / "face_queue.json"
DATASET_DIR = BASE_DIR.parent / "dataset"

print("🧑‍🦱 FaceExtractor started")

with open(FACE_QUEUE, "r") as f:
    jobs = json.load(f)

for job in jobs:
    uid = job["uid"]
    name = job["name"]
    images = job["images"]

    folder_name = f"{uid}_{name}"
    output_dir = DATASET_DIR / folder_name
    output_dir.mkdir(parents=True, exist_ok=True)

    face_count = 0

    for image_path in images:
        faces, img = detect_faces(image_path)

        if img is None:
            continue

        for (x, y, w, h) in faces:
            face_img = img[y:y+h, x:x+w]
            face_file = output_dir / f"face_{face_count}.jpg"

            # 0️⃣ Save face image
            cv2.imwrite(str(face_file), face_img)

            # 1️⃣ Get embedding
            embedding = get_simple_embedding(str(face_file))

            assigned_group = None
            min_distance = None

            # 2️⃣ Compare with existing embeddings
            if embedding is not None:
                groups = get_group_embeddings(uid)

                for g_id, g_embedding in groups:
                    d = face_distance(embedding, g_embedding)

                    if d < 0.5 and (min_distance is None or d < min_distance):
                        min_distance = d
                        assigned_group = g_id

            # 3️⃣ Create new group if no match
            if assigned_group is None:
                assigned_group = get_or_create_group(uid)

            # 4️⃣ Save face record
            insert_face(
                uid=uid,
                image_path=str(face_file),
                group_id=assigned_group,
                distance=min_distance,
                embedding=embedding
            )

            face_count += 1

    job["status"] = "FACE_EXTRACTED"
    print(f"✅ {face_count} faces saved for {folder_name}")

    if generate_thumbnail(output_dir):
        print("🖼️ Thumbnail generated :)")
    else:
        print("⚠️ Thumbnail not generated :(")

print("🚀 FaceExtractor finished")
