from config import Configuration
from app.Controller import Controller
from app.DataBase import Querys
from app.View.InterfazUsuario import InterfazUsuario


class main():
    def __init__(self):
        config = Configuration()
        engine, session = config.create_database_engine()
        querys = Querys.Querys(session)
        controller = Controller.Controller(querys)
        interfaz = InterfazUsuario()
        interfaz.Mostrar()
    
if __name__ == '__main__':
    main()
    
    