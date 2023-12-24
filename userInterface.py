import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
# from tkinter import messagebox
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
    labelFeedbackChooseFolder.config(text='Selected folder: ' + entryValue)
    writeTxt("projectRoute.txt", entryValue)

def executeProgram(confirmationWindow):
    try: 
        writeJson(toCreate, './toCreate.json')
        route = getValueFromInput(inputChooseFolder)
        createAllFiles(f'{route}/src')
        labelExecutionFeedback.config(text='files created successfully', fg=successColor)
        confirmationWindow.destroy()
        root.after(5000, root.destroy)
    except Exception as e:
        labelExecutionFeedback.config(text='something went wrong with the creation of files', fg=errorColor)
        print(e)
        confirmationWindow.destroy()

def deleteRoute(entryToDestroy, buttonToDestroy):
    entryToDestroy.destroy()
    buttonToDestroy.destroy()
    routeList.remove(entryToDestroy)

routeList = []
subrouteList = {}

def addNewRoute(button, **kwargs):
    newInput = tk.Entry(root, width=30)
    newInput.pack(before=button)

    buttonDeleteRoute = tk.Button(root, text='delete', command=lambda: deleteRoute(newInput, buttonDeleteRoute))
    buttonDeleteRoute.pack(before=button)
    routeList.append(newInput)


def exportRoutesToDict():
    for route in routeList:
        route = input.get()
        routeDict = {
            "name": route,
            "subroutes": []
        }
        toCreate['routes'].append(routeDict)

def confirmExecution():
    confirmationWindow = tk.Toplevel(root)
    confirmationWindow.title("Confirmation")

    label = tk.Label(confirmationWindow, text="Are you sure you want to execute the program?")
    label.pack(pady=10)

    cancel_button = tk.Button(confirmationWindow, text="Cancel", command=confirmationWindow.destroy)
    cancel_button.pack(side=tk.LEFT, padx=10)

    execute_button = tk.Button(confirmationWindow, text="Execute", command=lambda: executeProgram(confirmationWindow))
    execute_button.pack(side=tk.RIGHT, padx=10)

def showAppSection():
    componentsFrame.pack_forget()
    appFrame.pack()
    appButton.config(image=appBtnActiveImg)
    componentsButton.config(image=componentsBtnImg)

def showComponentsSection():
    appFrame.pack_forget()
    componentsFrame.pack()
    appButton.config(image=appBtnImg)
    componentsButton.config(image=componentsBtnActiveImg)

root = tk.Tk()
style = ttk.Style()

# size
# root.geometry("950x420")

bgColor = '#1A1A1A'
bgEntryColor = '#333333'
textColor = '#F2F2F2'
successColor = '#4CAF50'
errorColor = '#FF6666'
titleSize = ("Helvetica", 18)
textSize = ("Helvetica", 16)
smallTextSize = ("Helvetica", 10)
entryStyle = {
    'borderwidth': 0,
    'background': bgEntryColor,
    'foreground': textColor,
    'width': 50,
    'font': ('Helvetica', 16)
}

# style.configure('entryStyle', foreground=textColor, insertColor=textColor, background=bgEntryColor, padding=(10, 2))

root.configure(bg=bgColor)

# put a title to the window
root.title('next-project-initiator')

# create a h1
h1 = tk.Label(root, text='WELCOME TO NEXT PROJECT INITIATOR', bg=bgColor, fg=textColor, font=titleSize)
h1.pack(padx=24, pady=24)

##### PART 1 -> CHOOSE PROJECT FOLDER ####
chooseProjectFrame = tk.Frame(root, bg=bgColor)

# label and input - choose folder
labelChooseFolder = tk.Label(chooseProjectFrame, text='Choose a folder: ', bg=bgColor, fg=textColor, font=textSize)
inputChooseFolder = tk.Entry(chooseProjectFrame, **entryStyle)
labelChooseFolder.grid(row=0, column=0, padx=5, pady=0, columnspan=2)
inputChooseFolder.grid(row=1, column=1, padx=5, pady=0)

# label to check if entry was received
labelFeedbackChooseFolder = tk.Label(chooseProjectFrame, text=f'', bg=bgColor, fg=successColor, font=smallTextSize)
labelFeedbackChooseFolder.grid(row=2, column=0, padx=0, pady=0, columnspan=2)

# button to get input value
updateRouteImage = PhotoImage(file='./icons/update-button.png')
buttonChooseFolder = tk.Button(chooseProjectFrame, image=updateRouteImage, command=getEntryValue, borderwidth=0, background=bgColor)
buttonChooseFolder.grid(row=1, column=0, padx=5, pady=10)

chooseProjectFrame.pack()


#### PART 2 -> NAVBAR TO CHOOSE BETWEEN APP AND COMPONENTS ####
navbarFrame = tk.Frame(root, bg=bgColor, pady=50)
appFrame = tk.Frame(root, bg=bgColor)
componentsFrame = tk.Frame(root, bg=bgColor)

navbarFrame.pack()
appBtnActiveImg = PhotoImage(file='./icons/app-button-active.png')
appBtnImg = PhotoImage(file='./icons/app-button.png')
appButton = tk.Button(navbarFrame, image=appBtnActiveImg, command=showAppSection, borderwidth=0, background=bgColor, width=150)
appButton.grid(row=0, column=0, padx=10, pady=0)

componentsBtnActiveImg = PhotoImage(file='./icons/components-button-active.png')
componentsBtnImg = PhotoImage(file='./icons/components-button.png')
componentsButton = tk.Button(navbarFrame, image=componentsBtnImg, command=showComponentsSection, borderwidth=0, background=bgColor, width=150)
componentsButton.grid(row=0, column=1, padx=10, pady=0)


#### PART 3 -> CREATE APP SECTION TO INTRODUCE THE ROUTES FOR THE PROJECT ####
# apps input
buttonAddNewRoute = tk.Button(appFrame, text='add new route', command=lambda: addNewRoute(buttonAddNewRoute))
buttonAddNewRoute.pack()

confirmRoutes = tk.Button(appFrame, text='confirm routes', command=exportRoutesToDict)
confirmRoutes.pack()


#### PART 4 -> CREATE COMPONENTS SECTIONS TO INTRODUCE COMPONENT'S NAME ####



#### PART 5 -> EXECUTE PROGRAMM, CONFIRM INFO, GIVE FEEDBACK AND CLOSE WINDOW ####
appFrame.pack() # by default we have app section
executeFrame = tk.Frame(root, pady=50, bg=bgColor)
executeFrame.pack(side="bottom")

# button execute file creation
executeBtnImg = PhotoImage(file='./icons/execute-button.png')
buttonCreateFiles = tk.Button(executeFrame, image=executeBtnImg, command=confirmExecution, borderwidth=0, background=bgColor)
buttonCreateFiles.pack()

# execution feedback
labelExecutionFeedback = tk.Label(executeFrame, text='', bg=bgColor)
labelExecutionFeedback.pack()


try:
    with open("projectRoute.txt", "r") as file:
        savedValue = file.read()
        inputChooseFolder.insert(0, savedValue)
        labelFeedbackChooseFolder.config(text=f'Selected folder: {savedValue}')
except FileNotFoundError:
    pass

# print(subrouteList)
root.mainloop()