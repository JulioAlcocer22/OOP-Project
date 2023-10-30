import time
from selenium.webdriver.common.by import By


class Busqueda:

    def __init__(self, driver):
        self.driver = driver

    def conCadena(self, cadena):

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

        urlActual = urlActual.replace("%22%5D&network=%5B%22F%22%2C%22S%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH&sid=","%22%5D&network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&page=XXXXX&sid=")

        return urlActual

        
