package main

import (
	"net/http"
	"src/Controller"
)

func main() {

	c := Controller.ControllerInicio{}

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		switch r.URL.Path {
		case "/login":
			c.Controllerlogin(w, r)
		case "/login-submit":
			c.LoginSubmit(w, r)
		}
	})
	http.ListenAndServe("", nil)
}
