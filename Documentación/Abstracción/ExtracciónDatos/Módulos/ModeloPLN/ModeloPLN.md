# Bienvenidos al Procesamiento de Lenguaje Natural
Una de las problemáticas a la hora de recabar la información es que, en muchas de las ocasiones, en el aparado de experiencia únicamente ponen la empresa y la descripción del trabajo que realizan, o en su defecto, se añade un "rol", pero en su descricpión se hace referencia a otro. Es por ello que se optó por realizar un modelo para clasificar los roles de trabajo dependiendo de la descripción que estos tengan.

## Descripción

Se optó por utilizar un modelo pre entrenado del modelo BERT (Bidirectional Encoder Representations from Transformers) que la comunidad de Hugging Face ya ha elaborado anteriormente y puesto en su plataforma para que otros miembros de la comunidad puedan utilizarlos. Dicho modelo es BERT - cased, el cual tiene varias funciones, como son:
 - Clasificación de texto (el caso de este proyecto)
 - Extracción de Entidades Nombradas 
 - Preguntas y Respuestas (QA) 
 - Resumen Automático
 - Entre otras



Sin embargo, no se pudo llevar acabo, en su lugar se utilizó un un modelo NAIVE BAYES.
Entre las ventajas podemos destacar:
- Naive Bayes es uno de los algoritmos de Machine Learning más rápidos y sencillos para predecir una clase de conjuntos de datos.
- Se utiliza para clasificaciones binarias y de clases múltiples.
- Funciona mejor que otros algoritmos cuando hablamos de predicciones multiclase. 
- Es la opción más popular para problemas de clasificación de texto.


  La desventaja principal, por su parte, es que Naive Bayes asume que todas las características son independientes entre sí, de modo que nunca podrá aprender la relación existente entre ellas.

#### Tipos de modelo Naive Bayes:

- Gaussiano: según este modelo, las características siguen una distribución normal. De modo que, en caso de que los predictores tomen valores continuos en lugar de discretos, el modelo asume que estos valores se muestrean a partir de la distribución gaussiana.
- Multinomial: este modelo se usa cuando los datos cuentan con una distribución multinomial y se utilizan, principalmente, para resolver problemas de clasificación de documentos.
- Bernoulli: el tipo Bernoulli tiene un funcionamiento parecido al multinomial, pero las variables predictoras son las variables booleanas independientes.

En este caso se ultilizó el **Multinomial**


## Proceso de entranamiento

- Separación del dataset y de los parámetros para el entrenamiento y para la prueba
- Vectorización de las descripciones
- Entrenamiento del modelo
- Evaluación del modelo (se observa como predice las descripciones del dataset de prueba por medio de ciertas  métricas)


## Clases y su descripción

### DatosRoles

Atributos: 
- desarrolladores_web: diccionario que contiene descripciones en inglés y español de roles desempeñados en el area, junto con su respectiva etiqueta.
- desarrolladores_mobil: diccionario que contiene descripciones en inglés y español de roles desempeñados en el area, junto con su respectiva etiqueta.
- inteligencia_artificial: diccionario que contiene descripciones en inglés y español de roles desempeñados en el area, junto con su respectiva etiqueta.
- ciberseguridad: diccionario que contiene descripciones en inglés y español de roles desempeñados en el area, junto con su respectiva etiqueta.
- gestion: contiene diccionario que descripciones en inglés y español de roles desempeñados en el area (gestión de proyectos), junto con su respectiva etiqueta.
- ciencias_de_datos: diccionario que contiene descripciones en inglés y español de roles desempeñados en el area, junto con su respectiva etiqueta.
- educación: diccionario que contiene descripciones en inglés y español de roles desempeñados en el area, junto con su respectiva etiqueta.
- otros: diccionario que contiene descripciones en inglés y español de roles desempeñados en cualquier area menos de desarrollo de software, junto con su respectiva etiqueta.
- datos_totales: diccionario que junta todos los anteriores.

Métodos

-imprimirInformación: imprime la cantidad de descricpiones que contiene cada atributo.

### DivisorDataset

Métodos
- dividir: divide los datasets en datos de entrenamiento y de prueba.

### Entrenador

Métodos
- entrenar: entrena el modelo.
- visualizarPrecision: evalúa la precision del modelo  comparando los valores de la predicción hecha de los datos de prueba con sus parametros corrspondientes.



### Predictor

Métodos

- predecir: predice el área de la descripción dada.

### VectorizarDatos

Métodos
- vectorizar: vectoriza las descricpiones dadas.