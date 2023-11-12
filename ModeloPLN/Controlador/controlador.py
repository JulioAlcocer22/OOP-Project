from ModeloPLN.Modelo.DataCleaner import DataCleaner


class Controlador():
    """
    Pseudocodigo
    1. Tener el row dataset de las descripciones con sus respectivas etiquetas
    2. Limpiar dicho dataset
    3. Tokenizar

    ->En algun punto hay que dividir el dataset en datos de entrenamiento y en datos de validacion

    4. Cargar el modelo y hacer el fine-tunning


    """

    def reentrenar():
         

        rowDataset = ["E*#$sta es la primera oracion. Parte a dividir de la primera oracion. Segumos en la primera", "Esta es la segunda oracion. Parte a dividir de la segunda oracion.", "Okey, ya es la tercera", "Ojo, oracion de primer tipo. Esta es la segunda descripcion de tipo 1"]
        etiquetasRow = [1,2,3,1]

        limpiador = DataCleaner(rowDataset, etiquetasRow)

        cleanDataSet = []
        etiquetasClean = []

        limpiador.crearDatasetsNuevos(cleanDataSet, etiquetasClean)

        
    

    #def utilizar():


    