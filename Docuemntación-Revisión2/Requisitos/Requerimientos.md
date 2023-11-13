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
* El sistema recolecta los enlaces de los perfiles de LinkedIn de cada uno de los egresados y los da de alta a la base de datos,
* El sistema realiza 3 tipos de búsqueda: por pivote, por cadenas y por url.
* El sistema realiza el scrapping, uno por uno, de los enlaces previamente recolectados.
* El sistema da de alta en la base de datos la información recabada de los enlaces.

### **_RF-002 Base De Datos (Prioridad S)_**
---
* La base de datos cuenta con 4 tablas:
    1. Tabla de links.
    2. Tabla de información del egresado (nombre, carrera y universidad).
    3. Tabla de experiencia del egresado (puesto, duración, descripción).
    4. Tabla de egresado final (empresa, duración y rol).

### **_RF-003 Modelo Procesamiento Del Lenguaje Natural (Prioridad B)_**
---
* El sistema clasifica el rol de un egresado según su descripción del puesto en LinkedIn.

### **_RF-004 Análisis De Datos (Prioridad A)_**
---
* El sistema debe aplicar los filtros, las operaciones aritméticas y procesos estadísticos necesarios para responder a las preguntas:

    1. ¿Qué empresas contratan egresados de la Facultad de Matemáticas de la carrera de LIS?
    2. ¿Qué puestos han ocupado dichos egresados de LIS en sus respectivos trabajos?
    3. ¿Cuál es la duración promedio, de los egresados de LIS, en el que duran en un trabajo?

### **_RF-005 Interfaz Gráfica (Prioridad C)_**
---
* La interfaz presenta una parte para aplicar filtros para la universidad y carrera que se desea ver resultados.
* La interfaz presenta los datos de la base de datos mediante gráficas.

## Requisitos No Funcionales
### **_RNF-001 Mantenibilidad y Actualización de Datos(Prioridad S)_**
* Anualmente, se utiliza el código de Web Scrapping para recolectar nuevos egresados y actualizar la información de los egresados ya tomados en cuenta en la base de datos.