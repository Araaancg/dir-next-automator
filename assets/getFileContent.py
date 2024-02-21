def getFileContent(name, fileType):
    if fileType == "page":
        return 'import "./' + name.capitalize() + '.scss";export default function ' + name.capitalize() + '(): JSX.Element {return (<div><h1>' + name.capitalize() + '</h1></div>);}'
    elif fileType == "layout":
        return 'export default function RootLayout({children,}: {children: React.ReactNode;}): JSX.Element {return <div className="' + name.capitalize() + '-main-container">{ children }</div>;}'
    elif fileType == "functional":
        return 'import Template' + name + ' from "./' + name + '.template";const ' + name + ' =()=>{ return Template' + name + '();};export default ' + name + ';'
    elif fileType == "template":
        return 'import React from "react";import styles from "./' + name + '.module.scss";const Template' + name + ' = (): JSX.Element => {return <div></div>;};export default Template' + name + ';'