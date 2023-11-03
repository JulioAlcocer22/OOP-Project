from sqlalchemy import Column, Integer, String, Date, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
import sys
sys.path.append("./Model")
from Base import Base

class LinkEgresados(Base):
    __tablename__ = 'LinkEgresados'
    
    id = Column(Integer, autoincrement=True, primary_key=True) 
    link = Column(String(255), unique=True)
    pivote = Column(Boolean, default=False)
    
    EgresadoInfo = relationship("EgresadoInfo", backref="LinkEgresados")

    
    def __init__(self, link, pivote):
        self.link = link
        self.pivote = pivote
    
    def __repr__(self):
        return "<LinkEgresados(link='%s', pivote='%s')>" % (self.link, self.pivote)
