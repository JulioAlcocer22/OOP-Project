from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

delay = 15
driver = webdriver.Edge(r"msedgedriver.exe")
driver.get('https://www.linkedin.com/in/roger-solis/')

driver.implicitly_wait(delay) 

#Saltar pop up para iniciar sesion (Se utilizara para pruebas temporalmete)
actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.ENTER)
actions.perform()

driver.implicitly_wait(delay) 

#Obtener nombre del egresado
cadena_titulo = driver.title
division = cadena_titulo.split("-")
nombre_egresado = division[0]
print("Nombre egresado: ", nombre_egresado)
print("URL egresado: ", driver.current_url)

driver.close()

