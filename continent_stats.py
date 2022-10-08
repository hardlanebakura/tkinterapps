from tkinter import *
from PIL import ImageTk, Image
from database import db

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("App")
        self.geometry("340x189")
        #self._append_labels()
        self.add_exit_shortcut()

    def append_labels(self):
        self.label = Label(self, image=image)
        self.label.pack(padx=19, pady=19)
        self.label.bind("<Button-1>", lambda e: get_continent_clicked(e))
        self.label_name = Label()
        self.label_fsi = Label()
        self.label_fei = Label()
        self.label_mspi = Label()
        self.label_ori = Label()

    def add_exit_shortcut(self):
        self.bind("<Escape>", lambda e: self.destroy())

app = App()
image = ImageTk.PhotoImage(Image.open("map-7-continent-model.jpg").resize((290, 140), Image.Resampling.LANCZOS))
app.append_labels()

#image = ImageTk.PhotoImage(Image.open("map-7-continent-model.jpg").resize((290, 140), Image.Resampling.LANCZOS))

def get_continent(x, y):
    if 181 <= x <= 270 and 10 <= y <= 77:
        return "Asia"
    if 130 <= x <= 175 and 12 <= y <= 37:
        return "Europe"
    if (124 <= x <= 168 and 43 <= y <= 68) or (145 <= x <= 177 and 64 <= y <= 102):
        return "Africa"
    if 70 <= x <= 107 and 64 <= y <= 117:
        return "South America"
    if 25 <= x <= 94 and 8 <= y <= 63:
        return "North America"
    if 232 <= x <= 280 and 79 <= y <= 111:
        return "Oceania"

def get_continent_clicked(e):
    continent = [item for item in continents if item["continent"] == get_continent(e.x, e.y)]
    if len(continent) > 0:
        continent = continent[0]
        for i in range(1, 6):
            app.winfo_children()[i].pack(padx=21, anchor="w" if i > 1 else "center")
        app.label_name["text"] = continent["continent"]
        app.label_fsi["text"] = "Fragile States Indexes " + str(continent["FSI"])
        app.label_fei["text"] = "Factionalized Elites Indexes " + str(continent["FEI"])
        app.label_mspi["text"] = "Military Spending Percentage Indexes " + str(continent["MSPI"])
        app.label_ori["text"] = "Oil Reserves Indexes " + str(continent["ORI"])


#183, 10 270, 77

continents = db.to_dict("continents")

if __name__ == "__main__":
    app.mainloop()