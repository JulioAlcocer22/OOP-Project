from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re

delay = 15
link_egresado = 'https://mx.linkedin.com/in/viviana-guadalupe-azcorra-novelo-351706231?trk=public_profile_browsemap'
driver = webdriver.Edge(r"msedgedriver.exe")
driver.get(link_egresado)

driver.implicitly_wait(delay) 

#Saltar pop up para iniciar sesion (Se utilizara para pruebas temporalmete)
actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.ENTER)
actions.perform()

driver.implicitly_wait(delay) 


#-----------------------------------------------------------ok mejorable con class
xpath_nombre = '//*[@id="main-content"]/section[1]/div/section/section[1]/div/div[2]/div[1]/h1'
row_data = driver.find_element_by_xpath(xpath_nombre).text
print("Nombre del egresado: ", row_data)
print("URL egresado: ", driver.current_url)
#-----------------------------------------------------------ok


# Devolver los campos que se encuentran en el apartado de educacion
a = driver.find_elements_by_class_name("education__list")
for x in a:
	print(x.text)


driver.close()


# Devuelve absolutamente todo ----> profile-section-card__contents 