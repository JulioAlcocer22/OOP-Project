from sqlalchemy import select, and_
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
import sys
sys.path.append("./Connection")
from Connection import Connection
sys.path.append("./Model")
from Base import Base
from LinkEgresados import LinkEgresados
from EgresadoInfo import EgresadoInfo
from Experiencia import Experiencia
from Egresados import Egresados

class Querys():
    
    def __init__(self):
        self.Connection = Connection.Connection()
        
    def insertLink(self, link, pivote):
        if self.Connection.session != None:
            try:
                link = LinkEgresados(link, pivote)
                self.Connection.session.merge(link)
                self.Connection.session.commit()
            except IntegrityError as e:
                self.Connection.session.rollback()
            except SQLAlchemyError as e:
                self.Connection.session.rollback()
                print(e)
            finally:
                self.Connection.session.close()
        else:
            print("Sin conexion a la base de datos")
        
    def recuperarTodosLink(self):
        if self.Connection.session != None:
            try:
                link = self.Connection.session.query(LinkEgresados.link).all()
                return link
            except SQLAlchemyError as e:
                print(e)
                return []
            finally:
                self.Connection.session.close()
        else:
            print("Sin conexion a la base de datos")
            return []
    
    def recuperarIdLink(self, link):
        if self.Connection.session != None:
            try:
                link = self.Connection.session.query(LinkEgresados.id).filter(LinkEgresados.link == link).first()
                return link
            except SQLAlchemyError as e:
                print(e)
                return []
            finally:
                self.Connection.session.close()
        else:
            print("Sin conexion a la base de datos")
            return []       
        
    def recuperarPivotes(self):
        if self.Connection.session != None:
            try:
                link = self.Connection.session.query(LinkEgresados.link).filter(LinkEgresados.pivote == 1).all()
                return link
            except SQLAlchemyError as e:
                print(e)
                return []
            finally:
                self.Connection.session.close()
        else:
            print("Sin conexion a la base de datos")
            return []
    
    def insertEgresadoInfo(self, idLink, nombre, universidad, carrera):
        if self.Connection.session != None:
            try:
                egresadoInfo = EgresadoInfo(idLink, nombre, universidad, carrera)
                self.Connection.session.merge(egresadoInfo)
                self.Connection.session.commit()
            except IntegrityError as e:
                self.Connection.session.rollback()
            except SQLAlchemyError as e:
                self.Connection.session.rollback()
                print(e)
            finally:
                self.Connection.session.close()
        else:
            print("Sin conexion a la base de datos")
        
    def recuperarTodosEgresadoInfo(self):
        if self.Connection.session != None:
            try:
                egresadoInfo = self.Connection.session.query(EgresadoInfo).all()
                return egresadoInfo
            except SQLAlchemyError as e:
                print(e)
                return []
            finally:
                self.Connection.session.close()
        else:
            print("Sin conexion a la base de datos")
            return []
    
    def recuperarEgresadoInfo(self, idLink, nombre, universidad, carrera):
        if self.Connection.session != None:
            try:
                egresadoInfo = self.Connection.session.query(EgresadoInfo.id).filter(EgresadoInfo.idLink == idLink, EgresadoInfo.nombre == nombre, EgresadoInfo.universidad == universidad, EgresadoInfo.carrera == carrera).first()
                return egresadoInfo
            except SQLAlchemyError as e:
                print(e)
                return []
            finally:
                self.Connection.session.close()
        else:
            print("Sin conexion a la base de datos")
            return []
    
    def recuperarEgresadoInfoEstudios(self, universidad, carrera):
        if self.Connection.session != None:
            try:
                stmt = select(LinkEgresados.link, EgresadoInfo.nombre, EgresadoInfo.universidad, EgresadoInfo.carrera).where(and_(EgresadoInfo.universidad == universidad, EgresadoInfo.carrera == carrera)).join(EgresadoInfo)
                egresadoInfo = self.Connection.session.execute(stmt).fetchall()
                return egresadoInfo
            except SQLAlchemyError as e:
                print(e)
                return []
            finally:
                self.Connection.session.close()
        else:
            print("Sin conexion a la base de datos")
            return []
    
    def insertExperiencia(self, idEgresado, Empresa, Puesto, Descripcion, Duracion, FechaInicio, FechaFin):
        if self.Connection.session != None:
            try:
                experiencia = Experiencia(idEgresado, Empresa, Puesto, Descripcion, Duracion, FechaInicio, FechaFin)
                self.Connection.session.merge(experiencia)
                self.Connection.session.commit()
            except IntegrityError as e:
                self.Connection.session.rollback()    
            except SQLAlchemyError as e:
                self.Connection.session.rollback()
                print(e)
            finally:
                self.Connection.session.close()
        else:
            print("Sin conexion a la base de datos")
        
    def recuperarTodosExperiencia(self):
        if self.Connection.session != None:
            try:
                experiencia = self.Connection.session.query(Experiencia).all()
                return experiencia
            except SQLAlchemyError as e:
                print(e)
                return []
            finally:
                self.Connection.session.close()
        else:
            print("Sin conexion a la base de datos")
            return []
    
    def recuperarExperiencia(self, idEgresado, Empresa, Puesto, Descripcion, Duracion):
        if self.Connection.session != None:
            try:
                experiencia = self.Connection.session.query(Experiencia.id).filter(Experiencia.idEgresado == idEgresado, Experiencia.Empresa == Empresa, Experiencia.Puesto == Puesto, Experiencia.Descripcion == Descripcion, Experiencia.Duracion == Duracion).first()
                return experiencia
            except SQLAlchemyError as e:
                print(e)
                return []
            finally:
                self.Connection.session.close()
        else:
            print("Sin conexion a la base de datos")
            return []
    
    def insertEgresados(self, idEgresado, idExperiencia, Rol):
        if self.Connection.session != None:
            try:
                egresados = Egresados(idEgresado, idExperiencia, Rol)
                self.Connection.session.merge(egresados)
                self.Connection.session.commit()
            except IntegrityError as e:
                self.Connection.session.rollback()
            except SQLAlchemyError as e:
                self.Connection.session.rollback()
                print(e)
            finally:
                self.Connection.session.close()
        else:
            print("Sin conexion a la base de datos")
        
    def recuperarTodosEgresados(self):
        if self.Connection.session != None:
            try:
                egresados = self.Connection.session.query(Egresados).all()
                return egresados
            except SQLAlchemyError as e:
                print(e)
                return []
            finally:
                self.Connection.session.close()
        else:
            print("Sin conexion a la base de datos")
            return []
    
    def recuperarEgresados(self, idEgresado, idExperiencia, Rol):
        if self.Connection.session != None:
            try:
                stmt = select(LinkEgresados.link, EgresadoInfo.nombre, EgresadoInfo.universidad, EgresadoInfo.carrera, Experiencia.Empresa, Experiencia.Puesto, Experiencia.Descripcion, Experiencia.Duracion, Egresados.Rol).where(and_(EgresadoInfo.id == idEgresado, Experiencia.id == idExperiencia, Egresados.Rol == Rol)).join(EgresadoInfo, Egresados.idEgresado == EgresadoInfo.id).join(Experiencia, Egresados.idExperiencia == Experiencia.id)
                egresados = self.Connection.session.execute(stmt).fetchall()
                return egresados
            except SQLAlchemyError as e:
                print(e)
                return []
            finally:
                self.Connection.session.close()
        else:
            print("Sin conexion a la base de datos")
            return []
   