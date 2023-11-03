from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import tkinter as tk

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from Controller.Configuracion import Configuracion
from Model.ScrapperPerfiles import ScrapperPerfiles
from Model.Limpieza import Limpieza
from Model.Scraper import Scraper
import requests
from selenium.webdriver.common.by import By

class AccionesBoton:

    def __init__(self):
        pass

    
    def metodoCadena(self):
        entradaCadena = simpledialog.askstring(
            "Entrada de texto", "Ingrese la cadena que desea buscar:")
        if entradaCadena:
            
            try:
                driver = webdriver.Edge()
            except:
                try:
                    driver = webdriver.Edge(r"msedgedriver.exe")
                except:
                    pass
                    

            config = Configuracion(driver)
            config.iniciarSesion()


            scraper = ScrapperPerfiles(driver)

            resultadoBusqueda = scraper.busquedaUrl.porCadena(entradaCadena)
            resultaddoIteracion = scraper.iteradorUrls.iniciarIteracion(resultadoBusqueda)

            Limpieza.test(resultaddoIteracion)
            # Regresa el arreglo, aqui iria la funcion que toma el arreglo y envia elemento por elemento a la base de datos
            driver.close()



    def metodoUrl(self):
        entradaURL = simpledialog.askstring(
            "Entrada de texto", "Ingrese la URL que desea buscar:")
        if entradaURL:
            try:
                driver = webdriver.Edge()
            except:
                try:
                    driver = webdriver.Edge(r"msedgedriver.exe")
                except:
                    pass
            
            config = Configuracion(driver)
            config.iniciarSesion()

            scraper = ScrapperPerfiles(driver)
            resultaddoIteracion = scraper.iteradorUrls.iniciarIteracion(entradaURL)

            Limpieza.test(resultaddoIteracion)
            # Regresa el arreglo, aqui iria la funcion que toma el arreglo y envia elemento por elemento a la base de datos
            driver.close()



    def actualizarPivotes(self):

        response = messagebox.askquestion(
            "Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
        if response == "yes":
            try:
                driver = webdriver.Edge()
            except:
                try:
                    driver = webdriver.Edge(r"msedgedriver.exe")
                except:
                    pass

            config = Configuracion(driver)
            config.iniciarSesion()

            driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")

            scraper = ScrapperPerfiles(driver)
            resultaddoIteracion = scraper.scrappearLinks.obtener_links()

            Limpieza.test(resultaddoIteracion)
            # Regresa el arreglo, aqui iria la funcion que toma el arreglo y envia elemento por elemento a la base de datos
            driver.close()


    def metodoPivotes(self):
        response = messagebox.askquestion(
            "Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
        if response == "yes":
            # Supongamos que recibio uno por uno los links de mis pivotes de la db
            # Por cuestiones practicas usaremos el link de cambranes como prueba
            try:
                driver = webdriver.Edge()
            except:
                try:
                    driver = webdriver.Edge(r"msedgedriver.exe")
                except:
                    pass

            config = Configuracion(driver)
            config.iniciarSesion()

            scraper = ScrapperPerfiles(driver)

            resultadoBusqueda = scraper.busquedaUrl.porPivote("https://www.linkedin.com/in/ecambranes/")
            resultaddoIteracion = scraper.iteradorUrls.iniciarIteracion(resultadoBusqueda)


            Limpieza.test(resultaddoIteracion)
            # resultaddoIteracion - Regresa el arreglo, aqui iria la funcion que toma el arreglo y envia elemento por elemento a la base de datos
            driver.close()

    def extraccionDeExperiencia(self):
        response = messagebox.askquestion(
            "Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
        if response == "yes":
            # Supongamos que recibio uno por uno los links de la db
            # Por cuestiones practicas usaremos el link de luis basto como prueba
            try:
                driver = webdriver.Edge()
            except:
                try:
                    driver = webdriver.Edge(r"msedgedriver.exe")
                except:
                    pass

            #exp = Experiencia(driver)
            #driver.get("https://mx.linkedin.com/in/viviana-guadalupe-azcorra-novelo-351706231?trk=public_profile_browsemap")
            #print(exp.verificarRequisitos("https://mx.linkedin.com/in/viviana-guadalupe-azcorra-novelo-351706231?trk=public_profile_browsemap",
                #"UNIVERSIDAD AUTONOMA DE YUCATAN", 'LICENCIADA EN ENSEÑANZA DE LAS MATEMATICAS'))

            driver.delete_all_cookies()
            driver.get("https://www.linkedin.com/in/luis-basto-diaz-41136396/")
            driver.delete_all_cookies()
            config = Configuracion(driver)
            config.saltarModal()

            #scrap = Scraper(driver)
            #scrap.obtenerExperiencia()
            
            education_list = driver.find_elements(By.CLASS_NAME, 'experience__list')
            for element in education_list:
                h3_elements = element.find_elements(By.TAG_NAME, 'h3')
                for h3 in h3_elements:
                    print(h3.text)
                    
            print("------------------------")
            education_list = driver.find_elements(By.CLASS_NAME, 'experience__list')
            for element in education_list:
                h4_elements = element.find_elements(By.TAG_NAME, 'h4')
                for h4 in h4_elements:
                    print(h4.text)
            
            print("------------------------")        
            education_list = driver.find_elements(By.CLASS_NAME, 'experience__list')
            for element in education_list:
                duration_elements = element.find_elements(By.TAG_NAME, 'p')
                for duration in duration_elements:
                    print(duration.text)
            print("------------------------")
        

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
