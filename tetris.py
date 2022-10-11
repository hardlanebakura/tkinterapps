from tkinter import *

root = Tk()

root.title("App")
root.geometry("381x287")
root.iconbitmap("logoicon.ico")

def get_arrow():
    print("1")

root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()