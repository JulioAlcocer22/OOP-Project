
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import tkinter as tk
import sys

from selenium.webdriver.common.by import By
from app import *
from app.Controller.Configuracion import Configuracion
from app.Model.ScrapperPerfiles import ScrapperPerfiles
from app.Model.Utilidades import Utilidades
from app.Model.ScraperDatos import ScraperDatos


class AccionesBoton:

    def __init__(self, querys):
        self.querys = querys

    def metodoCadena(self):
        entradaCadena = simpledialog.askstring(
            "Entrada de texto", "Ingrese la cadena que desea buscar:")
        if entradaCadena:

            driver = Utilidades.ingresoAPaginaConSesionIniciada()

            scraper = ScrapperPerfiles(driver)
            resultadoBusqueda = scraper.busquedaUrl.porCadena(entradaCadena)
            resultaddoIteracion = scraper.iteradorUrls.iniciarIteracion(resultadoBusqueda)

            for link in resultaddoIteracion:
                self.insertlink(link)
            # Utilidades.test(resultaddoIteracion)

            driver.close()

    def metodoUrl(self):
        entradaURL = simpledialog.askstring(
            "Entrada de texto", "Ingrese la URL que desea buscar:")
        if entradaURL:
            driver = Utilidades.ingresoAPaginaConSesionIniciada()

            scraper = ScrapperPerfiles(driver)
            resultaddoIteracion = scraper.iteradorUrls.iniciarIteracion(entradaURL)

            for link in resultaddoIteracion:
                self.insertlink(link)
            # Utilidades.test(resultaddoIteracion)

            driver.close()

    def actualizarPivotes(self):

        response = messagebox.askquestion(
            "Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
        if response == "yes":
            driver = Utilidades.ingresoAPaginaConSesionIniciada()

            driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")

            scraper = ScrapperPerfiles(driver)
            resultaddoIteracion = scraper.scrappearLinks.obtener_links()
            
            for link in resultaddoIteracion:
                self.insertPivote(link)

            # Utilidades.test(resultaddoIteracion)
            
            driver.close()

    def metodoPivotes(self):
        response = messagebox.askquestion(
            "Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
        if response == "yes":
            # Supongamos que recibio uno por uno los links de mis pivotes de la db
            # Por cuestiones practicas usaremos el link de BASTO como prueba
            for pivote in self.recuperarPivotes():
                driver = Utilidades.ingresoAPaginaConSesionIniciada()

                scraper = ScrapperPerfiles(driver)
                
                resultadoBusqueda = scraper.busquedaUrl.porPivote(pivote[0])
                resultadoIteracion = scraper.iteradorUrls.iniciarIteracion(resultadoBusqueda)

                for link in resultadoIteracion:
                    self.insertlink(link)

                # Utilidades.test(resultadoIteracion)
                # resultaddoIteracion - Regresa el arreglo, aqui iria la funcion que toma el arreglo y envia elemento por elemento a la base de datos
            driver.close()

    def metodoPivotesUnico(self):
            # "https://www.linkedin.com/in/luis-basto-diaz-41136396/"
            entradaURL = simpledialog.askstring(
                "Entrada de texto", "Ingrese la URL del pivote que desea buscar:")
            if entradaURL:
                # Supongamos que recibio uno por uno los links de mis pivotes de la db
                # Por cuestiones practicas usaremos el link de BASTO como prueba
                driver = Utilidades.ingresoAPaginaConSesionIniciada()

                scraper = ScrapperPerfiles(driver)

                resultadoBusqueda = scraper.busquedaUrl.porPivote(entradaURL)
                resultadoIteracion = scraper.iteradorUrls.iniciarIteracion(resultadoBusqueda)
                
                for link in resultadoIteracion:
                    self.insertlink(link)

                # Utilidades.test(resultadoIteracion)
                # resultaddoIteracion - Regresa el arreglo, aqui iria la funcion que toma el arreglo y envia elemento por elemento a la base de datos
                driver.close()

    def extraccionDeExperiencia(self):
            response = messagebox.askquestion(
                "Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
            if response == "yes":

                matrizResultado = []

                #aQUI VA EL ARREGLO DE 6 EN 6 QUE VIENE DE LA BASE DE DATOS
                # cambiar parametros a la funcion de arreglo definitivo por "Universidad Autonoma de Yucatan" y "Ciencias de la Computacion"
                arregloDefinitivo = self.recuperarEgresadoInfoEstudios("Universidad Autonoma de Yucatan", "Ingenieria de Software")
                for egresadoLink in arregloDefinitivo:
                    linkEgresado = egresadoLink[0]

                    driver, error = Utilidades.forzarIngresoAPaginaSinSesionIniciada(linkEgresado)
                    if error is not False:
                        continue

                    scraper = ScraperDatos(driver)
                    matrizCampoSimple = scraper.CampoSimple(linkEgresado)
                    matrizCampoCompuesto = scraper.CampoCompuesto(linkEgresado)
                    matrizResultado = matrizResultado + matrizCampoSimple + matrizCampoCompuesto

                    driver.close()

                for experiencia in matrizResultado: #aQUI ES DONDE SE ENVIAN LOS DATOS A LA DB
                    #Modificar la funcion de insertExperiencia con "Universidad Autonoma de Yucatan" y "Ciencias de la Computacion"
                    self.insertExperiencia(experiencia[0], "Universidad Autonoma de Yucatan", "Ingenieria de Software", experiencia[1], experiencia[2], experiencia[6], experiencia[5], experiencia[3], experiencia[4])
                sys.exit() # Se cierra por logica del negocio  

    def filtrarLIS(self):
        response = messagebox.askquestion(
            "Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
        if response == "yes":
        
            matrizResultado = []

            arregloDefinitivo = self.recuperarTodosLink(6) # Arreglo que viene de 6 en 6 de la base de datos

            for egresadoLink in arregloDefinitivo:
                
                linkEgresado = egresadoLink[0]
                
                driver, error = Utilidades.forzarIngresoAPaginaSinSesionIniciada(linkEgresado)
                if error is not False:
                    continue

                scraper = ScraperDatos(driver)

                arregloNombreEgresado = driver.find_elements(By.TAG_NAME, 'h1')
                nombreEgresado = arregloNombreEgresado[0].text

                if scraper.verificarUniversidad_Carrera_Egresado("Universidad Autónoma de Yucatán", "UADY", "Ingeniería de Software", "Software Engineering") and scraper.verificarExperiencia():
                    matrizResultado.append([nombreEgresado, linkEgresado])

                self.linkVisitado(linkEgresado)
                driver.delete_all_cookies()
                driver.close()

            for egresado in matrizResultado:
                self.insertEgresadoInfo(egresado[1], egresado[0], "Universidad Autonoma de Yucatan", "Ingenieria de Software")
            sys.exit() # Se cierra por logica del negocio

    def filtrarLCC(self):

        response = messagebox.askquestion(
            "Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
        if response == "yes":

            matrizResultado = []

            arregloDefinitivo = self.recuperarTodosLink(6) # Arreglo que viene de 6 en 6 de la base de datos

            for egresadoLink in arregloDefinitivo:
                
                linkEgresado = egresadoLink[0]

                driver, error = Utilidades.forzarIngresoAPaginaSinSesionIniciada(linkEgresado)
                if error is not False:
                    continue

                scraper = ScraperDatos(driver)

                arregloNombreEgresado = driver.find_elements(By.TAG_NAME, 'h1')
                nombreEgresado = arregloNombreEgresado[0].text

                if scraper.verificarUniversidad_Carrera_Egresado("Universidad Autónoma de Yucatán", "UADY", "Ciencias de la Computacion", "Computer Science") and scraper.verificarExperiencia():
                    matrizResultado.append([nombreEgresado, linkEgresado])

                self.linkVisitado(linkEgresado)
                driver.delete_all_cookies()
                driver.close()
                
            for egresado in matrizResultado:
                self.insertEgresadoInfo(egresado[1], egresado[0], "Universidad Autonoma de Yucatan", "Ciencias de la Computacion")
                
            sys.exit() # Se cierra por logica del negocio

    def limpiezaA(self):
        print("Se ejecuto la limpieza A")

    def limpiezaB(self):
        print("Se ejecuto la limpieza B")

    def probarConexiones(self):
        response = messagebox.askquestion(
            "Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
        if response == "yes":
            if Configuracion.testConexiones("www.google.com"):
                tk.messagebox.showinfo("Información", "La conexion a internet es estable")
            else:
                tk.messagebox.showerror("Error", "La conexion a internet es inestable")

    def recuperarPivotes(self):
        return self.querys.recuperarPivotes()    

    def insertlink(self, link):
        self.querys.insertLink(link, 0)
        
    def insertPivote(self, link):
        self.querys.insertLink(link, 1)
    
    def recuperarTodosLink(self, limite):
        return self.querys.recuperarTodosLink(limite)
    
    def linkVisitado(self, link):
        self.querys.linkRevisado(link)
    
    def insertEgresadoInfo(self, link, nombre, universidad, carrera):
        idlink = self.querys.recuperarIdLink(link)
        self.querys.insertEgresadoInfo(idlink[0], nombre, universidad, carrera)
    
    def recuperarEgresadoInfoEstudios(self, universidad, carrera):
        return self.querys.recuperarEgresadoInfoEstudios(universidad, carrera)
    
    def insertExperiencia(self, link, universidad, carrera, empresa, puesto, descripcion, duracion, fechaInicio, fechaFin):
        idlink = self.querys.recuperarIdLink(link)
        idEgresado = self.querys.recuperarEgresadoInfo(idlink[0], universidad, carrera)
        self.querys.insertExperiencia(idEgresado[0], empresa, puesto, descripcion, duracion, fechaInicio, fechaFin)
        
    def recuperarTodosExperiencia(self):
        return self.querys.recuperarTodosExperiencia()
    
    def insertEgresados(self, idEgresado, idExperiencia, Rol):
        self.querys.insertEgresados(idEgresado, idExperiencia, Rol)


   