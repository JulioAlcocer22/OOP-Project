from Modelo.Datos import DatosRoles
from Modelo.DivisorDatasets import DivisorDatasets
from Modelo.Entrenador import Entrenador
from Modelo.Vectorizador import VectorizadorDatos
from Modelo.Predictor import Predictor
from sklearn.naive_bayes import MultinomialNB

#pasar al controlador


dataset = []
etiquetas = []

for elemento in DatosRoles.datos_totales:
    etiquetas.append(elemento["ID"])
    dataset.append(elemento["Descripcion"])


#Separando datasets
divisor = DivisorDatasets(dataset, etiquetas)
descripciones_train, descripciones_test, parametro_train, parametro_test = divisor.dividir()

#vectorizando datasets
vectorizador = VectorizadorDatos()

descripciones_train_vectorizadas, descripciones_test_vectorizadas = vectorizador.vectorizar(descripciones_train, descripciones_test)


#print(descripciones_train_vectorizadas.shape)
#print(descripciones_test_vectorizadas.shape)

clf= MultinomialNB() #objeto clasificador
entrenador = Entrenador(descripciones_train_vectorizadas, parametro_train, descripciones_test_vectorizadas, parametro_test)

#Se entrena al clasificador
entrenador.entrenar(clf)

predictor = Predictor(clf, descripciones_test_vectorizadas)

predicciones = predictor.predecir()

print(descripciones_test)
print(predicciones)



print(type(predicciones))