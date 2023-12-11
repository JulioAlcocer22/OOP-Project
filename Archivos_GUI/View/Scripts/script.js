document.addEventListener('DOMContentLoaded', function () {
    document.getElementById("universidad").addEventListener("change", obtenerLicenciaturas);
    document.getElementById("resultados").addEventListener("click", function(){
        enviarResultados();
    });
});

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

function enviarResultados(){

    var universidad = document.getElementById("universidad").value;
    var licenciatura = document.getElementById("licenciatura").value;
    var jsonData = {
        "universidad": universidad,
        "licenciatura": licenciatura
    };

    localStorage.setItem("jsonData", JSON.stringify(jsonData));
}
