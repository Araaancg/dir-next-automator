import os
import shutil
from funcs import *

fileRoutes = ['module','page','layout']
fileComponents = ["template","functional","module"]

# FUNCIONES
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

def createRouteFiles(routeName, fileNames, path):
    routeName = capitalizeCamelCase(routeName)
    for name in fileNames:
        if name == "module":
            writeTxt(f'{routeName}.txt',"")
            changeExtension(f'{routeName}.txt', 'scss', module=True)
            shutil.move(f'./{routeName}.module.scss',f'{path}/{routeName}.module.scss')
        else:
            writeTxt(f'{name}.txt', writeText(routeName, name))
            changeExtension(f'{name}.txt', 'tsx')
            shutil.move(f'./{name}.tsx',f'{path}/{name}.tsx')
    return True

def createRoutes(routeList, folderPath):
    for route in routeList:
        path = f'{folderPath}/{route["name"].lower()}'
        os.makedirs(path)
        createRouteFiles(route["fallback-name"] if route.get('fallback-name') else route['name'], fileRoutes, path)
        if route["subroutes"]:
            createRoutes(route["subroutes"], path)
    return True

def createComponentsFiles(cName, fileNames, path):
    for fileType in fileNames:
        if fileType == "module":
            writeTxt(f'{cName}.txt',"")
            changeExtension(f'{cName}.txt', 'scss', module=True)
            shutil.move(f'./{cName}.module.scss',f'{path}/{cName}.module.scss') 
        elif fileType == "template":
            writeTxt(f'{cName}.txt', writeText(cName, fileType))
            changeExtension(f'{cName}.txt', 'tsx', template=True)
            shutil.move(f'./{cName}.template.tsx',f'{path}/{cName}.template.tsx')
        else:
            writeTxt(f'{cName}.txt', writeText(cName, fileType))
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

def createAllFiles(projectPath):
    # PASO 1: crear carpeta /componentes dentro de /src
    print(projectPath)
    os.makedirs(f'{projectPath}/components')

    # PASO 2: CREAMOS LOS ARCHIVOS BÁSICOS PARA ./app
    #  - page.tsx
    #  - layout.tsx
    #  - Home.module.scss
    
    # PASO 3: CREAMOS LAS CARPETAS DE RUTAS
    toCreate = getJson("./toCreate.json")
    routesToCreate = toCreate["routes"]
    folderRoutes = f"{projectPath}/app"  
    createRoutes(routesToCreate, folderRoutes)

    # PASO 4: CREAMOS LAS CARPETAS DE RUTAS
    # componentsToCreate = toCreate["components"]
    # compPath = f"{projectPath}/components"
    # createComponents(componentsToCreate,compPath)

