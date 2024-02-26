from utils.structure.handleJson import dumpData
from utils.structure.handleFiles import iterateProjectStructure
from utils.outputFolder.moveOutputFolder import moveOutputFolder
import customtkinter as ctk
from components.input import InputComponent
from components.button import ButtonComponent
from components.label import LabelComponent
from routes import ASSETS_PATH, JSON_FILE, OUTPUT_PATH
import shutil
import os

class MyApp:
    def __init__(self, root): # constructor method
        self.root = root # Tikinter root window or frame where the button will be placed

        # changing root title and size
        self.root.title("Create your own NextJS proyect structure")
        self.root.geometry("600x720")
        self.root.resizable(False, False) # horizontal, vertical
        root.protocol("WM_DELETE_WINDOW", self.onClose) # in case users doesn't execute program till the end


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
            root=self.footer, 
            onExecute=self.executeProgram, 
            text="EXECUTE",
            icon=f'{ASSETS_PATH}\\images\\execute.png'
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
        iterateProjectStructure(structure["src"], OUTPUT_PATH)
        moveOutputFolder("src", OUTPUT_PATH)
        self.onClose()
     
    def onClose(self):
        try:
            dumpData({}, JSON_FILE)
            if os.path.exists(OUTPUT_PATH):
                shutil.rmtree(OUTPUT_PATH)
            self.root.destroy()
        except Exception as e:
            print(f"Error removing folder '{OUTPUT_PATH}': {e}")

