# Bienvenidos a LinkedIn Scraper

## Introduccion:
Elaboraremos un artefacto de codigo que permita a traves del web scraping, obtener datos relevantes ( Roles de trabajo, tiempo de duracion proimedio, empresas donde han trabajado los egresados ) de los perfiles de linkedin de los alumnos egresados de la facultad de matematicas (UADY), especificamente de la carrera Lic. en Ingenieria de Software, con dichas datos recabados se obtendran estadisticas antes mencionadas. De igual manera, por medio del analisis del lenguaje natural, se analizaran las descripciones de los trabajos de los egresados. Finalmente los datos seran presentados por medio de una pagina web, de tal manera que toda la informacion este disponible para el publico en general.

---

## Descripcion de los componentes del proyecto:
### Importante: NO es una descripcion de clases, unicamente tiene el fin de segmentar los modulos pertinentes del proyecto.

El proyecto en si se compone de varias bloques, en este apartado se explican unicamente las descripciones generales, para acceder a descripciones mas detalladas, lo invitamos a acceder a las ramas especificas de cada parte.

### Web scarping / REST API
#### Responsable: Pablo Baeza / Daniel Kao

Este bloque sera el encargado de la obtencion y busqueda de los datos que se encuentren en los perfiles de linkedin. Dicho servicio sera alojado mediante una REST API para que de esa manera pueda ser consumido mediante el frontend.

### Base de datos / Analisis de datos 
#### Responsable: Alex Dzul

Este bloque tiene la finalidad de subir los la informacion a una base de datos, asi como limpiarlos y prepararlos para la siguiente fase, igualmente, 
por medio de metodos estadisticos se analizaran los datos recabados, para obtener las conclusiones necesarias que seran presentadas en nuestro frontend.

### Analisis del lenguaje natural
#### Responsable: Julio Alcocer

Por medio de metodos especificos de la area, analizar las descripciones de trabajo para obtener las conclusiones necesarios. **SE REQUIERE MAS INFORMACION**


### Pagina Web (Salida de datos)
#### Responsable: Rodrigo Canto / Daniel Kao

Una vez se han terminado los procesos anteriores, se mostrara por medio de una pagina web los datos al usuario de forma clara y amigable.

---

## Especificaciones Tecnicas:
Lenguaje de programacion para el web Scraping: Python V 3.11.1
Framework para el web Scraping ( Python ): Selenium V 4.12.0
Framework para la REST API: **Por definir**

Base de datos relacional ( SQL ): MySQL V 8.1.0
Alojamiento virtual de la base de datos: PlanetScale ( https://planetscale.com/ )
Lenguaje de programacion para el analisis de datos: **Por definir**

Lenguaje de programacion para el analisis del lenguaje natural: **Por definir**
Framework para el analisis del lenguaje natural: **Por definir**

"Lenguajes de programacion" para el diseño web: HTML5,  CSS3, C#
