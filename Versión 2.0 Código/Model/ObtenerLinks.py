import time
from Model.Busqueda import Busqueda
from Model.Iterador import Iterador
from Controller.Configuracion import Configuracion
from Model.Limpieza import Limpieza


class ObtenerLinks:

    def __init__(self, driver):
        self.driver = driver

    def porURL(self, varOriginal):
        varOriginal = varOriginal.replace("SWITCH_SEARCH_VERTICAL&", "SWITCH_SEARCH_VERTICAL&page=XXXXX&")
       
        iterador = Iterador(self.driver)
        arregloUnificado = []

        var = varOriginal.replace("XXXXX", "1")
        print(var)
        self.driver.get(var)
        time.sleep(5)
        arregloUnificado = arregloUnificado + iterador.obtener_links()
        # print(iterador.es_ultima_pagina())

        var = varOriginal.replace("XXXXX", "2")
        print(var)
        self.driver.get(var)
        time.sleep(5)
        arregloUnificado = arregloUnificado + iterador.obtener_links()
        # print(iterador.es_ultima_pagina())

        var = varOriginal.replace("XXXXX", "3")
        print(var)
        self.driver.get(var)
        time.sleep(5)
        arregloUnificado = arregloUnificado + iterador.obtener_links()
        # print(iterador.es_ultima_pagina())

        # print(arregloUnificado)
        #Limpieza.test(arregloUnificado)
        return arregloUnificado

