# FRAME WITH CHECKBOXES FOR OPTIONS
import customtkinter as ctk
from components.checkbox import CheckboxComponent

'''
option {
    id: string
    text: string
    defaultState: boolean
}
'''

class MoreOptionsComponent: 
    def __init__(self, root, options=()): # constructor method
        self.innerFrame = ctk.CTkFrame(root, fg_color='transparent')
        self.options = options
        self.isShowing = False

        self.checkboxes = []
    
    def createCheckboxes(self):
        self.emptyCheckboxes()
        for option in self.options:
            newCheckbox = CheckboxComponent(self.innerFrame, id=option["id"], label=option["text"], defaultState=option["defaultState"])
            self.checkboxes.append(newCheckbox)
            newCheckbox.checkbox.pack(fill='x', pady=5)
        
    def emptyCheckboxes(self):
        for checbox in self.checkboxes:
            checbox.checkbox.pack_forget()
        self.checkboxes.clear()
            
    def hide(self):
        self.innerFrame.pack_forget()
        self.isShowing = False
    
    def show(self):
        self.innerFrame.pack(fill='x', padx=20, pady=5)
        self.isShowing = True
    
    def changeOptions(self, newOptions):
        self.options = newOptions
        self.createCheckboxes()
    
    def getInfo(self):
        info = {}
        if len(self.checkboxes):
            for checkbox in self.checkboxes:
                info[checkbox.id] = checkbox.state.get()
        return info

        
