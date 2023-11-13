# Bienvenidos a Web Scraping 

Esta sección se enfoca principalmente en la obtención de los perfiles de LinkedIn de los alumnos egresados, así como recuperar la información pertinente de dichos usuarios. 

## Requisitos previos: 

Para el correcto funcionamiento de este módulo se requiere una cuenta de LinkedIn, preferentemente con muchos contactos populares, es decir, que tenga muchas personas conectadas. 

Por el momento se usará la cuenta personal de Pablo Ernesto Baeza Lara, pero se requerirá una nueva al entrar en producción, de uso exclusivo para el proyecto. 

## Limitaciones Técnicas: 

Después de múltiples pruebas se comprobó que BeutifulSoup4 no funciona para Web Scraping en LinkedIn, ya que, al intentar realizar el procedimiento, éste devuelve un código de error http 999 

(equivalente a 4**). El mismo caso se da con el Framework Scrapy. Por lo tanto, debido a esta serie de limitaciones, el presente módulo usará Selenium. 

 

## Descripción de las clases: 

La clase Selenium se omitirá ya que pertenece a una librería, por lo que se desconoce su estructura interna. 

 

## Consideraciones generales: 

El proyecto se encuentra elaborado utilizando la arquitectura denominada Modelo, Vista, Controlador. Comúnmente conocido como MVC, por lo que las carpetas correspondientes se encuentran en el proyecto. 

Debido a la estructura interna del Framework Selenium es indispensable el uso de un programa conocido como Driver, el cual es el que manipula el buscador web, el cual en este caso se ha optado por Microsoft Edge debido a su ligereza y velocidad. El driver se encuentra llamado como “msedgedriver.exe”, análogamente fue descomprimido del archivo denominado como “edgedriver_win64.zip” 

El repositorio cuenta con un archivo. gitignore que “veta” al archivo “.env”. 

El archivo “.env” es el encargado de guardar los datos sensibles que utiliza el web scraping, tales como el usuario y contraseña. 

“__pycahe__” únicamente almacena datos de cache, por lo que no hay nada de interés dentro de esta carpeta. 

La única funcionalidad del archivo main.py es la de iniciar la interfaz gráfica. 

## Carpeta “Controller”: 

La carpeta “Controller” contiene 2 archivos denominados “AccionesBoton.py” asi como “Configuracion.py”. 

 

El archivo “AccionesBoton.py” contiene únicamente la clase “AccionesBoton” la cual contiene los siguientes métodos. 

metodoCadena: Es la acción que se ejecuta al presionar el botón de “Por cadena”, la cual a grandes rasgos realiza las siguientes acciones. 

Inicia el web driver  

Llama a la clase Configuración e inicia sesión en el Login respectivo de LinkedIn. 

Llama a la clase ScrapperPerfiles y convierte la cadena de entrada en una URL valida. 

Dada esa respectiva url itera sobre todas las paginas de resultado y obtiene todos los links de los respectivos perfiles. 

Los links obtenidos los devuelve a la respectiva base de datos. 

Cierra el driver. 

 

metodoUrl: Es la acción que se ejecuta al presionar el botón de “Por URL”, la cual a grandes rasgos realiza las siguientes acciones. 

Inicia el web driver  

Llama a la clase Configuración e inicia sesión en el Login respectivo de LinkedIn. 

Recibe de entrada una URL valida, sobre esa respectiva URL itera sobre todas las páginas de resultado y obtiene todos los links de los respectivos perfiles. 

Los links obtenidos los devuelve a la respectiva base de datos. 

Cierra el driver. 

 

actualizarPivotes: Es la acción que se ejecuta al presionar el botón de “Actualizar pivotes” la cual a grandes rasgos realiza las siguientes acciones. 

Inicia el web driver  

Llama a la clase Configuración e inicia sesión en el Login respectivo de LinkedIn. 

Se accede directamente al URL donde se pueden visualizar a los usuarios conectados “amigos”. 

De toda esa pagina de resultado se obtienen todos los links y se procede a enviarla a la base de datos. 

 

 

metodoPivotes: Es la acción que se ejecuta al presionar el botón de “Por pivote”, la cual a grandes rasgos realiza las siguientes acciones. 

Inicia el web driver  

Llama a la clase Configuración e inicia sesión en el Login respectivo de LinkedIn. 

Recupera de la base de datos una a uno los URLs de nuestros pivotes 

Se accede al respectivo apartado de conectados de nuestros pivotes (básicamente los amigos de nuestros amigos) 

Devuelve los links encontrados a la base de datos, e itera sobre el siguiente link de pivotes en la base de datos 

 

extraccionDeExperiencia: Es la acción que se ejecuta al presionar el botón de “Extraer experiencia”, la cual a grandes rasgos realiza las siguientes acciones. 

Inicia el web driver  

Llama a la clase Utilidades y fuerza el web driver para terminar en la página deseada. 

Se obtienen los campos de empresa, puesto y duración de cada apartado de experiencia del perfil (Forma simple) 

Transforma las estructuras compuestas para convertirlas en simples, luego procede a repetir el paso anterior. 

Obtiene únicamente las descripciones que se encuentren del perfil. 

Todos los datos se envían a la base de datos correspondiente, y se itera con el siguiente perfil de la base de datos. 

testConexiones: Prueba que la conexión sea optima para realizar los procesos correspondientes. 

 

filtrarLIS: Toma los links de la base de datos y verifica si son Licenciados en ingeniería de software, pertenecen a la Universidad autónoma de yucatan y son considerados egresados, si cumplen todas las anteriores condiciones los envía a la base de datos correspondiente 

 

filtrarLCC: Toma los links de la base de datos y verifica si son Licenciados en Ciencia de la computación, pertenecen a la Universidad autónoma de Yucatán y son considerados egresados, si cumplen todas las anteriores condiciones los envía a la base de datos correspondiente 

 

El archivo “Configuracion.py” contiene únicamente la clase “Configuración” la cual contiene los siguientes métodos. 

- iniciarSesion: Realiza el inicio de sesión correspondiente para la plataforma de LinkedIn. 

- cerrarSesion: Procede a borrar las cookies del navegador, lo que funciona como cierre de sesión. 

- sitioWebDisponible: verifica si el sitio web se encuentra actualmente en línea. 

 

comprobarSubida: Comprueba la velocidad de subida del internet al cual esta conectado el presente programa. 

comprobarBajada: Comprueba la velocidad de bajada del internet al cual esta conectado el presente programa 

comprobarPing: Comprueba el ping de ciertas páginas web. 

testConexiones: Agrupa todos los métodos anteriormente mencionados, para garantizar que la conexiona a internet sea estable. 

lenguajeNavegadorEsEspañol: verifica que el navegador web se encuentre en español. 

lenguajeSOEsEspañol: Verifica que el sistema operativo se encuentre en español. 

 

## Carpeta “View”: 

La carpeta view únicamente contiene el archivo “InterfazUsuario.py”, el cual contiene la clase denominada como InterfazUsuario, el cual contiene únicamente un método, el cual es denominado mostrar, el cual tiene la única finalidad de mostrar la inetrza visual y todos los elementos que la componen como los botones etiquetas, etcétera. Cada botón tiene una acción asociada, la cuales fueron mencionadas al principio de la presente documentación. 

## Carpeta “Modelo”: 

La carpeta Modelo contiene los archivos denominados ScraperDatos.py, ScrapperPerfiles.py, e igualmente el archivo Utilidades.py. 

El archivo Utilidades.py contiene únicamente la clase “Utilidades” la cual contiene los siguientes métodos. 

Test: Imprime un arreglo dado, se eliminará para la entrega final. 

estadandarizarCadenas: convierte una cadena estándar en una cadena sin acentos y toda en mayúsculas. 

duplicadosArreglo: Dado un arreglo elimina los elementos duplicados. 

forzarIngresoAPaginaSinSesionIniciada: dada una Url de LinkedIn fuerza al web driver a acceder a dicha página. (LinkedIn por lo general pide un inicio de sesión, esta función anula esta restricción) 

ingresoAPaginaConSesionIniciada: Inicia la sesión en LinkedIn de manera segura. 

transformarNumeroEnMes: convierte un mes (forma numérica), en formato de letras (ENE. , FEB.) por ejemplo. 

separarDuracion: Se encarga que dada una fecha obtenida del web scraping, separa el inicio, final y duración (en meses) 

transformarDuracionEnMeses: Parte de la cadena de separarDuracion la utiliza para obtener la duración en meses, la cual se devuelve posteriormente. 

 

 

El archivo ScraperDatos.py contiene únicamente la clase “ScraperDatos” la cual contiene los siguientes métodos. 

CampoSimple: Dadas las siguientes estructuras presentes en los perfiles de linkedin.  

Obtener el apartado relacionado a Empresa, Puesto y fecha.   

CampoCompuesto: Dadas las siguientes estructuras presentes en los perfiles de linkedin. 

 

Convertirlos a la manera de campo simple y obtener los datos relacionados a Empresa, Puesto y fecha.   

unicamenteDescripciones: Obtiene las descripciones de trabajo del perfil presente independientemente de si es campo simple o compuesto. 

verificarExperiencia: Verifica si el perfil cuenta con el apartado de experiencia. 

verificarUniversidad_Carrera_Egresado: Verifica si el perfil estudio en cierta universidad y carrera, asimismo verifica si ya egreso teniendo en cuenta la fecha actual. 

 

El archivo ScraperPeriles.py contiene únicamente la clase “ScrapperPerfiles” la cual contiene 3 clases anidadas denominadas como   

BusquedaDeURLs 

IteradorDeURLs 

ScrappearLinks 

La clase anidada BusquedaDeURLs contiene los siguientes métodos: 

BusquedaDeURLs: dada una cadena de entrada tal como “lis uady”, lo transforma en una URL valida la cual puede entender LinkedIn. 

porPivote: Dado el URL de un pivote, lo modifica de tal manera que permite mostrar los contactos del pivote (Se hará más flexible en próximas entregas) 

 

La clase anidada IteradorDeURLs contiene los siguientes métodos: 

iniciarIteracion: Dada una URL itera entre todos sus resultados, análogamente obtiene todas los URL de usuarios de la presente página. 

es_ultima_pagina: Verifica si se ha alcanzado la ultima página de resultados valida. 

 

 

La clase anidada ScrappearLinkscontiene los siguientes métodos: 

obtener_links: Obtiene todos los links de la presente página. 

 