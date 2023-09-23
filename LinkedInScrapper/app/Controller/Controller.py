class Controller():
    def __init__(self, querys):
        self.querys = querys

    def recuperarPivotes(self):
        return self.querys.recuperarPivotes()    

    def insertlink(self, link):
        self.querys.insertLink(link, 0)
        
    def insertPivote(self, link):
        self.querys.insertLink(link, 1)
    
    def recuperarTodosLink(self):
        return self.querys.recuperarTodosLink()
    
    def insertEgresadoInfo(self, link, nombre, universidad, carrera):
        idlink = self.querys.recuperarIdLink(link)
        self.querys.insertEgresadoInfo(idlink[0], nombre, universidad, carrera)
    
    def recuperarEgresadoInfoEstudios(self, universidad, carrera):
        return self.querys.recuperarEgresadoInfoEstudios(universidad, carrera)
    
    def insertExperiencia(self, link, universidad, carrera, empresa, puesto, descripcion, duracion, fechaInicio, fechaFin):
        idlink = self.querys.recuperarIdLink(link)
        idEgresado = self.querys.recuperarEgresadoInfo(idlink[0], universidad, carrera)
        self.querys.insertExperiencia(idEgresado[0], empresa, puesto, descripcion, duracion, fechaInicio, fechaFin)
        
    def recuperarTodosExperiencia(self):
        return self.querys.recuperarTodosExperiencia()
    
    def insertEgresados(self, idEgresado, idExperiencia, Rol):
        self.querys.insertEgresados(idEgresado, idExperiencia, Rol)