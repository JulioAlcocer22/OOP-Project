from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import tkinter as tk


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from Controller.Configuracion import Configuracion
from Model.Busqueda import Busqueda
from Model.Iterador import Iterador
from Model.ObtenerLinks import ObtenerLinks
from Model.Limpieza import Limpieza
from Model.Scraper import Scraper


class AccionesBoton:

    def __init__(self):
        pass

    
    def metodoCadena(self):
        result = simpledialog.askstring(
            "Entrada de texto", "Ingrese la cadena que desea buscar:")
        if result:

            driver = webdriver.Edge(r"msedgedriver.exe")

            config = Configuracion(driver)
            config.iniciarSesion()

            busqueda = Busqueda(driver)
            varOriginal = busqueda.conCadena(result)
            
            obtenerdor = ObtenerLinks(driver)
            resultado = obtenerdor.porURL(varOriginal)

            Limpieza.test(resultado)
            # Regresa el arreglo, aqui iria la funcion que toma el arreglo y envia elemento por elemento a la base de datos
            driver.close()



    def metodoUrl(self):
        result = simpledialog.askstring(
            "Entrada de texto", "Ingrese la URL que desea buscar:")
        if result:
            driver = webdriver.Edge(r"msedgedriver.exe")
            
            config = Configuracion(driver)
            config.iniciarSesion()

            obtenerdor = ObtenerLinks(driver)
            resultado = obtenerdor.porURL(result)

            Limpieza.test(resultado)
            # Regresa el arreglo, aqui iria la funcion que toma el arreglo y envia elemento por elemento a la base de datos
            driver.close()



    def actualizarPivotes(self):

        response = messagebox.askquestion(
            "Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
        if response == "yes":
            driver = webdriver.Edge(r"msedgedriver.exe")

            config = Configuracion(driver)
            config.iniciarSesion()

            driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
            time.sleep(10)

            iterador = Iterador(driver)
            resultado = iterador.obtener_links()

            Limpieza.test(resultado)
            # Regresa el arreglo, aqui iria la funcion que toma el arreglo y envia elemento por elemento a la base de datos
            driver.close()


    def metodoPivotes(self):
        response = messagebox.askquestion(
            "Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
        if response == "yes":
            # Supongamos que recibio uno por uno los links de mis pivotes de la db
            # Por cuestiones practicas usaremos el link de cambranes como prueba
            driver = webdriver.Edge(r"msedgedriver.exe")

            config = Configuracion(driver)
            config.iniciarSesion()

            buscador = Busqueda(driver)
            var = buscador.porPivote("https://www.linkedin.com/in/ecambranes/")

            obtenerdor = ObtenerLinks(driver)
            resultado = obtenerdor.porURL(var)

            Limpieza.test(resultado)
            # Regresa el arreglo, aqui iria la funcion que toma el arreglo y envia elemento por elemento a la base de datos
            driver.close()

    def extraccionDeExperiencia(self):
        response = messagebox.askquestion(
            "Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
        if response == "yes":
            # Supongamos que recibio uno por uno los links de la db
            # Por cuestiones practicas usaremos el link de viviana como prueba
            driver = webdriver.Edge(r"msedgedriver.exe")
            #driver.delete_all_cookies()
            #exp = Experiencia(driver)
            #driver.get("https://mx.linkedin.com/in/viviana-guadalupe-azcorra-novelo-351706231?trk=public_profile_browsemap")
            #print(exp.verificarRequisitos("https://mx.linkedin.com/in/viviana-guadalupe-azcorra-novelo-351706231?trk=public_profile_browsemap",
                #"UNIVERSIDAD AUTONOMA DE YUCATAN", 'LICENCIADA EN ENSEÑANZA DE LAS MATEMATICAS'))


            driver.get("https://www.linkedin.com/in/luis-basto-diaz-41136396/")
            config = Configuracion(driver)
            config.saltarModal()

            scrap = Scraper(driver)
            scrap.obtenerExperiencia()

            driver.close()
            # Si es true obtiene la experiencia, sino continua con el siguiente
            # La funcion para obtener la experiencia sigue en desarrollo


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
