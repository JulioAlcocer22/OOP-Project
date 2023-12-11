from sklearn.naive_bayes import MultinomialNB


class Predictor:

    def __init__(self, clf, descripciones):
        self.clf = clf
        self.descripciones = descripciones

    def predecir(self):
        predicciones = self.clf.predict(self.descripciones)  # función para predecir
        return predicciones
