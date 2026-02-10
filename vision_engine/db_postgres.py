import psycopg2
import pickle

# ---------------------------------
# DB connection
# ---------------------------------
def get_connection():
    return psycopg2.connect(
        dbname="openshare_vision",
        user="postgres",
        password="2006",
        host="localhost",
        port="5432"
    )

# ---------------------------------
# Group helper
# ---------------------------------
def get_or_create_group(uid):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT group_id FROM face_groups WHERE uid = %s LIMIT 1",
        (uid,)
    )
    row = cur.fetchone()

    if row:
        group_id = row[0]
    else:
        cur.execute(
            "INSERT INTO face_groups (uid) VALUES (%s) RETURNING group_id",
            (uid,)
        )
        group_id = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()
    return group_id

# ---------------------------------
# Insert face with embedding
# ---------------------------------
def insert_face(uid, image_path, group_id, distance, embedding):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO faces (
            uid,
            image_path,
            group_id,
            distance,
            simple_embedding
        )
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            uid,
            image_path,
            group_id,
            distance,
            pickle.dumps(embedding)
        )
    )

    conn.commit()
    cur.close()
    conn.close()

# ---------------------------------
# Fetch embeddings for UID
# ---------------------------------
def get_group_embeddings(uid):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT group_id, simple_embedding
        FROM faces
        WHERE uid = %s
          AND simple_embedding IS NOT NULL
        """,
        (uid,)
    )

    rows = [
        (group_id, pickle.loads(embedding))
        for group_id, embedding in cur.fetchall()
    ]

    cur.close()
    conn.close()
    return rows

# =================================================
# 🧩 DELETE OPERATIONS
# =================================================

# 🧩 2.1 Delete ONE face
def delete_face(face_id):
    conn = get_connection()
    cur = conn.cursor()

    # Get image path first
    cur.execute(
        "SELECT image_path FROM faces WHERE face_id = %s",
        (face_id,)
    )
    row = cur.fetchone()

    if not row:
        cur.close()
        conn.close()
        return None

    image_path = row[0]

    # Delete DB row
    cur.execute(
        "DELETE FROM faces WHERE face_id = %s",
        (face_id,)
    )

    conn.commit()
    cur.close()
    conn.close()

    return image_path  # caller deletes file

# 🧩 2.2 Delete ONE group
def delete_group(group_id):
    conn = get_connection()
    cur = conn.cursor()

    # Get all image paths
    cur.execute(
        "SELECT image_path FROM faces WHERE group_id = %s",
        (group_id,)
    )
    rows = cur.fetchall()

    # Delete faces
    cur.execute(
        "DELETE FROM faces WHERE group_id = %s",
        (group_id,)
    )

    # Delete group
    cur.execute(
        "DELETE FROM face_groups WHERE group_id = %s",
        (group_id,)
    )

    conn.commit()
    cur.close()
    conn.close()

    return [r[0] for r in rows]  # caller deletes files

# 🧩 2.3 Delete ALL data of one UID
def delete_uid(uid):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT image_path FROM faces WHERE uid = %s",
        (uid,)
    )
    rows = cur.fetchall()

    cur.execute(
        "DELETE FROM faces WHERE uid = %s",
        (uid,)
    )

    cur.execute(
        "DELETE FROM face_groups WHERE uid = %s",
        (uid,)
    )

    cur.execute(
        "DELETE FROM persons WHERE uid = %s",
        (uid,)
    )

    conn.commit()
    cur.close()
    conn.close()

    return [r[0] for r in rows]  # caller deletes files
