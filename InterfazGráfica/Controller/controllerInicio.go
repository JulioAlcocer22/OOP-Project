package Controller

import (
	"fmt"
	"html/template"
	"net/http"
)

type ControllerInicio struct{}

func (c *ControllerInicio) Controllerlogin(w http.ResponseWriter, r *http.Request) {
	t, _ := template.ParseFiles("View/login.html")
	http.Handle("/Images/", http.StripPrefix("/Images/", http.FileServer(http.Dir("View/Images"))))
	http.Handle("/Scripts/", http.StripPrefix("/Scripts/", http.FileServer(http.Dir("View/Scripts"))))
	http.Handle("/Styles/", http.StripPrefix("/Styles/", http.FileServer(http.Dir("View/Styles"))))
	t.Execute(w, nil)
}

func (c *ControllerInicio) LoginSubmit(w http.ResponseWriter, r *http.Request) {
	universidad := r.FormValue("universidad")
	licenciatura := r.FormValue("licenciatura")
	fmt.Fprintf(w, "Universidad: %s - Licenciatura: %s", universidad, licenciatura)
}
