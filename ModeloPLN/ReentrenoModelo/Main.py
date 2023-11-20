#from Modelo.DataCleaner import DataCleaner
import Datos
from DatosPractiva import DatosPractica
from Datos import DatosRoles
from .Modelo.DataCleaner import DataCleaner

class Main:
    
    #Cargando datasets
    Dataset = []
    Etiquetas = []

    for elemento in DatosRoles.datos_totales:
        Etiquetas.append(elemento["ID"])
        Dataset.append(elemento["Descripcion"])

    #DatasetTokenizado = TokenizadorDatos(Dataset)

    #print(DatasetTokenizado[1])
   

    """
    rowDataset = ["E*#$sta es la primera oracion. Parte a dividir de la primera oracion. Segumos en la primera", "Esta es la segunda oracion. Parte a dividir de la segunda oracion.", "Okey, ya es la tercera", "Ojo, oracion de primer tipo. Esta es la segunda descripcion de tipo 1"]
    etiquetasRow = [1,2,3,1]

    limpiador = DataCleaner(rowDataset, etiquetasRow)

    cleanDataSet = []
    etiquetasClean = []

    limpiador.crearDatasetsNuevos(cleanDataSet, etiquetasClean)
    
    for etiqueta, oracion in zip(etiquetasClean, cleanDataSet):
        print(etiqueta, oracion)
    
    #Hasta este punto, ya se tiene la primera clase lista
    """

    