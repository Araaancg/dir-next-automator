import customtkinter as ctk

class CheckboxComponent:
    def __init__(self, root, id, label, defaultState=False):
        self.root = root
        self.label = label
        self.id = id
        self.state = ctk.BooleanVar(value=defaultState)

        self.checkbox = ctk.CTkCheckBox(root, text=self.label, variable=self.state)
