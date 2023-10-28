import time
from Busqueda import Busqueda
from Iterador import Iterador
from Configuracion import Configuracion
from Limpieza import Limpieza


class ObtenerLinks:

    def __init__(self, driver):
        self.driver = driver

    def porURL(self, varOriginal):
        varOriginal = varOriginal.replace(
            "SWITCH_SEARCH_VERTICAL&", "SWITCH_SEARCH_VERTICAL&page=XXXXX")
        config = Configuracion(self.driver)
        config.iniciarSesion()

        time.sleep(5)

        iterador = Iterador(self.driver)
        arregloUnificado = []

        var = varOriginal.replace("XXXXX", "1")
        self.driver.get(var)
        time.sleep(5)
        arregloUnificado = arregloUnificado + iterador.obtener_links()
        # print(iterador.es_ultima_pagina())

        var = varOriginal.replace("XXXXX", "2")
        self.driver.get(var)
        time.sleep(5)
        arregloUnificado = arregloUnificado + iterador.obtener_links()
        # print(iterador.es_ultima_pagina())

        var = varOriginal.replace("XXXXX", "3")
        self.driver.get(var)
        time.sleep(5)
        arregloUnificado = arregloUnificado + iterador.obtener_links()
        # print(iterador.es_ultima_pagina())

        # print(arregloUnificado)
        Limpieza.test(arregloUnificado)
        return arregloUnificado

    def conCadena(self, cadena):
        config = Configuracion(self.driver)
        config.iniciarSesion()

        time.sleep(5)

        busqueda = Busqueda(self.driver)
        varOriginal = busqueda.conCadena(cadena)
        iterador = Iterador(self.driver)
        arregloUnificado = []

        var = varOriginal.replace("XXXXX", "1")
        self.driver.get(var)
        time.sleep(5)
        arregloUnificado = arregloUnificado + iterador.obtener_links()
        # print(iterador.es_ultima_pagina())

        var = varOriginal.replace("XXXXX", "2")
        self.driver.get(var)
        time.sleep(5)
        arregloUnificado = arregloUnificado + iterador.obtener_links()
        # print(iterador.es_ultima_pagina())

        var = varOriginal.replace("XXXXX", "3")
        self.driver.get(var)
        time.sleep(5)
        arregloUnificado = arregloUnificado + iterador.obtener_links()
        # print(iterador.es_ultima_pagina())

        # print(arregloUnificado)
        Limpieza.test(arregloUnificado)
        return arregloUnificado

        """
		arregloUnificado = []
		ultima_pagina = False
		indice = 1
		while not ultima_pagina:
			var = var_original.replace("XXXXX", indice)
			driver.get(var)
			time.sleep(5)
			arregloUnificado = arregloUnificado + iterador.obtener_links()

			if iterador.es_ultima_pagina():
				ultima_pagina = True

			indice++
		return arregloUnificado
		"""

    def sinContexto(self, varOriginal):
        varOriginal = varOriginal.replace(
            "SWITCH_SEARCH_VERTICAL&", "SWITCH_SEARCH_VERTICAL&page=XXXXX")

        time.sleep(5)

        iterador = Iterador(self.driver)
        arregloUnificado = []

        var = varOriginal.replace("XXXXX", "1")
        self.driver.get(var)
        time.sleep(5)
        arregloUnificado = arregloUnificado + iterador.obtener_links()
        # print(iterador.es_ultima_pagina())

        var = varOriginal.replace("XXXXX", "2")
        self.driver.get(var)
        time.sleep(5)
        arregloUnificado = arregloUnificado + iterador.obtener_links()
        # print(iterador.es_ultima_pagina())

        var = varOriginal.replace("XXXXX", "3")
        self.driver.get(var)
        time.sleep(5)
        arregloUnificado = arregloUnificado + iterador.obtener_links()
        # print(iterador.es_ultima_pagina())

        # print(arregloUnificado)
        Limpieza.test(arregloUnificado)
        return arregloUnificado
