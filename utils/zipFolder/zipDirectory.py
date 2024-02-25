import zipfile
import os

def zipDirectory(directoryPath, zipPath):
    with zipfile.ZipFile(zipPath, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(directoryPath):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, directoryPath)
                zipf.write(file_path, arcname=arcname)