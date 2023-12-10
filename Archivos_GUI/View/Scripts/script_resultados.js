document.addEventListener("DOMContentLoaded", function(){
    obtenerResultados();
});

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

function mostrarDatosEntrada(universidad, carrera){
    document.getElementById("university-chosen").innerHTML = "Universidad: " + universidad;
    document.getElementById("carreer-chosen").innerHTML = "Carrera: " + carrera;
    document.getElementById("q-companies").innerHTML = "¿Qué empresas contratan egresados de la carrera de " + carrera + "?";
    document.getElementById("q-roles").innerHTML = "¿Qué puestos han ocupado los egresados de " + carrera + "?";
    document.getElementById("q-duration").innerHTML = "¿Cuál es la duración promedio de los egresados de " + carrera + " en el que duran en un trabajo?";
}

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

function mostrarDuracion(duracion){
    document.getElementById("duration").innerHTML = "La duracion promedio que un egresado permanece en un puesto es de " + duracion + " meses.";
}

function generarColorAleatorio(){
    var r = Math.floor(Math.random() * 256);
    var g = Math.floor(Math.random() * 256);
    var b = Math.floor(Math.random() * 256);

    var colorHexadecimal = "#" + r.toString(16) + g.toString(16) + b.toString(16);

    return colorHexadecimal;
}