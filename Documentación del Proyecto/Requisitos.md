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
* El sistema debe realizar la búsqueda de perfiles de los egresados de las Licenciaturas en Ingeniería de Software y Ciencias de la Computación.
* El sistema debe dar de alta en la base de datos la información recolectada de los egresados (URL de la página del perfil de LinkedIn, Nombre del perfil, Nombre de la empresa, Carrera, Universidad, Descripción del Rol y Duración).

### **_RF-002 Base De Datos (Prioridad S)_**
---
* El sistema debe almacenar la información de los egresados (URL de la página del perfil de LinkedIn, Nombre del perfil, Nombre de la empresa, Carrera, Universidad, Descripción del Rol y Duración).

### **_RF-003 Modelo Procesamiento Del Lenguaje Natural (Prioridad B)_**
---
* El sistema debe clasificar la descripción del trabajo que realiza la persona de acuerdo a los diversos roles definidos para el proyecto.

### **_RF-004 Análisis De Datos (Prioridad A)_**
---
* El sistema debe aplicar los filtros, las operaciones aritméticas y procesos estadísticos necesarios para responder a las preguntas:

    1. ¿Qué empresas contratan egresados de la Facultad de Matemáticas de la carrera de LIS?
    2. ¿Qué puestos han ocupado dichos egresados de LIS en sus respectivos trabajos?
    3. ¿Cuál es la duración promedio, de los egresados de LIS, en el que duran en un trabajo?

### **_RF-005 Interfaz Gráfica (Prioridad C)_**
---
* La interfaz debe presentar las gráficas obtenidas de los resultados del análisis de datos que responden las preguntas anteriormente mencionadas.
* El usuario no presenta problemas en cuanto al funcionamiento de la interfaz gráfica.
* La interfaz debe estar adaptable a tres tamaños de pantalla (celular, tableta y computadora).

## **Requisitos No Funcionales**
## *_Requerimientos De Producto_*
### *_RNF-001 (Prioridad S)_*
La base de datos cuenta con todas los requisitos de seguirdad para mantener seguros los datos recabados (encriptación, llaves primarias, llaves secundarias, etc.).

### *_RNF-002 (Prioridad C)_*
El sistema es de fácil uso e intuitivo para el usuario.

## *_Requerimientos Organizacionales_*
### *_RNF-003 (Prioridad A)_*
La recolección de datos de los perfiles de LinkedIn se realiza semestralmente para añadir nuevos registros en la base de datos y actualizar los ya registrados.
