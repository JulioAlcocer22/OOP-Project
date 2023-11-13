from sqlalchemy import Column, Integer, String, Date, Float, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
import sys
sys.path.append("./Model")
from Base import Base

class Experiencia(Base):
    __tablename__ = 'Experiencia'
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    idEgresado = Column(Integer, ForeignKey('EgresadoInfo.id')) 
    Empresa = Column(String(255))
    Puesto = Column(String(255))
    Descripcion = Column(String(255))
    Duracion = Column(Integer)
    FechaInicio = Column(Date)
    FechaFin = Column(Date)
    
    idexp = relationship("Egresados", backref="Experiencia")
    
    UniqueConstraint('idEgresado', 'Empresa', 'Puesto', 'Descripcion', 'Duracion', name='uix_2')
    
    def __init__(self, idEgresado, Empresa, Puesto, Descripcion, Duracion, FechaInicio, FechaFin):
        self.idEgresado = idEgresado
        self.Empresa = Empresa
        self.Puesto = Puesto
        self.Descripcion = Descripcion
        self.Duracion = Duracion
        self.FechaInicio = FechaInicio
        self.FechaFin = FechaFin
        
    def __repr__(self):
        return "<Experiencia(idEgresado='%s', Empresa='%s', Puesto='%s', Descripcion='%s', Duracion='%s', FechaInicio='%s', FechaFin='%s')>" % (
                self.idEgresado, self.Empresa, self.Puesto, self.Descripcion, self.Duracion, self.FechaInicio, self.FechaFin)