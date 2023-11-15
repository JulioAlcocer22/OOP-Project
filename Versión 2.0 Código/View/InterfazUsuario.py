from tkinter import *
import tkinter as tk
from tkinter import messagebox

from Controller.Configuracion import Configuracion
from Controller.AccionesBoton import AccionesBoton



class InterfazUsuario:

    def __init__(self):
        pass

    def Mostrar(self):
        if Configuracion.lenguajeSOEsEspañol():
            window = tk.Tk()
            window.title("LinkedIn Scraper")
            window.geometry("900x350")
            window.configure(bg="white")
            window.resizable(width=False, height=False)
            accionesBoton = AccionesBoton()

            # -----------------------------------------------------------
            etiqueta1 = Label(window, font="Forte 17",
                              text="Busqueda", width=20)
            etiqueta1.place(x=20, y=30)

            botonPorCadena = tk.Button(
                window, text="Por cadena", font="Georgia 12 ", command=lambda: accionesBoton.metodoCadena(), width=22, height=1)
            botonPorCadena.place(x=20, y=90)

            botonPorUrl = tk.Button(
                window, text="Por URL", font="Georgia 12 ", command=lambda: accionesBoton.metodoUrl(), width=22, height=1)
            botonPorUrl.place(x=20, y=160)

            botonActualizarPivotes = tk.Button(
                window, text="Actualizar pivotes", font="Georgia 12", command=lambda: accionesBoton.actualizarPivotes(), width=22, height=1)
            botonActualizarPivotes.place(x=20, y=230)

            botonTodosPivotes = tk.Button(
                window, text="Por pivotes", font="Georgia 12", command=lambda: accionesBoton.metodoPivotes(), width=22, height=1)
            botonTodosPivotes.place(x=20, y=300)

            # -----------------------------------------------------------

            etiqueta2 = Label(window, font="Forte 17",
                              text="Extraccion", width=20)
            etiqueta2.place(x=300, y=30)

            botonExtraer = tk.Button(window, text="Extraer experiencia", font="Georgia 12 ",
                                      command=lambda: accionesBoton.extraccionDeExperiencia(), width=22, height=1)
            botonExtraer.place(x=300, y=90)

            etiqueta3 = Label(window, font="Forte 17", text="Filtrar Links", width=20)
            etiqueta3.place(x=300, y=160)
            
            botonTest = tk.Button(window, text="Filtrar LIS", font="Georgia 12 ",
                                   command=lambda: accionesBoton.filtrarLIS(), width=22, height=1)
            botonTest.place(x=300, y=230)
            
            botonTest = tk.Button(window, text="Filtrar LCC", font="Georgia 12 ",
                                   command=lambda: accionesBoton.filtrarLCC(), width=22, height=1)
            botonTest.place(x=300, y=300)

            # -----------------------------------------------------------

            etiqueta4 = Label(window, font="Forte 17", text="Limpiar DB", width=20)
            etiqueta4.place(x=600, y=30)
            
            botonLimpiar = tk.Button(window, text="Borrar marca A", font="Georgia 12 ",
                                   command=lambda: accionesBoton.limpiezaA(), width=22, height=1)
            botonLimpiar.place(x=600, y=90)
            
            botonLimpiar = tk.Button(window, text="Borrar marca B", font="Georgia 12 ",
                                   command=lambda: accionesBoton.limpiezaB(), width=22, height=1)
            botonLimpiar.place(x=600, y=160)

            
            
            

            window.mainloop()
        else:
            messagebox.showerror(
                "Error", "El sistema operativo no se encuentra en español. La aplicación se cerrará.")






