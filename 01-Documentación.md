# LinkedIn Scrapper
LinkedIn Scrapper es un proyecto que consiste en un artefacto de código que,a través de Web Scrapping, obtiene información de los perfiles de LinkedIn de los egresados de la Facultad de Matemáticas UADY de la carrera de Ingeniería de Soffware. De igual manera, por medio de una análsiis de lenguaje natural, se analizarán las descripciones de los trabajaos de los egresados. Finalmente, los datos se presentarán mediante una página web de acceso para todo público.

# Tabla de Contenidos
- [Preguntas por Responder](#preguntas-por-responder)
- [Funcionalidades de LinkedIn Scrapper](#funcionalidades-de-linkedin-scrapper)
- [Tecnologías/Herramientas Usadas](#tecnologíasherramientas-usadas)
- [Responsables del Proyecto](#responsables-del-proyecto)

# Preguntas por Responder
El análisis de datos que se obtendrá al final del proyecto y que visualizará el usuario responderá a tres preguntas que a continuación se presentan:

- ¿Qué empresas contratan egresados de la Facultad de Matemáticas UADY de la carrera de Ingeniería de Software?
- ¿Qué puestos han ocupado dichos egresados en sus respectivas empresas?
- ¿Cuánto tiempo en promedio permanecen dichos egresados en cada trabajo? 

# Funcionalidades de LinkedIn Scrapper

- ## Web Scrapping / REST API
    ### Responsables: Pablo Baeza y Daniel Kao
    Este bloque consistirá en dos partes:
    
    - **Primera parte:** Este consiste en la búsqueda y recolección de datos que se encuentren en los perfiles de LinkedIn. Dicho servicio será alojado mediante una REST API para que pueda ser consumida por el frontend
    - **Segunda parte:**  Este consiste en la búsqueda y recolección de datos para el entrenamiento del modelo de análisis del lenguaje natural.

- ## Bases de Datos / Análisis de Datos
    ### Responsable: Alex Dzul
    Este bloque tiene la finalidad de subir los la información recabada del Web Scrapping a una base de datos, así como limpiarlos y prepararlos para la siguiente fase. Igualmente, por medio de métodos estadísticos se analizarán los datos recabados, para obtener las conclusiones necesarias que serán presentadas en el frontend.

- ## Análisis del Lenguaje Natural
    ### Responsable: Julio Alcocer

- ## Página Web
    #### Responsables: Rodrigo Canto y Daniel Kao
    Una vez se han terminado los procesos anteriores, se mostrará por medio de una página web los datos al usuario de forma clara y amigable.

# Tecnologías/Herramientas Por Usar
- **Lenguaje de programacion para el Web Scraping:** Python V 3.11.1 Framework para el web Scraping ( Python ): Selenium V 4.12.0 Framework para la REST API: Por definir

- **Base de datos relacional ( SQL ): MySQL V 8.1.0 Alojamiento virtual de la base de datos:** PlanetScale ( https://planetscale.com/ ) Lenguaje de programacion para el analisis de datos: Por definir

- **Lenguaje de programacion para el analisis del lenguaje natural:** Por definir Framework para el analisis del lenguaje natural: Por definir

- **Herramientas para el diseño web:** HTML5, CSS3, C#

# 

# Responsables del Proyecto
El proyecto está a cargo de estudiantes de 3° semestre de la carrera de Ingeniería de Software, bajo supervisión del docente Edgar Cambranes para la asignatura de Porgramación Orientada a Objetos. Los responsables son los siguientes:

- [Julio César Alcocer Herrera](http://www.linkedin.com/in/juliocalcocer011235)
- [Pablo Ernesto Baeza Lara](www.linkedin.com/in/pablo-baeza)
- [Rodrigo Adrián Canto Paredes](https://www.linkedin.com/in/rodrigo-adri%C3%A1n-canto-paredes-490461268/)
- [Alex Enrique Dzul López](https://www.linkedin.com/in/alex-dzul-l%C3%B3pez-967846258/)
- [Juan Daniel Kao Pech](www.linkedin.com/in/danielkaojp)