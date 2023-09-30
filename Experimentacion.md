# Experimentacion sobre las URLs al navegar por la pagina de linkedin:
## A continuacion se expone una serie de experimentos con la finalidad de encontrar patrones en las cadenas para la optimizacion de peticiones realizadas en el scraper.

### URL despues de iniciar sesion:
https://www.linkedin.com/feed/?trk=homepage-basic_sign-in-submit
### URL al presionar el boton de linkedin
https://www.linkedin.com/feed/
### Url al teclear "fmat uady" en el buscador de linkedin ( 3 intentos )
https://www.linkedin.com/search/results/all/?keywords=fmat%20uady&origin=GLOBAL_SEARCH_HEADER&sid=vRY
https://www.linkedin.com/search/results/all/?keywords=fmat%20uady&origin=GLOBAL_SEARCH_HEADER&sid=%3Agw
https://www.linkedin.com/search/results/all/?keywords=fmat%20uady&origin=GLOBAL_SEARCH_HEADER&sid=30k

### Url al teclear "software uady" en el buscador de linkedin ( 3 intentos )
https://www.linkedin.com/search/results/all/?keywords=software%20uady&origin=GLOBAL_SEARCH_HEADER&sid=%3A.x
https://www.linkedin.com/search/results/all/?keywords=software%20uady&origin=GLOBAL_SEARCH_HEADER&sid=Jel

### Nota: Al buscar presionar la barra lateral de personas arroja los mismos resultados que presionar los botones 1, 2, y 3er ( 556 resultados)

### Url al teclear "software uady" en el buscador de linkedin y presionar el boton personas( 3 intentos )
https://www.linkedin.com/search/results/people/?keywords=software%20uady&origin=SWITCH_SEARCH_VERTICAL&sid=r4M
https://www.linkedin.com/search/results/people/?keywords=software%20uady&origin=SWITCH_SEARCH_VERTICAL&sid=C6c
https://www.linkedin.com/search/results/people/?keywords=software%20uady&origin=SWITCH_SEARCH_VERTICAL&sid=gfZ

### Nota: Si elimino el ultimo segmento de las cadenas anteriores &sid=*** la pagina se recupera y no sifre afectaciones.
### Nota: Si elimino &origin=SWITCH_SEARCH_VERTICAL&sid=*** la pagina se recupera y no sifre afectaciones.

### Nota: Al ingresar https://www.linkedin.com/search/results/people/?keywords=software%20mexico&sid=oCO en la barra de busqueda aparece "software mexico"

### Al momento de escribir esta linea linkedin ha limitado los resultados de busqueda ( Se elimino historial de busqueda y cache ) 

### Nota: Si se manda muchas veces "software uady" la pagina limita los resultados a 16, si se cambia a "uady software" regresa a los 556 resultados originales.

### Url al teclear "software uady" en el buscador de linkedin y iterara sobre el pagination que se encuentra al final
https://www.linkedin.com/search/results/people/?keywords=software%20uady&origin=GLOBAL_SEARCH_HEADER&page=2&sid=W%3B)
https://www.linkedin.com/search/results/people/?keywords=software%20uady&origin=GLOBAL_SEARCH_HEADER&page=3&sid=Th~
https://www.linkedin.com/search/results/people/?keywords=software%20uady&origin=GLOBAL_SEARCH_HEADER&page=4&sid=.Wf
https://www.linkedin.com/search/results/people/?keywords=software%20uady&origin=GLOBAL_SEARCH_HEADER&page=7&sid=4G6
https://www.linkedin.com/search/results/people/?keywords=software%20uady&origin=GLOBAL_SEARCH_HEADER&page=56&sid=XnT

### Nota: al ingresar https://www.linkedin.com/search/results/people/?keywords=software%20uady&origin=GLOBAL_SEARCH_HEADER&page=57&sid=XnT ( La pagina 57 no existe ) devuelve:
![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/f6c298dc-1e05-44f8-bacb-7d23bd74a530)

### Nota: Dada la entrada "julio cesar alcocer herrera" y presionado el boton personas obtenemos:
![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/6c13ce72-7d05-4cbe-82db-9cd043bcbd60)
Notese que el link esta contenido en la clase "app-aware-link" y el nombre y el link se encuentran dentro de class="entity-result__title-text t-16

### Dado el link (https://www.linkedin.com/in/ecambranes/) y presionado el boton contactos:
https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAAAOo4HoBWdu3t3FHNyv7vZy0g5XgHsU4z3k%22%5D&network=%5B%22F%22%2C%22S%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH&sid=%40T3

https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAAAOo4HoBWdu3t3FHNyv7vZy0g5XgHsU4z3k%22%5D&network=%5B%22F%22%2C%22S%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH&sid=%40T3

https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAAAOo4HoBWdu3t3FHNyv7vZy0g5XgHsU4z3k%22%5D&network=%5B%22F%22%2C%22S%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH&sid=NgX
### Al eliminarse &sid=NgX la pagina no se inmuta

### Ingresado al perfil de cambranes, dado el boton contactos y modificado segun los filtros siguiente:
![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/277bfe3b-08d4-44bc-a879-f9336f0db8ec)

https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAAAOo4HoBWdu3t3FHNyv7vZy0g5XgHsU4z3k%22%5D&network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&sid=-ZR

https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAAAOo4HoBWdu3t3FHNyv7vZy0g5XgHsU4z3k%22%5D&network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&sid=.Hh

### Misma Url anterior, pero en la pagina 29.
https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAAAOo4HoBWdu3t3FHNyv7vZy0g5XgHsU4z3k%22%5D&network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&page=29&sid=)Qa

### Misma Url anterior, pero en la pagina 29.
https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAAAOo4HoBWdu3t3FHNyv7vZy0g5XgHsU4z3k%22%5D&network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&page=5&sid=PXK

### Misma Url anterior, pero en la pagina 29.
https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAAAOo4HoBWdu3t3FHNyv7vZy0g5XgHsU4z3k%22%5D&network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&page=1&sid=PXK

### Importante a considerar:
![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/8f23cfe8-c299-4749-abf4-7fa0bed1b47c)
![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/221b75ac-fd88-4bbe-908b-f4f835375641)
![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/2153a53d-ceaf-49e1-a521-701284036bd3)

Todos los perfiles contienen la etiqueta de clase:
Notese que el link esta contenido en la clase "app-aware-link" y el nombre y el link se encuentran dentro de class="entity-result__title-text t-16
Linkedin devuelve 10 perfiles por pagina de resultado.

### Nota: Al acceder a un perfil denominado miembro de linkedin: 
![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/b772d786-c79d-4d14-8bb8-35207e90903b)

### Ingresado Universidad Autónoma de Yucatán y dado click en personas devuelve 31000 resultados

### Sea el seiguiente caso devuelve solo 14000 resultados:

![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/f18f2ff1-c696-4617-bcf4-3d110033304a)

# Al parecer a fuerza requerimos Linkedin Premium ( Se agotaron el numero maximo de solicitudes mensaules ):
![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/ebb23d1f-f16b-4a21-8456-ca33e2d51f73)




