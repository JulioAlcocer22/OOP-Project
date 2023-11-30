from selenium import webdriver
import time
from Controller.Configuracion import Configuracion
from selenium.webdriver.common.by import By
import datetime
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager



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
        intentosDeEntrada = 0
        honeyPoot = False
        try:
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        except:
            driver = webdriver.Edge()

        driver.delete_all_cookies 

        fin = False
        while not fin:
            driver.get(egresado)

            if intentosDeEntrada >= 20:
                honeyPoot = True
                return None, honeyPoot
            
            elementos_h2 = driver.find_elements(By.TAG_NAME, 'h2')
            for elemento in elementos_h2:
                cadena = elemento.text
                driver.delete_all_cookies()

                if cadena.__contains__("Iniciar sesión para ver el perfil completo de"):
                    
                    fin = True
                    
            intentosDeEntrada = intentosDeEntrada + 1

        time.sleep(3)
        config = Configuracion(driver)
        config.saltarModal()

        return driver, honeyPoot

    @staticmethod
    def ingresoAPaginaConSesionIniciada():
        try:
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        except:
            driver = webdriver.Edge()
       
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
    def mesANumero(fechaInicio):
        cadena = fechaInicio

        cadena = cadena.replace("ene.", "01/01/")
        cadena = cadena.replace("feb.", "01/02/")
        cadena = cadena.replace("mar.", "01/03/")
        cadena = cadena.replace("abr.", "01/04/")
        cadena = cadena.replace("may.", "01/05/")
        cadena = cadena.replace("jun.", "01/06/")
        cadena = cadena.replace("jul.", "01/07/")
        cadena = cadena.replace("ago.", "01/08/")
        cadena = cadena.replace("sept.", "01/09/")
        cadena = cadena.replace("oct.", "01/10/")
        cadena = cadena.replace("nov.", "01/11/")
        cadena = cadena.replace("dic.", "01/12/")
        cadena = cadena.replace(" ", "")

        return cadena


    @staticmethod
    def separarDuracion(fechas, posicion_insercion):

        cadena = fechas
        cadena = cadena.replace("actualidad", "actualidad -")
        cadena = cadena[:posicion_insercion] + " - " + cadena[posicion_insercion:]
        lineas = cadena.split('-')
        
        nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]
        fechaInicioFormateada = Utilidades.mesANumero(nuevoArreglo[0])

        fechaFin = nuevoArreglo[1]
        fechaFinFormateada = Utilidades.mesANumero(nuevoArreglo[1])
        if fechaFin.__contains__("actualidad"):
            fecha_actual = datetime.datetime.now()
            año_actual = fecha_actual.year
            mes_actual = fecha_actual.month

            fechaFinFormateada = "01/" + str(mes_actual) + "/" + str(año_actual)

        try:
            duracion = nuevoArreglo[2]
        except:
            duracion = 0 #Error (Caso extraordinario)

        try:
            duracionMeses = Utilidades.transformarDuracionEnMeses(duracion)
        except:
            duracionMeses = 0 #Error (Caso extraordinario)
        

        return str(fechaInicioFormateada), str(fechaFinFormateada), str(duracionMeses)
    
    
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
                duracionMeses = int(nuevoArreglo[0]) * 12 + int(nuevoArreglo[1])

        return str(duracionMeses)
