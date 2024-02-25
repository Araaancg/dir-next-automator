import customtkinter as ctk
from PIL import Image

class LabelComponent():
    def __init__(self, root, text, icon=''):
        self.text = text
        self.icon = ctk.CTkImage(light_image=Image.open(icon), dark_image=Image.open(icon), size=(24, 24)) if len(icon) > 0 else ''
        self.label = ctk.CTkLabel(
            root, 
            text=self.text, 
            fg_color="transparent",
            image=self.icon,
            compound='left',
            font=("Arial", 16)
            )