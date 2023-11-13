from Controller import DBController
from ExperienciaVM import ExperienciaVM
from EgresadoInfoVM import EgresadoInfoVM
from linkVM import linkVM

if __name__ == '__main__':
    view = DBController.DBController()
    
    # parte 1 recuperar pivotes
    
    pivotes = view.recuperarPivotes()
    
    # parte 2 insertar link
    
    linkVM = linkVM("https://www.linkedin.com/in/Julio-Alcocer/", 0)
    
    view.insertlink(linkVM)
    
    links = view.recuperarTodosLink()
    
    # parte 3 insertar informacion del egresado 
    
    EgresadoInfoVM = EgresadoInfoVM(links[0].link, "Julio Alcocer", "FMAT", "LIS")
    
    view.insertEgresadoInfo(EgresadoInfoVM)
    
    # parte 4 recuperar informacion del egresado segun la universidad y carrera
    
    egresados = view.recuperarEgresadoInfoEstudios("FMAT", "LIS")
    
    # parte 5 insertar experiencia del link visitado
    
    ExperienciaVM = ExperienciaVM("Google", "Analista", "Desarrollador de Software", 5, "2015-01-01", "2016-01-01")
    
    view.insertExperiencia(egresados[0], ExperienciaVM)
    
    # parte 6 recuperar experiencia de todos los egresados
    
    experiencias = view.recuperarTodosExperiencia()
    
    # parte 7 insertar egresados
    
    view.insertEgresados(experiencias[0].idEgresado, experiencias[0].id, "Analista")