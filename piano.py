from tkinter import *
import os
from keys import *
from playsound import playsound
import cProfile
import pstats

#playsound needs pip install playsound==1.2.2

root = Tk()
root.title("App")
root.geometry("791x267")
root.iconbitmap("logoicon.ico")

def clicked_key(key):
    print(key)
    print(keyboard_sounds)
    #[item for item in frame.winfo_children() if item["text"] == key][0]
    playsound(f"keys_mp3/{keyboard_sounds[key]}.mp3")

WHITE_KEYS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
BLACK_KEYS = ["!", "@", "$", "%", "^", "*", "(", "Q", "W", "E", "T", "Y", "I", "O", "P", "S", "D", "G", "H", "J", "L", "Z", "C", "V", "B"]
BLACK_KEY_INDEXES = [0, 1, 3, 4, 5, 7, 8, 10, 11, 12, 14, 15, 17, 18, 19, 21, 22, 24, 25, 26, 28, 29, 31, 32, 33]

frame = Frame(root, width = 740, height = 210, bg = "yellow")
frame.place(relx = 0.05, rely = 0.1)

for i in range(len(WHITE_KEYS)):
    Button(frame, width = 2, height = 14, text = WHITE_KEYS[i], bg = "#fff", command = lambda j=i: WHITE_KEYS[i]).place(x = 7 + 20*i, y = 10)

for i in range(len(BLACK_KEY_INDEXES)):
    distance = 19 + 20 * BLACK_KEY_INDEXES[i]
    Button(frame, width=1, height=4, text=BLACK_KEYS[i], fg="#fff", bg="#000", command = lambda j=i: clicked_key(BLACK_KEYS[i])).place(x = distance, y = 2)

for key in WHITE_KEYS + BLACK_KEYS:
    root.bind(f"<{key}>", lambda key: clicked_key(key.char))

import cProfile, pstats

profiler = cProfile.Profile()
profiler.enable()
clicked_key("s")
profiler.disable()
stats = pstats.Stats(profiler).sort_stats('cumtime')
stats.print_stats(4)

root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()

