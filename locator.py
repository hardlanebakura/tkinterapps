from geopy.geocoders import Nominatim
from tkinter import *

def getinfo():
    geolocator = Nominatim(user_agent="geoapiExercises")
    place = e.get()
    place_res.set(place)
    location = geolocator.geocode(place)
    res.set(location)

# object of tkinter
# and background set for light grey
master = Tk()
master.configure(bg='light grey')

# variable Classes in tkinter
place_res = StringVar()
res = StringVar()

# creating label for each information
# name using widget Label
Label(master, text="Enter place :",
      bg="light grey").grid(row=0, sticky=W)
Label(master, text="Place :",
      bg="light grey").grid(row=1, sticky=W)
Label(master, text="Country Address :",
      bg="light grey").grid(row=2, sticky=W)

# creating label for class variable
# name using widget Entry
Label(master, text="", textvariable=place_res,
      bg="light grey").grid(row=1, column=1, sticky=W)
Label(master, text="", textvariable=res,
      bg="light grey").grid(row=2, column=1, sticky=W)

e = Entry(master)
e.grid(row=0, column=1)

# creating a button using the widget
# Button that will call the submit function
b = Button(master, text="Show", command=getinfo)
b.grid(row=0, column=2, columnspan=2,
       rowspan=2, padx=5, pady=5)

master.mainloop()

