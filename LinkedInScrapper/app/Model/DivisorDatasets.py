from sklearn.model_selection import train_test_split

#pasar al controlador

class DivisorDatasets:

    def __init__(self, dataset, etiquetas):
        self.dataset = dataset
        self.etiquetas = etiquetas

    def dividir(self):
        descripciones_train, descripciones_test, parametro_train, parametro_test = train_test_split(self.dataset, self.etiquetas, test_size = 0.20, random_state =0 )
        return descripciones_train, descripciones_test, parametro_train, parametro_test