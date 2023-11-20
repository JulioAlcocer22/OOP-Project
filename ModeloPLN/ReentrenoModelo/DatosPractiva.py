class DatosPractica():
    web = [
        {"ID":1, "Descripcion": "Dato web"},
    ]

    mobile = [
       {"ID":2, "Descripcion": "Dato mobile"},
    ]
        
    

    AI = [
       { "ID":3, "Descripcion": "Dato AI"},
    ]


    datos_totales = web + mobile + AI

    

    @classmethod
    def imprimirInf(cls):
        elementosWeb = len(cls.web)
        elementosMobile = len(cls.mobile)
        elementosAI = len(cls.AI)

        print("Web: ",elementosWeb)
        print("Mobile", elementosMobile)
        print("AI: ", elementosAI)