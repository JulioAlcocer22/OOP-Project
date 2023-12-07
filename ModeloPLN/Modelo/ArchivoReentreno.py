from Datos import DatosRoles
from Tokenizador import TokenizadorDatos

class Main():

     
    dataset = []
    etiquetas = []

    #Cargando datasets
    for elemento in DatosRoles.datos_totales:
        etiquetas.append(elemento["ID"])
        dataset.append(elemento["Descripcion"])

    tokenizador = TokenizadorDatos(dataset)
    dataset_tokenizado = tokenizador.tokenizar(dataset)
    print("Hola")

