from tkinter import ttk

class SeparatorComponent():
    def __init__(self, root, orientation):
        self.orientation = orientation
        self.separator = ttk.Separator(root, orient=self.orientation)
