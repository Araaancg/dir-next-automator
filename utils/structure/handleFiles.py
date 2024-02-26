# HANDLING ALL THAT HAS TO DO WITH FOLDERS AND FILES

import os
import shutil
from utils.structure.getFileContent import getFileContent
from utils.structure.toCamelCase import toCamelCase
from routes import ASSETS_PATH

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
                folderPath = os.path.join(proyectPath, item["name"])
                createFolder(folderPath) # create them
                if item["name"] == "app":
                    copyBasicFiles(f"{ASSETS_PATH}\\code", folderPath)

            elif item["type"] == "file": # handle single files
                fileName = item["name"].split(".")[0]
                fileExtension = item["name"].split(".")[1]
                createFile(proyectPath, fileName, fileExtension) # create them

            elif item["type"] == "component":
                createComponent(proyectPath, item["name"], divided=item.get("divided"), addStyles=item.get("css")) # create them

            elif item["type"] == "page":
                createPage(proyectPath, item["name"], addPage=item.get("page"), addLayout=item.get("layout"), addStyles=item.get("css"), isDynamic=item.get("dynamic")) # create them
            
            elif item["type"] == "route":
                createRoute(proyectPath, item["name"]) # create them
            
            if item.get("subpaths"):
                newPath = os.path.join(proyectPath, f"[{item["name"]}]") if (item["type"] == "page" and item["dynamic"]) else os.path.join(proyectPath, item["name"])
                iterateProjectStructure(item["subpaths"], newPath)
        return True
    except:
        return False

def createFolder(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        print(f"Folder '{path}' already exists.")
    return path

def createFile(path, name, extension, content=''):
    filePath = os.path.join(path, f"{name}.{extension}")
    try:
        with open(filePath, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"Error creating file: {e}")
    return filePath 

def createComponent(path, name, divided, addStyles):
    componentPath = os.path.join(path, name)
    createFolder(componentPath)
    if divided:
        templateContent = getFileContent(name, "template", css=addStyles)
        functionalContent = getFileContent(name, "functional")
        createFile(componentPath, f"{name}Template.template", "tsx", templateContent)
        createFile(componentPath, f"{name}", "ts", functionalContent)
    else:
        componentContent = getFileContent(name, "fullComponent", css=addStyles)
        createFile(componentPath, name, "tsx", componentContent)
    if addStyles:
        createFile(componentPath, toCamelCase(name, False), "scss")

def createPage(path, name, addPage, addLayout, addStyles, isDynamic):
    pagePath = os.path.join(path, f"[{name}]") if isDynamic else os.path.join(path, name)
    
    createFolder(pagePath)
    if addPage:
        pageContent = getFileContent(name, "page", css=addStyles)
        createFile(pagePath, "page", "tsx", pageContent)
    if addLayout:
        layoutContent = getFileContent(name, "layout")
        createFile(pagePath, "layout", "tsx", layoutContent)
    if addStyles:
        createFile(pagePath, toCamelCase(name, False), "scss")

def createRoute(path, name):
    routePath = os.path.join(path, name)
    createFolder(routePath)
    createFile(routePath, "route", "tsx")

def copyBasicFiles(sourceFolder, destinationFolder):
    os.makedirs(destinationFolder, exist_ok=True)
    for filename in os.listdir(sourceFolder):
        sourcePath = os.path.join(sourceFolder, filename)
        destinationPath = os.path.join(destinationFolder, filename)

        if os.path.isfile(sourcePath):
            shutil.copy2(sourcePath, destinationPath)
