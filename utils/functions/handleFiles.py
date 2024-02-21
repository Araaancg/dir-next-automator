# HANDLING ALL THAT HAS TO DO WITH FOLDERS AND FILES

import os
from assets.getFileContent import getFileContent


# create folders
# get data for different files, page.tsx, layout.tsx, route.tsx, component.tsx, component.scss, styles.scss
# see if folders have any subpaths and iterate through them

'''
TYPES OF FILES
- page.tsx
- layout.tsx
- component.template.tsx -> if its not divided, we would omit the .template
- component.ts -> if its not divided, we would't use it
- styles.scss - nothing written on it
- route.tsx - nothing written on it
'''

def iterateProjectStructure(estructure, proyectPath):
    try:
        for item in estructure:
            if item["type"] == "folder": # handle folders
                createFolder(proyectPath, item["name"]) # create them
                if item.get("subpaths"):
                    newPath = os.path.join(proyectPath, item["name"])
                    iterateProjectStructure(item["subpaths"], newPath)

            elif item["type"] == "file": # handle single files
                createFile(proyectPath, item["name"], item["extension"]) # create them

            elif item["type"] == "component":
                createFolder(proyectPath, item["name"]) # create them

            elif item["type"] == "page":
                createPage(proyectPath, item["name"]) # create them
            
            elif item["type"] == "route":
                createRoute(proyectPath, item["name"]) # create them
                
            
        return True
    except:
        return False

def createFolder(path, name):
    folderPath = os.path.join(path, name)
    try:
        print(folderPath)
        os.makedirs(folderPath)
        print(f"Folder '{name}' succesfully created at '{folderPath}'.")
    except FileExistsError:
        print(f"Folder '{name}' already exists at '{folderPath}'.")
    return folderPath

def createFile(path, name, extension, content=''):
    file_path = os.path.join(path, f"{name}.{extension}")
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"File '{name}.{extension}' created in '{path}'.")
    except Exception as e:
        print(f"Error creating file: {e}")
    return file_path 

def createComponent(path, name):
    # componentPath = os.path.join(path, name)
    createFolder(path, name)

def createPage(path, name):
    pagePath = os.path.join(path, name)
    createFolder(path, name)

    pageContent = getFileContent(name, "page")
    layoutContent = getFileContent(name, "layout")
    createFile(pagePath, "page", "tsx", pageContent)
    createFile(pagePath, "layout", "tsx", layoutContent)


def createRoute(path, name):
    createFolder(path, name)
    routePath = os.path.join(path, name)
    createFile(routePath, "route", "tsx")