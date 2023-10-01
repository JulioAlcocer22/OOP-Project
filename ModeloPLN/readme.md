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

## Clases

![CargadorDeDatos](https://github.com/JulioAlcocer22/OOP-Project/blob/699a79d40473b64005d7ab0288f801ace602ac5f/ModeloPLN/img/imgClaseCargadorDeDatos.png)

![DataCleaner](https://github.com/JulioAlcocer22/OOP-Project/blob/JulioAlcocerBranch/ModeloPLN/img/imgClaseDataCleaner.png)

![Tokenizador](https://github.com/JulioAlcocer22/OOP-Project/blob/699a79d40473b64005d7ab0288f801ace602ac5f/ModeloPLN/img/imgClaseTokenizazdor.png)

![ReentrenadorModelo](https://github.com/JulioAlcocer22/OOP-Project/blob/699a79d40473b64005d7ab0288f801ace602ac5f/ModeloPLN/img/imgClaseReentrenadorModelo.png)

![ImplementadorModelo](https://github.com/JulioAlcocer22/OOP-Project/blob/699a79d40473b64005d7ab0288f801ace602ac5f/ModeloPLN/img/imgClaseImplementadorModelo.png)



## Descripción de Clases

**CargadorDeDatos**  
Métodos:
- cargarDatos(): se encarga de obtener los datos en el formato requerido.

**DataCleaner**  
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