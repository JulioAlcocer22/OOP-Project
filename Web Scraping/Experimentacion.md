# Experimentación sobre las URL's al navegar por la página de LinkedIn:
## A continuación se expone una serie de experimentos con la finalidad de encontrar patrones en las cadenas para la optimización de peticiones realizadas en el scraper.

### URL después de iniciar sesión:
https://www.linkedin.com/feed/?trk=homepage-basic_sign-in-submit
### URL al presionar el botón de LinkedIn
https://www.linkedin.com/feed/
### URL al teclear *software uady* en el buscador de LinkedLn (3 intentos)
https://www.linkedin.com/search/results/all/?keywords=fmat%20uady&origin=GLOBAL_SEARCH_HEADER&sid=vRY
https://www.linkedin.com/search/results/all/?keywords=fmat%20uady&origin=GLOBAL_SEARCH_HEADER&sid=%3Agw
https://www.linkedin.com/search/results/all/?keywords=fmat%20uady&origin=GLOBAL_SEARCH_HEADER&sid=30k

### URL al teclear *software uady* en el buscador de LinkedIn (3 intentos)
https://www.linkedin.com/search/results/all/?keywords=software%20uady&origin=GLOBAL_SEARCH_HEADER&sid=%3A.x
https://www.linkedin.com/search/results/all/?keywords=software%20uady&origin=GLOBAL_SEARCH_HEADER&sid=Jel

### Nota: Al buscar presionar la barra lateral de personas, arroja los mismos resultados que presionar los botones 1, 2, y 3er (556 resultados)

### URL al teclear *software uady* en el buscador de LinkedIn y presionar el botón personas(3 intentos)
https://www.linkedin.com/search/results/people/?keywords=software%20uady&origin=SWITCH_SEARCH_VERTICAL&sid=r4M
https://www.linkedin.com/search/results/people/?keywords=software%20uady&origin=SWITCH_SEARCH_VERTICAL&sid=C6c
https://www.linkedin.com/search/results/people/?keywords=software%20uady&origin=SWITCH_SEARCH_VERTICAL&sid=gfZ

### Nota: Si elimino el último segmento de las cadenas anteriores &sid=*** , la página se recupera y no sufre afectaciones.
### Nota: Si elimino &origin=SWITCH_SEARCH_VERTICAL&sid=*** , la página se recupera y no sufre afectaciones.

### Nota: Al ingresar https://www.linkedin.com/search/results/people/?keywords=software%20mexico&sid=oCO en la barra de búsqueda, aparece "software mexico"

### Al momento de escribir esta linea, LinkedIn ha limitado los resultados de búsqueda (Se eliminó historial de búsqueda y caché) 

### Nota: Si se manda muchas veces *software uady*, la pagina limita los resultados a 16, si se cambia a "uady software" regresa a los 556 resultados originales.

### URL al teclear *software uady* en el buscador de LinkedIn e iterará sobre el pagination que se encuentra al final
https://www.linkedin.com/search/results/people/?keywords=software%20uady&origin=GLOBAL_SEARCH_HEADER&page=2&sid=W%3B)
https://www.linkedin.com/search/results/people/?keywords=software%20uady&origin=GLOBAL_SEARCH_HEADER&page=3&sid=Th~
https://www.linkedin.com/search/results/people/?keywords=software%20uady&origin=GLOBAL_SEARCH_HEADER&page=4&sid=.Wf
https://www.linkedin.com/search/results/people/?keywords=software%20uady&origin=GLOBAL_SEARCH_HEADER&page=7&sid=4G6
https://www.linkedin.com/search/results/people/?keywords=software%20uady&origin=GLOBAL_SEARCH_HEADER&page=56&sid=XnT

### Nota: al ingresar https://www.linkedin.com/search/results/people/?keywords=software%20uady&origin=GLOBAL_SEARCH_HEADER&page=57&sid=XnT ( La página 57 no existe ) devuelve:
![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/f6c298dc-1e05-44f8-bacb-7d23bd74a530)

### Nota: Dada la entrada "julio cesar alcocer herrera" y presionado el botón personas, obtenemos:
![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/6c13ce72-7d05-4cbe-82db-9cd043bcbd60)
Notese que el link esta contenido en la clase "app-aware-link" y el nombre y el link se encuentran dentro de class="entity-result__title-text t-16

### Dado el link (https://www.linkedin.com/in/ecambranes/) y presionado el botón contactos:
https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAAAOo4HoBWdu3t3FHNyv7vZy0g5XgHsU4z3k%22%5D&network=%5B%22F%22%2C%22S%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH&sid=%40T3

https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAAAOo4HoBWdu3t3FHNyv7vZy0g5XgHsU4z3k%22%5D&network=%5B%22F%22%2C%22S%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH&sid=%40T3

https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAAAOo4HoBWdu3t3FHNyv7vZy0g5XgHsU4z3k%22%5D&network=%5B%22F%22%2C%22S%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH&sid=NgX
### Al eliminarse &sid=NgX , la página no se inmuta

### Ingresando al perfil de Cambranes, dado el botón *Contactos* y modificando según los filtros siguientes:
![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/277bfe3b-08d4-44bc-a879-f9336f0db8ec)

https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAAAOo4HoBWdu3t3FHNyv7vZy0g5XgHsU4z3k%22%5D&network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&sid=-ZR

https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAAAOo4HoBWdu3t3FHNyv7vZy0g5XgHsU4z3k%22%5D&network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&sid=.Hh

### Misma URL anterior, pero en la página 29.
https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAAAOo4HoBWdu3t3FHNyv7vZy0g5XgHsU4z3k%22%5D&network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&page=29&sid=)Qa

### Misma URL anterior, pero en la página 29.
https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAAAOo4HoBWdu3t3FHNyv7vZy0g5XgHsU4z3k%22%5D&network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&page=5&sid=PXK

### Misma URL anterior, pero en la página 29.
https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAAAOo4HoBWdu3t3FHNyv7vZy0g5XgHsU4z3k%22%5D&network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&page=1&sid=PXK

### Importante a considerar:
![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/8f23cfe8-c299-4749-abf4-7fa0bed1b47c)
![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/221b75ac-fd88-4bbe-908b-f4f835375641)
![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/2153a53d-ceaf-49e1-a521-701284036bd3)

Todos los perfiles contienen la etiqueta de clase:
Nótese que el link esta contenido en la clase "app-aware-link" y el nombre y el link se encuentran dentro de class="entity-result__title-text t-16
LinkedIn devuelve 10 perfiles por página de resultado.

### Nota: Al acceder a un perfil denominado *Miembro de LinkedIn*: 
![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/b772d786-c79d-4d14-8bb8-35207e90903b)

### Ingresando Universidad Autónoma de Yucatán y dando click en *Personas*, devuelve 31000 resultados

### Sea el seiguiente caso, devuelve solo 14000 resultados:

![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/f18f2ff1-c696-4617-bcf4-3d110033304a)

# Al parecer, a fuerza requerimos LinkedIn Premium (Se agotaron el número máximo de solicitudes mensuales):
![image](https://github.com/JulioAlcocer22/OOP-Project/assets/75227439/ebb23d1f-f16b-4a21-8456-ca33e2d51f73)




