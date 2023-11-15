from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import tkinter as tk


from Controller.Configuracion import Configuracion
from Model.ScrapperPerfiles import ScrapperPerfiles
from Model.Utilidades import Utilidades
from Model.ScraperDatos import ScraperDatos


class AccionesBoton:

    def __init__(self):
        pass

    def metodoCadena(self):
        entradaCadena = simpledialog.askstring(
            "Entrada de texto", "Ingrese la cadena que desea buscar:")
        if entradaCadena:

            driver = Utilidades.ingresoAPaginaConSesionIniciada()

            scraper = ScrapperPerfiles(driver)

            resultadoBusqueda = scraper.busquedaUrl.porCadena(entradaCadena)
            resultaddoIteracion = scraper.iteradorUrls.iniciarIteracion(resultadoBusqueda)

            Utilidades.test(resultaddoIteracion)

            # Regresa el arreglo, aqui iria la funcion que toma el arreglo y envia elemento por elemento a la base de datos
            driver.close()

    def metodoUrl(self):
        entradaURL = simpledialog.askstring(
            "Entrada de texto", "Ingrese la URL que desea buscar:")
        if entradaURL:
            driver = Utilidades.ingresoAPaginaConSesionIniciada()

            scraper = ScrapperPerfiles(driver)
            resultaddoIteracion = scraper.iteradorUrls.iniciarIteracion(
                entradaURL)

            Utilidades.test(resultaddoIteracion)
            # Regresa el arreglo, aqui iria la funcion que toma el arreglo y envia elemento por elemento a la base de datos
            driver.close()

    def actualizarPivotes(self):

        response = messagebox.askquestion(
            "Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
        if response == "yes":
            driver = Utilidades.ingresoAPaginaConSesionIniciada()

            driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")

            scraper = ScrapperPerfiles(driver)
            resultaddoIteracion = scraper.scrappearLinks.obtener_links()

            Utilidades.test(resultaddoIteracion)
            print("fin")
            # Regresa el arreglo, aqui iria la funcion que toma el arreglo y envia elemento por elemento a la base de datos
            driver.close()

    def metodoPivotes(self):
        response = messagebox.askquestion(
            "Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
        if response == "yes":
            # Supongamos que recibio uno por uno los links de mis pivotes de la db
            # Por cuestiones practicas usaremos el link de cambranes como prueba
            driver = Utilidades.ingresoAPaginaConSesionIniciada()

            scraper = ScrapperPerfiles(driver)

            resultadoBusqueda = scraper.busquedaUrl.porPivote("https://www.linkedin.com/in/pablo-baeza/")
            resultaddoIteracion = scraper.iteradorUrls.iniciarIteracion(resultadoBusqueda)

            Utilidades.test(resultaddoIteracion)
            # resultaddoIteracion - Regresa el arreglo, aqui iria la funcion que toma el arreglo y envia elemento por elemento a la base de datos
            driver.close()

    def extraccionDeExperiencia(self):
        response = messagebox.askquestion(
            "Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
        if response == "yes":

            egresado = "https://www.linkedin.com/in/ecambranes/"
            driver = Utilidades.forzarIngresoAPaginaSinSesionIniciada(egresado)

            scraper = ScraperDatos(driver)
            scraper.CampoSimple()
            scraper.CampoCompuesto()
            

            driver.close()
            # https://mx.linkedin.com/in/viviana-guadalupe-azcorra-novelo-351706231
            # https://www.linkedin.com/in/luis-basto-diaz-41136396/
            # https://mx.linkedin.com/in/edgar-cambranes
            #https://mx.linkedin.com/in/edwin-fajardo

    def testConexiones(self):
        response = messagebox.askquestion(
            "Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
        if response == "yes":
            if Configuracion.testConexiones("www.google.com"):
                tk.messagebox.showinfo(
                    "Información", "La conexion a internet es estable")
            else:
                tk.messagebox.showerror(
                    "Error", "La conexion a internet es inestable")

    def filtrarLIS(self):

        egresado = "https://mx.linkedin.com/in/eduardocanchevazquez"
        driver = Utilidades.forzarIngresoAPaginaSinSesionIniciada(egresado)
        scraper = ScraperDatos(driver)

        if scraper.verificarUniversidad_Carrera_Egresado("Universidad Autónoma de Yucatán", "UADY", "Ingeniería de Software") and scraper.verificarExperiencia():
            print("Cumple las condiciones, metiendo a base de datos")

    def filtrarLCC(self):

        egresado = "https://www.linkedin.com/in/luis-basto-diaz-41136396/"
        driver = Utilidades.forzarIngresoAPaginaSinSesionIniciada(egresado)
        scraper = ScraperDatos(driver)

        if scraper.verificarUniversidad_Carrera_Egresado("Universidad Autónoma de Yucatán",  "UADY", "Ciencias Computacionales") and scraper.verificarExperiencia():
            print("Cumple las condiciones, metiendo a base de datos")

    def limpiezaA(self):

        print("Se ejecuto la limpieza A")

    def limpiezaB(self):

        print("Se ejecuto la limpieza B")
