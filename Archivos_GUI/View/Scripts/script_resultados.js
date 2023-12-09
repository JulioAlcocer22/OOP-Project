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

        /*Aqui es donde vas a llamar a las funciones para graficar
        le pasas como parametro los arreglos y ya los puedes usar*/
        escrbirDropdown(empresasNombre);
    })
    .catch(error => console.error('Error:', error));
    localStorage.clear();
}

/*Este es un ejemplo de una funcion donde se usan los arreglos
que necesitas, la vas a borrar y vas a poner las funciones para
las graficas*/
function escrbirDropdown(arregloDatos){

    var dropdownPrueba = document.getElementById("opciones")
    dropdownPrueba.innerHTML = "";

    arregloDatos.forEach(dato => {
        var option = document.createElement("option");
        option.value = dato;
        option.text = dato;
        dropdownPrueba.add(option);
    });

}