import cv2

# Load OpenCV Haar Cascade for face detection
FACE_CASCADE = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def detect_faces(image_path: str):
    """
    Detect faces in an image.
    Returns list of face boxes and the original image.
    """
    img = cv2.imread(image_path)

    if img is None:
        return [], None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = FACE_CASCADE.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    return faces, img
