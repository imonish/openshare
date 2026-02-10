import cv2
import numpy as np

def get_simple_embedding(image_path: str):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        return None

    img = cv2.resize(img, (100, 100))
    img = img.flatten().astype("float32")
    img /= 255.0

    return img
