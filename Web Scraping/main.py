# Importaciones necesarias
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Declaracion del tiempo de espera en segundos
delay = 15
link_egresado = 'https://mx.linkedin.com/in/viviana-guadalupe-azcorra-novelo-351706231?trk=public_profile_browsemap'

# Activacion del driver se requiere el archivo msedgedriver.exe asi como la ultima version del navegador Microsoft Edge
driver = webdriver.Edge(r"msedgedriver.exe")

# Ingresar al link declarado
driver.get(link_egresado)

# Espera mientras carga la pagina web ( Se puede reducir el tiempo dependiendo de la velocidad de la pc )
driver.implicitly_wait(delay) 

#Saltar pop up de inicio de sesion (Se utilizara para pruebas temporalmete)

# Presionar TAB y ENTER en el navegador
actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.ENTER)
actions.perform()

driver.implicitly_wait(delay) 


#-----------------------------------------------------------ok mejorable con class

# xpath del nombre del egresado en linkedin ( etiqueta inmutable )
xpath_nombre = '//*[@id="main-content"]/section[1]/div/section/section[1]/div/div[2]/div[1]/h1'

#Encontrar el nombre del egresado
row_data = driver.find_element_by_xpath(xpath_nombre).text
print("Nombre del egresado: ", row_data)
#Encontrar el url del egresado
print("URL egresado: ", driver.current_url)

#-----------------------------------------------------------ok


# Devolver los campos que se encuentran en el apartado de educacion ( Es un arreglo
a = driver.find_elements_by_class_name("education__list")
for x in a:
	print(x.text)

# Cerrar el driver y finalizar proceso
driver.close()


# Devuelve absolutamente todo ----> profile-section-card__contents 
