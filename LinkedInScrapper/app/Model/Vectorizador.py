from sklearn.feature_extraction.text import CountVectorizer

class VectorizadorDatos:

    def vectorizar(self, dataset_entrenamiento, dataset_a_predecir ):
        vect = CountVectorizer().fit(dataset_entrenamiento)  # Asignando tipo de vector
        descripciones__entrenamiento_vectorizadas = vect.transform(dataset_entrenamiento)  # Vectorizando datos
        descripciones_a_predecir_entrenadas = vect.transform(dataset_a_predecir)
        return descripciones__entrenamiento_vectorizadas, descripciones_a_predecir_entrenadas
