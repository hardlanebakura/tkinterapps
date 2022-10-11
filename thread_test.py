from tkinter import *
import time
import random
import threading

root = Tk()

root.title("App")
root.geometry("381x287")
root.iconbitmap("logoicon.ico")

def five_seconds():
    time.sleep(5)
    label.config(text = "5 Seconds Is Up!")

def rando():
    random_label["text"] = random.randint(1, 100)

label = Label(root, text = "Click me!")
label.pack(pady = 19)

button_1 = Button(root, text = "5 seconds", command = threading.Thread(target = five_seconds).start())
button_1.pack(pady = 19)

button_2 = Button(root, text = "Pick Random Number")
button_1.pack(pady = 19)

random_label = Button(root, command = rando)
random_label.pack(pady = 19)

root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()