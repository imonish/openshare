import sqlite3

conn = sqlite3.connect("vision_engine/db.sqlite3")
cursor = conn.cursor()

# -------------------------------
# Faces table (base)
# -------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS faces (
    face_id INTEGER PRIMARY KEY AUTOINCREMENT,
    uid TEXT NOT NULL,
    image_path TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# -------------------------------
# Face Groups table
# -------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS face_groups (
    group_id INTEGER PRIMARY KEY AUTOINCREMENT,
    uid TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# -------------------------------
# Alter faces table (safe way)
# -------------------------------
def add_column_safe(table, column, column_type):
    try:
        cursor.execute(
            f"ALTER TABLE {table} ADD COLUMN {column} {column_type}"
        )
        print(f"➕ Column added: {column}")
    except sqlite3.OperationalError:
        print(f"⚠️ Column already exists: {column}")

add_column_safe("faces", "group_id", "INTEGER")
add_column_safe("faces", "distance", "REAL")

conn.commit()
conn.close()

print("✅ Database initialized (PHASE 3 ready)")
