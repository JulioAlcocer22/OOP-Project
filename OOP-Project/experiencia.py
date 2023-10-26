from Configuracion import Configuracion
from Verificador import Verificador
import time


class Experiencia:

    def __init__(self, driver):
        self.driver = driver

    def verificarRequisitos(self, url, universidad, carrera):
        aprobado = False
        self.driver.get(url)
        time.sleep(5)
        config = Configuracion(self.driver)
        config.saltarModal()

        time.sleep(5)
        verif = Verificador(self.driver)
        # print(verif.existExperience())
        # print(verif.isUniversidadAndCarrera(universidad, carrera))

        if verif.existExperience() and verif.isUniversidadAndCarrera(universidad, carrera):
            # print("si cumple")
            return True

        return aprobado
