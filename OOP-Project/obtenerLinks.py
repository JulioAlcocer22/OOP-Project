from busqueda import Busqueda
from iterador import Iterador
import time
from configuracion import Configuracion
from limpieza import Limpieza


class ObtenerLinks:

	def __init__(self, driver):
		self.driver = driver

	def porURL(self, var_original):
		var_original = var_original.replace("SWITCH_SEARCH_VERTICAL&","SWITCH_SEARCH_VERTICAL&page=XXXXX")
		config = Configuracion(self.driver)
		config.iniciarSesion()

		time.sleep(5)

		iterador = Iterador(self.driver)
		arregloUnificado = []
		
		var = var_original.replace("XXXXX", "1")
		self.driver.get(var)
		time.sleep(5)
		arregloUnificado = arregloUnificado + iterador.obtener_links()
		#print(iterador.es_ultima_pagina())


		var = var_original.replace("XXXXX", "2")
		self.driver.get(var)
		time.sleep(5)
		arregloUnificado = arregloUnificado + iterador.obtener_links()
		#print(iterador.es_ultima_pagina())


		var = var_original.replace("XXXXX", "3")
		self.driver.get(var)
		time.sleep(5)
		arregloUnificado = arregloUnificado + iterador.obtener_links()
		#print(iterador.es_ultima_pagina())

		#print(arregloUnificado)
		Limpieza.test(arregloUnificado)
		return arregloUnificado



	def conCadena(self, cadena):
		config = Configuracion(self.driver)
		config.iniciarSesion()

		time.sleep(5)

		busqueda = Busqueda(self.driver)
		var_original = busqueda.conCadena(cadena)
		iterador = Iterador(self.driver)
		arregloUnificado = []
		
		var = var_original.replace("XXXXX", "1")
		self.driver.get(var)
		time.sleep(5)
		arregloUnificado = arregloUnificado + iterador.obtener_links()
		#print(iterador.es_ultima_pagina())


		var = var_original.replace("XXXXX", "2")
		self.driver.get(var)
		time.sleep(5)
		arregloUnificado = arregloUnificado + iterador.obtener_links()
		#print(iterador.es_ultima_pagina())


		var = var_original.replace("XXXXX", "3")
		self.driver.get(var)
		time.sleep(5)
		arregloUnificado = arregloUnificado + iterador.obtener_links()
		#print(iterador.es_ultima_pagina())

		#print(arregloUnificado)
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

	def sinContexto(self, var_original):
		var_original = var_original.replace("SWITCH_SEARCH_VERTICAL&","SWITCH_SEARCH_VERTICAL&page=XXXXX")

		time.sleep(5)

		iterador = Iterador(self.driver)
		arregloUnificado = []
		
		var = var_original.replace("XXXXX", "1")
		self.driver.get(var)
		time.sleep(5)
		arregloUnificado = arregloUnificado + iterador.obtener_links()
		#print(iterador.es_ultima_pagina())


		var = var_original.replace("XXXXX", "2")
		self.driver.get(var)
		time.sleep(5)
		arregloUnificado = arregloUnificado + iterador.obtener_links()
		#print(iterador.es_ultima_pagina())


		var = var_original.replace("XXXXX", "3")
		self.driver.get(var)
		time.sleep(5)
		arregloUnificado = arregloUnificado + iterador.obtener_links()
		#print(iterador.es_ultima_pagina())

		#print(arregloUnificado)
		Limpieza.test(arregloUnificado)
		return arregloUnificado