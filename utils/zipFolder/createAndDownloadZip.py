from utils.zipFolder.zipDirectory import zipDirectory
from tkinter import filedialog 
import os

def createAndDownloadZip(sourceDirectory, zipFilename):
    zipDirectory(sourceDirectory, zipFilename)

    # Ask the user for the destination directory to save the zip file
    destinationDirectory = filedialog.askdirectory(title="Select destination directory")

    if destinationDirectory:
        destination_path = os.path.join(destinationDirectory, zipFilename)
        os.rename(zipFilename, destination_path)
        print(f"Zip file created and saved at: {destination_path}")