import tkinter as tk
# from tkinter import PhotoImage
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
    labelFeedbackChooseFolder.config(text='project route: ' + entryValue)
    writeTxt("projectRoute.txt", entryValue)

def executeProgram(confirmationWindow):
    try: 
        writeJson(toCreate, './toCreate.json')
        route = getValueFromInput(inputChooseFolder)
        createAllFiles(f'{route}/src')
        labelExecutionFeedback.config(text='files created successfully')
        confirmationWindow.destroy()
        root.after(5000, root.destroy)
    except Exception as e:
        labelExecutionFeedback.config(text='something went wrong with the creation of files')
        print(e)
        confirmationWindow.destroy()

def deleteRoute(entryToDestroy, buttonToDestroy):
    entryToDestroy.destroy()
    buttonToDestroy.destroy()
    inputList.remove(entryToDestroy)

inputList = []

def addNewRoute(button):
    newInput = tk.Entry(root, width=30)
    newInput.pack(before=button)

    # buttonAddSubroute = tk.Button(root, text='add subroute')
    # buttonAddSubroute.pack(before=button)

    buttonDeleteRoute = tk.Button(root, text='delete', command=lambda: deleteRoute(newInput, buttonDeleteRoute))
    buttonDeleteRoute.pack(before=button)

    inputList.append(newInput)

def exportRoutesToDict():
    for input in inputList:
        inputValue = input.get()
        routeDict = {
            "name": inputValue,
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

def showComponentsSection():
    appFrame.pack_forget()
    componentsFrame.pack()

root = tk.Tk()

# size
# root.geometry("550x320")
root.geometry("650x420")

# put a title to the window
root.title('next-project-initiator')


##### PART 1 -> CHOOSE PROJECT FOLDER ####
chooseProjectFrame = tk.Frame(root)

# label and input - choose folder
labelChooseFolder = tk.Label(chooseProjectFrame, text='choose a project folder')
inputChooseFolder = tk.Entry(chooseProjectFrame)
labelChooseFolder.pack()
inputChooseFolder.pack()

# button to get input value
buttonChooseFolder = tk.Button(chooseProjectFrame, text='save', command=getEntryValue)
buttonChooseFolder.pack()

# label to check if entry was received
labelFeedbackChooseFolder = tk.Label(chooseProjectFrame, text='')
labelFeedbackChooseFolder.pack()

chooseProjectFrame.pack()


#### PART 2 -> NAVBAR TO CHOOSE BETWEEN APP AND COMPONENTS ####
appFrame = tk.Frame(root)
componentsFrame = tk.Frame(root)

appButton = tk.Button(root, text="App", command=showAppSection)
appButton.pack()

componentsButton = tk.Button(root, text="Components", command=showComponentsSection)
componentsButton.pack()


#### PART 3 -> CREATE APP SECTION TO INTRODUCE THE ROUTES FOR THE PROJECT ####
# apps input
buttonAddNewRoute = tk.Button(appFrame, text='add new route', command=lambda: addNewRoute(buttonAddNewRoute))
buttonAddNewRoute.pack()

confirmRoutes = tk.Button(appFrame, text='confirm routes', command=exportRoutesToDict)
confirmRoutes.pack()


#### PART 4 -> CREATE COMPONENTS SECTIONS TO INTRODUCE COMPONENT'S NAME ####



#### PART 5 -> EXECUTE PROGRAMM, CONFIRM INFO, GIVE FEEDBACK AND CLOSE WINDOW ####
executeFrame = tk.Frame(root)
executeFrame.pack()

# button execute file creation
buttonCreateFiles = tk.Button(executeFrame, text='create project', command=confirmExecution)
buttonCreateFiles.pack()

# execution feedback
labelExecutionFeedback = tk.Label(executeFrame, text='')
labelExecutionFeedback.pack()


try:
    with open("projectRoute.txt", "r") as file:
        savedValue = file.read()
        inputChooseFolder.insert(0, savedValue)
except FileNotFoundError:
    pass

appFrame.pack() # by default we have app section

root.mainloop()