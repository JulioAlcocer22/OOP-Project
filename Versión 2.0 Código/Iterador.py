import time
from Limpieza import Limpieza
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver.common.by import By


class Iterador:

    def __init__(self, driver):
        self.driver = driver

    def obtener_links(self):

        time.sleep(10)
        #enlaces = self.driver.find_element(By.CSS_SELECTOR,'a.app-aware-link')
        enlaces = self.driver.find_elements(By.TAG_NAME,"a")
  

        arregloDefinitivo = []

        for enlace in enlaces:

            url = enlace.get_attribute('href')
            if url.__contains__("https://www.linkedin.com/in/"):
                primer_char = url[28]

                if primer_char.islower():
                    arregloDefinitivo.append(url)

        arreglo_final = Limpieza.duplicadosArreglo(arregloDefinitivo)
        Limpieza.test(arreglo_final)

        return (arreglo_final)
    
    def obtener_links2(self):

        time.sleep(10)
        enlaces = self.driver.find_elements(By.CSS_SELECTOR,'a.app-aware-link')
        #enlaces = self.driver.find_elements(By.TAG_NAME,"a")
  

        arregloDefinitivo = []

        for enlace in enlaces:

            url = enlace.get_attribute('href')
            if url.__contains__("https://www.linkedin.com/in/"):
                primer_char = url[28]

                if primer_char.islower():
                    arregloDefinitivo.append(url)

        arreglo_final = Limpieza.duplicadosArreglo(arregloDefinitivo)
        #Limpieza.test(arreglo_final)

        return (arreglo_final)



    def es_ultima_pagina(self):

        time.sleep(5)
        elementos_h2 = self.driver.find_element(By.TAG_NAME,'h2')
        time.sleep(5)
        # Verifica si el elemento fue encontrado
        for elemento in elementos_h2:
            fin = False
            # print(elemento.text)
            cadena = elemento.text
            if cadena.__contains__("Ningún resultado encontrado"):
                fin = True
                # print("Ya no hay mas resultados")
        return fin
