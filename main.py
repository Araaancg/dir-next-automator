from app import MyApp
import customtkinter as ctk

def main(): # initialize the Tkinter root window
    root = ctk.CTk()
    MyApp(root)
    root.mainloop()

# conditional block that ensures the 'main' function is executed only when the secript is run directly (not imported as a module)
if __name__ == "__main__":
    main()