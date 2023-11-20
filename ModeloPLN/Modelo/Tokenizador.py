from transformers import BertTokenizer

class TokenizadorDatos:

    def __init__(self, sentences):
        self.sentences = sentences


    sentences = [
        "Esta es la primera oración.",
        "Esta es la segunda oración.",
        "Esta es la tercera oración."
    ]

    def tokenizar(self, sentences):
        #cargando modelo
        tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

        # Lista para almacenar las representaciones tokenizadas de las oraciones
        tokenized_sentences = []

        for sentence in sentences:
            # Utiliza el tokenizador para procesar cada oración
            tokens = tokenizer(
                sentence,
                padding='max_length',
                max_length=128,
                truncation=True,
                return_tensors="pt"
            )

            # Agrega la representación tokenizada a la lista
            tokenized_sentences.append(tokens)

        return tokenized_sentences
    
        # Ahora, tokenized_sentences contiene las representaciones tokenizadas de todas las oraciones en tu arreglo.
        print("Proceso finalizado")

        for i in tokenized_sentences:
            print(i)
            print("\n\n")
