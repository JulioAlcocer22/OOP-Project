from sqlalchemy import Column, Integer, String, Date, Float, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .LinkEgresados import LinkEgresados
from .Base import Base

class EgresadoInfo(Base):
    __tablename__ = 'EgresadoInfo'
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    idLink = Column(Integer, ForeignKey('LinkEgresados.id'))
    nombre = Column(String(255))
    universidad = Column(String(255))
    carrera = Column(String(255))
    revisado = Column(Boolean, default=False)
    
    UniqueConstraint('idLink', 'universidad', 'carrera', name='uix_1')
    
    Experiencia = relationship("Experiencia", backref="EgresadoInfo")
    Egresados = relationship("Egresados", backref="EgresadoInfo")
    
    def __init__(self, idlink, nombre, universidad, carrera, revisado=False):
        self.idLink = idlink
        self.nombre = nombre
        self.universidad = universidad
        self.carrera = carrera
        self.revisado = revisado
        
    def __repr__(self):
        return "<EgresadoInfo(idLink='%s', nombre='%s', universidad='%s', carrera='%s')>" % (self.idLink, self.nombre, self.universidad, self.carrera)