# BUTTON COMPONENT FOR THE GUI
import customtkinter as ctk
from PIL import Image

sizes = {
    "s": 24,
    "m": 32,
    "l": 48
}

class ButtonComponent: 
    def __init__(self, root, onExecute, text='', size="m", icon=''): # constructor method
        '''
        root: Tikinter root window or frame where the button will be placed
        onExecute: function to execute when the button will be pressed
        text: to be displayed inside the button
        size:
        icon: path to the folder of the icon in svg format
        '''
        self.root = root 
        self.onExecute = onExecute 
        self.width = sizes[size]
        self.icon = ctk.CTkImage(light_image=Image.open(icon), dark_image=Image.open(icon), size=(24, 24)) if len(icon) > 0 else ''

        # creating a tkinter 'Button' widget with the characteristics of the object and is assigned to the instance variable addButton
        # then we pack the button into the Tkinter window or frame
        self.button = ctk.CTkButton(
            root, 
            text=text, 
            command=self.onExecute,
            width=self.width,
            height=self.width,
            image=self.icon,
            fg_color="transparent",
            hover_color="#333",
            compound='right'
            )

    def setButtonText(self, newText):
        self.button.configure(text=newText)

    def setButtonIcon(self, iconPath, size=24):
        icon = ctk.CTkImage(light_image=Image.open(iconPath), dark_image=Image.open(iconPath), size=(size, size))
        self.button.configure(image=icon)

