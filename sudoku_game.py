from tkinter import *
import keyboard
from collections import Counter
import math

root = Tk()

root.title("App")
root.geometry("381x287")
root.iconbitmap("logoicon.ico")

frame = LabelFrame(root, height = 209, width = 240, borderwidth = 4)
frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)

for i in range(3):
    for j in range(3):
        globals()[f"3x3_grid_{i*3 + j}"] = LabelFrame(frame, borderwidth = 2, height = 70, width = 70)
        globals()[f"3x3_grid_{i * 3 + j}"].grid(row = i, column = j)

BOARD_1 = [None, 7, None, None, 6, None, 2, None, None, None, 2, None, None, None, None, 8, None, None, None, 4, 6, 8, 9, None, 7, 1, 5, None, 8, 4, 7, 1, None, None, None, None, None, 9, 7, None, None, None, 1, 3, None, \
    None, None, None, None, 5, 9, 4, 8, None, 6, 9, 7, None, 5, 8, 4, 3, None, None, None, 2, None, None, None, None, 8, None, None, None, 8, None, 6, None, None, 7, None]

def highlight_field(e, j):
    global highlighted
    if BOARD_1[j] != None: return
    e.widget["bg"] = "aqua"
    for widget in highlighted:
        widget["widget"]["bg"] = "#fff"
    highlighted = [{"widget": e.widget, "i": j}]

def enter_number(i):
    if len(highlighted) == 0:
        return
    highlighted[-1]["widget"]["text"] = i.char
    check_for_3x3_grid(highlighted[-1])
    check_for_column(highlighted[-1])
    check_for_row(highlighted[-1])

def check_for_3x3_grid(d):
    i = d["i"]
    elements = [item for item in range(81) if math.floor(item / 9) == math.floor(i/9)]
    text_elements = [str(globals()[f"label_{i}"]["text"]) for i in elements]
    widget_elements = [globals()[f"label_{i}"] for i in elements]
    unique_elements = [item for item in list(dict(Counter(text_elements)).keys()) if item != "" and dict(Counter(text_elements))[item] == 1]
    for item in widget_elements:
        item["fg"] = "red" if item["text"] != "" and str(item["text"]) not in unique_elements else "#000"
    return True if len(unique_elements) == 9 else False

def check_for_row(d):
    i = d["i"]
    row_beginnings = [i*27 + j*3 for i in range(3) for j in range(3)]
    rows = []
    for row in range(9):
        list1 = []
        for j in range(3):
            for k in range(3):
                list1.append(row_beginnings[row] + k + j*9)
        rows.append(list1)
    elements = [item for item in rows if i in item][0]
    text_elements = [str(globals()[f"label_{i}"]["text"]) for i in elements]
    widget_elements = [globals()[f"label_{i}"] for i in elements]
    unique_elements = [item for item in list(dict(Counter(text_elements)).keys()) if item != "" and dict(Counter(text_elements))[item] == 1]
    for item in widget_elements:
        item["fg"] = "red" if item["text"] != "" and str(item["text"]) not in unique_elements else "#000"
    return True if len(unique_elements) == 9 else False

def check_for_column(d):
    i = d["i"]
    print(i)
    columns = []
    column_beginnings = [i*9 + j for i in range(3) for j in range(3)]
    for row in range(9):
        list1 = []
        for j in range(3):
            for k in range(3):
                list1.append(column_beginnings[row] + k*3 + j*27)
        columns.append(list1)
    elements = [item for item in columns if i in item][0]
    print(elements)
    text_elements = [str(globals()[f"label_{i}"]["text"]) for i in elements]
    widget_elements = [globals()[f"label_{i}"] for i in elements]
    unique_elements = [item for item in list(dict(Counter(text_elements)).keys()) if item != "" and dict(Counter(text_elements))[item] == 1]
    print(unique_elements)
    for item in widget_elements:
        item["fg"] = "red" if item["text"] != "" and str(item["text"]) not in unique_elements else "#000"
    return True if len(unique_elements) == 9 else False

for grid_element in range(0, 9):
    for i in range(0, 3):
        for j in range(0, 3):
            globals()[f"label_{grid_element*9 + i*3 + j}"] = Label(globals()[f"3x3_grid_{str(grid_element)}"], width = 2, borderwidth = 2, relief = GROOVE, text = BOARD_1[grid_element*9 + i*3 + j] if BOARD_1[grid_element*9 + i*3 + j] is not None else "")
            globals()[f"label_{grid_element*9 + i*3 + j}"].grid(row = i, column = j)
            globals()[f"label_{grid_element * 9 + i * 3 + j}"].bind("<Button-1>", lambda e, k = grid_element*9 + i*3 + j: highlight_field(e, k))
            globals()[f"label_{grid_element * 9 + i * 3 + j}"].highlighted = False

highlighted = []

root.bind("<Escape>", lambda e: root.destroy())

for i in range(1, 10):
    root.bind(str(i), lambda i: enter_number(i))

if __name__ == "__main__":
    root.mainloop()