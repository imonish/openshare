import sqlite3

DB_PATH = "vision_engine/db.sqlite3"

def save_face(uid: str, image_path: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO faces (uid, image_path) VALUES (?, ?)",
        (uid, image_path)
    )

    conn.commit()
    conn.close()
