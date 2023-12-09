package Controller

import (
	DBConexion "DB"
	"Model"
	"encoding/json"
	"html/template"
	"log"
	"net/http"
)

type ControladorVistaInicial struct{}
type ControladorResultados struct{}

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
