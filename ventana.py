from tkinter import *

#creacion de la ventana de la aplicacion
class ventana (Frame):

    def __init__(self, master=None):
        super().__init__(master, width=680, height=260)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        pass