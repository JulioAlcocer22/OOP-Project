# Bienvenidos a Analis de Datos
Esta sección se enfoca principalmente en el análisis de los datos recabados en los procesos anteriores para poder responder a las preguntas de interés del proyecto. Para esto se usaran Stored Procedures dentro de la base de datos para poder realizar las consultas necesarias y así poder obtener los resultados esperados desde el backend de la pagina web.

## Requisitos previos:
Para el correcto funcionamiento de este módulo se requiere un servidor SQL server, por el momento se está usando la infraestructura de Azure.

## Limitaciones Técnicas:
Se está usando la versión 2019 de SQL Server, con créditos de prueba en Azure por lo que se encuentra limitado economicamente el almacenamiento y el poder de procesamiento.

---

## Descripción de los Stored Procedures

### AnalisisEmpresas
Esta SP recibe como parametros la universidad y la carrera que se desea analizar, se encarga de obtener la información de las empresas que se encuentran en la tabla EgresadosScraping, para esto se filtra la tabla segun los parametros de universidad y carrera, posteriormente se cuenta el numero de veces que aparece cada empresa en la tabla y se divide entre el numero de egresados unicos que existen, luego se ordena de mayor a menor, para así obtener las empresas más populares entre los egresados de la carrera y universidad deseada.

### AnalsisRoles
Esta SP recibe como parametros la universidad y la carrera que se desea analizar, se encarga de obtener la información de los roles que se encuentran en la tabla Egresados, para esto se filtra la tabla segun los parametros de universidad y carrera, posteriormente se cuenta el numero de veces que aparece cada rol en la tabla y se divide entre el numero de egresados unicos que existen, luego se ordena de mayor a menor, para así obtener los roles más populares entre los egresados de la carrera y universidad deseada.

### PromedioDuracion
Esta SP recibe como parametros la universidad y la carrera que se desea analizar, se encarga de obtener la información de la duracion de los egresados en sus empleos que se encuentran en la tabla EgresadosScraping, para esto se filtra la tabla segun los parametros de universidad y carrera, posteriormente aplica la funcion AVG() propia de SQL server para poder obtener el promedio de la duracion de los empleos de los egresados de la carrera y universidad deseada.