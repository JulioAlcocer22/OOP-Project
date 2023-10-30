import re
from selenium import webdriver
from Model.Limpieza import Limpieza
from selenium.webdriver.common.by import By

class Scraper:

    def __init__(self, driver):
        self.driver = driver

    def isUniversidadAndCarrera(self, universidad, carrera):
        verdad = False
        try:
            arregloDeEducacion = self.driver.find_elements_by_class_name(
                "education__list")

            elementoEstandarizado = Limpieza.estadandarizarCadenas(
                arregloDeEducacion[0].text)
        except:
            pass
        else:
            lineas = elementoEstandarizado.split('\n')

            nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]

            for i, entrada in enumerate(nuevoArreglo, start=1):
                # print(f"nuevoArreglo[{i}] = {entrada}")

                if universidad in entrada:
                    if nuevoArreglo[i].__contains__(carrera):
                        verdad = True

        return verdad

    def existExperience(self):
        verdad = False
        try:
            arregloDeEducacion = self.driver.find_elements_by_class_name(
                "experience__list")

            elementoEstandarizado = Limpieza.estadandarizarCadenas(
                arregloDeEducacion[0].text)
        except:
            print("NO encontrado")
        else:
            lineas = elementoEstandarizado.split('\n')

            nuevoArreglo = [linea.strip() for linea in lineas if linea.strip()]

            if len(nuevoArreglo) > 2:
                verdad = True

            # ---------------------------- testing
            # for i, entrada in enumerate(nuevoArreglo, start=1):
                # print(f"nuevoArreglo[{i}] = {entrada}")

            # print(nuevoArreglo)

        return verdad


    def verificarRequisitos(self, url, universidad, carrera):
        aprobado = False
        self.driver.get(url)
        time.sleep(5)
        config = Configuracion(self.driver)
        config.saltarModal()

        time.sleep(5)
        verif = Verificador(self.driver)
        # print(verif.existExperience())
        # print(verif.isUniversidadAndCarrera(universidad, carrera))

        if verif.existExperience() and verif.isUniversidadAndCarrera(universidad, carrera):
            # print("si cumple")
            return True

        return aprobado

    def obtenerExperiencia(self):

        
        arregloDeEducacion = self.driver.find_elements(By.CLASS_NAME, "experience__list")
        elemento_estandarizado = Limpieza.estadandarizarCadenas(arregloDeEducacion[0].text)

        lineas = elemento_estandarizado.split('\n')

        #for i, entrada in enumerate(lineas, start=1):
            #print(f"nuevoArreglo[{i}] = {entrada}")
        

        mi_lista = lineas
         
        #print(mi_lista)

        #mi_lista = ['PROFESOR', 'UNIVERSIDAD AUTONOMA DE YUCATAN', 'FEB. 2006 - ACTUALIDAD17 AÑOS 9 MESES', 'YUCATAN, MEXICO', 'AUDITOR DE TI', 'PROFESIONAL INDEPENDIENTE', 'NOV. 2015 - ACTUALIDAD8 AÑOS', 'YUCATAN, MEXICO', 'AUDITORIA INFORMATICA DE SOFTWARE CON EL FIN DE VERIFICAR LOS CONTROLES, SISTEMAS Y PROCEDIMIENTOS RELACIONADOS CON EL DESARROLLO Y MANTENIMIENTO DE APLICACIONES WEB Y MOVILES.', 'DISEÑADOR DE BASES', 'SEGEY', 'ENE. 2010 - DIC. 20101 AÑO', 'YUCATAN, MEXICO', 'ANALIZAR Y DISEÑAR LA BASE DE DATOS DEL SISTEMA DE CONTROL ESCOLAR DE NIVEL SUPERIOR DEL ESTADO DE YUCATAN (SCENSY) DE LA SECRETARIA GENERAL DE EDUCACION DEL ESTADO DE YUCATAN (SEGEY).', 'PROGRAMADOR', 'UADY, FACULTAD DE ODONTOLOGIA', 'AGO. 2000 - DIC. 20033 AÑOS 5 MESES']

        # Tu lista de ejemplo
        #mi_lista = ['PROFESOR', 'UNIVERSIDAD AUTONOMA DE YUCATAN', 'FEB. 2006 - ACTUALIDAD17 AÑOS 9 MESES', 'YUCATAN, MEXICO', 'AUDITOR DE TI', 'PROFESIONAL INDEPENDIENTE', 'NOV. 2015 - ACTUALIDAD8 AÑOS', 'YUCATAN, MEXICO', 'AUDITORIA INFORMATICA DE SOFTWARE CON EL FIN DE VERIFICAR LOS CONTROLES, SISTEMAS Y PROCEDIMIENTOS RELACIONADOS CON EL DESARROLLO Y MANTENIMIENTO DE APLICACIONES WEB Y MOVILES.', 'DISEÑADOR DE BASES', 'SEGEY', 'ENE. 2010 - DIC. 20101 AÑO', 'YUCATAN, MEXICO', 'ANALIZAR Y DISEÑAR LA BASE DE DATOS DEL SISTEMA DE CONTROL ESCOLAR DE NIVEL SUPERIOR DEL ESTADO DE YUCATAN (SCENSY) DE LA SECRETARIA GENERAL DE EDUCACION DEL ESTADO DE YUCATAN (SEGEY).', 'PROGRAMADOR', 'UADY, FACULTAD DE ODONTOLOGIA', 'AGO. 2000 - DIC. 20033 AÑOS 5 MESES']

        # Nueva lista para almacenar los elementos modificados
        nueva_lista = []

        # Recorre la lista original y agrega "---------" después de la cadena de más de 50 caracteres
        for elemento in mi_lista:
            nueva_lista.append(elemento)
            if len(elemento) > 50:
                nueva_lista.append("CCC")

        nueva_lista2 = []
        # Imprime la lista actualizada
        for elemento2 in nueva_lista:
            nueva_lista2.append(elemento2)
            if elemento2.__contains__("YUCATAN"): #agregar paises y estados juntos y separados
                nueva_lista2.append("BBB")
        
        
        nueva_lista3 = []
        for elemento in nueva_lista2:
            nueva_lista3.append(elemento)
            if any(elemento.startswith(mes) for mes in ("ENE.", "FEB.", "MAR.", "ABR.", "MAY.", "JUN.", "JUL.", "AGO.", "SEPT.", "OCT.", "NOV.", "DIC.")):
                nueva_lista3.append("AAA")



        #for elemento in nueva_lista3:
            #print(elemento)
        for i in range(len(nueva_lista3) - 4) :
            if nueva_lista3[i].__contains__("AAA") and nueva_lista3[i+2].__contains__("BBB") and nueva_lista3[i+4].__contains__("CCC"):
                nueva_lista3[i] = nueva_lista3[i].replace("AAA","")
                nueva_lista3[i+2] = nueva_lista3[i+2].replace("BBB","")
                nueva_lista3[i+4] = nueva_lista3[i+4].replace("CCC","----------")

        for i in range(len(nueva_lista3) - 2) :
            if nueva_lista3[i].__contains__("AAA") and nueva_lista3[i+2].__contains__("BBB"):
                nueva_lista3[i] = nueva_lista3[i].replace("AAA","")
                nueva_lista3[i+2] = nueva_lista3[i+2].replace("BBB","----------")

        for i in range(len(nueva_lista3)) :
            if nueva_lista3[i].__contains__("AAA"):
                nueva_lista3[i] = nueva_lista3[i].replace("AAA","----------")

        for i in range(len(nueva_lista3) - 1) :
            if nueva_lista3[i].__contains__("BBB") and nueva_lista3[i+1].__contains__("CCC"):
                nueva_lista3[i] = nueva_lista3[i].replace("BBB","")
                nueva_lista3[i+1] = nueva_lista3[i+1].replace("CCC","----------")


        for i in range(len(nueva_lista3) - 1) :
            if nueva_lista3[i].__contains__("----------") and nueva_lista3[i+2].__contains__("CCC"):
                nueva_lista3[i] = nueva_lista3[i].replace("----------","")
                nueva_lista3[i] = nueva_lista3[i].replace("CCC","----------")
           
        for i in range(len(nueva_lista3) - 2) :
 
            if nueva_lista3[i].__contains__("YUCATAN") and nueva_lista3[i+1].__contains__("----------") and len(nueva_lista3[i+2]) > 50:
                nueva_lista3[i+1] = nueva_lista3[i+1].replace("----------","")
    
        for i in range(len(nueva_lista3)) :
            if nueva_lista3[i].__contains__("BBB"):
                nueva_lista3[i] = nueva_lista3[i].replace("BBB","")

          

         

        mi_arreglo_sin_vacios = []
        for elemento in nueva_lista3:
            if elemento != "":
                mi_arreglo_sin_vacios.append(elemento)  

        for elemento in mi_arreglo_sin_vacios:
            print(elemento) 

#driver = 0
#scrap = Scraper(driver)
#scrap.obtenerExperiencia()