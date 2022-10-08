from tkinter import *

root = Tk()
root.title("App")

root.geometry("340x240")

label_code = Label(root, font = ("Helvetica", 28, "bold"), text = "")
label_code.config(height = 4, width = 17)
label_code.grid(row = 0, column = 0, columnspan = 4)

KEYCODE_LABEL_INFOS = {"event key": "The value of the key pressed. Accounts for modifiers keys that return CAPS and alternate chars.", "event code": "The physical key on the keyboard. Doesn't care if you are holding a modifier like Shift.", "similar keys": "", "event history": ""}
keycode_frame = LabelFrame(root)
keycode_frame.grid(row = 1, column = 0)

keys_history = []

for i in range(len(KEYCODE_LABEL_INFOS.keys())):
    keycode_label = LabelFrame(keycode_frame)
    keycode_label.grid(row = 1, column = i, pady = (1, 0))
    name = list(KEYCODE_LABEL_INFOS.keys())[i].replace(" ", "_")
    globals()[name] = Label(keycode_label, width = 14, bg = "#ffc600", text = list(KEYCODE_LABEL_INFOS.keys())[i])
    globals()[name].grid()
    globals()[f"{name}_text"] = Label(keycode_label, height = 4, font = ("", 24, "bold"))
    globals()[f"{name}_text"].grid()
    globals()[f"{name}_description"] = Label(keycode_label, height = 10, width = 14, bg = "darkgrey", text = list(KEYCODE_LABEL_INFOS.values())[i])
    globals()[f"{name}_description"].grid()

def get_keycodes(e):
    print(vars(e)["keysym"])
    print(vars(e)["keycode"])
    keys_history.append(vars(e)["keysym"])
    print(keys_history[-4:])
    label_code["text"] = vars(e)["keysym"]
    event_key_text["text"] = vars(e)["keysym"]
    event_code_text["text"] = vars(e)["keycode"]
    event_history_text["text"] = " ".join(keys_history[-4:-2]) + "\n" + " ".join(keys_history[-2:])

root.bind("<Key>", lambda e: get_keycodes(e))

root.mainloop()