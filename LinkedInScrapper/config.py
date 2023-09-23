from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import environ

class Configuration():
    
    def __init__ (self):
        env = environ.Env(DEGUBUG=(bool, False))
        environ.Env.read_env()
        DEBUG = env('DEBUG')
        self.username = env('DB_USERNAME')
        self.password = env('DB_PASSWORD')
        self.database = env('DB_DATABASE')
        self.server = env('DB_SERVER')
        
    
    def get_database_url(self): 
        return ('mssql+pyodbc://'+self.username+':'+self.password+'@'+self.server+'/'+self.database+'?driver=ODBC+Driver+17+for+SQL+Server')
    
    def create_database_engine(self):
        try:
            engine = create_engine(self.get_database_url())
            Session = sessionmaker(engine)
            session = Session()
            return engine, session
        except SQLAlchemyError as e:
            print(e)
            return None, None