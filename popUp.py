import tkinter as tk
from tkinter import messagebox
 # Create the main application window
  # Hide the main window

def msgSucces():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Transcation Status","Amount has been sent successfully")
    root.mainloop() 
def fail():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Information","Show your face infront of camera")
    root.mainloop()
def msgFail():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Transcation Status","Face not recognised")
    root.mainloop() 
def MultipleFace():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Transcation Status","Multiple Face Detected")
    root.mainloop() 


