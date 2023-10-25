from selenium import webdriver
import time
from limpieza import Limpieza

class Iterador:

	def __init__(self, driver):
		self.driver = driver



	def obtener_links(self):
		
		time.sleep(10)
		#enlaces = self.driver.find_elements_by_css_selector('a.app-aware-link')
		enlaces = self.driver.find_elements_by_tag_name("a")

		arreglo_definitivo = []

		for enlace in enlaces:
		    url = enlace.get_attribute('href')
		    if url.__contains__("https://www.linkedin.com/in/"): 
		    	primer_char = url[28]

		    	if primer_char.islower():
		    		arreglo_definitivo.append(url)

	


		arreglo_final = Limpieza.duplicadosArreglo(arreglo_definitivo)
		Limpieza.test(arreglo_final)

		return(arreglo_final)  #<----------arreglo final definitivo plus ultra + 1

	def es_ultima_pagina(self):
		
		time.sleep(5)
		elementos_h2 = self.driver.find_elements_by_tag_name('h2')
		time.sleep(5)
		# Verifica si el elemento fue encontrado
		for elemento in elementos_h2:
			fin = False
			#print(elemento.text)
			cadena = elemento.text
			if cadena.__contains__("Ningún resultado encontrado"):
				fin = True
				#print("Ya no hay mas resultados")
		return fin 

	

#multiples_url(busqueda_con_cadena("lis uady"), 2)
cadena_TODO_UADY = "https://www.linkedin.com/search/results/people/?heroEntityKey=urn%3Ali%3Aorganization%3A10646336&keywords=uady%20(universidad%20aut%C3%B3noma%20de%20yucat%C3%A1n)&origin=SWITCH_SEARCH_VERTICAL&page=XXXXX&position=1&searchId=e8b4deec-d1a1-4a2f-93eb-81bbfbacb525&sid=Tr1"

#multiples_url(cadena_TODO_UADY, 3)
#multiples_url(link_cambranes, 3)
#multiples_url(link_basto, 3)


link_cambranes = "https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAAAOo4HoBWdu3t3FHNyv7vZy0g5XgHsU4z3k%22%5D&network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&page=XXXXX&sid="
  


