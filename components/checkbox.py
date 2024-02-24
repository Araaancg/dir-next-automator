import customtkinter as ctk

class CheckboxComponent:
    def __init__(self, root, label):
        self.root = root
        self.label = label
        self.state = ctk.BooleanVar()

        self.checkbox = ctk.CTkCheckBox(root, text=self.label, variable=self.state)
