from tkinter import *
import requests
from dotenv import dotenv_values
from PIL import ImageTk, Image

API_KEY = dotenv_values(".env")["OPENWEATHER_API_KEY"]

URL = "http://api.openweathermap.org/data/2.5/"

show_cities = False

def get_text(e):
    global canvas
    global label_city
    global label_temp
    global window_city
    global bg
    global image
    response = requests.get(f"{URL}weather?q={e.get()}&units=metric&APPID={API_KEY}").json()
    if response["cod"] == 200:
        img_src = "hot.jpg" if round(response["main"]["temp"]) > 15 else "cold.jpg"
        if not show_cities:
            canvas.itemconfig(2, state="normal")
            canvas.itemconfig(3, state="normal")
        label_city["text"] = response["name"] + ", " + response["sys"]["country"]
        label_temp["text"] = str(round(response["main"]["temp"])) + " °C"
        image = ImageTk.PhotoImage(Image.open(img_src).resize((140, 140), Image.Resampling.LANCZOS))
        canvas.itemconfig(bg, image=image)

root = Tk()
root.geometry("340x220")

entry_text = StringVar()
entry_text.trace('w', lambda name, index, mode, text=entry_text: get_text(entry_text))

entry = Entry(root, textvariable = entry_text)
entry.pack(pady = 19)

image = ImageTk.PhotoImage(Image.open("hot.jpg").resize((140, 140), Image.Resampling.LANCZOS))
canvas = Canvas(root, height = 140, width = 140)
bg = canvas.create_image(0, 0, anchor=NW, image=image)
canvas.pack()

label_city = Label(root)
label_temp = Label(root)
window_city = canvas.create_window(70, 10, anchor=N, window=label_city)
window_temp = canvas.create_window(70, 40, anchor=N, window=label_temp)
canvas.itemconfig(canvas.find_all()[-1], state="hidden")
canvas.itemconfig(canvas.find_all()[-2], state="hidden")

root.mainloop()