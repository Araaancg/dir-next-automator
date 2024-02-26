from tkinter import filedialog 
import os
import shutil

def moveOutputFolder(folderName, outputFolder):
    destinationDirectory = filedialog.askdirectory(title="Select destination directory")

    if destinationDirectory:
        destinationPath = os.path.join(destinationDirectory, folderName)

        # Check if the destination file already exists
        counter = 0
        while os.path.exists(destinationPath):
            # If it exists, modify the filename by adding a counter
            newFolderName = f"{folderName}({counter})" if counter != 0 else f"{folderName}"
            destinationPath = os.path.join(destinationDirectory, newFolderName)
            counter += 1
            
        shutil.move(outputFolder, destinationPath)
