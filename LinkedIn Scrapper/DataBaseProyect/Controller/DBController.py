from Model import Querys
from linkVM import linkVM
from EgresadoInfoVM import EgresadoInfoVM
from ExperienciaVM import ExperienciaVM

class DBController():
    def __init__(self):
        self.controller = Querys.Querys()

    def recuperarPivotes(self):
        return self.controller.recuperarPivotes()    

    def insertlink(self, linkVM):
        self.controller.insertLink(linkVM.link, 0)
        
    def insertPivote(self, linkVM):
        self.controller.insertLink(linkVM.link, 1)
    
    def recuperarTodosLink(self):
        return self.controller.recuperarTodosLink()
    
    def insertEgresadoInfo(self, EgresadoInfoVM):
        idlink = self.controller.recuperarIdLink(EgresadoInfoVM.link).id
        self.controller.insertEgresadoInfo(idlink, EgresadoInfoVM.nombre, EgresadoInfoVM.universidad, EgresadoInfoVM.carrera)
    
    def recuperarEgresadoInfoEstudios(self, universidad, carrera):
        return self.controller.recuperarEgresadoInfoEstudios(universidad, carrera)
    
    def insertExperiencia(self, Egresado,  ExperienciaVM):
        idlink = self.controller.recuperarIdLink(Egresado.link).id
        idEgresado = self.controller.recuperarEgresadoInfo(idlink, Egresado.nombre, Egresado.universidad, Egresado.carrera).id
        self.controller.insertExperiencia(idEgresado, ExperienciaVM.empresa, ExperienciaVM.puesto, ExperienciaVM.descripcion, ExperienciaVM.duracion, ExperienciaVM.fechaInicio, ExperienciaVM.fechaFin)
        
    def recuperarTodosExperiencia(self):
        return self.controller.recuperarTodosExperiencia()
    
    def insertEgresados(self, idEgresado, idExperiencia, Rol):
        self.controller.insertEgresados(idEgresado, idExperiencia, Rol)