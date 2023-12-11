package Server

import (
	"Controller"
	"net/http"
)

func InicializarServidor() {
	mux := http.NewServeMux()
	manejarRutas(mux)
	servirRecursos(mux)
	http.ListenAndServe(":8080", mux)
}

func servirRecursos(mux *http.ServeMux) {
	mux.Handle("/Images/", http.StripPrefix("/Images/", http.FileServer(http.Dir("View/Images"))))
	mux.Handle("/Scripts/", http.StripPrefix("/Scripts/", http.FileServer(http.Dir("View/Scripts"))))
	mux.Handle("/Styles/", http.StripPrefix("/Styles/", http.FileServer(http.Dir("View/Styles"))))
}

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
