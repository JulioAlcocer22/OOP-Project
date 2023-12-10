# **Requisitos Del Proyecto**
## **Escala De Prioridades**
Se definieron las siguientes escalas para clasificar los requisitos:
* Prioridad S (Muy Alta)
* Prioridad A (Alta)
* Prioridad B (Media)
* Prioridad C (Baja)

## **Requisitos Funcionales**
### **_RF-001 Web Scrapping (Prioridad S)_** 
---
- [x] El sistema recolecta los enlaces de los perfiles de LinkedIn de cada uno de los egresados y los da de alta a la base de datos. (Se cumple por medio de los metodos implementado metodoCadena, metodoUrl, etc)
- [x] El sistema realiza 3 tipos de búsqueda: por pivote, por cadenas y por url.( Los tres tipos de busqueda se encuentran funcionales y presentes en la interfaz grafica del desarrollador)
- [x] El sistema realiza el scrapping, uno por uno, de los enlaces previamente recolectados. (Se cumple explicitamente con las funciones extraer experiencia LIS-LCC)
- [x] El sistema da de alta en la base de datos la información recabada de los enlaces.( Se cumple con las funciones implementadas internamente)

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
- [x] El sistema clasifica el rol de un egresado según su descripción del puesto en LinkedIn.(Se cumple con las funciones implementadas de ALN)

### **_RF-004 Análisis De Datos (Prioridad A)_**
---
- [x] El sistema debe aplicar los filtros, las operaciones aritméticas y procesos estadísticos necesarios para responder a las preguntas:

    1. ¿Qué empresas contratan egresados de la Facultad de Matemáticas de la carrera de LIS?
    2. ¿Qué puestos han ocupado dichos egresados de LIS en sus respectivos trabajos?
    3. ¿Cuál es la duración promedio, de los egresados de LIS, en el que duran en un trabajo?
     
Se cumple ya que se cuentan con los datos suficientes para realizar los procesos estadisticos necesarias, la informacion obtenida mediante el Web Scraping, es la justa y necesaria para responder las preguntas.

### **_RF-005 Interfaz Gráfica (Prioridad C)_**
---
- [x] La interfaz presenta una parte para aplicar filtros para la universidad y carrera que se desea ver resultados. (Es apreciable en la pagina web)
- [x] La interfaz presenta los datos de la base de datos mediante gráficas.(Es apreciable en la pagina web)

## Requisitos No Funcionales
### **_RNF-001 Mantenibilidad y Actualización de Datos(Prioridad S)_**
- [x] Anualmente, se utiliza el código de Web Scrapping para recolectar nuevos egresados y actualizar la información de los egresados ya tomados en cuenta en la base de datos.

- Actualización de Datos: Esto se cumple debido a que para el apartado de Web Scraping se diseño una GUI simple ( para el desarrollador ) que permite ejecutar todas las operaciones anteriormente mencionadas con solo un boton, lo que implica que no es necesario compilar ni modificar nada para el ususario final.
- Mantenibilidad: El codigo se encuentra extremadamente modularizado, presentando alta cohesion y bajo acoplamiento de tal manera que si se quisiera alterar el giro del programa, muchas funciones pueden ser reutilizadas.De igual manera, se ha realizado el codigo pensando en su durabilidad a largo plazo, haciendo las funciones bien delimitadas y explicitas.
