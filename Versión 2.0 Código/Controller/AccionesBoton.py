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
                print("ya entre")
                driver = webdriver.Edge()
            except:
                try:
                    print("ya entre 2")
                    driver = webdriver.Edge(r"msedgedriver.exe")
                except:
                    pass

            #exp = Experiencia(driver)
            #driver.get("https://mx.linkedin.com/in/viviana-guadalupe-azcorra-novelo-351706231?trk=public_profile_browsemap")
            #print(exp.verificarRequisitos("https://mx.linkedin.com/in/viviana-guadalupe-azcorra-novelo-351706231?trk=public_profile_browsemap",
                #"UNIVERSIDAD AUTONOMA DE YUCATAN", 'LICENCIADA EN ENSEÑANZA DE LAS MATEMATICAS'))

            
            #https://mx.linkedin.com/in/viviana-guadalupe-azcorra-novelo-351706231
            #https://www.linkedin.com/in/luis-basto-diaz-41136396/
            #https://mx.linkedin.com/in/edgar-cambranes
            driver.get("https://mx.linkedin.com/in/edgar-cambranes")
            """
            config = Configuracion(driver)
            config.iniciarSesion()
            time.sleep(5)
            
            driver.get("https://mx.linkedin.com/in/edgar-cambranes")
            driver.delete_all_cookies()
            """
            config = Configuracion(driver)
            
            time.sleep(20)
            config.saltarModal()

          

            elementsf = driver.find_elements(By.CSS_SELECTOR, "a.experience-group-header__url")

            # Itera a través de los elementos y obtén el contenido
            for elementf in elementsf:
                elemento = elementf.text

                lineas = elemento.split('\n')
                nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]

                empresa = nuevoArreglo[0]
    

                print(empresa)



            #OBTENER DATOS CASO MULTIPLES
            elements = driver.find_elements(By.CSS_SELECTOR, "li.profile-section-card.experience-group-position")
            for element in elements:
                elemento = element.text
                lineas = elemento.split('\n')
                nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]

                puesto = nuevoArreglo[0]
                duracion = nuevoArreglo[1]

                print(puesto + "---" + duracion)



            
            #OBTENER DATOS CASO BASTO
            experience_items = driver.find_elements(By.CSS_SELECTOR, ".profile-section-card.experience-item")
            for item in experience_items:
                elemento = item.text
                lineas = elemento.split('\n')
                nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]

                empresa = nuevoArreglo[0]
                puesto = nuevoArreglo[1]
                duracion = nuevoArreglo[2]

                print( empresa + "---" + puesto + "---" + duracion)
                #print(item.text)


               
            #OBTENER DESCRIPCIONES CASO BASTO
            css_selector3 = '.experience__list .profile-section-card__contents .profile-section-card__meta .experience-item__description.experience-item__meta-item'
            element3 = driver.find_elements(By.CSS_SELECTOR, css_selector3)
            for elements in element3:
                print(elements.text)
                 

 
           

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
