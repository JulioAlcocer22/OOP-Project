from sqlalchemy import Column, Integer, String, Date, Float, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
import sys
sys.path.append("./Model")
from Base import Base

class EgresadoInfo(Base):
    __tablename__ = 'EgresadoInfo'
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    idLink = Column(Integer, ForeignKey('LinkEgresados.id'))
    nombre = Column(String(255))
    universidad = Column(String(255))
    carrera = Column(String(255))
    
    UniqueConstraint('idLink', 'nombre', 'universidad', 'carrera', name='uix_1')
    
    Experiencia = relationship("Experiencia", backref="EgresadoInfo")
    Egresados = relationship("Egresados", backref="EgresadoInfo")
    
    def __init__(self, idLink, nombre, universidad, carrera):
        self.idLink = idLink
        self.nombre = nombre
        self.universidad = universidad
        self.carrera = carrera
        
    def __repr__(self):
        return "<EgresadoInfo(idLink='%s', nombre='%s', universidad='%s', carrera='%s')>" % (self.idLink, self.nombre, self.universidad, self.carrera)