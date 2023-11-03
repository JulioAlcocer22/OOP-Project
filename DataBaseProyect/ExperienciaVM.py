from EgresadoInfoVM import EgresadoInfoVM

class ExperienciaVM:
    
    def __init__(self, egresado, empresa, puesto, descripcion, duracion):
        self.egresado = EgresadoInfoVM(egresado)
        self.empresa = empresa
        self.puesto = puesto
        self.descripcion = descripcion
        self.duracion = duracion
        