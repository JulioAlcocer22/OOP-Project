from limpieza import Limpieza
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

class Verificador:

	def __init__(self, driver):
		self.driver = driver
		

	def isUniversidadAndCarrera(self, universidad, carrera):
		verdad = False
		try:
			arregloDeEducacion = self.driver.find_elements_by_class_name("education__list")
			
			elemento_estandarizado = Limpieza.estadandarizarCadenas(arregloDeEducacion[0].text)
		except:
			pass
		else:
			lineas = elemento_estandarizado.split('\n')
				
			nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]

			for i, entrada in enumerate(nuevoArreglo, start=1):
				#print(f"nuevoArreglo[{i}] = {entrada}")

				if universidad in entrada:
				   	if nuevoArreglo[i].__contains__(carrera):
				   		verdad = True

		return verdad

	def existExperience(self):
		verdad = False
		try:
			arregloDeEducacion = self.driver.find_elements_by_class_name("experience__list")

			elemento_estandarizado = Limpieza.estadandarizarCadenas(arregloDeEducacion[0].text)
		except:
			print("NO encontrado")
		else:
			lineas = elemento_estandarizado.split('\n')
				
			nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]

			if len(nuevoArreglo) > 2:
				verdad = True

			#---------------------------- testing
			#for i, entrada in enumerate(nuevoArreglo, start=1):
				#print(f"nuevoArreglo[{i}] = {entrada}")

			#print(nuevoArreglo)

		return verdad