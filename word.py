from tkinter import *
import PyPDF2
from tkinter.filedialog import askopenfiles
from pygame import mixer
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()

image_play = ImageTk.PhotoImage(Image.open("music_play_button.jpg").resize((40, 40), Image.Resampling.LANCZOS))
img_stop = ImageTk.PhotoImage(Image.open("music_stop_button.jpg").resize((40, 40), Image.Resampling.LANCZOS))

mixer.init()

current_song = {}

def get_song(file):
    if file is not None:
        mixer.music.load(file)
        mixer.music.play(-1)
        label_play = Label(root, image = image_play)
        label_play.pack()
        label_stop = Label(root)
        label_stop.pack()
        label_song_name = Label(root, text = "1")
        label_song_name.pack()
        label_song = LabelFrame(root)
        label_song.pack()
        label_p = Label(label_song, bg = "yellow")
        label_p.pack(side = LEFT)
        label_marker = Label(label_song, width = 4, bg = "red")
        label_marker.pack(side = LEFT)
        label_l = Label(label_song, width = 96, bg = "green")
        label_l.pack(side = LEFT)
        label_seconds = Label(root, text = "1")
        label_seconds.pack()

root.title("App")
root.geometry("381x287")
root.iconbitmap("logoicon.ico")

menu = Menu(root)
root.config(menu = menu)

songs = []

def get_new_file():
    global listbox_all_songs
    files = askopenfiles(filetypes = [('All files', '*.mp3')])
    file_names = [file.name.split(".")[0] for file in files]
    for file in file_names:
        listbox_all_songs.insert(END, file)
        songs.append({"song": file.split("/")[-1], "location": file + ".mp3"})

def play_song(new_song = False):
    song = songs[listbox_all_songs.curselection()[0]]["location"]
    print(current_song)
    #no songs were selected yet
    if "song" not in current_song or new_song:
        current_song["pos"] = 0
    current_song["song"] = song
    mixer.music.load(song)
    mixer.music.play(start = round(current_song["pos"]/1000))
    label_stop_song.pack()
    label_play_song.pack_forget()

def stop_song():
    current_song["pos"] += mixer.music.get_pos()
    mixer.music.stop()
    label_stop_song.pack_forget()
    label_play_song.pack()

file_menu = Menu(menu, tearoff = 0)
menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", command = get_new_file)

listbox_all_songs = Listbox(root, width = 50)
listbox_all_songs.pack(pady = 19)
listbox_all_songs.bind("<Double-1>", lambda e: play_song(True))

button_choose_song = Button(root, text = "Choose song", command = get_new_file)
button_choose_song.pack(pady = 19)

label_play_song = Button(root, image = image_play)
label_play_song.bind("<Button-1>", lambda e: play_song())
label_stop_song = Label(root, image = img_stop)
label_stop_song.bind("<Button-1>", lambda e: stop_song())

root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()