from sqlalchemy import Column, Integer, String, Date, Float, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .Base import Base

class Egresados(Base):
    __tablename__ = 'Egresados'
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    idEgresado = Column(Integer, ForeignKey('EgresadoInfo.id'))
    idExperiencia = Column(Integer, ForeignKey('Experiencia.id'))
    Rol = Column(String(255))
    
    UniqueConstraint('idEgresado', 'idExperiencia', name='uix_3')
    
    def __init__(self, idEgresado, idExperiencia, Rol):
        self.idEgresado = idEgresado
        self.idExperiencia = idExperiencia
        self.Rol = Rol
        
    def __repr__(self):
        return "<Egresados(idEgresado='%s', idExperiencia='%s', Rol='%s')>" % (self.idEgresado, self.idExperiencia, self.Rol)
    
    