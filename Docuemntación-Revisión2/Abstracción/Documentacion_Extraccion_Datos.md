# Documentacion del modulo Extraccion de datos

Esta seccion, es la unificacion de Web Scrapping, Analisis del Lenguaje Natural, asi como la logica de la base de Datos.

A continuacion se explicara de forma breve, completa y consisa el como esta estructurado el modulo, asi como sus funcionalidades.

Cabe destacar que esta seccion unicamente "extrae" informacion, mas no la visualiza al publico en general, dicho ya es trabajo de la GUI.

## Organizacion basica.
Todo la seccion se encuentra alojada en la carpeta LinkedInScrapper que analogamente cuenta con multiples elementos, lo cuales seran descritos a 
continuacion:

- **app**: La carpeta mas importante de todas, es aquel que contiene las carpetas correspondientes al MVC, debido a su gran estructura sera abordada con detalle mas adelante.
- **gitignore**: Es el archivo que impide que los archivos de tipo .env puedan ser subidos al repositorio local.
- **edgedriver_win64.zip**: Es el zip del driver, el cual permite realizar todas las acciones pertinentes, la razon por la cual fue incluido en el repositorio local es en caso de que el driver se corrompa, exista una version virgen del zip.
- **msedgedriver.exe** : Es el driver, osea la el programa que permite que el eb Scrapping se ejecute de manera exitosa, es indispensable que siempre se encuentre en el directorio actual.
- **estructura_env.txt**: Debido a que no es posible subir archivos .env al repositorio, se agrego este archivo para mostrar la estructura necesaria para que el programa pueda ser ejecutado, esto da libertad para que pueda ser cambiada la base de datos asi como el perfil de LinkedIn a utilizar.
- **requirements.txt**: Con el fin de tener un correcto manejo de referencias se creo el archivo para poder instalar todas las referencias al mismo tiempo, el comando necesario es: pip install -r requierements.txt
-  **run.py**: Es el encargado de arrancar todas las partes necesarias para la ejecucion del proyecto, es el archivo maestro que se compila.
