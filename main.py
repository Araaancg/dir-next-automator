from utils.functions.handleJson import getData, dumpData
from utils.functions.handleFiles import iterateProjectStructure
import customtkinter as ctk
from components.input import InputComponent
from components.button import ButtonComponent


# proyectPath = './tests/src'

JSON_FILE = "./tests/test-1.json"

# structure = getData("./toCreate.json")
# iterateProjectStructure(structure["src"], proyectPath)


class MyApp:
    def __init__(self, root): # constructor method
        self.root = root # Tikinter root window or frame where the button will be placed

        # changing root title and size
        self.root.title("I guess this would qualify as a title")
        self.root.geometry("450x620")
        self.root.resizable(True, True) # horizontal, vertical

        self.inputs = []
        self.addInputField()

        self.addInputButton = ButtonComponent(
            self.root, 
            self.addInputField, 
            "add input"
            )
        self.addInputButton.button.pack(pady=10, side="bottom")
        
        self.addInputButton = ButtonComponent(
            self.root, 
            self.getInfoFromInputs, 
            "get info"
            )
        self.addInputButton.button.pack(pady=10, side="bottom")

    def addInputField(self):
        # create a new input component
        inputComponent = InputComponent(self.root, "folder")
        inputComponent.frame.pack(pady=10)
        self.inputs.append(inputComponent)
    
    def getInfoFromInputs(self):
        allInfo = []
        for input in self.inputs:
            inputInfo = input.getInfo()
            allInfo.append(inputInfo)

        dumpData(allInfo, JSON_FILE)


def main(): # initialize the Tkinter root window
    root = ctk.CTk()
    MyApp(root)
    root.mainloop()


# conditional block that ensures the 'main' function is executed only when the secript is run directly (not imported as a module)
if __name__ == "__main__":
    main()
