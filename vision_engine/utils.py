import os

def delete_files(paths):
    for path in paths:
        if path and os.path.exists(path):
            os.remove(path)
