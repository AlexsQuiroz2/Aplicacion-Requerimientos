from tkinter import *

#creacion de la ventana de la aplicacion
class ventana (Frame):

    def __init__(self, master=None):
        super().__init__(master, width=680, height=260)
        self.master = master
        self.pack()
        self.create_widgets()

    def fNuevo(self):
        pass

    def create_widgets(self):
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0, width=93, height=259)

        #creacion del bonton de Nuevo
        self.btnNuevo=Button(frame1, text="Nuevo", command=self.fNuevo, bg="blue", fg="white")
        self.btnNuevo.place(x=5, y=50, width=80, height=30)