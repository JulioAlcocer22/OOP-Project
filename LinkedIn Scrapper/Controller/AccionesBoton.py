from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import tkinter as tk

from Controller.Configuracion import Configuracion
from Model.ScrapperPerfiles import ScrapperPerfiles
from Model.Utilidades import Utilidades
from Model.ScraperDatos import ScraperDatos
from Model.linkVM import linkVM

from DataBaseProyect.Controller.DBController import DBController

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
            resultaddoIteracion = scraper.iteradorUrls.iniciarIteracion(
                resultadoBusqueda)

            Utilidades.test(resultaddoIteracion)
            # Regresa el arreglo, aqui iria la funcion que toma el arreglo y envia elemento por elemento a la base de datos
            driver.close()
            for link in resultaddoIteracion:
                link = linkVM(link)
                DBController.insertlink(link)

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
            for link in resultaddoIteracion:
                link = linkVM(link)
                DBController.insertlink(link)

    def actualizarPivotes(self):

        response = messagebox.askquestion(
            "Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
        if response == "yes":
            driver = Utilidades.ingresoAPaginaConSesionIniciada()()

            driver.get(
                "https://www.linkedin.com/mynetwork/invite-connect/connections/")

            scraper = ScrapperPerfiles(driver)
            resultaddoIteracion = scraper.scrappearLinks.obtener_links()

            Utilidades.test(resultaddoIteracion)
            # Regresa el arreglo, aqui iria la funcion que toma el arreglo y envia elemento por elemento a la base de datos
            driver.close()
            for link in resultaddoIteracion:
                link = linkVM(link)
                DBController.insertPivote(link)

    def metodoPivotes(self):
        response = messagebox.askquestion(
            "Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
        if response == "yes":
            # Supongamos que recibio uno por uno los links de mis pivotes de la db
            # Por cuestiones practicas usaremos el link de cambranes como prueba
            driver = Utilidades.ingresoAPaginaConSesionIniciada()

            scraper = ScrapperPerfiles(driver)

            for linkpivote in DBController.recuperarPivotes():
                resultadoBusqueda = scraper.busquedaUrl.porPivote(linkpivote)
                resultaddoIteracion = scraper.iteradorUrls.iniciarIteracion(
                    resultadoBusqueda)

                Utilidades.test(resultaddoIteracion)
                # Regresa el arreglo, aqui iria la funcion que toma el arreglo y envia elemento por elemento a la base de datos
                driver.close()
                for link in resultaddoIteracion:
                    link = linkVM(link)
                    DBController.insertlink(link)

    def extraccionDeExperiencia(self):
        response = messagebox.askquestion(
            "Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
        if response == "yes":

            for egresado in DBController.recuperarEgresadoInfoEstudios('FMAT', 'LIS'):
                driver = Utilidades.forzarIngresoAPaginaSinSesionIniciada(egresado)

                scraper = ScraperDatos(driver)
                resultadoSimple = scraper.CampoSimple()
                resultadoCompuesto = scraper.CampoCompuesto()
                #unir listas de resultados
                resultadoSimple.extend(resultadoCompuesto)
                # scraper.unicamenteDescripciones()

                driver.close()
                for experiencia in resultadoSimple:
                    DBController.insertExperiencia(egresado, experiencia)

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

        for link in DBController.recuperarTodosLink():
            driver = Utilidades.forzarIngresoAPaginaSinSesionIniciada(link)
            scraper = ScraperDatos(driver)

            if scraper.verificarUniversidad_Carrera_Egresado("Universidad Autónoma de Yucatán", "UADY", "Ingeniería de Software") and scraper.verificarExperiencia():
                print("Cumple las condiciones, metiendo a base de datos")
                DBController.insertEgresadoInfo(link, 'nombre', 'Universidad Autónoma de Yucatán', "Ingeniería de Software")
                

    def filtrarLCC(self):

        for link in DBController.recuperarTodosLink():
            driver = Utilidades.forzarIngresoAPaginaSinSesionIniciada(link)
            scraper = ScraperDatos(driver)

            if scraper.verificarUniversidad_Carrera_Egresado("Universidad Autónoma de Yucatán", "Ciencias Computacionales") and scraper.verificarExperiencia():
                print("Cumple las condiciones, metiendo a base de datos")
                DBController.insertEgresadoInfo(link, 'nombre', 'Universidad Autónoma de Yucatán', "Ciencias Computacionales")