import tkinter as tk
# from tkinter import PhotoImage
from createFiles import createAllFiles
from funcs import * 

toCreate = {
    "routes":[],
    "components":{}
}

'''
TO DO: 
- when confirm new route -> update the toCreate dict
- give delete route button a function
- try execute the programm and check that the route section works
- please organise the functions and factorize
'''

def getValueFromInput(input):
    route = input.get()
    return route

def getEntryValue():
    entryValue = getValueFromInput(inputChooseFolder)
    labelFeedbackChooseFolder.config(text='project route: ' + entryValue)
    writeTxt("projectRoute.txt", entryValue)

def executeProgram():
    try: 
        route = getValueFromInput(inputChooseFolder)
        createAllFiles(f'{route}/src')
        labelExecutionFeedback.config(text='files created successfully')
    except Exception as e:
        print(e)

def confirmRoute(input, btnConfirm):
    input.config(state='disable')
    btnConfirm.config(text='delete')

def addNewRoute(widgetList, button):
    newInput = tk.Entry(root, width=30)
    newInput.pack(before=button)
    buttonConfirmRoute = tk.Button(root, text='confirm', command=lambda: confirmRoute(newInput, buttonConfirmRoute))
    buttonConfirmRoute.pack(before=button)
    widgetList.append(newInput)

root = tk.Tk()

inputList = []

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
buttonAddNewRoute = tk.Button(root, text='add new route', command=lambda: addNewRoute(inputList, buttonAddNewRoute))

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

buttonAddNewRoute.pack()

root.mainloop()