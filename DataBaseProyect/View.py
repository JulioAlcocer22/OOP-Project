from Controller import LinkScrapperController
from linkVM import linkVM
from EgresadoInfoVM import EgresadoInfoVM
from ExperienciaVM import ExperienciaVM

class View:
    def __init__(self):
        self.controller = LinkScrapperController.LinkScrapperController()

    def recuperarPivotes(self):
        return self.controller.recuperarPivotes()    

    def insertlink(self, linkVM):
        self.controller.insertLink(linkVM.link, linkVM.pivote)
    
    def recuperarTodosLink(self):
        return self.controller.recuperarTodosLink()
    
    def insertEgresadoInfo(self, EgresadoInfoVM):
        idlink = self.controller.recuperarIdLink(EgresadoInfoVM.link).id
        self.controller.insertEgresadoInfo(idlink, EgresadoInfoVM.nombre, EgresadoInfoVM.universidad, EgresadoInfoVM.carrera)
    
    def recuperarEgresadoInfoEstudios(self, universidad, carrera):
        return self.controller.recuperarEgresadoInfoEstudios(universidad, carrera)
    
    def insertExperiencia(self, ExperienciaVM):
        idlink = self.controller.recuperarIdLink(ExperienciaVM.egresado.link).id
        idEgresado = self.controller.recuperarEgresadoInfo(idlink, ExperienciaVM.egresado.nombre, ExperienciaVM.egresadouniversidad, ExperienciaVM.egresado.carrera).id
        self.controller.insertExperiencia(idEgresado, ExperienciaVM.Empresa, ExperienciaVM.Puesto, ExperienciaVM.Descripcion, ExperienciaVM.Duracion)
        
    def recuperarTodosExperiencia(self):
        return self.controller.recuperarTodosExperiencia()
    
    def insertEgresados(self, idEgresado, idExperiencia, Rol):
        self.controller.insertEgresados(idEgresado, idExperiencia, Rol)
        
if __name__ == '__main__':
    view = View()
    
    # parte 1 recuperar pivotes
    
    pivotes = view.recuperarPivotes()
    
    print(pivotes)
    
    # parte 2 insertar link
    
    linkVM = linkVM("https://www.linkedin.com/in/edua-raiez-dddd/", 0)
    
    view.insertlink(linkVM)
    
    links = view.recuperarTodosLink()
    
    print(links)
    
    # parte 3 insertar informacion del egresado 
    
    EgresadoInfoVM = EgresadoInfoVM(links[1].link, "Eduardo Ramirez", "Universidad de Guadalajara", "Ingenieria en Computacion")
    
    view.insertEgresadoInfo(EgresadoInfoVM)
    
    # parte 4 recuperar informacion del egresado segun la universidad y carrera
    
    egresadosUDG = view.recuperarEgresadoInfoEstudios("Universidad de Guadalajara", "Ingenieria en Computacion")
    
    # parte 5 insertar experiencia del link visitado
    
    ExperienciaVM = ExperienciaVM(egresadosUDG[0], "IBM", "Desarrollador", "Desarrollador de Software", 12)
    
    view.insertExperiencia(ExperienciaVM)
    
    # parte 6 recuperar experiencia de todos los egresados
    
    experiencias = view.recuperarTodosExperiencia()
    
    # parte 7 insertar egresados
    
    view.insertEgresados(experiencias[0].idEgresado, experiencias[0].id, "Desarrollador")
    
    
    