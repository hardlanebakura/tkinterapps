from tkinter import *
from _datetime import datetime
from pygame import mixer
import time
from threading import Timer

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

root = Tk()

root.title("App")
root.geometry("381x287")
root.iconbitmap("logoicon.ico")

frame_1 = LabelFrame(root, height = 104, bg = "green")
frame_1.place(relx = 0.4, rely = 0.3)

frame_2 = LabelFrame(frame_1, height = 94, width = 148, bg = "#000")
frame_2.grid(padx = 1, pady = 1)

label_h = Label(frame_2, width = 3, text = "00", fg = "green", bg = "#000")
label_h.grid(row = 0, column = 0)

mixer.init()

def get_entry_h_text(text):
    if len(text.get()) == 2:
        text_content = text.get() if re.match('^([0-1][0-9]|2[0-3])', text.get()) is not None else ""
        text.set(text_content)
    elif len(text.get()) == 3:
        text.set(text.get()[-1])

def get_entry_m_text(text):
    if len(text.get()) == 2:
        text_content = text.get() if re.match('^([0-5][0-9])', text.get()) is not None else ""
        text.set(text_content)
    elif len(text.get()) == 3:
        text.set(text.get()[-1])

def get_clicks(e):
    if e.widget == label_h:
        label_h.grid_forget()
        entry_h.grid(row = 0, column = 0)
        entry_m.grid_forget()
        label_m["text"] = entry_m_text.get()
        label_m.grid(row = 0, column = 2)
    elif e.widget == label_m:
        label_m.grid_forget()
        entry_m.grid(row = 0, column = 2)
        entry_h.grid_forget()
        label_h["text"] = entry_h_text.get()
        label_h.grid(row = 0, column = 0)
    elif e.widget == entry_h or e.widget == entry_m:
        pass
    else:
        label_h["text"] = entry_h_text.get()
        label_h.grid(row=0, column=0)
        entry_m.grid_forget()
        label_m["text"] = entry_m_text.get()
        label_m.grid(row=0, column=2)
        entry_h.grid_forget()
        [h, m] = datetime.now().strftime("%H:%M").split(":")
        [h1, m1] = [entry_h_text.get(), entry_m_text.get()]
        if h == h1 and m == m1:
            mixer.music.load("keys_mp3/A5.wav")
            mixer.music.play(-1)

def set_timers():
    entry_m.grid_forget()
    label_m["text"] = entry_m_text.get()
    label_m.grid(row=0, column=2)
    entry_h.grid_forget()
    label_h["text"] = entry_h_text.get()
    label_h.grid(row=0, column=0)

#periodically check if current time is displayed on the alarm clock
def get_time():
    [h, m] = datetime.now().strftime("%H:%M").split(":")
    [h1, m1] = [entry_h_text.get(), entry_m_text.get()]
    if h == h1 and m == m1:
        mixer.music.load("keys_mp3/A5.wav")
        mixer.music.play(-1)
        btn_stop_alarm.grid(padx = 153, pady = 40)
    else:
        btn_stop_alarm.grid_forget()

rt = RepeatedTimer(1, get_time)

def stop_alarm():
    btn_stop_alarm.grid_forget()
    rt.stop()

entry_h_text = StringVar()
entry_h_text.set("00")
entry_h_text.trace("w", lambda name, index, mode, text=entry_h_text: get_entry_h_text(entry_h_text))

entry_h = Entry(frame_2, width = 3, textvariable = entry_h_text)

entry_m_text = StringVar()
entry_m_text.set("00")
entry_m_text.trace("w", lambda name, index, mode, text=entry_m_text: get_entry_m_text(entry_m_text))

entry_m = Entry(frame_2, width = 3, textvariable = entry_m_text)

label_middle = Label(frame_2, text = ":", fg = "green", bg = "#000").grid(row = 0, column = 1)

label_m = Label(frame_2, width = 3, text = "00", fg = "green", bg = "#000")
label_m.grid(row = 0, column = 2)

btn_stop_alarm = Button(root, text = "Stop alarm!", command = stop_alarm)

root.bind("<Escape>", lambda e: root.destroy())

root.bind("<Button-1>", lambda e: get_clicks(e))

root.mainloop()