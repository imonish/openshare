from vision_engine.db_postgres import delete_face
from vision_engine.utils import delete_files

face_id = 1  # ⚠️ change to an existing face_id

path = delete_face(face_id)

if path:
    delete_files([path])
    print("✅ Face deleted")
else:
    print("⚠️ Face not found")
