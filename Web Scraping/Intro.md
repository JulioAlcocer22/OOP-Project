# Bienvenidos a Web Scraping
Esta sección se enfoca principalmente en la obtención de los perfiles de LinkedIn de los alumnos egresados, así como recuperar la información pertinente de dichos usuarios.

## Requisitos previos:
Para el correcto funcionamiento de este módulo se requiere una cuenta de LinkedIn, preferentemente con muchos contactos populares, es decir, que tenga muchas personas conectadas.
Por el momento se usará la cuenta personal de Pablo Ernesto Baeza Lara, pero se requerirá una nueva al entrar en producción, de uso exclusivo para el proyecto.

## Limitaciones Técnicas:
Después de múltiples pruebas se comprobó que BeutifulSoup4 no funciona para Web Scarping en LinkedIn, ya que al intentar realizar el procedimiento, éste devuelve un codigo de error http 999
(equivalente a 4**). El mismo caso se da con el framework Scrapy. Por lo tanto debido a esta serie de limitaciones, el presente módulo usará Selenium.

## Diseño del modulo:

### Diagramas de clase del modulo ( Aprobacion pendiente)
![image](/Web%20Scraping/Diagramas%20de%20Clase/Diagrama%20de%20Clase_Web%20Scrapping.jpg)
![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/412cba1a-52c3-436f-bfba-3974e8042e2e)

---

## Descripción de las clases:
#### Se omitirá la descripción de las clases Verificador, Test y Configuarcion, ya que son autodescriptivas en cuanto a sus métodos.
#### La clase Selenium se omitirá ya que pertenece a una librería, por lo que se desconoce su estructura interna.

### Scraper
Contiene 2 métodos:
- Obtener_nombre_y_URL: Obtiene los datos antes mencionados para posteriormente guardarlos en la tabla A. (Ver última imagen "Diagramas de clase del módulo")
- Experiencia_egresado: Obtiene los datos pertinentes del egresado para posteriormente guardarlos en la tabla B. (Ver última imagen "Diagramas de clase del módulo")

### Iterador
Contiene 2 métodos:
- entre_elementos_de_respuesta: Itera entre los resultados que devuelve una búsqueda arbitraria de LinkedIn.
- entre_paginas de respuesta: Manipula la URL de la actual página para así poder iterar para moverse entre páginas.

### SQL_Scraper
Contiene 6 metodos:
- Limpiar_duplicado (Tabla A): Limpia los elementos duplicados presentes en la tabla A.
- Limpiar_Miembro_de_LinkedIn(Tabla A): Limpia los elementos Miembro de LinkedIn (Perfiles anónimos) presentes en la tabla A
- Set_datos (Tabla A): Mediante procedimientos SQL envía los datos correspondientes a la Tabla A.
- Get_datos (Tabla A): Mediante procedimientos SQL obtiene los datos correspondientes a la Tabla A. 
- Set_datos (Tabla B): Mediante procedimientos SQL envía los datos correspondientes a la Tabla B.
- Agregar_Pivote: Agrega un elemento con la estructura de la Tabla A (nombre, url), a una tabla especial denominada *Pivotes*.
- Eliminar_Pivote: Elimina un elemento con la estructura de la Tabla A (nombre, url), a una tabla especial *Pivotes*.

#### ¿Qué es un pivote?
Un usuario pivote es un perfil de LinkedIn el cual posee muchos "conectados" que pertenecen al grupo poblacional que estamos buscando. Al ser sus "amigos" en LinkedIn podemos acceder a todos sus "conectados", lo que facilita el proceso de búsqueda de los egresados. 

### Automata
Contiene 3 métodos:
- Ingresar_cadena_en_barra_de_busqueda: Inserta en el buscador de LinkedIn ciertas cadenas predefinidas como "fmat software", "lis yucatan", entre otras.
- Ajustar_busqueda_mostrar_todo_UADY: Mediante la manipulación de los filtros de LinkedIn, mostrará a todas aquellas personas que estudien en la UADY (Estudios Superiores).
- Acceder_contactos_pivote_popular: Por medio de automatización se accederán a los contactos del perfil pivote.

### Busqueda_egresados
Por medio del tipo de búsqueda designado (alguno de los 3 métodos de la clase Automata), buscará a los egresados que cumplan las caracteristicas pertinentes.

#### ¿Qué es un egresado?
Para este proyecto, consideramos un perfil/persona **_egresado_** como aquella que cumpla con todas las siguientes características:
- Estudió en la Universidad Autonoma de Yucatán.
- Estudió en la Facultad de Matemáticas.
- Finalizó sus estudios en la Licenciatura en Ingenieria de Software.
- Ha tenido al menos trabajo y está presente en el apartado de experiencia de LinkedIn.

#### Consideraciones generales
- El mdulo esta diseñado para funcionar con o sin la suscripcion Premium, sin embargo tal vez la segunda opcion ofrezca mejores resultados.
- Al momento de entregar el producto, la Tabla A ya se encontrará previamente cargado con datos de los egresados, para así poder buscar su "nueva experiencia" la n cantidad de veces necesaria.
- La tabla A se puede actualizar mediante el botón cuando se considere pertinente. (Ver imágenes anexo)
