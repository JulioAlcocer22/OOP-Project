from config import Configuration
from app.Controller import Controller
from app.DataBase import Querys
import test

def main():
    config = Configuration()
    engine, session = config.create_database_engine()
    querys = Querys.Querys(session)
    controller = Controller.Controller(querys)

    
if __name__ == '__main__':
    main()
    
    