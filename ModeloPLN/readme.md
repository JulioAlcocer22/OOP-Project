# Apartado de Procesamiento de Lenguaje Natural
Una de las problemáticas a la hora de recabar la información es que, en muchas de las ocasiones, en el aparado de experiencia únicamente ponen la empresa y la descripción del trabajo que realizan, o en su defecto, si ponen un "rol", pero la descricpión de dicho rol corresponde a otro. Es por estas razones que se optó por realizar un modelo para clasificar los roles de trabajo dependiendo de la descripción que estos tengan.

## Descripción

Se optó por utilizar un modelo pre entrenado del modelo BERT (Bidirectional Encoder Representations from Transformers) que la comunidad de Hugging Face ya ha elaborado anteriormente y puesto en su plataforma para que otros miembros de la comunidad puedan utilizarlos. 

## Etapas en el proceso de reentrenamiento de un modelo basado en BERT
1. **Preparación de datos**
    - En esta parte se recolecta, limpia y preprocesan los datos (descripciones de trabajo) para que estén en el formato adecuado para su uso posterior.
2. **Reentrnamiento del modelo**
    - Se cargará un modelo, en este caso desde Hugging Face, y se ajustará para que sea afín al objetivo del trabajo.
    - Se definen los parámetros para el entrenamiento, al igual que el entrenamiento en si mismo.
3. **Validacion y optimización**
    - Una vez entrenado, hay que verificar que cumple con la tarea que debe, de no ser así se vuelve a la etapa anterior a hacer los ajustes pertinentes.
4. **Aplicacion y uso del modelo**
    - Implemetación del modelo para que realice la tarea específica para la que fue reentrenado. 

## Clases y su descripción


**DatosEgresado**  
Atrubutos: 
- nombre: obtenido de la base de datos.
- empresa: obtenido de la base de datos.
- rol: este dato es el que se quiere conseguir con el modelo.
- descripcion: obtenido de la base de datos.

**SQL_ROL**  
Metodos:
- obtenerDatos(): se encarga de obtener los datos necesarios para hacer la predicción.
- subirDatos(): se encarga de subir al servidor los datos completos (incluyendo el rol) en formato de tabla.


**DatosReentreno**  
Atributos:
- descripcion: contiene la descripcion de trabajos previamente catalogados.
- categoria: se asigna dependiendo el rol que indica el dataset.  

Metodos:
- cargarDatos(): obtiene los datos de una libreria de Kaggle.

**DataCleaner**  
Atributos:
- rowData: de datos empleado tomamos unicamente la descripcion de los roles.
- cleanData: datos limpios resultado de pasar por los métodos.

Métodos:
- eliminadorCaracteresEspeciales():deja unicamente letras.
- convertidorMinusculas().
- eliminadorStopWords(): se encarga de elminar palabras como *que*, *de*.

**Tokenizador**  
Métodos:
- tokenizarTexto(): convierte cara palabra en un token con el que el modelo BERT asocia cada palabra.

**ReentrenadorModelo**  
Métodos:
- cargarModelo(): se encarga de importar el modelo desde la libreria Hugging Face
- configurarModelo(): se encarga de hacer los ajustes necesarios para la problemática a trabajar.
- entrenarModelo().

**ImplementadorModelo**  
Métodos: 
+ clasificarDatos(): utiliza el modelo entrenado ingresando los datos (descripciones de los roles) que queremos clasificar.