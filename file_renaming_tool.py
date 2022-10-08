from tkinter import *
from tkinter.filedialog import askdirectory
import os
from PIL import ImageTk, Image

current_directory = os.path.dirname(os.path.abspath(__file__))

root = Tk()
root.title("App")
root.geometry("301x298")
root.iconbitmap("logoicon.ico")

files = os.listdir(askdirectory())

entry = Entry(root)
entry.pack(pady = 19)

label = Label(root)
label.pack()

root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()
