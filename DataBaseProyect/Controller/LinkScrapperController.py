from sqlalchemy import select, and_
import sys
sys.path.append("./DataBase")
from Connection import Connection
sys.path.append("./Model")
from Base import Base
from LinkEgresados import LinkEgresados
from EgresadoInfo import EgresadoInfo
from Experiencia import Experiencia
from Egresados import Egresados

class LinkScrapperController():
    
    def insertLink(self, link, pivote):
        link = LinkEgresados(link, pivote)
        Connection.session.add(link)
        Connection.session.commit()
        Connection.session.close()
        
    def recuperarTodosLink(self):
        link = Connection.session.query(LinkEgresados.link).all()
        Connection.session.close()
        return link
    
    def recuperarIdLink(self, link):
        link = Connection.session.query(LinkEgresados.id).filter(LinkEgresados.link == link).first()
        Connection.session.close()
        return link
    
    def recuperarPivotes(self):
        try:
            link = Connection.session.query(LinkEgresados.link).filter(LinkEgresados.pivote == 1).all()
            return link
        except Exception as e:
            print(e)
            return []
        finally:
            Connection.session.close()
    
    def insertEgresadoInfo(self, idLink, nombre, universidad, carrera):
        egresadoInfo = EgresadoInfo(idLink, nombre, universidad, carrera)
        Connection.session.add(egresadoInfo)
        Connection.session.commit()
        Connection.session.close()
        
    def recuperarTodosEgresadoInfo(self):
        egresadoInfo = Connection.session.query(EgresadoInfo).all()
        Connection.session.close()
        return egresadoInfo
    
    def recuperarEgresadoInfo(self, idLink, nombre, universidad, carrera):
        egresadoInfo = Connection.session.query(EgresadoInfo.id).filter(EgresadoInfo.idLink == idLink, EgresadoInfo.nombre == nombre, EgresadoInfo.universidad == universidad, EgresadoInfo.carrera == carrera).first()
        Connection.session.close()
        return egresadoInfo
    
    def recuperarEgresadoInfoEstudios(self, universidad, carrera):
        stmt = select(LinkEgresados.link, EgresadoInfo.nombre, EgresadoInfo.universidad, EgresadoInfo.carrera).where(and_(EgresadoInfo.universidad == universidad, EgresadoInfo.carrera == carrera)).join(EgresadoInfo)
        egresadoInfo = Connection.session.execute(stmt).fetchall()
        Connection.session.close()
        return egresadoInfo
    
    def insertExperiencia(self, idEgresado, Empresa, Puesto, Descripcion, Duracion):
        experiencia = Experiencia(idEgresado, Empresa, Puesto, Descripcion, Duracion)
        Connection.session.add(experiencia)
        Connection.session.commit()
        Connection.session.close()
        
    def recuperarTodosExperiencia(self):
        experiencia = Connection.session.query(Experiencia).all()
        Connection.session.close()
        return experiencia
    
    def recuperarExperiencia(self, idEgresado, Empresa, Puesto, Descripcion, Duracion):
        experiencia = Connection.session.query(Experiencia.id).filter(Experiencia.idEgresado == idEgresado, Experiencia.Empresa == Empresa, Experiencia.Puesto == Puesto, Experiencia.Descripcion == Descripcion, Experiencia.Duracion == Duracion).first()
        Connection.session.close()
        return experiencia
    
    def insertEgresados(self, idEgresado, idExperiencia, Rol):
        egresados = Egresados(idEgresado, idExperiencia, Rol)
        Connection.session.add(egresados)
        Connection.session.commit()
        Connection.session.close()
        
    def recuperarTodosEgresados(self):
        egresados = Connection.session.query(Egresados).all()
        Connection.session.close()
        return egresados
    
    def recuperarEgresados(self, idEgresado, idExperiencia, Rol):
        egresados = Connection.session.query(Egresados.id).filter(Egresados.idEgresado == idEgresado, Egresados.idExperiencia == idExperiencia, Egresados.Rol == Rol).first()
        Connection.session.close()
        return egresados
    
   