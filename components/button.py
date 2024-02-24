# BUTTON COMPONENT FOR THE GUI
from tkinter import ttk
import customtkinter as ctk

class ButtonComponent: 
    def __init__(self, root, onExecute, text, styles="none"): # constructor method
        '''
            root: Tikinter root window or frame where the button will be placed
            onExecute: function to execute when the button will be pressed
            text: to be displayed inside the button
        '''
        self.root = root 
        self.onExecute = onExecute 

        # creating a tkinter 'Button' widget with the characteristics of the object and is assigned to the instance variable addButton
        # then we pack the button into the Tkinter window or frame
        self.button = ctk.CTkButton(
            root, 
            text=text, 
            command=self.onExecute,
            )

    def setButtonText(self, newText):
        self.button.configure(text=newText)

