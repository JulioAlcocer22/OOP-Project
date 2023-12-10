# Documentación GUI
## Introducción
En la presente documentación se encontrará información detallada acerca de la funcionalidad del backend asociada al proyecto ***LinkedinScrapper***, se explicará de manera puntual las piezas de código fundamentales para poder desarrollar y poner en ejecución esta parte del proyecto de una forma correcta y funcional. Para realizar una explicación más sencilla es necesario señalar la utilización del patrón MVC, por este mismo motivo empezaremos a dividir las secciones a detallar por carpetas.

## Tabla de Contenido
* [Model](#model)
	* [EstructurasJSON.go](#estructurasjsongo)
* [DBConexion](#dbconexion)
	* [Conexion.go](#conexiongo)
	* [ConsultasDB.go](#consultasdbgo)
		* [Función: obtenerLicenciaturas()](#función-obtenerlicenciaturas)
		* [Función: obtenerUniversidades()](#función-obteneruniversidades)
		* [Función: obtenerEmpresas()](#función-obtenerempresas)
		* [Función: obtenerRoles()](#función-obtenerroles)
		* [Función: obtenerDuracion()](#función-obtenerduración)
		* [Función: obtenerResultados()](#función-obtenerresultados)
* [Controller](#controller)
	* [Controlador.go](#controladorgo)
		* [Función: CargarVistaInicial()](#función-cargarvistainicial)
		* [Funcion: RecuperarLicenciaturas()](#función-recuperarlicenciaturas)
		* [Función: CargarVistaResultados()](#función-cargarvistaresultados)
		* [Función: ObtenerResultados()](#funcic3b3n-obtenerresultados-1)
* [Vista](#vista)
	* [Scripts](#scripts)
		* [script.js](#scriptjs)
			* [Función: obtenerLicenciaturas()](#funcic3b3n-obtenerlicenciaturas-1)
			* [Función: enviarResultados()](#función-enviarresultados)
			* [Código que se ejecuta](#código-que-se-ejecuta)
		* [script_resultados.js](#script_resultadosjs)
			* [Función: mostrarDatosEntrada()](#función-mostrardatosentrada)
			* [Función: graficarDatosEmpresa()](#función-graficardatosempresas)
			* [Función: graficarDatosRoles()](#función-graficardatosroles)
			* [Función: mostrarDuración()](#función-mostrarduracion)
			* [Función: generarColorAleatorio()](#función-generarcoloraleatorio)
			* [Función: obtenerResultados()](#funcic3b3n-obtenerresultados-2)
	* [Otras Subcarpetas y Archivos](#otras-subcarpetas-y-archivos)
* [Server](#server)
	* [Servidor.go](#servidorgo)
		* [Función: manejarRutas()](#función-manejarrutas)
		* [Función: servirRecursos()](#función-servirrecursos)
		* [Función: InicializarServidor()](#función-inicializarservidor)
* [Main](#main)

## **Model**
---
Dentro de esta carpeta se encuentran las estructuras cuya funcionalidad corresponde a almacenar los datos provenientes de nuestras futuras consultas a la base de datos, de esta forma se podrán manipular los registros de forma sencilla.

### *EstructurasJSON.go*
---
Este archivo hace más explícita la forma de nuestras estructuras de datos, notemos que todas tienen etiquetas JSON asociadas, esto ocurre pues JSON es una estructura universal para el intercambio y la transferencia de información.

```golang
package Model

type DatosEntrada struct {
	UniversidadItem  string `json:"UniversidadItem"`
	LicenciaturaItem string `json:"LicenciaturaItem"`
}

type Licenciatura struct {
	LicenciaturaItem string `json:"Degree"`
}

type Universidad struct {
	UniversidadItem string `json:"University"`
}

type Empresa struct {
	EmpresaItem    string  `json:"EmpresaItem"`
	PorcentajeItem float64 `json:"PorcentajeItem"`
}

type Rol struct {
	RolItem        string  `json:"RolItem"`
	PorcentajeItem float64 `json:"PorcentajeItem"`
}

type Duracion struct {
	DuracionItem float64 `json:"DuracionItem"`
}

type DatosFinales struct {
	Empresa  []Empresa  `json:"Empresa"`
	Rol      []Rol      `json:"Rol"`
	Duracion []Duracion `json:"Duracion"`
}
```

## **DBConexion**
---
En esta carpeta se encuentran los archivos asociados a la base de datos, los cuales permiten realizar conexiones y consultas para obtener la información que es solicitada por el usuario.

### *Conexion.go*
---
Este archivo permite crear la conexion a la base de datos. Usa la información pertinente para realizar la conexión y se manejan las excepciones correspondientes para evitar errores en caso de que la conexión no se establezca de forma correcta.
Es importante señalar la instalación del paquete ***github.com/microsoft/go-mssqldb***, el cual corresponde al driver de SQLServer que permite realizar la conexión.

```golang
package DBConexion

import (
	"context"
	"database/sql"
	"fmt"
	"log"

	_ "github.com/microsoft/go-mssqldb"
)

var db *sql.DB
var server = "coder-wizards.database.windows.net"
var port = 1433
var user = "POO_Admin"
var password = "password"
var database = "tic-solutions"

func ObtenerConexion() (db *sql.DB, err error) {
	connString := fmt.Sprintf("server=%s;user id=%s;password=%s;port=%d;database=%s;",
		server, user, password, port, database)

	db, err = sql.Open("sqlserver", connString)
	if err != nil {
		log.Fatal("Error creando el pool de conexiones: ", err.Error())
	}

	ctx := context.Background()
	err = db.PingContext(ctx)

	if err != nil {
		log.Fatal(err.Error())
	}

	return
}
```

### *ConsultasDB.go*
---
Dentro de este archivo se realizan las consultas correspondientes para obtener la información necesaria de la base de datos, por obviedad cada función asociada a este archivo invoca a **ObtenerConexión** antes de realizar cada consulta. Cabe señalar que todos los registros que se obtienen como resultado de las consultas se guardan en estructuras con etiquetas JSON asociadas para su posterior transferencia mediante solicitudes HTTP.

### Función: ObtenerLicenciaturas()
Esta función es la encargada de obtener las licenciaturas correspondientes a la universidad seleccionada mediante la consulta ***Select * FROM dbo.RecuperarCarreras(Universidad)*** .

```golang
func (consultas *ObjetoConsulta) ObtenerLicenciaturas(universidad string) (opcionesLicenciatura []Model.Licenciatura) {
	db, err := ObtenerConexion()
	defer db.Close()
	if err != nil {
		log.Fatal("Error realizando la conexion a la base de datos", err.Error())
	}

	rows, err := db.Query("SELECT * FROM dbo.RecuperarCarreras(@universidad)", sql.Named("universidad", universidad))
	defer rows.Close()
	if err != nil {
		log.Fatal("Error al realizar la consulta asociada a las licenciaturas", err.Error())
	}

	for rows.Next() {
		var licenciatura Model.Licenciatura
		err := rows.Scan(&licenciatura.LicenciaturaItem)
		if err != nil {
			log.Fatal("Error al obtener los datos de las licenciaturas", err.Error())
		}
		opcionesLicenciatura = append(opcionesLicenciatura, licenciatura)
	}
	return
}
```

### Función: ObtenerUniversidades()
A la hora de cargar la página inicial, esta función se encarga de recuperar todas las universidades disponibles en la base de datos mediante la consulta ***SELECT * FROM dbo.RecuperarUniversidades()***, estos datos son mostrados al usuario para que pueda realizar la elección de interés.

```golang
func (consultas *ObjetoConsulta) ObtenerUniversidades() (opcionesUniversidad []Model.Universidad) {
	db, err := ObtenerConexion()
	defer db.Close()
	if err != nil {
		log.Fatal("Error realizando la conexion a la base de datos", err.Error())
	}

	rows, err := db.Query("SELECT * FROM dbo.RecuperarUniversidades()")
	defer rows.Close()
	if err != nil {
		log.Fatal("Error realizando consulta para recuperar universidades", err.Error())
	}

	for rows.Next() {
		var universidad Model.Universidad
		err := rows.Scan(&universidad.UniversidadItem)
		if err != nil {
			log.Fatal("Error al obtener las universidades", err.Error())
		}
		opcionesUniversidad = append(opcionesUniversidad, universidad)
	}
	return
}
```

### Función: obtenerEmpresas()
Entrando dentro del contexto de la visualización de resultados, esta función ejecuta la consulta ***EXECUTE dbo.AnalisisEmpresas "universidad", licenciatura"***, este método devuelve todas las empresas disponibles y el porcentaje asociado a cada una de ellas, siempre tomando como parámetro la universidad y licenciatura correspondientes.

```golang
func (consultas *ObjetoConsulta) obtenerEmpresas(universidad string, licenciatura string) (resultadosEmpresas []Model.Empresa) {
	db, err := ObtenerConexion()
	defer db.Close()
	if err != nil {
		log.Fatal("Error realizando la conexion a la base de datos", err.Error())
	}

	rows, err := db.Query("EXECUTE dbo.AnalisisEmpresas @universidad, @licenciatura", sql.Named("universidad", universidad), sql.Named("licenciatura", licenciatura))
	defer rows.Close()
	if err != nil {
		log.Fatal("Error realizando la consulta a la base de datos", err.Error())
	}

	for rows.Next() {
		var empresa Model.Empresa
		err := rows.Scan(&empresa.EmpresaItem, &empresa.PorcentajeItem)
		if err != nil {
			log.Fatal("Error ejecutando la consulta de las empresas", err.Error())
		}

		resultadosEmpresas = append(resultadosEmpresas, empresa)
	}
	return
}
```

### Función: obtenerRoles()
Análoga a la función anterior, esta se encarga de recopilar todos los roles que se encuentran disponibles en la base de datos los cuales se obtuvieron mediante el procesamiento de lenguaje natural (PLN), estos datos también tienen un porcentaje asociado, y se recuperan con la consulta ***EXECUTE dbo.AnalisisRoles "universidad", "licenciatura"***.

```golang
func (consultas *ObjetoConsulta) obtenerRoles(universidad string, licenciatura string) (resultadosRoles []Model.Rol) {
	db, err := ObtenerConexion()
	defer db.Close()
	if err != nil {
		log.Fatal("Error realizando la conexión a la base de datos", err.Error())
	}

	rows, err := db.Query("EXECUTE dbo.AnalisisRoles @universidad, @licenciatura", sql.Named("universidad", universidad), sql.Named("licenciatura", licenciatura))
	defer rows.Close()
	if err != nil {
		log.Fatal("Error al ejecutar la consulta asociada a los roles", err.Error())
	}

	for rows.Next() {
		var rol Model.Rol
		err := rows.Scan(&rol.RolItem, &rol.PorcentajeItem)
		if err != nil {
			log.Fatal("Error al obtener los datos de los roles", err.Error())
		}
		resultadosRoles = append(resultadosRoles, rol)
	}
	return
}
```

### Función: obtenerDuración()
Esta función devuelve un número, el cual corresponde al promedio de duración de los egresados en las empresas, este número claramente varía dependiendo de la universidad y la licenciatura que se esté tomando en cuenta. La consulta que recupera este valor es ***EXECUTE dbo.PromedioDuracion "universidad", "licenciatura"***.

```golang
func (consultas *ObjetoConsulta) obtenerDuracion(universidad string, licenciatura string) (resultadosDuracion []Model.Duracion) {
	db, err := ObtenerConexion()
	defer db.Close()
	if err != nil {
		log.Fatal("Error realizando la conexión a la base de datos", err.Error())
	}

	rows, err := db.Query("EXECUTE dbo.PromedioDuracion @universidad, @licenciatura", sql.Named("universidad", universidad), sql.Named("licenciatura", licenciatura))
	defer rows.Close()
	if err != nil {
		log.Fatal("Error al ejecutar la consulta asociada a la duracion", err.Error())
	}

	for rows.Next() {
		var duracion Model.Duracion
		err := rows.Scan(&duracion.DuracionItem)
		if err != nil {
			log.Fatal("Error al obtener los datos de duracion", err.Error())
		}
		resultadosDuracion = append(resultadosDuracion, duracion)
		//fmt.Println(duracion.DuracionItem)
	}
	return
}
```

### Función ObtenerResultados()
Por temas de practicidad, esta función se encarga de invocar a las tres funciones detalladas con anterioridad, esto ocurre pues los registros resultantes de estas tres funciones son los que se necesitan transerir a la vista asociada a los resultados para su visualización.

```golang
func ObtenerResultados(universidad string, licenciatura string) (resultadosFinales Model.DatosFinales) {
	consultas := ObjetoConsulta{}
	resultadosFinales.Empresa = consultas.obtenerEmpresas(universidad, licenciatura)
	resultadosFinales.Rol = consultas.obtenerRoles(universidad, licenciatura)
	resultadosFinales.Duracion = consultas.obtenerDuracion(universidad, licenciatura)
	return
}
```

## **Controller**
---
Esta carpeta contiene los archivos asociados al controlador, el cual será el encargado de administrar las solicitudes HTTP realizadas por el usuario y brindar la respuesta correspondiente.

### *Controlador.go*
---
En este archivo se definen dos tipos de controladores, cada uno esta asociado a una respectiva vista y su función es manipular las solicitudes HTTP, estos controladores también serán los encargados de ejecutar las vistas asociadas a cada ruta e indicar cuando se realizarán las consultas correspondientes a la base de datos. Cabe señalar que, en caso de realizar consultas, el controlador se encargará de codificar estos registros a estructuras JSON para que puedan ser enviados como respuesta a las solicitudes HTTP anteriormente mencionadas.

### Función: CargarVistaInicial()
Como su nombre lo indica esta función será la encargada de cargar la vista inicial dentro del servidor, esto permitirá al usuario visualizar la página en una ruta específica la cual será detallada posteriormente. Además de esto, se crea un objeto consultas para recuperar las universidades disponibles. Se destaca el uso del paquete **html/template** para lograr esta funcionalidad. 

```golang
func (c *ControladorVistaInicial) CargarVistaInicial(w http.ResponseWriter, r *http.Request) {

	consultas := DBConexion.ObjetoConsulta{}

	t, err := template.ParseFiles("View/login.html")
	if err != nil {
		log.Fatal(err)
		http.Error(w, "Error al cargar la plantilla", http.StatusInternalServerError)
		return
	}

	universidadesDisponibles := consultas.ObtenerUniversidades()
	err1 := t.Execute(w, universidadesDisponibles)
	if err1 != nil {
		log.Fatal(err1)
		http.Error(w, "Error al renderizar la plantilla", http.StatusInternalServerError)
		return
	}
}
```

### Función: RecuperarLicenciaturas()
Esta función esta asociada al controlador de la vista inicial, crea un objeto de tipo ObjetoConsulta para realizar la consulta asociada a las licenciaturas, de esta forma, será posible visualizar las licenciaturas correspondientes a la universidad seleccionada.

```golang
func (c *ControladorVistaInicial) RecuperarLicenciaturas(w http.ResponseWriter, r *http.Request) {

	consultas := DBConexion.ObjetoConsulta{}

	var data Model.Universidad
	if err := json.NewDecoder(r.Body).Decode(&data); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	licenciaturas := consultas.ObtenerLicenciaturas(data.UniversidadItem)
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(licenciaturas)
}
```

### Función: CargarVistaResultados()
Análoga a la función CargarVistaInicial, este método tiene la funcionalidad de cargar y renderizar la vista asociada a los resultados en el servidor, esta vista también tiene su dirección asociada para que el usuario pueda acceder a ella, visualizarla y realizar acciones.

```golang
func (c *ControladorResultados) CargarVistaResultados(w http.ResponseWriter, r *http.Request) {

	//Cuando carges tu página web en el directorio View, cambia el nombre de la plantilla
	t, err := template.ParseFiles("View/prueba.html")
	if err != nil {
		log.Fatal(err)
		http.Error(w, "Error al cargar la plantilla", http.StatusInternalServerError)
		return
	}

	err1 := t.Execute(w, nil)
	if err != nil {
		log.Fatal(err1)
		http.Error(w, "Error al renderizar la plantilla", http.StatusInternalServerError)
		return
	}
}
```

### Función: ObtenerResultados()
Esta función esta asociada al controlador de la vista resultados y se encarga de invocar a la función ObtenerResultados del archivo ConsultasDB.go, la cual, llama a las funciones asociadas a recuperar las empresas, los roles y la duración de egresados. Estos registros serán visualizados en la vista resultados mediante gráficos estadísticos.

```golang
func (c *ControladorResultados) ObtenerResultados(w http.ResponseWriter, r *http.Request) {

	var datosEntrada Model.DatosEntrada

	if err := json.NewDecoder(r.Body).Decode(&datosEntrada); err != nil {
		log.Fatal(err)
		http.Error(w, "Error al decodificar la solicitud JSON", http.StatusBadRequest)
		return
	}

	resultadosFinales := DBConexion.ObtenerResultados(datosEntrada.UniversidadItem, datosEntrada.LicenciaturaItem)
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(resultadosFinales)
}
```

## **Vista**
---
En esta carpeta se encuentran los archivos del frontend de la página web del proyecto (archivos HTML, CSS, JavaScript). Se encarga de la visuazlización de la infromación recopilada y manipulada a lo largo del proyecto, donde se presentan gráficas para la interpretación de la información, así como un apartado para elegir la universidad y carrera que se desea ver su información.

### *Scripts*
---
Esta subcarpeta contiene dos archivos JavaScript, cada uno correspondiente a su propia vista, los cuales sirven para la interactividad y creación de la gráficas:

### *script.js*
---
Este archivo tiene las siguientes funcionalidades:

### Función: obtenerLicenciaturas()
En este método se realiza la lógica para la obtención y presentación de las opciones en una lista desplegable, un formulario en este caso. Se restringe al usuario el acceso a los resultados hasta que se seleccionen todos los campos necesarios. Asimismo, se realiza una solicitud para recuperar las licenciatruras de la base de datos, según la universidad elegida.

```javascript
function obtenerLicenciaturas(){

    if (document.getElementById("universidad").value === "default") {
        document.getElementById("licenciatura").innerHTML = ""; 
        document.getElementById("licenciatura").disabled = true;
        document.getElementById("resultados").disabled = true;
    }
    else{
        var university = document.getElementById("universidad").value;
        var data = {
            "university": university
        };
        
        fetch("http://localhost:8080/recuperar-licenciaturas", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })

        .then(response => response.json())
        .then(data => {
            
            var degreeDropdown = document.getElementById("licenciatura");
            degreeDropdown.innerHTML = "";
            degreeDropdown.disabled = false;
            console.log(data);
    
            data.forEach(opcion => {
                var option = document.createElement("option");
                option.value = opcion.Degree;
                option.text = opcion.Degree;
                degreeDropdown.add(option);
            });
        })
        .catch(error => console.error('Error:', error));
        document.getElementById("resultados").disabled = false;
    }
}
```

### Función: enviarResultados()
Este método se encarga de la lectura de datos del usuarios (las opciones elegidas) y su almacenamiento local en un objeto JSON para la persistencia de esos datos, incluso cuando se cambie a la siguiente vista.

```javascript
function enviarResultados(){

    var universidad = document.getElementById("universidad").value;
    var licenciatura = document.getElementById("licenciatura").value;
    var jsonData = {
        "universidad": universidad,
        "licenciatura": licenciatura
    };

    localStorage.setItem("jsonData", JSON.stringify(jsonData));
}
```

### Código que se ejecuta
El siguiente código representa lo que se ejecuta cuando se cargue por completo la página. En éste se agregan dos eventos, los cuales consisten en la selección de universidad y el botón de "ver resultados", será cuando ocurran esos eventos que se llamarán a las funciones anteriores.

```javascript
document.addEventListener('DOMContentLoaded', function () {
    document.getElementById("universidad").addEventListener("change", obtenerLicenciaturas);
    document.getElementById("resultados").addEventListener("click", function(){
        enviarResultados();
    });
});
```

### *script_resultados.js*
---
Este archivo cuenta con las siguientes funciones:

### Función: mostrarDatosEntrada()
Esta función busca en el archivo HTML las etiquetas con nombre de ID's específicos para la visualización de algunas frases que cambian dependiendo de las opciones elegidas por el usuario.

```javascript
function mostrarDatosEntrada(universidad, carrera){
    document.getElementById("university-chosen").innerHTML = "Universidad: " + universidad;
    document.getElementById("carreer-chosen").innerHTML = "Carrera: " + carrera;
    document.getElementById("q-companies").innerHTML = "¿Qué empresas contratan egresados de la carrera de " + carrera + "?";
    document.getElementById("q-roles").innerHTML = "¿Qué puestos han ocupado los egresados de " + carrera + "?";
    document.getElementById("q-duration").innerHTML = "¿Cuál es la duración promedio de los egresados de " + carrera + " en el que duran en un trabajo?";
}
```

### Función: graficarDatosEmpresas()
Este método se encarga de localizar la etiqueta donde se insertará la gráfica, así como la presentación de los datos. Se emplea una gráfica de barras para la visaulziación de esta información (empresas).

Nota: Por el momento, para una mejor visualización de la información, si la cantidad de empresas es mayor a 15, solamente se presenta el 10% del total de empresas que hayan, de lo contrario, se despliegan todos. Esto por el motivo de que la librería utilizada no permite una buena visualización de la gráfica cuando son más de 15 atributos.

```javascript
function graficarDatosEmpresas(empresasNombre, empresasPorcentaje){
    var ctx = document.getElementById('companiesChart').getContext('2d');
    var longitud = empresasNombre.length;
    var colores = [];
    var empresasMostradas = [];
    var porcentajesMostrados = [];
    var i;

    if(longitud > 15){
        longitud *= 0.10;
    }

    for(i = 0; i < longitud; i++){
        colores.push(generarColorAleatorio());
        empresasMostradas.push(empresasNombre[i]);
        porcentajesMostrados.push(empresasPorcentaje[i]);
    }

    var data = {
        labels: empresasMostradas,
        datasets: [{
            data: porcentajesMostrados,
            backgroundColor: colores
        }]
    };

    var options = {
        legend: { display: false },
        title: {
            display: true,
            text: "Porcentaje de egresados contratados por cada empresa"
        }
    };

    var myBarChart = new Chart(ctx, {
        type: 'bar',
        data: data,
        options: options
    });
}
```

### Función: graficarDatosRoles()
Este método es similar al anterior, sin embargo, aquí se emplea una gráfica de barras para la visualización de esta información.

Nota: Por el momento, para una mejor visualización de la información, si la cantidad de roles es mayor a 15, solamente se presenta el 10% del total de roles que hayan, de lo contrario, se despliegan todos. Esto por el motivo de que la librería utilizada no permite una buena visualización de la gráfica cuando son más de 15 atributos.

```javascript
function graficarDatosRoles(rolesNombre, rolesPorcentaje){
    var ctx = document.getElementById('rolesChart').getContext('2d');
    var longitud = rolesNombre.length;
    var colores = [];
    var rolesMostrados = [];
    var porcentajesMostrados = [];
    var i;

    if(longitud > 15){
        longitud *= 0.10;
    }

    for(i = 0; i < longitud; i++){
        colores.push(generarColorAleatorio());
        rolesMostrados.push(rolesNombre[i]);
        porcentajesMostrados.push(rolesPorcentaje[i]);
    }

    var data = {
        labels: rolesMostrados,
        datasets: [{
            data: porcentajesMostrados,
            backgroundColor: colores
        }]
    };

    var options = {
        legend: { display: false },
        title: {
            display: true,
            text: "Roles ocupados por egresados"
        }
    };

    var myPieChart = new Chart(ctx, {
        type: 'pie',
        data: data,
        options: options
    });
}
```

### Función: mostrarDuracion()
Este método se encarga de buscar el lugar donde debe ir la información en el HTML y despliega a la página la frase que responde a la pregunta.

```javascript
function mostrarDuracion(duracion){
    document.getElementById("duration").innerHTML = "La duracion promedio que un egresado permanece en un puesto es de " + duracion + " meses.";
}
```

### Función: generarColorAleatorio()
Este método se encarga de asignar colores de manera aleatoria, lo cual sirve al momento de graficar, pues la cantidad de empresas o roles siempre cambiará con el tiempo por lo que no hay manera de asignar color a cada uno de manera manual. Por tal motivo, esta función genera un código hexadecimal que representa un color en el HTML y se despliega en la gráfica.

```javascript
function generarColorAleatorio(){
    var r = Math.floor(Math.random() * 256);
    var g = Math.floor(Math.random() * 256);
    var b = Math.floor(Math.random() * 256);

    var colorHexadecimal = "#" + r.toString(16) + g.toString(16) + b.toString(16);

    return colorHexadecimal;
}
```

### Función: obtenerResultados()
Este método recupera el objeto JSON enviado de la vista anterior (que contiene la universidad y licenciatura elegidas por el usuario) y las convierte a datos que JavaScript puede interpretar. Luego se realiza una solicitud para recuperar las empresas, roles, sus respectivos porcentajes, y duración de la base de datos mediante un objeto JSON. Finalmente se llaman a las funciones anteriores para la visualización de los datos recopilados y se limpia el almacenamiento local.

```javascript
function obtenerResultados(){

    var jsonDataString = localStorage.getItem("jsonData");
    console.log(jsonDataString);

    var jsonData = JSON.parse(jsonDataString);

    var universidad = jsonData.universidad;
    var licenciatura = jsonData.licenciatura;

    var jsonData = {
        "UniversidadItem": universidad,
        "LicenciaturaItem": licenciatura
    };

    fetch("http://localhost:8080/obtener-resultados", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })

    .then(response => response.json())
    .then(data => {

        //Estos son los arreglos que se van a usar para graficar
        let empresasNombre = [];
        let empresasPorcentaje = [];
        let rolesNombre = [];
        let rolesPorcentaje = [];
        let duracion;

        //En esta lógica se itera sobre el json para recuperar los datos
        data.Empresa.forEach(empresa => {
            empresasNombre.push(empresa.EmpresaItem);
            empresasPorcentaje.push(empresa.PorcentajeItem);
        });

        data.Rol.forEach(rol => {
            rolesNombre.push(rol.RolItem);
            rolesPorcentaje.push(rol.PorcentajeItem);
        });

        duracion = data.Duracion[0].DuracionItem;

        mostrarDatosEntrada(universidad, licenciatura);
        graficarDatosEmpresas(empresasNombre, empresasPorcentaje);
        graficarDatosRoles(rolesNombre, rolesPorcentaje);
        mostrarDuracion(duracion);
    })
    .catch(error => console.error('Error:', error));
    localStorage.clear();
}
```

### *Otras Subcarpetas y Archivos*
En la carpeta de la vista se pueden encontrar subcarpetas que realmente no tienen tanta importancia como lo serían los archivos JavaScript. A continuación, se describen brevemente cada uno de ellos:
* Images: Carpeta que almacena las imágenes utilizadas para la página web.
* Styles: Carpeta que contiene dos archivos .css correspondientes a cada una de las vistas y que sirven para el diseño y estética de la página.
* login.html: Archivo .html que contiene la vista inicial donde se encuentra el login con el formulario de entrada.
* results.html: Archivo .html que contiene la vista donde se presentan las gráficas y la información.

## **Server**
---
En esta carpeta se encuentra toda la lógica asociada al servidor web, dentro de esta se designa un puerto para el servidor, se alojan recursos asociados a las vistas y se definen las direcciones url asociadas a cada funcionalidad del controlador.

### *Servidor.go*
---
Este archivo tiene las siguientes funcionalidades:

### Función: manejarRutas()
Dentro de este método se inicializan los controladores para ambas vistas, se definen las rutas que se van a manejar para el servidor y a cada una se le asocia una funcionalidad del controlador, la cual será ejecutada cuando el usuario haga una solicitud HTTP.

```golang
func manejarRutas(mux *http.ServeMux) {

	ctrlInicio := Controller.ControladorVistaInicial{}
	ctrlResultados := Controller.ControladorResultados{}

	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		switch r.URL.Path {
		case "/inicio":
			ctrlInicio.CargarVistaInicial(w, r)
		case "/vista-resultados":
			ctrlResultados.CargarVistaResultados(w, r)
		case "/recuperar-licenciaturas":
			ctrlInicio.RecuperarLicenciaturas(w, r)
		case "/obtener-resultados":
			ctrlResultados.ObtenerResultados(w, r)
		}
	})
}
```

### Función: servirRecursos()
Esta función permite cargar recursos asociados a las vistas (archivos CSS y JavaScript) para que puedan ser alojados por el servidor, con esto, cada vez que se cargue una página en el servidor, sus recursos asociados también se cargarán, por lo tanto, podrán ser visibles y funcionales.

```golang
func servirRecursos(mux *http.ServeMux) {
	mux.Handle("/Images/", http.StripPrefix("/Images/", http.FileServer(http.Dir("View/Images"))))
	mux.Handle("/Scripts/", http.StripPrefix("/Scripts/", http.FileServer(http.Dir("View/Scripts"))))
	mux.Handle("/Styles/", http.StripPrefix("/Styles/", http.FileServer(http.Dir("View/Styles"))))
}
```

### Función: InicializarServidor()
Esta función inicializa el servidor local, crea un multiplexor para asociar cada ruta con su respectiva función de respuesta, además se define el puerto sobre el cual nuestro servidor web va a escuchar las distintas solicitudes HTTP que puedan aparecer.

```golang
func InicializarServidor() {
	mux := http.NewServeMux()
	manejarRutas(mux)
	servirRecursos(mux)
	http.ListenAndServe(":8080", mux)
}
```

## **Main**
Dentro de la función principal, se importa el paquete Server para ejecutar la función que inicializa el servidor, esto es lo único que se necesita para poder alojar las páginas web que corresponden a las vistas asociadas a este proyecto.

```golang
package main

import (
	"Server"
)

func main() {
	Server.InicializarServidor()
}

```