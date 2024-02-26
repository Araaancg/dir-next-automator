from utils.structure.toCamelCase import toCamelCase

def getFileContent(name, fileType, **kwargs):
    extraLine = ''
    if kwargs.get("css"):
        extraLine = f'import "./' + toCamelCase(name, False) + '.scss";'

    if fileType == "page":
        return extraLine + ';export default function ' + toCamelCase(name) + '(): JSX.Element {return (<div><h1>' + toCamelCase(name) + '</h1></div>);}'
    elif fileType == "layout":
        return 'export default function RootLayout({children}: {children: React.ReactNode;}): JSX.Element {return <div className="' + toCamelCase(name, False) + '-main-container">{ children }</div>;}'
    elif fileType == "functional":
        return 'import Template' + toCamelCase(name) + ' from "./' + toCamelCase(name) + '.template";const ' + toCamelCase(name) + ' =()=>{ return Template' + toCamelCase(name) + '();};export default ' + toCamelCase(name) + ';'
    elif fileType == "template":
        return 'import React from "react";' + extraLine + 'const Template' + toCamelCase(name) + ' = (): JSX.Element => {return <div></div>;};export default Template' + toCamelCase(name) + ';'
    elif fileType == "fullComponent":
        return 'import React from "react";' + extraLine + 'const ' + toCamelCase(name) + ' = (): JSX.Element => {return <div></div>;};export default ' + toCamelCase(name) + ';'