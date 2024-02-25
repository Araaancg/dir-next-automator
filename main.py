from utils.structure.handleJson import dumpData
from utils.structure.handleFiles import iterateProjectStructure
from utils.zipFolder.createAndDownloadZip import createAndDownloadZip
import customtkinter as ctk
from components.input import InputComponent
from components.button import ButtonComponent
from components.label import LabelComponent

JSON_FILE = "./tests/test-2.json"
PROYECT_PATH = "./tests/src"
ASSETS_PATH = "C:\\Users\\Aran\\Desktop\\myCode\\nextProjectInitiator\\assets"


class MyApp:
    def __init__(self, root): # constructor method
        self.root = root # Tikinter root window or frame where the button will be placed

        # changing root title and size
        self.root.title("I guess this would qualify as a title")
        self.root.geometry("600x720")
        self.root.resizable(False, False) # horizontal, vertical

        # HEADER -> src/ folder 
        self.header = ctk.CTkFrame(self.root, fg_color="transparent")
        self.header.pack(anchor="nw", fill='x')

        self.topLabel = LabelComponent(self.header, '   src', icon=f'{ASSETS_PATH}\\images\\folder.png')
        self.topLabel.label.pack(side="left", pady=10, padx=10)

        self.addInputButton = ButtonComponent(
            self.header, 
            self.addInputField, 
            icon=f'{ASSETS_PATH}\\images\\plus.png'
            )
        self.addInputButton.button.pack(pady=10, side="left")

        # BODY -> all inputs
        self.body = ctk.CTkScrollableFrame(self.root, fg_color="transparent", height=600)
        self.body.pack(anchor="nw", fill='x')
        self.inputs = []

        self.addInputField()

        # FOOTER -> execute program logic
        self.footer = ctk.CTkFrame(self.root, fg_color="transparent")
        self.footer.pack(anchor="sw", fill="x")
        self.addInputButton = ButtonComponent(
            self.footer, 
            self.executeProgram, 
            "EXECUTE"
            )
        self.addInputButton.button.pack(pady=10, side="bottom")


    def addInputField(self):
        # create a new input component
        inputComponent = InputComponent(self.body, "folder")
        self.inputs.append(inputComponent)
    
    def getInfoFromInputs(self):
        allInfo = {"src":[]}
        for input in self.inputs:
            inputInfo = input.getInfo()
            allInfo["src"].append(inputInfo)
        dumpData(allInfo, JSON_FILE)
        return allInfo
    
    def executeProgram(self):
        structure = self.getInfoFromInputs()
        iterateProjectStructure(structure["src"], PROYECT_PATH)
        createAndDownloadZip(PROYECT_PATH, "src.zip")



def main(): # initialize the Tkinter root window
    root = ctk.CTk()
    MyApp(root)
    root.mainloop()


# conditional block that ensures the 'main' function is executed only when the secript is run directly (not imported as a module)
if __name__ == "__main__":
    main()
