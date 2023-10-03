# Bienvenidos a Web Scraping
Esta sección se enfoca principalmente en la obtención de los perfiles de LinkedIn de los alumnos egresados, así como recuperar la información pertinente de dichos usuarios.

## Requisitos previos:
Para el correcto funcionamiento de este módulo se requiere una cuenta de LinkedIn, preferentemente con muchos contactos populares, es decir, que tenga muchas personas conectadas.
Por el momento se usará la cuenta personal de Pablo Ernesto Baeza Lara, pero se requerirá una nueva al entrar en producción, de uso exclusivo para el proyecto.

## Limitaciones Técnicas:
Después de múltiples pruebas se comprobó que BeutifulSoup4 no funciona para Web Scarping en LinkedIn, ya que al intentar realizar el procedimiento, éste devuelve un codigo de error http 999
(equivalente a 4**). El mismo caso se da con el framework Scrapy. Por lo tanto debido a esta serie de limitaciones, el presente módulo usará Selenium.

## Diseño del modulo:


### **_Tabla A_**
![Imagen Tabla A](Images/TablaA.jpg)
### **_Tabla B_**
![Imagen Tabla B](Images/TablaB.jpg)

---

## Descripción de las clases
#### **_La clase Selenium se omitirá ya que pertenece a una librería, por lo que se desconoce su estructura interna_**

### BusquedaEgresados
La clase `BusquedaEgresados` se encarga de buscar a los egresados que cumplan con ciertas características utilizando uno de los 3 métodos de la clase `Automata`. Puede considerarse como el punto de entrada o "main" del módulo de Web Scraping.

#### **_¿Qué es un egresado?_**
Para este proyecto, consideramos un perfil/persona **_egresado_** como aquella que cumpla con todas las siguientes características:
- Estudió en la Universidad Autonoma de Yucatán.
- Estudió en la Facultad de Matemáticas.
- Finalizó sus estudios en la Licenciatura en Ingenieria de Software.
- Ha tenido al menos trabajo y está presente en el apartado de experiencia de LinkedIn.

### Métodos de la Clase BusquedaEgresados

- `insertarEnBarraBusqueda`: Este método es llamado a través del Front-end y permite la búsqueda de los enlaces de los egresados mediante búsquedas predefinidas en la barra de búsqueda.
- `buscarUADY`: Este método es llamado a través del Front-end y permite la búsqueda de los enlaces de los egresados buscando a todas aquellas personas que pertenezcan a la UADY.
- `AccederContactosDePivote`: Este método es llamado a través del Front-end y permite la búsqueda de los enlaces de los egresados por medio de ciertos contactos populares con los que se ha conectado previamente.

## Clase Iterador

La clase `Iterador` se encarga de moverse dentro de LinkedIn y contiene 2 métodos:

- `entre_elementos_de_respuesta`: Itera entre los resultados que devuelve una búsqueda arbitraria de LinkedIn.
- `entre_paginas_de_respuesta`: Manipula la URL de la página actual para así poder iterar y moverse entre páginas.

## Clase Verificador

La clase `Verificador` contiene 3 métodos que validan que el perfil cumpla con las características de un egresado:

- `esUADY`: Valida que el perfil corresponda a un egresado de la UADY.
- `esLIS`: Valida que el perfil sea de un egresado UADY de la carrera de la Licenciatura en Ingeniería de Software.
- `tieneExperiencia`: Valida que el perfil tenga información en el apartado de Experiencia de LinkedIn (al menos una experiencia laboral).

## Clase Configuracion

La clase `Configuracion` contiene 4 métodos que permiten configurar la página de LinkedIn según las necesidades:

- `paginaEnEspanol`: Configura el navegador para que la página esté en español.
- `buscarContrasenasAlmacenadas`: Toma la contraseña almacenada de las variables de entorno.
- `iniciarSesion`: Inicia sesión en LinkedIn.
- `cerrarSesion`: Cierra la sesión de LinkedIn.

## Clase Automata

La clase `Automata` contiene 3 métodos:

- `Ingresar_cadena_en_barra_de_busqueda`: Inserta en el buscador de LinkedIn ciertas cadenas predefinidas como "fmat software", "lis yucatan", entre otras.
- `Ajustar_busqueda_mostrar_todo_UADY`: Mediante la manipulación de los filtros de LinkedIn, muestra a todas aquellas personas que estudian en la UADY (Estudios Superiores).
- `Acceder_contactos_pivote_popular`: Por medio de automatización, se accede a los contactos del perfil pivote.

## Clase Test

La clase `Test` contiene 4 métodos para manejar errores que puedan ocurrir durante el Web Scraping:

- `hayInternet`: Valida que el dispositivo esté conectado a Internet.
- `conexionEstable`: Valida que exista una conexión estable.
- `edgeCaido`: Valida que el navegador Microsoft Edge no esté caído.
- `linkedInnCaido`: Valida que la aplicación web de LinkedIn no esté caída.

## Clase Scraper

La clase `Scraper` contiene 1 método y un atributo para obtener los datos necesarios:

- `Obtener_nombre_y_URL`: Obtiene los datos antes mencionados para posteriormente guardarlos en la tabla A.
- `linkPagina`: Es una variable privada de tipo cadena que guarda los respectivos enlaces de LinkedIn.

## Clase SQL_Links

La clase `SQL_Links` contiene 2 métodos:

- `subirLinks`: Se encarga de la "subida" de datos a su respectiva tabla en la base de datos.
- `subirLinks`: Se encarga de la "subida" de datos a su respectiva tabla en la base de datos.

## Clase EgresadosScrapingSQL

La clase `EgresadosScrapingSQL` contiene 7 atributos que corresponden a los campos de la base de datos:

- `link`: Variable privada de tipo cadena que contiene el enlace del respectivo egresado.
- `nombre`: Variable privada de tipo cadena que contiene el nombre del respectivo egresado.
- `empresa`: Variable privada de tipo cadena que contiene la empresa donde labora el respectivo egresado.
- `universidad`: Variable privada de tipo cadena que contiene la universidad donde egresó el respectivo egresado.
- `carrera`: Variable privada de tipo cadena que contiene la carrera del respectivo egresado.
- `descripción`: Variable de tipo cadena que contiene la descripción del puesto del respectivo egresado.
- `duración`: Variable privada de tipo cadena que contiene la duración de los empleos del respectivo egresado.

## Clase SQL_Scraper

La clase `SQL_Scraper` contiene 6 métodos:

- `Limpiar_duplicado (Tabla A)`: Limpia los elementos duplicados presentes en la tabla A.
- `Limpiar_Miembro_de_LinkedIn(Tabla A)`: Limpia los elementos Miembro de LinkedIn (Perfiles anónimos) presentes en la tabla A.
- `Set_datos (Tabla A)`: Mediante procedimientos SQL, envía los datos correspondientes a la Tabla A.
- `Get_datos (Tabla A)`: Mediante procedimientos SQL, obtiene los datos correspondientes a la Tabla A.
- `Set_datos (Tabla B)`: Mediante procedimientos SQL, envía los datos correspondientes a la Tabla B.
- `Agregar_Pivote`: Agrega un elemento con la estructura de la Tabla A (nombre, URL), a una tabla especial denominada Pivotes.
- `Eliminar_Pivote`: Elimina un elemento con la estructura de la Tabla A (nombre, URL), a una tabla especial Pivotes.

#### **_¿Qué es un pivote?_**
Un usuario pivote es un perfil de LinkedIn el cual posee muchos "conectados" que pertenecen al grupo poblacional que estamos buscando. Al ser sus "amigos" en LinkedIn podemos acceder a todos sus "conectados", lo que facilita el proceso de búsqueda de los egresados. 

## Consideraciones generales
- El módulo está diseñado para funcionar con o sin la suscripción Premium, sin embargo tal vez la segunda opción ofrezca mejores resultados.
- Al momento de entregar el producto, la Tabla A ya se encontrará previamente cargada con datos de los egresados, para así poder buscar su "nueva experiencia" la n cantidad de veces necesaria.
- La tabla A se puede actualizar mediante el botón cuando se considere pertinente. (Ver imágenes anexo)
