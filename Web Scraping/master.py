from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import re
import database
import pyodbc
import json
import time


delay = 10
link_egresado = 'https://www.linkedin.com/in/pablo-baeza'
#https://mx.linkedin.com/in/viviana-guadalupe-azcorra-novelo-351706231?trk=public_profile_browsemap
driver = webdriver.Edge(r"msedgedriver.exe")


def saltarModal():
	driver.get(link_egresado)
	time.sleep(5)
	actions = ActionChains(driver)
	actions.send_keys(Keys.TAB)
	actions.send_keys(Keys.ENTER)
	actions.perform()
	time.sleep(5)



def estadandarizarCadenas(s):
	cambios = (
		("á", "a"),
		("é", "e"),
		("í", "i"),
		("ó", "o"),
		("ú", "u"),
	)

	for a, b in cambios:
		s = s.replace(a, b).replace(a.upper(), b.upper())

	return s.upper()
	

def isUniversidadAndCarrera(universidad, carrera):
	verdad = False
	try:
		arregloDeEducacion = driver.find_elements_by_class_name("education__list")
		
		elemento_estandarizado = estadandarizarCadenas(arregloDeEducacion[0].text)
	except:
		pass
	else:
		lineas = elemento_estandarizado.split('\n')
			
		nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]

		for i, entrada in enumerate(nuevoArreglo, start=1):
			print(f"nuevoArreglo[{i}] = {entrada}")

			if universidad in entrada:
			   	if nuevoArreglo[i].__contains__(carrera):
			   		verdad = True

	return verdad

def existExperience():
	verdad = False
	try:
		arregloDeEducacion = driver.find_elements_by_class_name("experience__list")
		
		elemento_estandarizado = estadandarizarCadenas(arregloDeEducacion[0].text)
	except:
		pass
	else:
		lineas = elemento_estandarizado.split('\n')
			
		nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]

		if len(nuevoArreglo) > 2:
			verdad = True

		#---------------------------- testing
		for i, entrada in enumerate(nuevoArreglo, start=1):
			print(f"nuevoArreglo[{i}] = {entrada}")

	return verdad
		    	

#saltarModal()
#print(existExperience())
#print(isUniversidadAndCarrera("UNIVERSIDAD AUTONOMA DE YUCATAN", 'LICENCIATURA EN INGENIERIA DE SOFTWARE'))
#driver.close()

def iniciarSesion():
	delay = 10
	linkHomePage = 'https://www.linkedin.com/home'
	email = 'xxxxxxx' #SECRETOOOOOOOOOOOOOOO
	password = 'xxxxxxx'  #SECRETOOOOOOOOOOOOOOO

	driver.get(linkHomePage) #Se dirige a la página principal de LinkedIn
	driver.implicitly_wait(delay)  #Espera hasta que la página cargue

	inputUser = driver.find_element(By.NAME, "session_key")
	inputUser.send_keys(email)
	

	inputPassword = driver.find_element(By.NAME, "session_password")
	inputPassword.send_keys(password)
	driver.implicitly_wait(5)
	inputPassword.send_keys(Keys.ENTER)

#----------------------------------------------
#iniciarSesion()
#driver.maximize_window()
#driver.implicitly_wait(5)
#campo_de_texto = driver.find_element_by_class_name('search-global-typeahead__input')
#campo_de_texto.send_keys('software uady')
#campo_de_texto.send_keys(Keys.ENTER)


#driver.implicitly_wait(5)
#boton_persona = driver.find_element_by_xpath('//*[@id="search-reusables__filters-bar"]/ul/li[1]/button')
#boton_persona.click()

#driver.implicitly_wait(5)
#----------------------------------------------
#print("inicia")
#try:
	#arregloDeEducacion = driver.find_elements_by_xpath('/html/body/main/section/ol/li[*]/a')
		
	#elemento_estandarizado = estadandarizarCadenas(arregloDeEducacion[0].text)
#except:
	#pass
#else:
	#lineas = elemento_estandarizado.split('\n')
			
	#nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]

		#---------------------------- testing
	#for i, entrada in enumerate(nuevoArreglo, start=1):
		#print(f"nuevoArreglo[{i}] = {entrada}")


#print("acaba")
#https://www.linkedin.com/search/results/people/?keywords=uady           &origin=GLOBAL_SEARCH_HEADER&sid=GQJ
#https://www.linkedin.com/search/results/people/?keywords=software%20uady&origin=SWITCH_SEARCH_VERTICAL&sid=BAY
#https://www.linkedin.com/search/results/people/?keywords=software%20uady&origin=SWITCH_SEARCH_VERTICAL&page=2&sid=Dyl

#https://www.linkedin.com/search/results/people/?keywords=software%20 uady%20 lis&origin=GLOBAL_SEARCH_HEADER&sid=%2C(s
#https://www.linkedin.com/search/results/people/?keywords= pablo%20 ernesto%20 baeza%20 lara &origin=GLOBAL_SEARCH_HEADER&sid=~z4
#https://www.linkedin.com/search/results/people/?keywords=pablo%20%20lara&origin=GLOBAL_SEARCH_HEADER&page=6&sid=QFy

#ER
#https://www.linkedin.com/search/results/people/?keywords=   *  ( cadena  * %20 )*   * cadena &origin=GLOBAL_SEARCH_HEADER& page= (numero) &sid=xxx

def busqueda_con_cadena(cadena):

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


def multiples_url(url, indice_final):

	for i in range(indice_final):
		nueva_url = url.replace("XXXXX", str(i))
		print(nueva_url) 


#multiples_url(busqueda_con_cadena("lis uady"), 2)
cadena_TODO_UADY = "https://www.linkedin.com/search/results/people/?heroEntityKey=urn%3Ali%3Aorganization%3A10646336&keywords=uady%20(universidad%20aut%C3%B3noma%20de%20yucat%C3%A1n)&origin=SWITCH_SEARCH_VERTICAL&page=XXXXX&position=1&searchId=e8b4deec-d1a1-4a2f-93eb-81bbfbacb525&sid=Tr1"

#multiples_url(cadena_TODO_UADY, 3)


link_cambranes = "https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAAAOo4HoBWdu3t3FHNyv7vZy0g5XgHsU4z3k%22%5D&network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&page=XXXXX&sid="
link_basto =     "https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAABRXgI0BwCsTdV-qkdhpzZ2dUYR3UB4McyE%22%5D&network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&page=XXXXX&sid="

#multiples_url(link_cambranes, 3)
#multiples_url(link_basto, 3)

iniciarSesion()
time.sleep(5)

#Cadena que sabemos que no existe
#driver.get("https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAABRXgI0BwCsTdV-qkdhpzZ2dUYR3UB4McyE%22%5D&network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&page=39&sid=")

    

def es_ultima_pagina(url):
	driver.get(url)
	time.sleep(5)
	elementos_h2 = driver.find_elements_by_tag_name('h2')
	time.sleep(5)
	# Verifica si el elemento fue encontrado
	for elemento in elementos_h2:
		fin = False
		print(elemento.text)
		cadena = elemento.text
		if cadena.__contains__("Ningún resultado encontrado"):
			fin = True
			print("Ya no hay mas resultados")



#Encontrar links de una pagina de resultado
driver.get("https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAABRXgI0BwCsTdV-qkdhpzZ2dUYR3UB4McyE%22%5D&network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&page=20&sid=")

time.sleep(10)
enlaces = driver.find_elements_by_css_selector('a.app-aware-link')

arreglo_limpio = []
# Itera a través de los enlaces e imprime sus URLs
for enlace in enlaces:
    url = enlace.get_attribute('href')
    print(url)

    if url.__contains__("https://www.linkedin.com/in/"):
    	arreglo_limpio.append(url) 

print(arreglo_limpio)

arreglo_definitivo = []
for enlace in arreglo_limpio:
	print(enlace)
	#print(enlace[28])

	primer_char = enlace[28]
	if primer_char.islower():
		arreglo_definitivo.append(enlace)


mi_arreglo_sin_duplicados = []
for elemento in arreglo_definitivo:
    if elemento not in mi_arreglo_sin_duplicados:
        mi_arreglo_sin_duplicados.append(elemento)
        print("-----------------------------")
        print(elemento)

#print(mi_arreglo_sin_duplicados)  <----------arreglo final definitivo plus ultra + 1



    
 
