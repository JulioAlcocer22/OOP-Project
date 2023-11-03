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
    
    idexp = relationship("Egresados", backref="Experiencia")
    
    UniqueConstraint('idEgresado', 'Empresa', 'Puesto', 'Descripcion', 'Duracion', name='uix_2')
    
    def __init__(self, idEgresado, Empresa, Puesto, Descripcion, Duracion):
        self.idEgresado = idEgresado
        self.Empresa = Empresa
        self.Puesto = Puesto
        self.Descripcion = Descripcion
        self.Duracion = Duracion
        
    def __repr__(self):
        return "<Experiencia(idEgresado='%s', Empresa='%s', Puesto='%s', Descripcion='%s', Duracion='%s')>" % (self.idEgresado, self.Empresa, self.Puesto, self.Descripcion, self.Duracion)