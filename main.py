
from menus.menu import Menu
from app import App
import tkinter as tk

if __name__ == "__main__":
    modo = input("Elige el modo de ejecución (1 = Interfaz gráfica, 2 = Consola): ")
    if modo == "1":
        ventana = tk.Tk()
        app = App(ventana)
        ventana.mainloop()
    else:
        menu = Menu()
        menu.mostrar_menu()
