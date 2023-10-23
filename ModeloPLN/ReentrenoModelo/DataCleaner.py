import re
class DataCleaner:
    rowDataSet = []
    etiquetasRow = []
    

    #constructor
    def __init__(self, rowDataSet, etiquetasRow):
        self.rowDataSet = rowDataSet
        self.etiquetasRow = etiquetasRow
   
        

    def dividirOraciones(self, texto):

        oraciones = []
        inicio = 0

        for i in range(len(texto)):
            if texto[i] == '.':
                oraciones.append(texto[inicio:i + 1])
                inicio = i + 2  # Agrega 2 para omitir el espacio después del punto y considerar el inicio de la siguiente oración

        # Agrega la última oración si hay texto después del último punto
        if inicio < len(texto):
            oraciones.append(texto[inicio:])

        return oraciones

    def eliminarCaracteresEspeciales(self,cadena):
        # Define una expresión regular que busca cualquier carácter que no sea una letra, coma o punto
        patron = r'[^a-zA-Z,\. ]'
        # Usa re.sub para reemplazar todos los caracteres no deseados con una cadena vacía
        cadena_limpia = re.sub(patron, '', cadena)
        return cadena_limpia
    

    def crearDatasetsNuevos(self, cleanDataSet, etiquetasClean  ):

        for elemento, etiqueta in zip(self.rowDataSet, self.etiquetasRow): 
            oraciones = self.dividirOraciones(elemento)

            for nuevaOracion in oraciones:
                cleanDataSet.append(self.eliminarCaracteresEspeciales(nuevaOracion))
                etiquetasClean.append(etiqueta)

