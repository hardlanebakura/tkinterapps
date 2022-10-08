from tkinter import *
import matplotlib
from database import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

matplotlib.use('TkAgg')

db.cursor.execute("SELECT * FROM fragile_states_indexes LIMIT 5")
fsi = db.cursor.fetchall()
fsi_data = dict(zip([country[1] for country in fsi], [country[2] for country in fsi]))

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter Matplotlib Demo')

        # prepare data
        data = fsi_data
        languages = data.keys()
        popularity = data.values()

        # create a figure
        figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, self)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(languages, popularity)
        axes.set_title("Fragile states indexes")
        axes.set_ylabel("Indexes")

        figure_canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self._add_exit_shortcut()

    def _add_exit_shortcut(self):
        self.bind("<Escape>", lambda e: self.destroy())

if __name__ == '__main__':
    app = App()
    app.mainloop()