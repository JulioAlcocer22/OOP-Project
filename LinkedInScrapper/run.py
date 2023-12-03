from config import Configuration
from app import *
from app.Controller import AccionesBoton
from app.DataBase import Querys
from app.View import InterfazUsuario

class main():
    def __init__(self):
        config = Configuration()
        engine, session = config.create_database_engine()
        querys = Querys.Querys(session)
        controller = AccionesBoton.AccionesBoton(querys)
        interfaz = InterfazUsuario()
        interfaz.Mostrar()
    
if __name__ == '__main__':
    main()
    
    