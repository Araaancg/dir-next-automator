import customtkinter as ctk 
from components.button import ButtonComponent
from components.checkbox import CheckboxComponent
from components.separator import SeparatorComponent

projectPath = "C:\\Users\\Aran\\Desktop\\myCode\\nextProjectInitiator\\assets\\images"



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
        self.deleteInputButton = ButtonComponent(self.innerFrame, self.deleteInput, icon=f'{projectPath}\\trash.png')

        # CHECKBOXES
        # for component: divided and css
        self.dividedCheckbox = CheckboxComponent(self.innerFrame, "divided")
        self.cssCheckbox = CheckboxComponent(self.innerFrame, "add css")
        # for page: page, layout, dynamic and css (recycling css checkbox from component)
        self.pageCheckbox = CheckboxComponent(self.innerFrame, "add page")
        self.layoutCheckbox = CheckboxComponent(self.innerFrame, "add layout")
        self.dynamicCheckbox = CheckboxComponent(self.innerFrame, "dynamic")

        # SUBROUTES
        self.subroutes = []
        self.addSubrouteButton = ButtonComponent(self.innerFrame, self.addSubroute, icon=f'{projectPath}\\plus.png')

        # self.managingCheckboxes()
        self.manageButtonTypeIcon()

        separator = SeparatorComponent(self.innerFrame, "vertical")
        separator.separator.grid(row = 0, column = 0, sticky="ns")
        self.changeTypeButton.button.grid(row = 0, column = 1)
        self.input.grid(row = 0, column = 2)
        self.deleteInputButton.button.grid(row = 0, column = 3)
        self.addSubrouteButton.button.grid(row = 0, column = 4)

        self.innerFrame.pack(padx=(50 * self.level, 0))

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
        # self.managingCheckboxes()
    
    # def managingCheckboxes(self):
    #     allCheckboxes = (self.dividedCheckbox, self.cssCheckbox, self.pageCheckbox, self.layoutCheckbox, self.dynamicCheckbox)
    #     checkboxMapping = {
    #         "component": (self.dividedCheckbox, self.cssCheckbox),
    #         "page": (self.pageCheckbox, self.layoutCheckbox, self.cssCheckbox, self.dynamicCheckbox),
    #     }
    #     checkboxesToPack = checkboxMapping.get(self.type, ())

    #     for checkbox in allCheckboxes:
    #         if checkbox in checkboxesToPack:
    #             checkbox.checkbox.pack()
    #         else:
    #             checkbox.checkbox.pack_forget()
    
    def getInfo(self):
        info = {"name": self.getInputText(), "type": self.type}
        if self.type == "component":
            info["divided"] = self.dividedCheckbox.state.get()
            info["addCss"] = self.cssCheckbox.state.get()
        elif self.type == "page":
            info["page"] = self.pageCheckbox.state.get()
            info["layout"] = self.layoutCheckbox.state.get()
            info["addCss"] = self.cssCheckbox.state.get()
            info["dynamic"] = self.dynamicCheckbox.state.get()
        if len(self.subroutes) > 0:
            info["subroutes"] = []
            for inputRoute in self.subroutes:
                info["subroutes"].append(inputRoute.getInfo())

        return info
    
    def manageButtonTypeIcon(self):
        self.changeTypeButton.setButtonIcon(f"{projectPath}\\{self.type}.png")

    def addSubroute(self):
        newInput = InputComponent(self.frame, "folder", level= self.level + 1)     
        newInput.frame.pack()
        self.subroutes.append(newInput)

    def deleteInput(self):
        index = -1
        for i, inputRoute in enumerate(self.subroutes):
            if inputRoute == self:
                index = i
                break

        if index != -1:
            self.subroutes.pop(index)

        self.frame.destroy()
