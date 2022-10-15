from tkinter import *
from PIL import ImageTk, Image

from nba_api.stats.static import teams

root = Tk()

root.title("App")
root.geometry("381x287")
root.iconbitmap("logoicon.ico")

rooth = root.winfo_height()

frame_buttons = LabelFrame(root)
frame_buttons.place(x = 10, y = 4)

button_back = Button(frame_buttons, text = "←", command = lambda: go_back(), state = DISABLED, bg = "#00f", fg = "#fff")
button_back.pack(side = LEFT)
button_forward = Button(frame_buttons, text = "→", command = lambda: go_forward(), state = DISABLED, bg = "#00f", fg = "#fff")
button_forward.pack(side = LEFT)

frame = LabelFrame(root)
frame_row_1 = LabelFrame(frame)
frame_row_2 = LabelFrame(frame)

frame_team = LabelFrame(root, borderwidth = 0, highlightthickness = 0)

all_teams = teams.get_teams()
images = [ImageTk.PhotoImage(Image.open(f"nba_team_logos/{team['full_name'].lower().replace(' ', '-')}.png").resize((140, 140),Image.Resampling.LANCZOS)) for team in all_teams]
searches = {}

def get_main():
    frame.pack(pady=rooth / 3)
    frame_row_1.pack()
    frame_row_2.pack()
    frame_team.pack_forget()

get_main()

for i in range(len(all_teams)):
    frame_n = frame_row_1 if i < 15 else frame_row_2
    globals()[f"label_{i}"] = Canvas(frame_n, bg="#000", width=100, height=100)
    globals()[f"label_{i}"].image = images[i]
    globals()[f"label_{i}"].create_image(49, 49, anchor=CENTER, image=images[i])
    globals()[f"label_{i}"].team = all_teams[i]
    globals()[f"label_{i}"].pack(side=LEFT)
    globals()[f"label_{i}"].bind("<Button-1>", lambda e: get_team(e))

def get_team(e, called_by_button=False):
    global searches
    team = e.widget.team if type(e) == Event else e
    frame.pack_forget()
    frame_team.pack()
    if len(searches.keys()) == 0:
        get_team_labels(team, e.widget.image)
    else:
        #2nd search
        if frame_team.winfo_children()[0]["text"] != searches["full_name"]:
            for item in frame_team.winfo_children():
                item.destroy()
            get_team_labels(team)
    searches = team
    if not called_by_button: go_forward()

def get_team_labels(team, image=None):
    #if image exists it is first visit
    label_title = Label(frame_team, text=team["full_name"], font=("Helvetica", 22, "bold"))
    label_title.pack(pady=19)
    logo = Canvas(frame_team, bg="#000", height=100, width=100)
    logo.create_image(49, 49, anchor=CENTER, image=images[all_teams.index(searches)] if image is None else image)
    logo.pack()
    label_city = Label(frame_team, text=team["city"], font=("Helvetica", 12, "bold"))
    label_city.pack()
    label_state = Label(frame_team, text=team["state"], font=("Helvetica", 11, "bold"))
    label_state.pack()
    label_year_founded = Label(frame_team, text=team["year_founded"], font=("Helvetica", 11, "bold"))
    label_year_founded.pack()

def go_back():
    button_back["state"] = "disabled"
    button_forward["state"] = "normal" if len(searches.keys()) > 0 else "disabled"
    get_main()

def go_forward():
    button_back["state"] = "normal"
    button_forward["state"] = "disabled"
    get_team(searches, True)

menu = Menu(root)
root.config(menu = menu)

root.bind("<Escape>", lambda e: root.destroy())

file_menu = Menu(menu, tearoff = 0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Close", command = lambda: root.destroy())

if __name__ == "__main__":
    root.mainloop()
