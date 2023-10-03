# **Proceso**
## **Tabla de Contenido**
* [Descripción del Proceso](#descripción-del-proceso)
* [Gestión del Proceso](#gestión-del-proceso)
* [Métricas de Participación del Proyecto](#métricas-de-participación-del-proyecto)


## **Descripción Del Proceso**
A continuación, se describen brevemente los roles y responsabilidades de los integrantes del equipo:

### **Julio Alcocer**
**Rol:** Procesamiento del Lenguaje Natural.

**Responsabilidades:**
-	Creación del modelo informático.
-	Entrenamiento del modelo informático.
-	Reentrenamiento del modelo informático.

### **Pablo Baeza**
**Rol:** Web Scraping.

**Responsabilidades:**
-	Obtención de los datos de la página web de LinkedIn.
-	Limpieza de las cadenas obtenidas.
-	Manejo de altas y bajas de las tablas necesarias.

### **Rodrigo Canto**
**Rol:** Front-end.

**Responsabilidades:**
-	Elaboración de una página web agradable e intuitiva para el usuario.
-	Correcto manejo de los datos obtenidos en la base de datos.
-	Hosting de la respectiva página web.

### **Alex Dzul**
**Rol:** Análisis estadístico y manejo de base de datos.

**Responsabilidades:**
-	Elaboración de la estructura de la base de datos.
-	Mantenimiento del hosting de la base de datos.
-	Operaciones de “altas y bajas” en la respectiva base de datos.
-	Garantizar la seguridad en la base de datos.

### **Daniel Kao**
**Rol:** Apoyo a los módulos de Web Scraping y Front-end, así como revisión de la documentación.

**Responsabilidades:**
-	Revisar que la documentación esté completa y que aporte el valor necesario.
-	Asesorar al área de Front–end en cuanto a buenas prácticas y técnicas.
-	Asegurar la calidad de los procesos del área de Web Scraping.


Para el proceso y avance del proyecto, se optó finalmente por emplear la herramienta de Microsoft Teams para videollamadas o sesiones que puedan surgir a lo largo de la entrega. Esto por el motivo que la plataforma guarda un registro de cada videollamada, así como cada integrante posee una cuenta institucional. Sin embargo, también habrá momentos que hayan reuniones de equipo de manera presencial, por lo que se tomará una evidencia del producto de dicha sesión.


## **Gestión Del Proceso**
A continuación, se presentan cada una de las reuniones que hubo en el equipo para la realización del proyecto.

### **Primera Reunión**

**Participantes:** Julio Alcocer, Daniel Kao, Alex Dzul, Rodrigo Canto, Pablo Baeza.

**Tema:** Discusión sobre la temática del proyecto.

**Resumen:**
El proyecto había sido recientemente asignado por nuestro cliente el Dr. Edgar Cambranes, antes de iniciar el borrador del proyecto requeríamos su aprobación formal, en equipo debíamos decidir cuál sería la temática del proyecto. Varios miembros del equipo comentaron ideas de proyecto tales como un Sistema de Recursos humanos, Un analizador de redes sociales para una empresa, un sistema de monitoreo de flotillas, entre otros proyectos no muy factibles. Concluimos que el proyecto de sistema de recursos humanos era el mas factible por el momento.

### **Segunda Reunión**

**Participantes:** Daniel Kao, Rodrigo Canto, Pablo Baeza.

**Tema:** Profundización sobre el sistema de recursos Humanos.

**Resumen:**
De manera informal se ahondó brevemente sobre las funcionalidades del proyecto, las capacidades del sistema y la importancia y la factibilidad de este, en un principio se veía bastante bien, aunque en retrospectiva era un sistema del tipo "Altas, bajas y cambios".

### **Tercera Reunión**

**Participantes:** Julio Alcocer, Alex Dzul, Pablo Baeza.

**Tema:** Adecuación de funcionalidades

**Resumen:**
En la reunión se abordaron varios aspectos mejorables, un amigo del padre de Alex Dzul aportó valiosa información que permitió mejorar las funcionalidades del presente proyecto. El proyecto ya estaba tomando forma.

### **Cuarta Reunión**

**Participantes:** Julio Alcocer, Daniel Kao, Alex Dzul, Rodrigo Canto, Pablo Baeza.

**Tema:** Replanteamiento del proyecto

**Resumen:**
Después de ser abordados por nuestro cliente sobre la verdadera utilidad de nuestro proyecto, nos propuso un proyecto más interesante y con una mayor dificultad técnica, pero que otorga valor real a la sociedad en general inclusive para los propios alumnos, se acordó tener una reunión en 2 días donde expusiéramos nuestras ideas respecto al proyecto propuesto.

### **Quinta Reunión**

**Participantes:** Julio Alcocer, Daniel Kao, Alex Dzul, Rodrigo Canto, Pablo Baeza.

**Tema:** Definición formal de la nueva propuesta

**Resumen:**
Unos días después de la última reunión y ya más calmados respecto al cambio del proyecto. En intervalos de 5 minutos, cada integrante expuso sus ideas, así como sus respectivas adecuaciones por el proyecto propuesto, debido a que era bastante ambicioso y requería de bastante esfuerzo. Se llegaron a los acuerdos siguientes:
- El proyecto de gestión de recursos humanos quedó completamente descartado.
- El proyecto propuesto por el cliente sería nuestro nuevo proyecto.
- El cambio de proyecto se le comunicará a nuestro cliente en la brevedad.
- Se acordó de reducir el alcance únicamente a la carrera de LIS y LCC.
- Se acordó el uso de web scripting en Python, así como el procesamiento de Lenguaje natural.

### **Sexta Reunión**

**Participantes:** Julio Alcocer, Alex Dzul, Pablo Baeza.

**Tema:** Dudas referentes al diseño del proyecto.

**Resumen:**
Después de la última reunión se dio un tiempo para definir a grandes rasgos cómo se estructuraría el proyecto, hubo un ligero conflicto en cuanto a la manera de presentar los datos, si a manera de reporte descargable o si los resultados se visualizarían en una página web, después de discutir varios aspectos de tiempo y esfuerzo, se acordó que lo más factible sería mostrar la información en una página web, para que así la información fuera de acceso al público general.

### **Séptima Reunión**

**Participantes:** Julio Alcocer, Daniel Kao, Alex Dzul, Rodrigo Canto, Pablo Baeza.

**Tema:** Dudas referentes al diseño del proyecto (Parte 2).

**Resumen:**
Más tarde se inició la reunión en cuanto a las tecnologías a utilizar, para la parte de Web Scraping y Análisis del Lenguaje Natural se concluyó que la mejor opción sería Python, ya que ofrece todas las bibliotecas con la funcionalidad necesaria. Para el apartado de base de datos se decidió SqlServer ya que uno de nuestros integrantes ya cuenta con experiencia profesional. Sin embargo, al momento de seleccionar cuál sería el lenguaje para nuestro Front-end se armó la discusión ya que por una parte un integrante argumentaba que lo mejor sería usar C#, por el potencial que tiene, otro integrante propuso que la opción más factible y sencilla de aprender sería GO, ya que en dicho lenguaje se puede realizar la funcionalidad deseada sin mucho problema. Finalmente, la persona encargada del Front-end se inclinó por usar C#, decisión que respetó todo el equipo y se quedó como oficial.

### **Octava Reunión**

**Participantes:** Alex Dzul, Pablo Baeza.

**Tema:** Acuerdos sobre el uso de base de datos.

**Resumen:**
De manera fugaz y breve se delimitaron los campos básicos necesarios para llevar a cabo las operaciones estadísticas que debía cumplir el apartado de Web Scraping, se concluyó con el diseño de las 2 tablas necesarias para finalizar el proceso de obtención de datos.

### **Novena Reunión**

**Participantes:** Julio Alcocer, Daniel Kao, Alex Dzul, Rodrigo Canto.

**Tema:** Realización formal de la documentación.

**Resumen:**
De manera no presencial se reunieron los integrantes del equipo para iniciar el proceso de integración de sus respectivos diagramas de clase, así como los artefactos a utilizar.

### **Décima Reunión**

**Participantes:** Julio Alcocer, Daniel Kao, Alex Dzul, Rodrigo Canto, Pablo Baeza.

**Tema:** Realización formal de la documentación (Parte 2).

**Resumen:**
De manera no presencial se reunieron los integrantes del equipo para finalizar el proceso de integración de sus respectivos diagramas de clase, así como los artefactos a utilizar, se realizaron las adecuaciones necesarias para mantener coherente el diseño del proyecto. Se refinó la documentación existente.




## **Métricas De Participación Del Proyecto**
La métrica formal de contribución se define de la siguiente manera:
| Criterio                                           | Muy bueno (10 pts)             |  Bueno (9 pts)                 | Regular (7 pts)      |  Mala (4 pts) | Muy Mala (1 pts)
| ------------- | ------------ | ----------- | ------- | ---------------| -------- |
| El integrante respetó las normas establecidas en el repositorio.  | ✔️                        |                           |                           | | |
| El integrante entregó la documentación en tiempo y forma.   | ✔️                        |                           |                           | |
| El integrante entregó su código siguiendo buenas prácticas.   | ✔️                        |                           |                           | |
| El integrante acató las recomendaciones de su respectivo líder.   | ✔️                        |                           |                           | |
| El integrante mantuvo siempre actualizado al equipo   | ✔️                        |                           |                           | |
| El integrante asistió y participó a las sesiones programadas (si le corresponde) para el proyecto. | ✔️  | | | | |

La forma de evaluar a cada integrante durante cada entrega de avances del proyecto será a través de la tabla anterior. Esta consiste de un sistema de puntos (máximo 60, 10 por cada criterio) donde cada integrante deberá conseguir la mayor cantidad de puntos al cumplir con cada uno de los criterios de la tabla. Al final, el procentaje de participación y compromiso con el proyecto depende de la cantidad de puntos obtenidos entre el máximo de puntos a obtener. Por ejemplo: si se obtuvieron 30 puntos durante el proceso de la segunda entrega, entonces el porcentaje de participación de ese integrante será de 50% (100 * (30/60) = 50).

El encargado de evaluar a cada integrante será el líder, pero en el caso de la evaluación del líder, serán los integrantes quienes lo evalúen. Y dichas evaluaciones serán públicas para todo el equipo.
