# ADVERTENCIA: **REDISEÑO URGENTE DEL MODULO**
### Despues de muchas pruebas se comprobo que bs4 no funciona para web scarping en linkedin ya que devuelve un codigo de error 999 ( equivalente a 4** ). El mismo caso es posible para scrapy. Por lo tanto se tendra que rediseñar el modulo para selenium ( EN PROCESO ).

## Documentar las version usadas del explorador, del web driver y de python.



# Bienvenidos a Web Scraping
Esta seccion se enfoca principalmente en la obtencion de los perfiles de linkedin de los alumnos egresados, asi como recuperar la finformacion pertinente de dichos usuarios.

## Requisitos previos:
Para el correcto funcionamiento de este modulo se requiere una cuenta de linkedin, preferentemente con muchos contactos populares ( osea con muchas personas conectadas ). 
Por el momento se usara la cuenta personal de Pablo Ernesto Baeza Lara, pero se requerira una nueva al entrar en produccion.

## Diseño del modulo:
A continuacion se definira formalmente los componentes que componen al modulo, no es un diagrama UML formalmente, pero servira para conocer la estructura interna de esta seccion.

![Diagrama](/Diagrama.jpeg)

---

### Scrapper
Es la superclase que engloba a Exploratorio y Formal, de tal manera que su llamada se define como Scrapper.Exploratorio y Scrapper.Formal.

### Exploratorio
Es la clase con la unica y exclusiva finalidad de encontrar en linkedin a los egresados correspondientes, dicha clase devuelve como salida general en una tabla SQL un registro
el cual contiene 2 campos, el primero consiste en el nombre de perfil de linkedin y el segundo corresponde al link asociado a dicho perfil.

### Busqueda
Es el metodo directo de la clase exploratorio, dicha define los criterios de busqueda. ( Dicho modulo esta pensado en caso que se decida buscar a los alumnos egresados de x universidad, x facultad o de x carrera)
Recurre a metodos de la clase criterios ( IsUADY?, IsFMAT?, IsLIS?, IsEgresado? )

### Lineal
Dicho metodo consiste en un algoritmo que utiliza automatizacion computacional para asi "insertar" en la barra de busqueda de linkedin" cadenas como "software uady", "fmat lis", entre muchas otras cadenas que permitan obtener resultados de los alumnos. una vez que linkedin devuelva los usuarios correspondientes a la busqueda "iterara" entre cada usuario para ver si concuerda con los criterios previamente establecidos, si concuerda con la descripcion se insertara en la base de datos, sino se descartara. Dicho proceso se repetira hasta agotar todas las opciones posibles.

### Por referencia:
Este es el metodo mas complejo pero "potente" de busqueda, consiste en que dado una lista selecta de perfiles populares de linkedin ( Dr. Edgar Cambranes, Mtr. Luis Basto, etc )
iterar entre todos sun contactos conocidos, ajustando los filtros para asi alcanzar el mayor numero de personas posibles. Dicho no garantiza encontrar todos los egresados, pero si ofrece una busqueda mas fina que el tipo de busqueda lineal

### Consideraciones generales:
- En tiempo de ejecucion se puede seleccionar cual metodo de busqueda deseea realizar, inclusive seleccionar ambos ( Lo cual seria lo idoneo ).
- Aunque existe la suscripcion premium por el momento no se usara ya que aun nos encontramos en fase exploratoria.
- El modulo esta diseñado para funcionar con o sin la suscripcion premium, sin embargo tal vez la segunda opcion ofrezca mejores resultados.

---

### Formal
Dicho segmento es el que obtiene los datos de interes de cada egresado ( Empresa, Puesto , Descripcion, Duracion ).
Requiere previamente el paso de exploratorio para funcionar correctamente. 

### Busqueda experiencia:
Es el scarping en bruto, con la base de datos previamente obtenida, el scrapter tomara cada uno de los links y buscara la seccion de experiencia, una vez ahi, obtendra todos los datos previamente mencionados y los enviara a la base de datos. ( Devolvera los n trabajos que ha tenido el egresado.

### Consideraciones importantes:
- Cabe aclarar que la devolucion de datos a una base SQL es una clase por separado, con la finalidad de mantener el principio de responsabilidad unico.
- Ademas de las clases SQL previamente mencionadasse contara con una clase adicional que sera la encargada de eliminar los registros duplicados.



