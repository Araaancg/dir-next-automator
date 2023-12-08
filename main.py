import os
import json
import shutil

# proyectPath = "../change-the-block/web_v3/src"
proyectPath = ''

# FUNCIONES
def getData(jsonFile):
    with open(jsonFile, encoding="utf8") as file:
        return json.load(file)

def createFile(fileName, text):
    file = open(fileName, 'w')
    if text:
        file.write(text)
    file.close()

def capitalizeCamelCase(str):
    newStr = "".join([a.capitalize() for a in str.split("-")])
    return newStr

def changeExtension(fileName, newExtension, **fileType):
    if fileType.get("module"):
        os.rename(fileName, f'{fileName.split(".")[0]}.module.{newExtension}')
    elif fileType.get("template"):
        os.rename(fileName, f'{fileName.split(".")[0]}.template.{newExtension}')
    else:
        os.rename(fileName, f'{fileName.split(".")[0]}.{newExtension}')

def writeText(name, fileType):
    if fileType == "page":
        return 'import styles from "./' + name + '.module.scss"; export default function ' + name +'():JSX.Element {return (<main><p>' + name + '</p></main>)}'
    elif fileType == "layout":
        return 'export default function RootLayout({children,}: {children: React.ReactNode;}): JSX.Element {return <main className="' + name + '-main-container">{ children }</main>;}'
    elif fileType == "functional":
        return 'import Template' + name + ' from "./' + name + '.template";const ' + name + ' =()=>{ return Template' + name + '();};export default ' + name + ';'
    elif fileType == "template":
        return 'import React from "react";import styles from "./' + name + '.module.scss";const Template' + name + ' = (): JSX.Element => {return <div></div>;};export default Template' + name + ';'

# PASO 1: CREAR CARPETA /src
# dentro de la carpeta, crear carpeta 'componentes'

os.makedirs(f'{proyectPath}/components')

# PASO 2: CREAMOS LOS ARCHIVOS BÁSICOS PARA ./app
#  - page.tsx
#  - layout.tsx
#  - Home.module.scss

fileRoutes = ['module','page','layout']
def createRouteFiles(routeName, fileNames, path):
    routeName = capitalizeCamelCase(routeName)
    for name in fileNames:
        if name == "module":
            createFile(f'{routeName}.txt',"")
            changeExtension(f'{routeName}.txt', 'scss', module=True)
            shutil.move(f'./{routeName}.module.scss',f'{path}/{routeName}.module.scss')
        else:
            createFile(f'{name}.txt', writeText(routeName, name))
            changeExtension(f'{name}.txt', 'tsx')
            shutil.move(f'./{name}.tsx',f'{path}/{name}.tsx')
    return True

# PASO 3: CREAMOS LAS CARPETAS DE RUTAS

toCreate = getData("./toCreate.json")

routesToCreate = toCreate["routes"]
folderRoutes = f"{proyectPath}/app"

def createRoutes(routeList, folderPath):
    for route in routeList:
        path = f'{folderPath}/{route["name"].lower()}'
        os.makedirs(path)
        createRouteFiles(route["fallback-name"] if route.get('fallback-name') else route['name'], fileRoutes, path)
        if route["subroutes"]:
            createRoutes(route["subroutes"], path)
    return True

createRoutes(routesToCreate, folderRoutes)

# PASO 4: CREAMOS LAS CARPETAS DE RUTAS

componentsToCreate = toCreate["components"]
compPath = f"{proyectPath}/components"
fileComponents = ["template","functional","module"]

def createComponentsFiles(cName, fileNames, path):
    for fileType in fileNames:
        if fileType == "module":
            createFile(f'{cName}.txt',"")
            changeExtension(f'{cName}.txt', 'scss', module=True)
            shutil.move(f'./{cName}.module.scss',f'{path}/{cName}.module.scss') 
        elif fileType == "template":
            createFile(f'{cName}.txt', writeText(cName, fileType))
            changeExtension(f'{cName}.txt', 'tsx', template=True)
            shutil.move(f'./{cName}.template.tsx',f'{path}/{cName}.template.tsx')
        else:
            createFile(f'{cName}.txt', writeText(cName, fileType))
            changeExtension(f'{cName}.txt', 'ts')
            shutil.move(f'./{cName}.ts',f'{path}/{cName}.ts')
    return True

def createComponents(compList, folderPath):
    for k, v in compList.items():
        path = f'{folderPath}/{k}'
        os.makedirs(path)
        for c in v:
            cPath = f'{path}/{c}'
            os.makedirs(cPath)
            createComponentsFiles(c, fileComponents, f"{path}/{c}")
    return True

createComponents(componentsToCreate,compPath)
