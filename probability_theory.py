from tkinter import *
from player import Player
from goalkeeper import Goalkeeper
import json
from collections import Counter
import random

root = Tk()
root.geometry("307x280")

def get_players_from_json(filename="players.json"):
    with open(filename, "r") as file:
        players = json.load(file)
        for i in range(len(players)):
            players[i] = Goalkeeper(players[i]) if "goalkeeper_url" in players[i] else Player(players[i])
    return players

def get_player_columns(players):
    return [(player.short_name, player.overall, player.dob, player.club_name) for player in players]

def get_matching_birthdays(players):
    birthdays = [player[2][5:] for player in players]
    d = dict(Counter(birthdays))
    all_matches = []
    for k in d.keys():
        if d[k] > 1:
            all_matches.append([player for player in players if player[2][5:] == k])
    return all_matches

def get_random_players():
    label_grid._update_content(sorted(random.sample(players, 23), key=lambda item: item[1], reverse=True))

def get_rgbtohex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

class LabelGrid(Frame):
    """
    Creates a grid of labels that have their cells populated by content.
    """
    def __init__(self, master, content=([0, 0], [0, 0]), *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.content = content[:23]
        self.content_size = (len(content), len(content[0]))
        self._create_labels()
        self._display_labels()


    def _update_content(self, content):
        self.content = content
        self.content_size = (len(content), len(content[0]))
        self._create_labels()
        self._display_labels()

    def _create_labels(self):
        def __put_content_in_label(row, column, highlighted_players):
            content = self.content[row][column]
            content_type = type(content).__name__
            col_widths = {0: 19, 1: 2, 2: 12, 3: 19}
            self.labels[row][column]['width'] = col_widths[column]
            self.labels[row][column]['text'] = content
            if row in highlighted_players:
                self.labels[row][column]['fg'] = get_rgbtohex(255, 0, 0)

        self.labels = list()
        same_birthday_players = get_matching_birthdays(self.content)
        global label_n
        label_n["text"] = f"There are {len(same_birthday_players)} birthdays by {sum([len(player) for player in same_birthday_players])} players"
        print(self.content)
        print(same_birthday_players)
        same_birthday_players = [self.content.index(item) for sublist in same_birthday_players for item in sublist]
        for i in range(23):
            self.labels.append(list())
            for j in range(self.content_size[1]):
                self.labels[i].append(Label(self))
                #(self.content[i][j])
                __put_content_in_label(i, j, same_birthday_players)

    def _display_labels(self):
        for i in range(23):
            for j in range(self.content_size[1]):
                self.labels[i][j].grid(row=i, column=j)


    def _clear_labels(self):
        for item in self.winfo_children():
            item.destroy()

btn = Button(root, text = "Get random!", command = lambda: get_random_players())
btn.grid(pady = 11)

label_n = Label(root, text = "")
label_n.grid(pady = 19)

players = get_player_columns(get_players_from_json())
label_grid = LabelGrid(root, players)
label_grid.grid(pady = 12)

root.mainloop()