from tkinter import * # Import whole module
import requests
import pyttsx3
import tkinter as tk
from tkinter import messagebox 
from tkinter import simpledialog
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import re
import database
import pyodbc
import json
import time
from configuracion import Configuracion
from verificador import Verificador
from busqueda import Busqueda
from iterador import Iterador
from obtenerLinks import ObtenerLinks
from obtenerLinks import ObtenerLinks
from experiencia import Experiencia
from limpieza import Limpieza
import locale


class LinkedInScraper:  
    def __init__(self): 

        if Configuracion.lenguajeSOEsEspañol(): 
            window = tk.Tk()  
            window.title("LinkedIn Scraper")  
            window.geometry("600x350")
            window.configure(bg="white")   
            window.resizable(width=False, height=False)


            #-----------------------------------------------------------
            etiqueta1 =Label(window,font="Forte 17",text ="Busqueda",width=20)
            etiqueta1.place(x=20, y=30)

            boton_por_cadena = tk.Button(window, text="Por cadena",font="Georgia 12 ", command=lambda: metodo_cadena(), width=22,height=1)
            boton_por_cadena.place(x=20, y=90)

            boton_por_url = tk.Button(window, text="Por URL",font="Georgia 12 ", command=lambda: metodo_url(), width=22,height=1)
            boton_por_url.place(x=20, y=160)

            boton_actualizar_pivotes = Button(window, text = "Actualizar pivotes",font="Georgia 12",command=lambda: actualizar_pivotes(), width=22,height=1)
            boton_actualizar_pivotes.place(x=20, y=230)

            boton_todos_pivotes = Button(window, text = "Por pivotes",font="Georgia 12",command=lambda: metodo_pivotes(), width=22,height=1)
            boton_todos_pivotes.place(x=20, y=300)

            #-----------------------------------------------------------

            etiqueta2 =Label(window,font="Forte 17",text ="Extraccion",width=20)
            etiqueta2.place(x=300, y=30)


            boton_extraer = tk.Button(window, text="Extraer experiencia",font="Georgia 12 ", command=lambda: extraccion_de_experiencia(), width=22,height=1)
            boton_extraer.place(x=300, y=90)

            etiqueta3 =Label(window,font="Forte 17",text ="Test",width=20)
            etiqueta3.place(x=300, y=160)


            boton_test = tk.Button(window, text="Probar conexion",font="Georgia 12 ", command=lambda: test_conexiones(), width=22,height=1)
            boton_test.place(x=300, y=230)

            window.mainloop()
        else:
            messagebox.showerror("Error", "El sistema operativo no se encuentra en español. La aplicación se cerrará.")




def metodo_cadena():
    result = simpledialog.askstring("Entrada de texto", "Ingrese la cadena que desea buscar:")
    if result:
        driver = webdriver.Edge(r"msedgedriver.exe")
        obtenerdor = ObtenerLinks(driver)
        obtenerdor.conCadena(result)
        #Regresa el arreglo, aqui iria la funcion que toma el arreglo y envia elemento por elemento a la base de datos
        driver.close()
    else:
        messagebox.showerror("Error", "No se ingreso ninguna cadena")


def metodo_url():
    result = simpledialog.askstring("Entrada de texto", "Ingrese la URL que desea buscar:")
    if result:
       driver = webdriver.Edge(r"msedgedriver.exe")
       obtenerdor = ObtenerLinks(driver)
       obtenerdor.porURL(texto)
       #Regresa el arreglo, aqui iria la funcion que toma el arreglo y envia elemento por elemento a la base de datos
       driver.close()
    else:
        messagebox.showerror("Error", "No se ingreso ninguna URL")


def actualizar_pivotes():

    response = messagebox.askquestion("Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
    if response == "yes":
        driver = webdriver.Edge(r"msedgedriver.exe")
        config = Configuracion(driver)
        config.iniciarSesion()
        driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
        time.sleep(10)

        iterador = Iterador(driver)
        iterador.obtener_links()
        #Regresa el arreglo, aqui iria la funcion que toma el arreglo y envia elemento por elemento a la base de datos
        driver.close()


def metodo_pivotes():
    response = messagebox.askquestion("Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
    if response == "yes":
        #Supongamos que recibio uno por uno los links de mis pivotes de la db
        #Por cuestiones practicas usaremos el link de cambranes como prueba
        driver = webdriver.Edge(r"msedgedriver.exe")
        config = Configuracion(driver)
        config.iniciarSesion()
        buscador = Busqueda(driver)
        buscador.porPivote("https://www.linkedin.com/in/ecambranes/")
        obtenerdor = ObtenerLinks(driver)
        obtenerdor.sinContexto(driver.current_url)
        #Regresa el arreglo, aqui iria la funcion que toma el arreglo y envia elemento por elemento a la base de datos
    

def extraccion_de_experiencia():
    response = messagebox.askquestion("Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
    if response == "yes":
        #Supongamos que recibio uno por uno los links de la db
        #Por cuestiones practicas usaremos el link de viviana como prueba
        driver = webdriver.Edge(r"msedgedriver.exe")
        exp = Experiencia(driver)
        driver.get("https://mx.linkedin.com/in/viviana-guadalupe-azcorra-novelo-351706231?trk=public_profile_browsemap")
        print(exp.verificarRequisitos("https://mx.linkedin.com/in/viviana-guadalupe-azcorra-novelo-351706231?trk=public_profile_browsemap", "UNIVERSIDAD AUTONOMA DE YUCATAN", 'LICENCIADA EN ENSEÑANZA DE LAS MATEMATICAS'))
        
        #Si es true obtiene la experiencia, sino continua con el siguiente
        #La funcion para obtener la experiencia sigue en desarrollo

def test_conexiones():
    response = messagebox.askquestion("Pregunta", "¿Estás seguro de que deseas continuar?, El proceso no se puede detener.")
    if response == "yes":
        if Configuracion.testConexiones("www.google.com"):  
            tk.messagebox.showinfo("Información", "La conexion a internet es estable")
        else:
            tk.messagebox.showerror("Error", "La conexion a internet es inestable")



LinkedInScraper()
