from configuracion import Configuracion
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

class Busqueda:

	def __init__(self, driver):
		self.driver = driver

	def conCadena(self, cadena):

		lineas = cadena.split(' ')
				
		nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]
		#print(nuevoArreglo)

		pre_cadena = ""
		for i in range(len(nuevoArreglo) - 1):
		    sub_cadena = nuevoArreglo[i]
		    #print(f"Elemento {i}: {sub_cadena}")
		    pre_cadena = pre_cadena + sub_cadena + "%20"
			
		pre_cadena = pre_cadena + nuevoArreglo[len(nuevoArreglo) - 1]
		#print(nuevoArreglo[len(nuevoArreglo) - 1])
		#print(pre_cadena)

		return "https://www.linkedin.com/search/results/people/?keywords=" + pre_cadena + "&origin=GLOBAL_SEARCH_HEADER&page=XXXXX&sid="

	def porPivote(self, cadena):
		
		self.driver.get(cadena)
		time.sleep(5)

		boton_contactos_persona = self.driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/ul/li/a/span')
		boton_contactos_persona.click()
		time.sleep(5)

		boton_contactos_desplegable = self.driver.find_element_by_xpath('/html/body/div[5]/div[3]/div[2]/section/div/nav/div/ul/li[3]/div/span/button')
		boton_contactos_desplegable.click()
		time.sleep(5)

		boton_contactos_tercer = self.driver.find_element_by_xpath('/html/body/div[5]/div[3]/div[2]/section/div/nav/div/ul/li[3]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[3]/label/p/span[1]')
		boton_contactos_tercer.click()
		time.sleep(5)

		boton_contactos_tercer_aceptar = self.driver.find_element_by_xpath('/html/body/div[5]/div[3]/div[2]/section/div/nav/div/ul/li[3]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]')
		boton_contactos_tercer_aceptar.click()