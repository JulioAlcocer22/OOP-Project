import time
from Model.Utilidades import Utilidades
from selenium import *
from selenium.webdriver.common.by import By

class ScrapperPerfiles:

    def __init__(self, driver):
        self.driver = driver
        self.busquedaUrl = self.BusquedaDeURLs(self.driver)
        self.scrappearLinks = self.ScrappearLinks(self.driver)
        self.iteradorUrls = self.IteradorDeURLs(self.driver, self.scrappearLinks)

    class BusquedaDeURLs:

        def __init__(self, driver):
            self.driver = driver

        def porCadena(self, cadena):
            lineas = cadena.split(' ')
            nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]

            preCadena = ""
            for i in range(len(nuevoArreglo) - 1):
                subCadena = nuevoArreglo[i]
                preCadena = preCadena + subCadena + "%20"

            preCadena = preCadena + nuevoArreglo[len(nuevoArreglo) - 1]

            return "https://www.linkedin.com/search/results/people/?keywords=" + preCadena + "&origin=GLOBAL_SEARCH_HEADER&page=XXXXX&sid="

        def porPivote(self, cadena):
            self.driver.get(cadena)
            time.sleep(5)
            botonContactosPersona = self.driver.find_element(By.XPATH,
                '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/ul/li/a/span')
            botonContactosPersona.click()
            time.sleep(5)

            urlActual = self.driver.current_url
            urlActual = urlActual.replace(
                "%22%5D&network=%5B%22F%22%2C%22S%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH&sid=",
                "%22%5D&network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&page=XXXXX&sid=")

            return urlActual

    class IteradorDeURLs:

        def __init__(self, driver, scrappearLinksInstancia, iteradorDeURLsInstancia):
            self.driver = driver
            self.scrappearLinksInstancia = scrappearLinksInstancia
            self.iteradorDeURLsInstancia = iteradorDeURLsInstancia

        def iniciarIteracion(self, varOriginal):
            varOriginal = varOriginal.replace("SWITCH_SEARCH_VERTICAL&", "SWITCH_SEARCH_VERTICAL&page=XXXXX&")

            arregloUnificado = []
            esUltimaPagina = self.iteradorDeURLsInstancia.es_ultima_pagina()
            
            paginaVisitar = 1
            while not esUltimaPagina:
                var = varOriginal.replace("XXXXX", str(paginaVisitar))
                self.driver.get(var)
                time.sleep(5)
                arregloUnificado = arregloUnificado + self.scrappearLinksInstancia.obtener_links()
                paginaVisitar = paginaVisitar + 1 


            return arregloUnificado


        def es_ultima_pagina(self):
            time.sleep(5)
            elementos_h2 = self.driver.find_elements(By.TAG_NAME, 'h2')
            time.sleep(5)
            for elemento in elementos_h2:
                fin = False
                cadena = elemento.text
                if cadena.__contains__("Ningún resultado encontrado"):
                    fin = True
                    # print("Ya no hay mas resultados")
            return fin

    class ScrappearLinks:

        def __init__(self, driver):
            self.driver = driver

        def obtener_links(self):
            time.sleep(10)
            enlaces = self.driver.find_elements(By.TAG_NAME, "a")

            arregloDefinitivo = []

            for enlace in enlaces:
                url = enlace.get_attribute('href')
                if url.__contains__("https://www.linkedin.com/in/"):
                    primer_char = url[28]

                    if primer_char.islower():
                        arregloDefinitivo.append(url)

            arreglo_final = Utilidades.duplicadosArreglo(arregloDefinitivo)
            # Limpieza.test(arreglo_final)

            return arreglo_final