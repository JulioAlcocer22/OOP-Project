# **Requisitos Del Proyecto**

# Tabla de Contenido
* [Escala de Prioridades](#escala-de-prioridades)
* [Requisitos Funcionales](#requisitos-funcionales)
    * [RF-001](#rf-001-web-scrapping-prioridad-s)
    * [RF-002](#rf-002-base-de-datos-prioridad-s)
    * [RF-003](#rf-003-modelo-procesamiento-del-lenguaje-natural-prioridad-b)
    * [RF-004](#rf-004-análisis-de-datos-prioridad-a)
    * [RF-005](#rf-005-interfaz-gráfica-prioridad-c)
* [Requisitos No Funcionales](#requisitos-no-funcionales)
    * [RNF-001](#rnf-001-mantenibilidad-y-actualización-de-datosprioridad-s)

* [Correspondencia con los RF/RNF](#correspondencia-con-los-rfrnf)
    * [Verificación RF-001](#verificación-rf-001)
    * [Verificación RF-002](#verificación-rf-002)
    * [Verificación RF-003](#verificación-rf-003)
    * [Verificación RF-004](#verificación-rf-004)
    * [Verificación RF-005](#verificación-rf-005)
    * [Verificación RNF-001](#verificación-rnf-001)

## **Escala De Prioridades**
Se definieron las siguientes escalas para clasificar los requisitos:
* Prioridad S (Muy Alta)
* Prioridad A (Alta)
* Prioridad B (Media)
* Prioridad C (Baja)

## **Requisitos Funcionales**
### **_RF-001 Web Scrapping (Prioridad S)_** 
---
- [x] El sistema recolecta los enlaces de los perfiles de LinkedIn de cada uno de los egresados y los da de alta a la base de datos. 
- [x] El sistema realiza 3 tipos de búsqueda: por pivote, por cadenas y por url.
- [x] El sistema realiza el scrapping, uno por uno, de los enlaces previamente recolectados.
- [x] El sistema da de alta en la base de datos la información recabada de los enlaces.

### **_RF-002 Base De Datos (Prioridad S)_**
---
**Se cambio la estructura de la base de datos, los requisitos se modificaron**
* La base de datos cuenta con 4 tablas:
    1. Tabla de links.
    2. Tabla de información del egresado (nombre, carrera y universidad).
    3. Tabla de experiencia del egresado (puesto, duración, descripción).
    4. Tabla de egresado final (empresa, duración y rol).

### **_RF-003 Modelo Procesamiento Del Lenguaje Natural (Prioridad B)_**
---
- [x] El sistema clasifica el rol de un egresado según su descripción del puesto en LinkedIn.

### **_RF-004 Análisis De Datos (Prioridad A)_**
---
- [x] El sistema debe aplicar los filtros, las operaciones aritméticas y procesos estadísticos necesarios para responder a las preguntas:

    1. ¿Qué empresas contratan egresados de la Facultad de Matemáticas de la carrera de LIS?
    2. ¿Qué puestos han ocupado dichos egresados de LIS en sus respectivos trabajos?
    3. ¿Cuál es la duración promedio, de los egresados de LIS, en el que duran en un trabajo?

### **_RF-005 Interfaz Gráfica (Prioridad C)_**
---
- [x] La interfaz presenta una parte para aplicar filtros para la universidad y carrera que se desea ver resultados.
- [x] La interfaz presenta los datos de la base de datos mediante gráficas.

## Requisitos No Funcionales
### **_RNF-001 Mantenibilidad y Actualización de Datos(Prioridad S)_**
- [x] Anualmente, se utiliza el código de Web Scrapping para recolectar nuevos egresados y actualizar la información de los egresados ya tomados en cuenta en la base de datos.

## Correspondencia con los RF/RNF

### Verificación RF-001
---
- El sistema recolecta enlaces de LinkedIn por medio de varios métodos, como: *metodoCadena, metodoURL, etc*.
- Existen tres tipos de búsqueda que se encuentran funcionales y presentes en la interfaz grafica del desarrollador para el Web Scrapping.
- El método de extraer expriencia LIS-LCC se encuentra en la interfaz del desarrollador y realiza la recolección de experiencia del perfil de LinkedIn de manera eficiente.
- El módulo de Web Scrapping cuenta con la conexión a la base de datos para la interacción de ambas partes.

### Verificación RF-002
---
- La base de datos cuenta ya con las tablas creadas correspondientes al proyecto.

### Verificación RF-003
---
- Funciones implementadaS en el módulo de PLN para recibir una descripción de la base de datos y retornar a éste un rol correspondiente a dicha descripción.

### Verificación RF-004
---
- Con los datos recopilados del Web Scrapping, se pueden realizar los procesos estadísticos necesarios para responder a las preguntas del proyecto.

### Verificación RF-005
---
- La interfaz cuenta con una primera vista que funciona como un Log in, al seleccionar una universidad y una carrera.
- La interfaz cuenta con una segunda vista que funciona para visualizar los datos recopilados y analizados a manera de gráficas para una mejor compresión.

### Verificación RNF-001
---
- Actualización de Datos: En el apartado de Web Scraping se diseñó una GUI simple (para el desarrollador) que permite ejecutar todas las operaciones anteriormente mencionadas con sólo un botón, lo que implica que no es necesario compilar ni modificar nada para el ususario final.
- Mantenibilidad: El código se encuentra extremadamente modularizado, presentando alta cohesión y bajo acoplamiento, de tal manera que si se quisiera alterar el giro del programa, muchas funciones pueden ser reutilizadas. De igual manera, se ha realizado el código pensando en su durabilidad a largo plazo, haciendo las funciones bien delimitadas y explícitas.