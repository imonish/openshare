import cv2
from pathlib import Path


def is_valid_image(image_path: str) -> bool:
    """
    Check whether an image is readable and valid.
    """
    path = Path(image_path)

    if not path.exists():
        return False

    img = cv2.imread(str(path))
    return img is not None
