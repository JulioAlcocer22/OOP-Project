import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Controller.Configuracion import Configuracion
class Scraper:

    def __init__(self, driver):
        self.driver = driver
    """
    def isUniversidadAndCarrera(self, universidad, carrera):
        verdad = False
        try:
            arregloDeEducacion = self.driver.find_elements_by_class_name(
                "education__list")

            #elementoEstandarizado = Limpieza.estadandarizarCadenas(
                #arregloDeEducacion[0].text)
        except:
            pass
        else:
            #lineas = elementoEstandarizado.split('\n')

            #nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]

            for i, entrada in enumerate(nuevoArreglo, start=1):
                # print(f"nuevoArreglo[{i}] = {entrada}")

                if universidad in entrada:
                    if nuevoArreglo[i].__contains__(carrera):
                        verdad = True

        return verdad

    def existExperience(self):
        verdad = False
        try:
            arregloDeEducacion = self.driver.find_elements_by_class_name(
                "experience__list")

            elementoEstandarizado = Limpieza.estadandarizarCadenas(
                arregloDeEducacion[0].text)
        except:
            print("NO encontrado")
        else:
            lineas = elementoEstandarizado.split('\n')

            nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]

            if len(nuevoArreglo) > 2:
                verdad = True

            # ---------------------------- testing
            # for i, entrada in enumerate(nuevoArreglo, start=1):
                # print(f"nuevoArreglo[{i}] = {entrada}")

            # print(nuevoArreglo)

        return verdad


    def verificarRequisitos(self, url, universidad, carrera):
        aprobado = False
        self.driver.get(url)
        time.sleep(5)
        #config = Configuracion(self.driver)
        #config.saltarModal()

        time.sleep(5)
        #verif = Verificador(self.driver)
        # print(verif.existExperience())
        # print(verif.isUniversidadAndCarrera(universidad, carrera))

        #if verif.existExperience() and verif.isUniversidadAndCarrera(universidad, carrera):
            # print("si cumple")
            #return True

        return aprobado
    """
    def obtenerExperiencia(self):
        
        pass
       
       
        
        
