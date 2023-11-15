import datetime
from selenium.webdriver.common.by import By
from Model.Utilidades import Utilidades





class ScraperDatos:

    def __init__(self, driver):
        self.driver = driver
        self.PADDINGSIMPLE = 22
        self.PADDINGCOMPUESTO = 23

    def CampoSimple(self):

        experience_items = self.driver.find_elements(By.CSS_SELECTOR, ".profile-section-card.experience-item")
        
        for item in experience_items:
            try:
                description_elements = item.find_element(By.CSS_SELECTOR, ".experience__list .show-more-less-text__text--less").text
            except :
                description_elements = "NOPE"
            
            
            elemento = item.text
            lineas = elemento.split('\n')
            nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]

            puesto = nuevoArreglo[0]
            empresa = nuevoArreglo[1]
            fechas = nuevoArreglo[2]

            inicio, fin, duracion = Utilidades.separarDuracion(fechas, self.PADDINGSIMPLE)

            print(empresa + "---" + puesto + "---" + inicio + "---" + fin + "---" + duracion + "---" + description_elements)
            print("")

        return 0  # Aqui se devolveria el objeto deseado

    def CampoCompuesto(self):
        # Itera a través de los elementos y obtén el contenido
        elementsf = self.driver.find_elements(
            By.CSS_SELECTOR, "a.experience-group-header__url")
        for elementf in elementsf:
            elemento = elementf.text
            lineas = elemento.split('\n')
            nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]
            puesto = nuevoArreglo[0]

            # OBTENER DATOS CASO MULTIPLES
            elements = self.driver.find_elements(By.CSS_SELECTOR, "li.profile-section-card.experience-group-position")
            for element in elements:
                elemento = element.text
                lineas = elemento.split('\n')
                nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]
                
                try:
                    description_elements = element.find_element(By.CSS_SELECTOR, ".experience__list .show-more-less-text__text--less").text
                except :
                    description_elements = "NOPE"

                empresa = nuevoArreglo[0]
                fechas = nuevoArreglo[1]

                inicio, fin, duracion = Utilidades.separarDuracion(fechas, self.PADDINGCOMPUESTO)


                print(puesto  + "---" + empresa + "---" + inicio + "---" + fin + "---" + duracion + "---" + description_elements)
                print("")

        return 0  # Aqui se devolveria el objeto deseado

    def unicamenteDescripciones(self):

        description_elements = self.driver.find_elements(By.CSS_SELECTOR, ".experience__list .show-more-less-text__text--less")
        descriptions = [element.text for element in description_elements]

        for description in descriptions:
            print(description)

        return 0  # Aqui se devolveria el objeto deseado

    def verificarExperiencia(self):
        verdad = False
        elementos_h2 = self.driver.find_elements(By.TAG_NAME, 'h2')
        for elemento in elementos_h2:
            cadena = elemento.text
            if cadena.__contains__("Experiencia"):
                verdad = True

        return verdad

    def verificarUniversidad_Carrera_Egresado(self, universidad, acronimoUniversidad,  carrera):
        verdad = False
        anioActual = datetime.datetime.now().year
        universidad = Utilidades.estadandarizarCadenas(universidad)
        carrera = Utilidades.estadandarizarCadenas(carrera)
        acronimoUniversidad = Utilidades.estadandarizarCadenas(acronimoUniversidad)
        
        
        arregloNombreEgresado = self.driver.find_elements(By.TAG_NAME, 'h1')
        nombreEgresado = arregloNombreEgresado[0].text

            
            

        experience_items = self.driver.find_elements(By.CSS_SELECTOR, ".profile-section-card.education__list-item")
        for item in experience_items:
            elemento = item.text
            lineas = elemento.split('\n')
            nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]
            if len(nuevoArreglo) >= 3:

                anioEgreso = int(nuevoArreglo[2].split("-")[1].strip())
                nuevoArreglo[0] = Utilidades.estadandarizarCadenas(nuevoArreglo[0])
                nuevoArreglo[1] = Utilidades.estadandarizarCadenas(nuevoArreglo[1])

                
                if nuevoArreglo[0].__contains__(universidad) or nuevoArreglo[0].__contains__(acronimoUniversidad) and nuevoArreglo[1].__contains__(carrera) and anioEgreso <= anioActual:
                    print (nombreEgresado + "---" + universidad + "---" + carrera)
                    verdad = True
        return verdad
