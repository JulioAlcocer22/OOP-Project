from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import tkinter as tk
from Controller.RS_uady_software import RS_uady_software

from selenium.webdriver.common.by import By
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

            print("===========================")

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

            resultadoBusqueda = scraper.busquedaUrl.porPivote("https://www.linkedin.com/in/luis-basto-diaz-41136396/")
            resultaddoIteracion = scraper.iteradorUrls.iniciarIteracion(resultadoBusqueda)

            Utilidades.test(resultaddoIteracion)
            # resultaddoIteracion - Regresa el arreglo, aqui iria la funcion que toma el arreglo y envia elemento por elemento a la base de datos
            driver.close()

    def extraccionDeExperiencia(self):
        response = messagebox.askquestion(
            "Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
        if response == "yes":

            matrizResultado = []

            arregloDefinitivo = [['Daniel F. Baas', 'https://www.linkedin.com/in/danielbaas03'], ['Genny Andrea Centeno Metri', 'https://www.linkedin.com/in/gennycenteno'], ['José Antonio Maldonado Roig', 'https://www.linkedin.com/in/jos%C3%A9-antonio-maldonado-roig-b09269106'], ['Rafael Rodriguez', 'https://www.linkedin.com/in/rafaelroguz']]
            for egresadoLink in arregloDefinitivo:
                segundo_elemento = egresadoLink[1]

                #egresado = "https://www.linkedin.com/in/ecambranes/"
                driver = Utilidades.forzarIngresoAPaginaSinSesionIniciada(segundo_elemento)

                scraper = ScraperDatos(driver)
                matrizCampoSimple = scraper.CampoSimple()
                matrizCampoCompuesto = scraper.CampoCompuesto()
                matrizResultado = matrizResultado + matrizCampoSimple + matrizCampoCompuesto
                print("======================================")
                print(matrizResultado)
                

                driver.close()
            print("$$$$$$$$$$$$$$")
            print(matrizResultado)
            print("FIN")

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
        
            matrizResultado = []

            arregloDefinitivo = RS_uady_software.microarreglo35

            for egresadoLink in arregloDefinitivo:

                #egresado = "https://mx.linkedin.com/in/eduardocanchevazquez"
                driver = Utilidades.forzarIngresoAPaginaSinSesionIniciada(egresadoLink)
                scraper = ScraperDatos(driver)

                arregloNombreEgresado = driver.find_elements(By.TAG_NAME, 'h1')
                nombreEgresado = arregloNombreEgresado[0].text

                if scraper.verificarUniversidad_Carrera_Egresado("Universidad Autónoma de Yucatán", "UADY", "Ingeniería de Software") and scraper.verificarExperiencia():
                    matrizResultado.append([nombreEgresado, egresadoLink])
                    print("==============================")
                    print(matrizResultado)

                driver.delete_all_cookies()
                driver.close()

           
            print(matrizResultado)
            print("FIN")


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
