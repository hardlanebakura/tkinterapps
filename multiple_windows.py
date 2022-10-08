from tkinter import *
from mongo_collections import DatabaseAtlas
import random
import string
from PIL import ImageTk, Image

login = Tk()

login.geometry("393x517")
login.title("Login")

entry_username_text = StringVar()
entry_password_text = StringVar()

entry_username = Entry(login, width = 40, textvariable = entry_username_text).pack(pady = 11)
entry_password = Entry(login, width = 40, textvariable = entry_password_text).pack(pady = 11)

def new_window(username):
    greeting = Tk()

    greeting.geometry("281x140")
    greeting.title("Greeting")

    label_1 = Label(greeting, text=f"Welcome {username}").pack()

    greeting.mainloop()

def user_login():
    d = DatabaseAtlas.findAll("random_usernames", {})[0]
    #mcps391846 axks@7876648
    if entry_username_text.get() == d["username"] and entry_password_text.get() == d["password"]:
        login.destroy()
        new_window(d["username"])

def generate_random_users():
    for users in range(400):
        d = {}
        d["username"] = "".join(random.choice(string.ascii_lowercase) if i < 4 else str(random.randrange(10)) for i in range(10))
        d["password"] = "".join(random.choice(string.ascii_lowercase) for i in range(4)) + "@" + "".join(str(random.randrange(10)) for i in range(7))
        DatabaseAtlas.insertOne("random_usernames", d)

#generate_random_users()

btn = Button(login, text = "Login", command = user_login).pack(pady = 11)

login.mainloop()
