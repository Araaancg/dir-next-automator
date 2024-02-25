import customtkinter as ctk 
from components.button import ButtonComponent
from components.separator import SeparatorComponent
from components.moreOptions import MoreOptionsComponent
from utils.structure.handleJson import getData

ASSETS_PATH = "C:\\Users\\Aran\\Desktop\\myCode\\nextProjectInitiator\\assets"


optionsMapping = getData("C:\\Users\\Aran\\Desktop\\myCode\\nextProjectInitiator\\assets\\data\\options.json")

class InputComponent:
    def __init__(self, root, type, level=0):
        self.frame = ctk.CTkFrame(root, fg_color="transparent")
        self.innerFrame = ctk.CTkFrame(self.frame, fg_color="transparent")

        self.level = level

        # types: folder, file, component, page, route
        self.type = type

        # CREATING THE INPUT ITSELF
        self.input = ctk.CTkEntry(self.innerFrame)

        # BUTTON TO TOGGLE BETWEEN THE DIFFERENT TYPES OF INPUT 
        self.changeTypeButton = ButtonComponent(self.innerFrame, self.changeInputType)

        # BUTTON TO DELETE THE INPUT
        self.deleteInputButton = ButtonComponent(self.innerFrame, self.deleteInput, icon=f'{ASSETS_PATH}\\images\\trash.png')

        # CHECKBOXES - MORE OPTIONS
        self.moreOptions = MoreOptionsComponent(self.frame)
        self.moreOptionsButton = ButtonComponent(self.innerFrame, self.toggleOptions, icon=f'{ASSETS_PATH}\\images\\downCaret.png')

        # SUBROUTES
        self.subroutes = []
        self.addSubrouteButton = ButtonComponent(self.innerFrame, self.addSubroute, icon=f'{ASSETS_PATH}\\images\\plus.png')

        separator = SeparatorComponent(self.innerFrame, "vertical")
        separator.separator.grid(row = 0, column = self.level, sticky="ns")
        self.changeTypeButton.button.grid(row = 0, column = self.level + 1)
        self.input.grid(row = 0, column = self.level + 2)
        self.deleteInputButton.button.grid(row = 0, column = self.level + 3)
        self.addSubrouteButton.button.grid(row = 0, column = self.level + 4)

        self.innerFrame.pack(anchor='nw')
        self.frame.pack(anchor='nw', fill='x') if self.level > 0 else self.frame.pack(anchor='nw', fill='x', padx=(20, 0))
  
        self.managingCheckboxes()
        self.manageButtonTypeIcon()
            
    def getInputText(self):
        return self.input.get()
    
    def changeInputType(self):
        availableTypes = ["folder", "file", "component", "page", "route"]
        currentIndex = availableTypes.index(self.type)
        nextIndex = currentIndex + 1
        if currentIndex == len(availableTypes) - 1:
            nextIndex = 0
        self.type = availableTypes[nextIndex]
        self.manageButtonTypeIcon()
        self.managingCheckboxes()
    
    def managingCheckboxes(self):
        if optionsMapping.get(self.type):
            self.moreOptions.changeOptions(optionsMapping[self.type])
            self.showOptionsButton()
        else:
            self.moreOptions.changeOptions(())
            self.hideOptionsButton()
 
    def toggleOptions(self):
        if self.moreOptions.isShowing:
            self.moreOptionsButton.setButtonIcon(f'{ASSETS_PATH}\\images\\downCaret.png')  
            self.moreOptions.hide()
        else: 
            self.moreOptionsButton.setButtonIcon(f'{ASSETS_PATH}\\images\\upCaret.png')
            self.moreOptions.show()
    
    def getInfo(self):
        info = {"name": self.getInputText(), "type": self.type}
        info.update(self.moreOptions.getInfo())
        if len(self.subroutes) > 0:
            info["subpaths"] = []
            for inputRoute in self.subroutes:
                info["subpaths"].append(inputRoute.getInfo())

        return info
    
    def manageButtonTypeIcon(self):
        self.changeTypeButton.setButtonIcon(f"{ASSETS_PATH}\\images\\{self.type}.png")

    def addSubroute(self):
        newInput = InputComponent(self.frame, "folder", level=(self.level + 1))     
        newInput.frame.pack(side="bottom")
        self.subroutes.append(newInput)
        newInput.addSeparators()

    def deleteInput(self):
        index = -1
        for i, inputRoute in enumerate(self.subroutes):
            if inputRoute == self:
                index = i
                break

        if index != -1:
            self.subroutes.pop(index)

        self.frame.destroy()
    
    def hideOptionsButton(self):
        self.moreOptionsButton.button.grid_forget()

    def showOptionsButton(self):
        self.moreOptionsButton.button.grid(row = 0, column = self.level + 5)

    def addSeparators(self):
        for i in range(self.level):
            separator = SeparatorComponent(self.innerFrame, "vertical")
            separator.separator.grid(row=0, column=0 + i, sticky="ns", padx=(0, 20))