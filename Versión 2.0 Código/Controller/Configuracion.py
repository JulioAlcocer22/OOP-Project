from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os
import socket
import speedtest
from ping3 import ping
import locale


class Configuracion:
    def __init__(self, driver):
        self.driver = driver

    def iniciarSesion(self):
        load_dotenv()
        delay = 5
        email = os.getenv('USER')
        password = os.getenv('PSW')

        self.driver.get('https://www.linkedin.com/home')
        self.driver.implicitly_wait(delay)

        inputUser = self.driver.find_element(By.NAME, "session_key")
        inputUser.send_keys(email)
        inputPassword = self.driver.find_element(By.NAME, "session_password")
        inputPassword.send_keys(password)

        self.driver.implicitly_wait(delay)
        inputPassword.send_keys(Keys.ENTER)

    # NO USADA
    def cerrarSesion(self):
        delay = 5
        self.driver.implicitly_wait(delay)
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(delay)
        self.driver.refresh()

    def saltarModal(self):
        time.sleep(5)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    @staticmethod
    def sitioWebDisponible(url):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        try:
            s.connect((url, 80))
        except (socket.gaierror, socket.timeout):
            s.close()
            return False
        else:
            s.close()
            return True

    @staticmethod
    def comprobarSubida():
        s = speedtest.Speedtest()
        subida = round((round(s.upload()) / 1048576), 2)
        return subida

    @staticmethod
    def comprobarBajada():
        s = speedtest.Speedtest()
        bajada = round((round(s.download()) / 1048576), 2)
        return bajada

    @staticmethod
    def comprobarPing(host):
        st = speedtest.Speedtest()
        ping_time = ping(host)
        if ping_time is not None:
            return ping_time
        else:
            return 9999

    @staticmethod
    def testConexiones(urlNavegador):
        contador = 0

        if Configuracion.sitioWebDisponible("www.linkedin.com") and Configuracion.sitioWebDisponible(urlNavegador):
            contador = contador + 1

        if Configuracion.comprobarBajada() > 10 and Configuracion.comprobarSubida() > 3:
            contador = contador + 1

        if Configuracion.comprobarPing("www.linkedin.com") < 100 and Configuracion.comprobarPing(urlNavegador) < 3:
            contador = contador + 1

        if contador == 3:
            return True
        else:
            return False

    # NO USADA
    def lenguajeNavegadorEsEspañol(self):
        language = self.driver.execute_script("return navigator.language")
        if "es" in language:
            return True
        else:
            return False

    @staticmethod
    def lenguajeSOEsEspañol():
        idioma_sistema = locale.getdefaultlocale()

        if idioma_sistema[0].__contains__("es"):
            return True
        else:
            return False
