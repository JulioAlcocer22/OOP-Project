# Bienvenidos a Web Scraping
Esta seccion se enfoca principalmente en la obtencion de los perfiles de linkedin de los alumnos egresados, asi como recuperar la informacion pertinente de dichos usuarios.

## Requisitos previos:
Para el correcto funcionamiento de este modulo se requiere una cuenta de linkedin, preferentemente con muchos contactos populares ( osea con muchas personas conectadas ). 
Por el momento se usara la cuenta personal de Pablo Ernesto Baeza Lara, pero se requerira una nueva al entrar en produccion.

## Limitaciones Tecnicas:
Despues de multiples pruebas se comprobo que BeutifulSoup4 no funciona para web scarping en LinkedIn ya que al intentar realizar el procedimiento devuelve un codigo de error http 999 
( equivalente a 4** ). El mismo caso se da con el framework Scrapy. Por lo tanto debido a esta serie de limitaciones, el presente modulo usara Selenium.

## Diseño del modulo:

### Diagramas de clase del modulo ( Aprobacion pendiente )
![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/5a55e38e-ef17-4ac6-aca5-ac8fe89135f9)
![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/99977586-25fb-486d-9f6b-fed54497df46)
![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/c926d6f2-bc27-41bd-a39f-452cd1385382)
![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/412cba1a-52c3-436f-bfba-3974e8042e2e)

---

## Descripcion de las clases:
#### Se omitira la descripcion de las clases Verificador, Test, Configuarcion ya que son autodescriptivas en cuanto a sus metodos.
#### La clase selenium se omitira ya que pertenece a una libreria, por lo que se desconoce su estructura interna.

### Scraper
Contiene 2 metodos:
- Obtener_nombre_y_URL: Obtiene los datos antes mencionadas para posteriormente guardarlos en la tabla A ( Ver ultima imagen "Diagramas de clase del modulo" )
- Experiencia_egresado: Obtiene los datos pertinentes del egresado para posteriormente guardarlos en la tabla B ( Ver ultima imagen "Diagramas de clase del modulo" )

### Iterador
Contiene 2 metodos:
- entre_elementos_de_respuesta: Itera entre los resultados que devuelve una busqueda albitraria de LinkedIn
- entre_paginas de respuesta: Manipula la URL de la actaul pagina para asi poderer interar para moverse entre paginas.

### SQL_Scraper
Contiene 6 metodos:
- Limpiar_duplicado ( Tabla A ): Limpia los elementos duplicados presentes en la tabla A
- Limpiar_Miembro_de_LinkedIn( Tabla A ): Limpia los elementos Miembro de LinkedIn ( Perfiles anonimos ) presentes en la tabla A
- Set_datos ( Tabla A ): Mediante procedimientos SQL envia los datos correspondientes a la Tabla A 
- Get_datos ( Tabla A ): Mediante procedimientos SQL obtiene los datos correspondientes a la Tabla A 
- Set_datos ( Tabla B ): Mediante procedimientos SQL envia los datos correspondientes a la Tabla B
- Agregar_Pivote: Agrega un elemento con la estructura de la Tabla A ( nombre, url ), a una tabla especial denominada Pivotes.
- Eliminar_Pivote: Elimina un elemento con la estructura de la Tabla A ( nombre, url ), a una tabla especial Pivotes.

#### ¿Que es un pivote?
Un usuario pivote es un perfil de LinkedIn el cual poseen muchos "conectados" que pertenecen al grupo poblacional que estamos buscando. Al ser sus "amigos" en LinkedIn podemos acceder a todos sus "conectados", lo que facilita el proceso de busqueda de los egresados. 

### Automata
Contiene 3 metodos:
- Ingresar_cadena_en_barra_de_busqueda: Inserta en el buscador de LinkedIn ciertas cadenas predefinidas como "fmat software", "lis yucatan", entre otras.
- Ajustar_busqueda_mostrar_todo_UADY: Mediante la manipulacion de los filtros de LinkedIn, mostrara a todas aquellas personas que estudien en la UADY ( Estudios Superiores ).
- Acceder_contactos_pivote_popular: Por medio de automatizacion se accederan a los contactos del perfil pivote

### Busqueda_egresados
Por medio del tipo de busqueda designado ( Alguno de los 3 metodos de automata ), buscara a los egresados que cumplan las caracteristicas pertinentes.

#### ¿Que es un egresado?
Es aquella persona fisica quien cumple con los siguientes caracteristicas:
- Estudio en la Universidad Autonoma de Yucatan
- Estudio en la Facultad de Matematicas
- Finalizo sus estudios en la Lic. en Ingenieria de Software
- Ha tenido un trabajo o mas, presente en el apartado de experiencia de LinkedIn.
