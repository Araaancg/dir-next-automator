import tkinter as tk
from tkinter import PhotoImage
from createFiles import createAllFiles 

def getRoute():
    route = inputChooseFolder.get()
    return route

def getEntryValue():
    entryValue = getRoute()
    labelFeedbackChooseFolder.config(text='entry value: ' + entryValue)

    with open("projectRoute.txt", "w") as file:
        file.write(entryValue)

def executeProgram():
    try: 
        route = getRoute()
        createAllFiles(f'{route}/src')
        labelExecutionFeedback.config(text='files created successfully')
    except Exception as e:
        print(e)

def confirmAppRoute():
    inputText = inputAppRoute.get()
    inputAppRoute.destroy()
    labelConfirmAppRoute = tk.Label(root, text=inputText)
    labelConfirmAppRoute.pack()



root = tk.Tk()
checkIcon = PhotoImage(file='./icons/check.png')

# size
root.geometry("550x320")

# put a title to the window
root.title('next-project-initiator')

# label and input - choose folder
labelChooseFolder = tk.Label(root, text='choose a project folder')
inputChooseFolder = tk.Entry(root)

# button to get input value
buttonChooseFolder = tk.Button(root, text='save', command=getEntryValue)

# label to check if entry was received
labelFeedbackChooseFolder = tk.Label(root, text='')

# button execute file creation
buttonCreateFiles = tk.Button(root, text='Create Files', command=executeProgram)

# execution feedback
labelExecutionFeedback = tk.Label(root, text='')

# apps input
inputAppRoute = tk.Entry(root)
buttonConfirmRoute = tk.Button(root, text='confirm', image=checkIcon, command=confirmAppRoute)


try:
    with open("projectRoute.txt", "r") as file:
        savedValue = file.read()
        inputChooseFolder.insert(0, savedValue)
except FileNotFoundError:
    pass

# pack everything
labelChooseFolder.pack()
inputChooseFolder.pack()
labelFeedbackChooseFolder.pack()
buttonChooseFolder.pack()
buttonCreateFiles.pack()
labelExecutionFeedback.pack()

inputAppRoute.pack()
buttonConfirmRoute.pack()

root.mainloop()