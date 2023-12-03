import datetime
from selenium.webdriver.common.by import By
from app import *
from app.Model.Utilidades import Utilidades
import datetime

class ScraperDatos:

    def __init__(self, driver):
        self.driver = driver
        self.PADDINGSIMPLE = 22
        self.PADDINGCOMPUESTO = 23

    def CampoSimple(self, linkEgresado):
        matrizCampoSimple = []

        experience_items = self.driver.find_elements(By.CSS_SELECTOR, ".profile-section-card.experience-item")
        
        for item in experience_items:
            try:
                description_elements = item.find_element(By.CSS_SELECTOR, ".experience__list .show-more-less-text__text--less").text
            except :
                description_elements = "" 
            
            elemento = item.text
            lineas = elemento.split('\n')
            nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]

            puesto = nuevoArreglo[0]
            empresa = nuevoArreglo[1]
            fechas = nuevoArreglo[2]

            try :
                inicio, fin, duracion = Utilidades.separarDuracion(fechas, self.PADDINGSIMPLE)
            except:
                inicio = 0
                fin = 0
                duracion = 0
            

            if duracion != str(0):
                matrizCampoSimple.append([linkEgresado, empresa, puesto, inicio, fin, duracion, description_elements])

        return matrizCampoSimple

    def CampoCompuesto(self, linkEgresado):
        matrizCampoCompuesto = []

        elementsf = self.driver.find_elements(By.CSS_SELECTOR, "a.experience-group-header__url")
        for elementf in elementsf:
            elemento = elementf.text
            lineas = elemento.split('\n')
            nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]
            puesto = nuevoArreglo[0]

            elements = self.driver.find_elements(By.CSS_SELECTOR, "li.profile-section-card.experience-group-position")
            for element in elements:
                elemento = element.text
                lineas = elemento.split('\n')
                nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]
                
                try:
                    description_elements = element.find_element(By.CSS_SELECTOR, ".experience__list .show-more-less-text__text--less").text
                except :
                    description_elements = ""

                empresa = nuevoArreglo[0]
                fechas = nuevoArreglo[1]

                try :
                    inicio, fin, duracion = Utilidades.separarDuracion(fechas, self.PADDINGSIMPLE)
                except:
                    inicio = 0
                    fin = 0
                    duracion = 0

                if duracion != str(0):
                    matrizCampoCompuesto.append([linkEgresado, empresa, puesto, inicio, fin, duracion, description_elements])


        return matrizCampoCompuesto

    #NO USADO
    def unicamenteDescripciones(self):

        description_elements = self.driver.find_elements(By.CSS_SELECTOR, ".experience__list .show-more-less-text__text--less")
        descriptions = [element.text for element in description_elements]

        for description in descriptions:
            print(description)

        return 0

    def verificarExperiencia(self):
        verdad = False
        elementos_h2 = self.driver.find_elements(By.TAG_NAME, 'h2')
        for elemento in elementos_h2:
            cadena = elemento.text
            if cadena.__contains__("Experiencia"):
                verdad = True

        return verdad

    def verificarUniversidad_Carrera_Egresado(self, universidad, acronimoUniversidad,  nombreCarrera, nombreCarreraAlternativo):
        verdad = False
        anioActual = datetime.datetime.now().year
        universidad = Utilidades.estadandarizarCadenas(universidad)
        nombreCarrera = Utilidades.estadandarizarCadenas(nombreCarrera)
        acronimoUniversidad = Utilidades.estadandarizarCadenas(acronimoUniversidad)
        nombreCarreraAlternativo = Utilidades.estadandarizarCadenas(nombreCarreraAlternativo)
        
        experience_items = self.driver.find_elements(By.CSS_SELECTOR, ".profile-section-card.education__list-item")
        
        for item in experience_items:
            elemento = item.text
            lineas = elemento.split('\n')
            nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]
            if len(nuevoArreglo) >= 3:

                try:
                    anioEgreso = int(nuevoArreglo[2].split("-")[1].strip())
                except:
                    fecha_actual = datetime.datetime.now()
                    anioEgreso = fecha_actual.year

                nuevoArreglo[0] = Utilidades.estadandarizarCadenas(nuevoArreglo[0])
                nuevoArreglo[1] = Utilidades.estadandarizarCadenas(nuevoArreglo[1])


                if nuevoArreglo[0].__contains__(universidad) or nuevoArreglo[0].__contains__(acronimoUniversidad):
                    if nuevoArreglo[1].__contains__(nombreCarrera) or nuevoArreglo[1].__contains__(nombreCarreraAlternativo):
                        if anioEgreso <= anioActual:
                            verdad = True

        return verdad
