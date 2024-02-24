import customtkinter as ctk 
from components.button import ButtonComponent
from components.checkbox import CheckboxComponent

class InputComponent:
    def __init__(self, root, type):
        self.frame = ctk.CTkFrame(root)
        # types: folder, file, component, page, route
        self.type = type

        # CREATING THE INPUT ITSELF
        self.input = ctk.CTkEntry(self.frame)

        # BUTTON TO TOGGLE BETWEEN THE DIFFERENT TYPES OF INPUT 
        self.changeTypeButton = ButtonComponent(self.frame, self.changeInputType, "folder")

        # BUTTON TO DELETE THE INPUT
        self.deleteInputButton = ButtonComponent(self.frame, self.deleteInput, "X")

        # CHECKBOXES
        # for component: divided and css
        self.dividedCheckbox = CheckboxComponent(self.frame, "divided")
        self.cssCheckbox = CheckboxComponent(self.frame, "add css")
        # for page: page, layout, dynamic and css (recycling css checkbox from component)
        self.pageCheckbox = CheckboxComponent(self.frame, "add page")
        self.layoutCheckbox = CheckboxComponent(self.frame, "add layout")
        self.dynamicCheckbox = CheckboxComponent(self.frame, "dynamic")

        # SUBROUTES
        self.subroutes = []
        self.addSubrouteButton = ButtonComponent(self.frame, self.addSubroute, "add subroute")

        # self.managingCheckboxes()

        # self.frame.columnconfigure(0, weight=1)
        # self.frame.columnconfigure(1, weight=2)
        # self.frame.columnconfigure(2, weight=1)
        # self.frame.columnconfigure(4, weight=1)
        # self.frame.columnconfigure(5, weight=1)
        # self.frame.columnconfigure(6, weight=1)

        # self.frame.rowconfigure(0, weight=1)
        # self.frame.rowconfigure(1, weight=1)

        self.changeTypeButton.button.grid(row = 0, column = 1)
        self.input.grid(row = 0, column = 1)
        self.deleteInputButton.button.grid(row = 0, column = 3)
        self.addSubrouteButton.button.grid(row = 1, column = 2)

    def getInputText(self):
        return self.input.get()
    
    def changeInputType(self):
        availableTypes = ["folder", "file", "component", "page", "route"]
        currentIndex = availableTypes.index(self.type)
        nextIndex = currentIndex + 1
        if currentIndex == len(availableTypes) - 1:
            nextIndex = 0
        self.type = availableTypes[nextIndex]
        self.changeTypeButton.setButtonText(availableTypes[nextIndex])
        # self.managingCheckboxes()
    
    # def managingCheckboxes(self):
        # allCheckboxes = (self.dividedCheckbox, self.cssCheckbox, self.pageCheckbox, self.layoutCheckbox, self.dynamicCheckbox)
        # checkboxMapping = {
        #     "component": (self.dividedCheckbox, self.cssCheckbox),
        #     "page": (self.pageCheckbox, self.layoutCheckbox, self.cssCheckbox, self.dynamicCheckbox),
        # }
        # checkboxesToPack = checkboxMapping.get(self.type, ())

        # for checkbox in allCheckboxes:
        #     if checkbox in checkboxesToPack:
        #         checkbox.checkbox.pack()
        #     else:
        #         checkbox.checkbox.pack_forget()
    
    def getInfo(self):
        info = {"name": self.getInputText(), "type": self.type}
        # if self.type == "component":
        #     info["divided"] = self.dividedCheckbox.state.get()
        #     info["addCss"] = self.cssCheckbox.state.get()
        # elif self.type == "page":
        #     info["page"] = self.pageCheckbox.state.get()
        #     info["layout"] = self.layoutCheckbox.state.get()
        #     info["addCss"] = self.cssCheckbox.state.get()
        #     info["dynamic"] = self.dynamicCheckbox.state.get()
        # if len(self.subroutes) > 0:
        #     info["subroutes"] = []
        #     for inputRoute in self.subroutes:
        #         info["subroutes"].append(inputRoute.getInfo())

        return info

    def addSubroute(self):
        newInput = InputComponent(self.frame, "folder")
        newInput.frame.grid(row = 3, rowspan = 2, column = 1, columnspan = 6, pady=5)
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
