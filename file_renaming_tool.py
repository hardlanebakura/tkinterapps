from tkinter import *
from tkinter.filedialog import askdirectory
import os
from PIL import ImageTk, Image
import math

current_directory = os.path.dirname(os.path.abspath(__file__))

root = Tk()
root.title("App")
root.geometry("301x298")
root.iconbitmap("logoicon.ico")

files = os.listdir(askdirectory())

def get_search_text(text):
    matched_files = [file.split(".mp3")[0] for file in files if text.get() in file]
    #print(matched_files)
    n = len(matched_files)
    math.ceil(n/10)
    if n > 0:
        pages_n = math.ceil(n/10)
        if n > 10:
            label_go_to_page["text"] = "Go to page"
            label_go_to_page.pack()
    else:
        label_go_to_page.pack_forget()

entry_text = StringVar()
entry_text.trace("w", lambda name, index, mode, text= entry_text: get_search_text(entry_text))

entry = Entry(root, textvariable = entry_text)
entry.pack(pady = 19)

label = Label(root)
label.pack()

label_go_to_page = Label(root)

root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()
