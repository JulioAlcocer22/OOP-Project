
Esta seccion, es la unificacion de Web Scrapping, Analisis del Lenguaje Natural, asi como la logica de la base de Datos.

A continuacion se explicara de forma breve, completa y consisa el como esta estructurado el modulo, asi como sus funcionalidades.

Cabe destacar que esta seccion unicamente "extrae" informacion, mas no la visualiza al publico en general, dicho ya es trabajo de la GUI.

# Organizacion basica.
Todo la seccion se encuentra alojada en la carpeta LinkedInScrapper que analogamente cuenta con multiples elementos, lo cuales seran descritos a 
continuacion:

- **app**: La carpeta mas importante de todas, es aquel que contiene las carpetas correspondientes al MVC, debido a su gran estructura sera abordada con detalle mas adelante.
- **gitignore**: Es el archivo que impide que los archivos de tipo .env puedan ser subidos al repositorio local.
- **edgedriver_win64.zip**: Es el zip del driver, el cual permite realizar todas las acciones pertinentes, la razon por la cual fue incluido en el repositorio local es en caso de que el driver se corrompa, exista una version virgen del zip.
- **msedgedriver.exe** : Es el driver, osea la el programa que permite que el eb Scrapping se ejecute de manera exitosa, es indispensable que siempre se encuentre en el directorio actual.
- **estructura_env.txt**: Debido a que no es posible subir archivos .env al repositorio, se agrego este archivo para mostrar la estructura necesaria para que el programa pueda ser ejecutado, esto da libertad para que pueda ser cambiada la base de datos asi como el perfil de LinkedIn a utilizar.
- **requirements.txt**: Con el fin de tener un correcto manejo de referencias se creo el archivo para poder instalar todas las referencias al mismo tiempo, el comando necesario es: pip install -r requierements.txt
-  **run.py**: Es el encargado de arrancar todas las partes necesarias para la ejecucion del proyecto, es el archivo maestro que se compila.

# Organizacion de la carpeta app.
La carpeta app cuenta con 4 carpetas, las que corresponden a la estructura MVC. Las cuales son Controller, Database, Model y View. A continuacion se describiran las carpetas asi como los archivos y clases que la componen.

## Controller
Sin duda una de las carpetas mas importantes ya que contiene toda lo logica del programa.Esta carpeta cuenta con 3 archivos, los cuales son:

- AccionesBoton.py
- Configuracion.py
- MainPrueba.py

Ahora empezaremos describiendo los metodos y clases asociadas a cada archivo.

### AccionesBoton
Este archivo tiene como responsabilidad que, sea presionado un boton de la View realice una accion determinada. Seran explicados ahora los metodos que componen la clase.

#### metodoCadena
La funcion de este metodo es iniciar sesion en LinkedIn, ingresar una cadena albitraria a la barra de busqueda, obtenener todos los links asociados a la busqueda de la pagina actual, e iterar hasta llegar a la ultima pagina. Cuando ya se hayan agotado los resultados, se precede a enviar el arreglo resultante a la base de datos. Hasta el momento todos los perfiles que se envian no necesariamente son egresados, simplemente son perfiles que por alguna razon cubrieron cierto criterio de busqueda.

#### metodoUrl
La funcion de este metodo es iniciar sesion en LinkedIn, ingresar a una URl albitraria antes proporcionada, obtenener todos los links asociados a la busqueda de la pagina actual, e iterar hasta llegar a la ultima pagina. Cuando ya se hayan agotado los resultados, se precede a enviar el arreglo resultante a la base de datos. Hasta el momento todos los perfiles que se envian no necesariamente son egresados, simplemente son perfiles que por alguna razon cubrieron cierto criterio de busqueda.

#### actualizarPivotes
La funcion de este metodo es iniciar sesion en LinkedIn, dirigirse a la seccion de contactos y obtener todos los link de los contactos
asociados, finalmente dicho links se enviaran a la base de datos para ser almacenados para futuras operaciones.

Se le denominan como pivotes debido a que dichos contactos tienen asociado muchos otros contactos, esto nos es util ya que LinkedIn solo permite ver los contactos de un contacto cuando dicho es tu "amigo". Ventaja que aprovecharemos para metodos de busqueda posteriores.

#### metodoPivotes

Este metodo para funcionar de manera adecuada requiere que se cuente con una membresia de LinkedIn premium esto debido a que en las cuentas gratuitas se cuenta con cierto limite de busqueda mensual, sin embargo debido a que un pivote en promedio posee 300 o mas contactos es posible que se termine el limite gratuito mensual, lo que estropearia por completo el proceso.

Lo que realiza este metodo es que itera sobre los pivotes ( previamente alojados en la base de datos ), ya situado en el pivote se operan los parametros para asi mostrar todos los contactos que tiene ese pivote, mostrados todos los contactos se obtienen los links y se itera hasta agotar todos los contactos, el arreglo resultado se envia a la base de datos. Este proceso se repite hasta que se han obtenido todos los contactos de todos los pivotes. Cabe mencionar que este proceso en especial es extremadamente tardado por lo que se suplica usarlo con cautela.

#### metodoPivotesUnico

Como se menciono anteriormente existe un limite mensual para las cuentas gratuitas, debido a que durante la realizacion de este proyecto no se conto con el presupuesto suficiente se decidio a crear este metodo especial.

Este metodo recibe una URL la cual debe ser un pivote, una vez insertada la URl se dirige al apartado de contactos del pivote, mostrados todos los contactos se obtienen los links y se itera hasta agotar todos los contactos, el arreglo resultado se envia a la base de datos.

Basicamente es una version reducida del metodoPivotes.

#### filtrarLIS

Anteriormente habiamos obtenido una gran cantidad de links de perfiles, pero pra cuestiones de este proyecto, nos interesa que los perfiles cumplan ciertas caracteristicas:

- Sea egresado de la carrera de "Licenciatura en Ingenieria de Software" de la Universidad autonoma de Yucatan (Facultad de Matematicas).
- Que cuente con al menos una experiencia laboral previa.

Se tomaran de 6 en 6 los perfiles de la base de datos.


Nota: La razon por la que se toman de 6 en 6 los perfiles es que para este procedimiento no se inicia sesion en LinkedIn por lo que la pagina despues de 6 busquedas de perfil te exige el inicio de sesion, el cual queremos evitar a toda costa debido a que si se inicia la sesion la estructura HTML cambia drasticamente, lo que impide que sea Scrapeada la pagina. De igual manera si se llegara a iniciar multiples veces seguida la sesion, el perfil se bloquearia, lo cual es indeseable.

Se acceden a los perfiles individualmente, se cierra el modal que te invita a iniciar sesion, se verifica los campos de educacion y experiencia, si se verifica que cumple con las condiciones se marca como egresado de LIS e igualmente se marca como visitado, s no es el caso unicamente se marca como visitado. Se iteran los otros 5 links restantes y finalmente se cierra todo el programa.

Nota: La razon por cual se cierra todo el programa es que se descubrio una libreria que permite descargar y ejecutar el driver mas reciente, sin embargo nos dimos cuenta que en cada iteracion ese driver compilado poseia una Ip diferente, lo que nos permitia reiniciar el contador de 6 en 6. La aplicacion se cierra completamente para que cuando se vuelva a compilar se compile de nuevo un nuevo driver y asi se tenga una nueva Ip para escrapear otros nuevos 6 perfiles.

#### filtrarLCC

Es exactamente el mismo procedimiento anteriormente mencionado solo que con las sigyientes condiciones de filtrado:

- Sea egresado de la carrera de "Licenciatura en Ciencias de la Computacion" de la Universidad autonoma de Yucatan (Facultad de Matematicas).
- Que cuente con al menos una experiencia laboral previa.

#### extraccionDeExperienciaLIS





