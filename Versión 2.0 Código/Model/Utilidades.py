from selenium import webdriver
import time
from Controller.Configuracion import Configuracion
from selenium.webdriver.common.by import By
import datetime
import os
from selenium.webdriver.edge.service import Service
import re
import subprocess
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from msedge.selenium_tools import Edge, EdgeOptions
class Utilidades:

    def __init__(self):
        pass

    @staticmethod
    def test(arr):
        for i, entrada in enumerate(arr, start=1):
            print(f"arr[{i}] = {entrada}")

    @staticmethod
    def estadandarizarCadenas(s):
        cambios = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )

        for a, b in cambios:
            s = s.replace(a, b).replace(a.upper(), b.upper())

        return s.upper()

    @staticmethod
    def duplicadosArreglo(arreglo):
        arregloSinDuplicados = []

        for elemento in arreglo:
            if elemento not in arregloSinDuplicados:
                arregloSinDuplicados.append(elemento)

        return arregloSinDuplicados

    @staticmethod
    def forzarIngresoAPaginaSinSesionIniciada(egresado):
      
        # Configuración del proxy
        proxy_address = "172.67.181.41:80"

        # Configuración de opciones del navegador Edge
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        #edge_options.add_argument('--proxy-server=http://%s' % proxy_address)

        # Ruta al controlador de Microsoft Edge
        edge_driver_path = r'C:\Users\a19201679\Desktop\POO PROYECT\OOP-Project\Versión 2.0 Código\msedgedriver.exe'

        # Crear una instancia del navegador con las opciones configuradas
        driver = Edge(executable_path=edge_driver_path, options=edge_options)
        
        #LA BUENA
        #driver = webdriver.Edge(executable_path=r'C:\Users\a19201679\Desktop\POO PROYECT\OOP-Project\Versión 2.0 Código\msedgedriver.exe')
       
  
  

      


        fin = False
        while not fin:
            driver.get(egresado)
            time.sleep(1)
            elementos_h1 = driver.find_elements(By.TAG_NAME, 'h1')
            for elemento in elementos_h1:
                cadena = elemento.text
                if cadena.__contains__("verifica"):
                        print("esperando")
                        time.sleep(8)
            
            elementos_h2 = driver.find_elements(By.TAG_NAME, 'h2')
            for elemento in elementos_h2:
                cadena = elemento.text
                
                if cadena.__contains__("Iniciar sesión para ver el perfil completo de"):
                    fin = True

        time.sleep(3)
        config = Configuracion(driver)
        config.saltarModal()

        return driver

    @staticmethod
    def ingresoAPaginaConSesionIniciada():
        try:
            driver = webdriver.Edge()
        except:
            try:
                driver = webdriver.Edge(r"msedgedriver.exe")
            except:
                raise Exception("No se encontro el Web Driver")

        config = Configuracion(driver)
        config.iniciarSesion()

        return driver

    @staticmethod
    def transformarNumeroEnMes(numeroMes):
        if numeroMes == 1:
            return "ene. "
        elif numeroMes == 2:
            return "feb. "
        elif numeroMes == 3:
            return "mar. "
        elif numeroMes == 4:
            return "abr. "
        elif numeroMes == 5:
            return "may. "
        elif numeroMes == 6:
            return "jun. "
        elif numeroMes == 7:
            return "jul. "
        elif numeroMes == 8:
            return "ago. "
        elif numeroMes == 9:
            return "sep. "
        elif numeroMes == 10:
            return "oct. "
        elif numeroMes == 11:
            return "nov. "
        elif numeroMes == 12:
            return "dic. "

    @staticmethod
    def separarDuracion(fechas):
        cadena = fechas
        # caso 1
        cadena = cadena.replace("actualidad", "actualidad -")
        # caso 2
        posicion_insercion = 22

        cadena = cadena[:posicion_insercion] + \
            " - " + cadena[posicion_insercion:]

        lineas = cadena.split('-')
        nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]
        fechaInicio = nuevoArreglo[0]  # ok

        fechaFin = nuevoArreglo[1]
        if fechaFin.__contains__("actualidad"):
            fecha_actual = datetime.datetime.now()
            año_actual = fecha_actual.year
            mes_actual = fecha_actual.month

            mesFormateada = Utilidades.transformarNumeroEnMes(mes_actual)

            fechaFin = mesFormateada + str(año_actual)

        duracion = nuevoArreglo[2]
        duracionMeses = Utilidades.transformarDuracionEnMeses(duracion)

        return fechaInicio, fechaFin, duracionMeses

    @staticmethod
    def transformarDuracionEnMeses(duracion):
        duracionMeses = 0
        cadena = duracion
        cadena = cadena.replace("años", "año")
        cadena = cadena.replace("meses", "mes")
        cadena = cadena.replace("mes", "")
        cadena = cadena.replace("año", " - ")

        if len(cadena) <= 2:

            duracionMeses = int(cadena)

        else:
            lineas = cadena.split('-')
            nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]
            numeroDeElementos = len(nuevoArreglo)
            if numeroDeElementos == 1:
                duracionMeses = int(nuevoArreglo[0]) * 12

            else:
                duracionMeses = int(
                    nuevoArreglo[0]) * 12 + int(nuevoArreglo[1])

        return str(duracionMeses)
