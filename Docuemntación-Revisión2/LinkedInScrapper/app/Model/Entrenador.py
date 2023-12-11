from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

class Entrenador:

    def __init__(self, descripciones_entrenamiento_vectorizadas, parametro_train, descripciones_test_vectorizadas, parametro_test):
        self.descripciones_entrenamiento_vectorizadas = descripciones_entrenamiento_vectorizadas
        self.parametro_train = parametro_train
        self.descricpciones_test_vectorizadas = descripciones_test_vectorizadas
        self.parametro_test = parametro_test


    def entrenar(self, clf):
        clf.fit(self.descripciones_entrenamiento_vectorizadas, self.parametro_train) #ajuste al clasificador X_test_vectorized = vect.transform(X_test), aqui se realiza el entrenamiento



    def visualizarPrecision(self):

        predictions = self.clf.predict(self.descripciones_test_vectorizadas) #función para predecir

        print('Accuracy', accuracy_score(self.parametro_test,predictions))
        print('F1-score', f1_score(self.parametro_test, predictions, average = 'weighted'))
        print('Precision', precision_score(self.parametro_test, predictions, average = 'weighted'))
        print('Recall', recall_score(self.parametro_test, predictions, average = 'weighted'))
