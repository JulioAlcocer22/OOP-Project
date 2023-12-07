#from Modelo.DataCleaner import DataCleaneri
from DatosPractiva import DatosPractica
from Datos import DatosRoles


class Main:
    
    #Cargando datasets
    Dataset = []
    Etiquetas = []

    for elemento in DatosRoles.datos_totales:
        Etiquetas.append(elemento["ID"])
        Dataset.append(elemento["Descripcion"])

    