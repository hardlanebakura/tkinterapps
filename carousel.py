from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.geometry("290x280")
root.title("App")

IMAGES = ("heart.jpeg", "teletubbies.jpg", "squirtle.png", "alakazam.jpg")

get_image = lambda image_src: ImageTk.PhotoImage(Image.open(f"carousel_images/{image_src}"))

image = get_image(IMAGES[0])
image_text = StringVar(root, IMAGES[0])

#The tk.Frame object isnt a pure python object, rather its an wrapped object in a tcl interpreter and thats why you can't address the attributes you intuitively think you can.
#You need to adress the attributes in a way the tcl interpreter is able to handle and therefore methods are created like widget.configure.
class PyLabel(Label):
    def __init__(self,master,**kwargs):
        super().__init__(master)
        self.configure(**kwargs)

label_img = PyLabel(root, image=image, height=180, width=220)
label_img.grid(row = 0, column = 1, pady = 20)

def move_button_back():
    global label_img
    global button_forward
    active_item = IMAGES.index(image_text.get())
    status["text"] = set_status_text(active_item)
    image_name = IMAGES[active_item - 1]
    image_src = get_image(IMAGES[active_item - 1])
    image_text.set(image_name)
    label_img.configure(image = image_src)
    label_img.image = image_src
    active_item = active_item - 1
    if active_item == 0:
        button_back["state"] = "disabled"
    button_forward["state"] = "normal"

def move_button_forward():
    global label_img
    global button_forward
    global button_back
    global status
    active_item = IMAGES.index(image_text.get())
    status["text"] = set_status_text(active_item + 2)
    image_name = IMAGES[active_item + 1]
    image_src = get_image(IMAGES[active_item + 1])
    image_text.set(image_name)
    #configure is needed in order to prevent delete
    label_img.configure(image = image_src)
    label_img.image = image_src
    if active_item == len(IMAGES) - 2:
        button_forward["state"] = "disabled"
    button_back["state"] = "normal"

set_status_text = lambda i: f"Image {i} of {len(IMAGES)}"

button_back = Button(root, text = "<<", command=lambda: move_button_back(), state="disabled")
button_back.grid(row = 0, column = 0, pady = 20)
button_forward = Button(root, text = ">>", command=lambda: move_button_forward())
button_forward.grid(row = 0, column = 2, pady = 20)

status = Label(root, text = f"Image 1 of {len(IMAGES)}", bd = 1, padx = 19, pady = 4, relief = SUNKEN)
status.place(relx = 0.5, rely = 0.9, anchor = CENTER)

root.mainloop()