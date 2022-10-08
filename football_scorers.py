from tkinter import *
from PIL import ImageTk, Image
from urllib.request import urlopen, Request
from goalkeeper import Goalkeeper
from player import Player
import json
import io

def get_image_from_URL(URL, column):
    VALUES = {"player": (26, 26), "club": (22, 22), "nation": (15, 15)}
    req = Request(url = URL, headers = HEADERS)
    u = urlopen(req)
    raw_data = u.read()
    u.close()
    image = Image.open(io.BytesIO(raw_data)).resize(VALUES[column], Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    return photo

def get_players_from_json(filename="players.json"):
    with open(filename, "r") as file:
        players = json.load(file)
        for i in range(len(players)):
            players[i] = Goalkeeper(players[i]) if "goalkeeper_url" in players[i] else Player(players[i])
    return players

def get_entry_text_players_columns(player):
    for COLUMN in COLUMNS:
        if COLUMN[-4:] == "_url":
            player[COLUMNS.index(COLUMN)] = get_image_from_URL(player[COLUMNS.index(COLUMN)], COLUMN.split("_")[0])
    return player

COLUMNS = ["short_name", "player_face_url", "overall", "club_logo_url", "nation_flag_url"]
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
      'AppleWebKit/537.11 (KHTML, like Gecko) '
      'Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}

def get_entry_text_players(text_var):
    global search_player
    global label_grid
    text_var.set(re.sub("[^A-Za-z]+", "", text_var.get()))
    text = text_var.get().lower()
    matching_players = [player for player in all_players if text in vars(player)["short_name"].lower()][:10]
    if (len(matching_players) < len(all_players)): label_grid._clear_labels()
    players = get_players(matching_players)
    label_grid._update_content(players)

#get column values for the selected group of players
def get_players(all_players, length = 10):
    players = []
    for i in range(len(all_players)):
        list1 = [vars(all_players[i])[COLUMNS[j]] for j in range(len(COLUMNS))]
        players.append(get_entry_text_players_columns(list1))
    return players

class LabelGrid(Frame):
    """
    Creates a grid of labels that have their cells populated by content.
    """
    def __init__(self, master, content=([0, 0], [0, 0]), *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.content = content
        self.content_size = (len(content), len(content[0]))
        self._create_labels()
        self._display_labels()


    def _update_content(self, content):
        self.content = content
        self.content_size = (len(content), len(content[0]))
        self._create_labels()
        self._display_labels()

    def _create_labels(self):
        def __put_content_in_label(row, column):
            content = self.content[row][column]
            content_type = type(content).__name__
            if content_type in ('str', 'int'):
                self.labels[row][column]['text'] = content
            elif content_type == 'PhotoImage':
                self.labels[row][column]['image'] = content

        self.labels = list()
        for i in range(self.content_size[0]):
            self.labels.append(list())
            for j in range(self.content_size[1]):
                self.labels[i].append(Label(self))
                __put_content_in_label(i, j)

    def _display_labels(self):
        for i in range(self.content_size[0]):
            for j in range(self.content_size[1]):
                self.labels[i][j].grid(row=i, column=j)

    def _clear_labels(self):
        for item in self.winfo_children():
            item.destroy()

if __name__ == '__main__':
    all_players = get_players_from_json()
    root = Tk()
    root.geometry('400x210')
    root.title('Players')
    search_player_text = StringVar()
    search_player_text.trace('w', lambda name, index, mode, text=search_player_text: get_entry_text_players(search_player_text))
    search_player = Entry(root, textvariable=search_player_text)
    search_player.pack()

    players = get_players(all_players[:10])
    label_grid = LabelGrid(root, players)
    label_grid.pack(pady = 19)
    root.mainloop()