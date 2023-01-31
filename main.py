from tkinter import *
from ventana import *

#ciclo de uso autonomo de la aplicacion
def main():
    root = Tk()
    root.wm_title("Aplicacion de verificaion de requerimientos")
    app = ventana(root)
    app.mainloop()


if __name__ == "__main__":
    main()
