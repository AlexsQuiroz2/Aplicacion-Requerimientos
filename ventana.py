from tkinter import *

#creacion de la ventana de la aplicacion
class ventana (Frame):

    def __init__(self, master=None):
        super().__init__(master, width=1366, height=768)
        self.master = master
        self.pack()
        self.create_widgets()

    def fNuevo(self):
        pass

    def fModificar(self):
        pass

    def fEliminar(self):
        pass

    def create_widgets(self):
        #---------------Primera seccino---------------
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0, width=210, height=768)

        #Bonton de Nuevo
        self.btnNuevo=Button(frame1, text="Nuevo", command=self.fNuevo, bg="blue", fg="white")
        self.btnNuevo.place(x=45, y=30, width=110, height=50)

        #Boton de Modificar
        self.btnModificar=Button(frame1, text="Modificar", command=self.fNuevo, bg="blue", fg="white")
        self.btnModificar.place(x=45, y=90, width=110, height=50)

        #Bonton de Eliminar
        self.btnEliminar=Button(frame1, text="Eliminar", command=self.fNuevo, bg="blue", fg="white")
        self.btnEliminar.place(x=45, y=150, width=110, height=50)

        #---------------Segunda seccion---------------
        frame2 = Frame(self, bg="#d3dde3")
        frame2.place(x=215, y=0, width=390, height=768)

        #entrada de datos
        lbl = Label(frame2, text=("Llene los siguiente campos"))
        lbl.place(x=6, y=30)

        lbl1 = Label(frame2, text="Id: ")
        lbl1.place(x=6, y=130)

        self.txtCampaña=Entry(frame2)
        self.txtCampaña.place(x=6, y=150, width=350, height=50)

        lbl2 = Label(frame2, text="Campaña: ")
        lbl2.place(x=6, y=230)

        self.txtSerie=Entry(frame2)
        self.txtSerie.place(x=6, y=250, width=350, height=50)

        lbl3 = Label(frame2, text="Service Tag: ")
        lbl3.place(x=6, y=330)

        self.txtCampaña=Entry(frame2)
        self.txtCampaña.place(x=6, y=350, width=350, height=50)

        lbl4 = Label(frame2, text="Hostname: ")
        lbl4.place(x=6, y=430)

        self.txtCampaña=Entry(frame2)
        self.txtCampaña.place(x=6, y=450, width=350, height=50)

        #Bonton de Guardar
        self.btnNuevo=Button(frame2, text="Guardar", command=self.fNuevo, bg="#33CC66", fg="white")
        self.btnNuevo.place(x=125, y=530, width=110, height=50)
        
        #Bonton de Cancelar
        self.btnNuevo=Button(frame2, text="Cancelar", command=self.fNuevo, bg="red", fg="white")
        self.btnNuevo.place(x=245, y=530, width=110, height=50)