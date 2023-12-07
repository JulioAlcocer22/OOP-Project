from tkinter import *
import tkinter as tk
from tkinter import messagebox
from app.DataBase.Querys import Querys

from app import *
from app.Controller.Configuracion import Configuracion
from app.Controller.AccionesBoton import AccionesBoton

class InterfazUsuario:

    def __init__(self, querys):
        self.querys = querys

    def Mostrar(self):
        if Configuracion.lenguajeSOEsEspañol():
            window = tk.Tk()
            window.title("LinkedIn Scraper")
            window.geometry("900x450")
            window.configure(bg="white")
            window.resizable(width=False, height=False)
            accionesBoton = AccionesBoton(self.querys)

            # -----------------------------------------------------------
            
            etiquetaBusqueda = Label(window, font="Forte 17",
                              text="Busqueda", width=20)
            etiquetaBusqueda.place(x=20, y=30)

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
                window, text="Por pivotes ( Premium )", font="Georgia 12", command=lambda: accionesBoton.metodoPivotes(), width=22, height=1)
            botonTodosPivotes.place(x=20, y=300)

            botonPivoteUnico = tk.Button(
                window, text="Pivote Unico", font="Georgia 12", command=lambda: accionesBoton.metodoPivotesUnico(), width=22, height=1)
            botonPivoteUnico.place(x=20, y=370)

            # -----------------------------------------------------------

            etiquetaExtraccion = Label(window, font="Forte 17",
                              text="Extraccion", width=20)
            etiquetaExtraccion.place(x=300, y=30)

            botonExtraerLIS = tk.Button(window, text="Extraer experiencia LIS", font="Georgia 12 ",
                                      command=lambda: accionesBoton.extraccionDeExperienciaLIS(), width=22, height=1)
            botonExtraerLIS.place(x=300, y=90)
            
            botonExtraerLCC = tk.Button(window, text="Extraer experiencia LCC", font="Georgia 12 ",
                                      command=lambda: accionesBoton.extraccionDeExperienciaLCC(), width=22, height=1)
            botonExtraerLCC.place(x=300, y=120)
            
            # -----------------------------------------------------------

            etiquetaFiltrarLinks = Label(window, font="Forte 17", text="Filtrar Links", width=20)
            etiquetaFiltrarLinks.place(x=300, y=160)
            
            botonFiltrarLIS = tk.Button(window, text="Filtrar LIS", font="Georgia 12 ",
                                   command=lambda: accionesBoton.filtrarLIS(), width=22, height=1)
            botonFiltrarLIS.place(x=300, y=230)

            botonFiltrarLCC = tk.Button(window, text="Filtrar LCC", font="Georgia 12 ",
                                   command=lambda: accionesBoton.filtrarLCC(), width=22, height=1)
            botonFiltrarLCC.place(x=300, y=300)

            # -----------------------------------------------------------

            etiquetaLimpiarDB = Label(window, font="Forte 17", text="Limpiar DB", width=20)
            etiquetaLimpiarDB.place(x=600, y=30)
            
            botonLimpiarA = tk.Button(window, text="Borrar marca A", font="Georgia 12 ",
                                   command=lambda: accionesBoton.limpiezaA(), width=22, height=1)
            botonLimpiarA.place(x=600, y=90)
            
            botonLimpiarB = tk.Button(window, text="Borrar marca B", font="Georgia 12 ",
                                   command=lambda: accionesBoton.limpiezaB(), width=22, height=1)
            botonLimpiarB.place(x=600, y=160)
            
            botonTestConexiones = tk.Button(window, text="Probar Conexiones", font="Georgia 12 ",
                                   command=lambda: accionesBoton.probarConexiones(), width=22, height=1)
            botonTestConexiones.place(x=600, y=230)

            botonALN1 = tk.Button(window, text="Accion ALN 1", font="Georgia 12 ",
                                   command=lambda: accionesBoton.AccionALN1(), width=22, height=1)
            botonALN1.place(x=600, y=300)

            botonALN2 = tk.Button(window, text="Accion ALN 2", font="Georgia 12 ",
                                   command=lambda: accionesBoton.AccionALN2(), width=22, height=1)
            botonALN2.place(x=600, y=370)

            window.mainloop()
            
        else:
            messagebox.showerror(
                "Error", "El sistema operativo no se encuentra en español. La aplicación se cerrará.")






