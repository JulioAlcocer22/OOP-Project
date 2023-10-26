import re
from selenium import webdriver
# VERSION ACTUALIZADA PROXIMAMENTE
class scarper:

    def __init__(self, driver):
        self.driver = driver

    def scraperLinkEgresado(self):
        driver = webdriver.Edge(r"msedgedriver.exe")
        print(driver.current_url)

        #connection = database.ConectionDatabase()
        #connection.getConnection()
        #cursor = connection.connection.cursor()

        # link = "https://mx.linkedin.com/in/queso_plumaaaaaaa"
        link = driver.current_url

        #cursor.execute("INSERT INTO dbo.LinkEgresados VALUES (?)", link)

        #cursor.commit()
        #connection.closeConnection()

    # En casa ya tengo la nueva version SE OMITE LA REV DE CAMELCASE

    def obtenerExperiencia(self):

        salida_experiencia = ['PROFESOR', 'UNIVERSIDAD AUTONOMA DE YUCATAN', 'FEB. 2006 - ACTUALIDAD17 AÑOS 9 MESES', 'YUCATAN, MEXICO', 'AUDITOR DE TI', 'PROFESIONAL INDEPENDIENTE', 'NOV. 2015 - ACTUALIDAD8 AÑOS', 'YUCATAN, MEXICO', 'AUDITORIA INFORMATICA DE SOFTWARE CON EL FIN DE VERIFICAR LOS CONTROLES, SISTEMAS Y PROCEDIMIENTOS RELACIONADOS CON EL DESARROLLO Y MANTENIMIENTO DE APLICACIONES WEB Y MOVILES.',
                              'DISEÑADOR DE BASES', 'SEGEY', 'ENE. 2010 - DIC. 20101 AÑO', 'YUCATAN, MEXICO', 'ANALIZAR Y DISEÑAR LA BASE DE DATOS DEL SISTEMA DE CONTROL ESCOLAR DE NIVEL SUPERIOR DEL ESTADO DE YUCATAN (SCENSY) DE LA SECRETARIA GENERAL DE EDUCACION DEL ESTADO DE YUCATAN (SEGEY).', 'PROGRAMADOR', 'UADY, FACULTAD DE ODONTOLOGIA', 'AGO. 2000 - DIC. 20033 AÑOS 5 MESES']

        arreglo_sin_fecha = []

        for i, entrada in enumerate(salida_experiencia, start=1):
            # print(f"nuevoArreglo[{i}] = {entrada}")
            patron = r'[A-Z]*, [A-Z]*, [A-Z]*|[A-Z]*, [A-Z]*(, [A-Z]*)?'

            entrada = entrada.lstrip()  # Elimina espacios en blanco al principio
            entrada = entrada.rstrip()

            if re.findall(patron, entrada) or entrada.__contains__("MEXICO"):
                coincidencias = re.findall(patron, entrada)
                # print(coincidencias)
            else:
                entrada = entrada.lstrip()  # Elimina espacios en blanco al principio
                entrada = entrada.rstrip()
                # print(entrada)
                arreglo_sin_fecha.append(entrada)

        print("------------------------test")

        for i, entrada in enumerate(arreglo_sin_fecha, start=1):
            # print(f"arr[{i}] = {entrada}")
            # MEJORABLE
            patron = r'(ENE|FEB|MAR|ABR|MAY|JUN|JUL|AGO|SEP|OCT|NOV|DIC)[.,]?\s.*'

            if re.findall(patron, entrada):

                # detalle con las descripciones
                arreglo_sin_fecha.insert(i, "------------")

        arreglo_limiezito = []
        for i, cadena in enumerate(arreglo_sin_fecha, start=1):

            # MEJORABLE
            patron = r'(ENE|FEB|MAR|ABR|MAY|JUN|JUL|AGO|SEP|OCT|NOV|DIC)[.,]?\s.*'

            if re.findall(patron, cadena):
                cadena = cadena[21:]
                if cadena.startswith("D"):
                    cadena = cadena[1:]

            cadena = cadena.replace(" MESES", "")
            cadena = cadena.replace("AÑOS", "*")
            cadena = cadena.replace("AÑO", "*")
            cadena = cadena.replace("*", "* 0")
            cadena = cadena.replace("0 ", "0")
            # print(cadena)

            arreglo_limiezito.append(cadena)

        for i, cadena in enumerate(arreglo_limiezito, start=1):
            print(cadena)
