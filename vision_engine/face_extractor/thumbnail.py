import cv2
from pathlib import Path


def generate_thumbnail(face_dir: Path):
    """
    Select the largest face image and save it as thumbnail.jpg
    """
    face_images = list(face_dir.glob("face_*.jpg"))

    if not face_images:
        return False

    best_face = None
    max_area = 0

    for img_path in face_images:
        img = cv2.imread(str(img_path))
        if img is None:
            continue

        h, w, _ = img.shape
        area = h * w

        if area > max_area:
            max_area = area
            best_face = img

    if best_face is None:
        return False

    thumbnail_path = face_dir / "thumbnail.jpg"
    cv2.imwrite(str(thumbnail_path), best_face)
    return True
