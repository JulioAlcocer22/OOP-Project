from sqlalchemy import select, and_
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.Model.LinkEgresados import LinkEgresados
from app.Model.EgresadoInfo import EgresadoInfo
from app.Model.Experiencia import Experiencia
from app.Model.Egresados import Egresados

class Querys():
    
    def __init__(self, session):
        self.session = session
        
    def insertLink(self, link, pivote):
        if self.session != None:
            try:
                link = LinkEgresados(link, pivote, 0)
                self.session.merge(link)
                self.session.commit()
            except IntegrityError as e:
                self.session.rollback()
            except SQLAlchemyError as e:
                self.session.rollback()
                print(e)
            finally:
                self.session.close()
        else:
            print("Sin conexion a la base de datos")
        
    def recuperarTodosLink(self, limite):
        if self.session != None:
            try:
                link = self.session.query(LinkEgresados.link).limit(limite).all()
                return link
            except SQLAlchemyError as e:
                print(e)
                return []
            finally:
                self.session.close()
        else:
            print("Sin conexion a la base de datos")
            return []
    
    def recuperarIdLink(self, link):
        if self.session != None:
            try:
                link = self.session.query(LinkEgresados.id).filter(LinkEgresados.link == link).first()
                self.session.commit()
                return link
            except SQLAlchemyError as e:
                print(e)
                return []
            finally:
                self.session.close()
        else:
            print("Sin conexion a la base de datos")
            return []       
        
    def recuperarPivotes(self):
        if self.session != None:
            try:
                link = self.session.query(LinkEgresados.link).filter(LinkEgresados.pivote == 1).all()
                return link
            except SQLAlchemyError as e:
                print(e)
                return []
            finally:
                self.session.close()
        else:
            print("Sin conexion a la base de datos")
            return []
        
    def linkRevisado(self, link):
        if self.session != None:
            try:
                link = self.session.query(LinkEgresados).filter(LinkEgresados.link == link).first()
                link.revisado = 1
                self.session.commit()
            except SQLAlchemyError as e:
                self.session.rollback()
                print(e)
            finally:
                self.session.close()
        else:
            print("Sin conexion a la base de datos")    
    
    def insertEgresadoInfo(self, idLink, nombre, universidad, carrera):
        if self.session != None:
            try:
                egresadoInfo = EgresadoInfo(idLink, nombre, universidad, carrera)
                self.session.merge(egresadoInfo)
                self.session.commit()
            except IntegrityError as e:
                self.session.rollback()
            except SQLAlchemyError as e:
                self.session.rollback()
                print(e)
            finally:
                self.session.close()
        else:
            print("Sin conexion a la base de datos")
        
    def recuperarTodosEgresadoInfo(self):
        if self.session != None:
            try:
                egresadoInfo = self.session.query(EgresadoInfo).all()
                return egresadoInfo
            except SQLAlchemyError as e:
                print(e)
                return []
            finally:
                self.session.close()
        else:
            print("Sin conexion a la base de datos")
            return []
    
    def recuperarEgresadoInfo(self, idLink, universidad, carrera):
        if self.session != None:
            try:
                egresadoInfo = self.session.query(EgresadoInfo.id).filter(EgresadoInfo.idLink == idLink, EgresadoInfo.universidad == universidad, EgresadoInfo.carrera == carrera).first()
                return egresadoInfo
            except SQLAlchemyError as e:
                print(e)
                return []
            finally:
                self.session.close()
        else:
            print("Sin conexion a la base de datos")
            return []
    
    def recuperarEgresadoInfoEstudios(self, universidad, carrera):
        if self.session != None:
            try:
                stmt = select(LinkEgresados.link).where(and_(EgresadoInfo.universidad == universidad, EgresadoInfo.carrera == carrera)).join(EgresadoInfo)
                egresadoInfo = self.session.execute(stmt).fetchall()
                return egresadoInfo
            except SQLAlchemyError as e:
                print(e)
                return []
            finally:
                self.session.close()
        else:
            print("Sin conexion a la base de datos")
            return []
    
    def insertExperiencia(self, idEgresado, Empresa, Puesto, Descripcion, Duracion, FechaInicio, FechaFin):
        if self.session != None:
            try:
                experiencia = Experiencia(idEgresado, Empresa, Puesto, Descripcion, Duracion, FechaInicio, FechaFin)
                self.session.merge(experiencia)
                self.session.commit()
            except IntegrityError as e:
                self.session.rollback()    
            except SQLAlchemyError as e:
                self.session.rollback()
                print(e)
            finally:
                self.session.close()
        else:
            print("Sin conexion a la base de datos")
        
    def recuperarTodosExperiencia(self):
        if self.session != None:
            try:
                experiencia = self.session.query(Experiencia).all()
                return experiencia
            except SQLAlchemyError as e:
                print(e)
                return []
            finally:
                self.session.close()
        else:
            print("Sin conexion a la base de datos")
            return []
    
    def recuperarExperiencia(self, idEgresado, Empresa, Puesto):
        if self.session != None:
            try:
                experiencia = self.session.query(Experiencia.id).filter(Experiencia.idEgresado == idEgresado, Experiencia.Empresa == Empresa, Experiencia.Puesto == Puesto).first()
                return experiencia
            except SQLAlchemyError as e:
                print(e)
                return []
            finally:
                self.session.close()
        else:
            print("Sin conexion a la base de datos")
            return []
    
    def insertEgresados(self, idEgresado, idExperiencia, Rol):
        if self.session != None:
            try:
                egresados = Egresados(idEgresado, idExperiencia, Rol)
                self.session.merge(egresados)
                self.session.commit()
            except IntegrityError as e:
                self.session.rollback()
            except SQLAlchemyError as e:
                self.session.rollback()
                print(e)
            finally:
                self.session.close()
        else:
            print("Sin conexion a la base de datos")
        
    def recuperarTodosEgresados(self):
        if self.session != None:
            try:
                egresados = self.session.query(Egresados).all()
                return egresados
            except SQLAlchemyError as e:
                print(e)
                return []
            finally:
                self.session.close()
        else:
            print("Sin conexion a la base de datos")
            return []
    
    def recuperarEgresados(self, idEgresado, idExperiencia):
        if self.session != None:
            try:
                stmt = select(LinkEgresados.link, EgresadoInfo.nombre, EgresadoInfo.universidad, EgresadoInfo.carrera, Experiencia.Empresa, Experiencia.Puesto, Experiencia.Descripcion, Experiencia.Duracion, Egresados.Rol).where(and_(EgresadoInfo.id == idEgresado, Experiencia.id == idExperiencia)).join(EgresadoInfo, Egresados.idEgresado == EgresadoInfo.id).join(Experiencia, Egresados.idExperiencia == Experiencia.id)
                egresados = self.session.execute(stmt).fetchall()
                return egresados
            except SQLAlchemyError as e:
                print(e)
                return []
            finally:
                self.session.close()
        else:
            print("Sin conexion a la base de datos")
            return []
   