from tkinter import *
import requests
from dotenv import dotenv_values
from playsound import playsound
import re
from PIL import ImageTk, Image, ImageDraw

URL = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/"
API_KEY = dotenv_values(".env")["MERRIAM-WEBSTER_API_KEY"]

root = Tk()

root.geometry("391x381")
root.title("App")
root.iconbitmap("logoicon.ico")

def draw_image(output_path):
    image = Image.new("RGB", (140, 140), "#fff")
    draw = ImageDraw.Draw(image)
    draw.polygon([(24, 19), (24, 127), (122, 73)], fill = "#000")
    image.save(output_path)

def get_search(text):
    text.set(re.sub("[^A-Za-z]", "", text.get()))
    if len(text.get()) > 0:
        response = requests.get(f"{URL}{text.get()}?key={API_KEY}").json()
        get_label_for_correct(response[0]) if len(response) > 0 and "meta" in response[0] else get_label_for_fail()

def get_label_for_correct(data):
    display_labels(data)
    audio_file = get_audio_file(data)
    data["meta"]["id"] = data["meta"]["id"].split(":")[0]
    label_name["text"] = data["meta"]["id"]
    label_functional["text"] = data["fl"]
    label_stems["text"] = ", ".join(data["meta"]["stems"])
    meaning_text = ""
    for item in data["def"][0]["sseq"]:
        meanings = list(item[0][1].keys())
        meaning = item[0][1][meanings[1]] if len(meanings) > 1 else item[0][1][meanings[0]]
        meaning = re.sub(r'{bc}|{it}|{/it}', "", meaning[0][1])
        meaning_text += meaning + "\n"
        label_meaning["text"] = meaning_text
    label_audio.pack_forget() if audio_file == None else label_audio.pack()

def display_labels(data):
    #print(data)
    pass

def get_label_for_fail():
    pass

def get_audio_file(data):
    try:
        audio = data["hwi"]["prs"][0]["sound"]["audio"]
        return f"https://media.merriam-webster.com/audio/prons/en/us/mp3/{audio[0]}/{audio}.mp3"
    except Exception:
        return None

draw_image("label_audio.jpg")
image = ImageTk.PhotoImage((Image.open("label_audio.jpg").resize((40, 40), Image.Resampling.LANCZOS)))

search_text = StringVar()
search_text.trace('w', lambda name, index, mode, text= search_text: get_search(search_text))

search = Entry(root, textvariable=search_text)
search.pack(pady = 19)

label_success = Frame(root)
label_success.pack()
label_fail = Label(root, fg = "red")
label_fail.pack()

#additional_labels
label_name = Label(root, font = ("Helvetica", 16, "bold"))
label_name.pack()
label_phonetic = Label(root)
label_phonetic.pack()
label_audio = Label(root, image = image)
label_meaning = Label(root)
label_meaning.pack()
label_functional = Label(root)
label_functional.pack()
label_stems = Label(root)
label_stems.pack()

root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()
