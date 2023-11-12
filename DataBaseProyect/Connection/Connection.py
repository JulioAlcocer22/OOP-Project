from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import environ

class Connection():
    
    
    env = environ.Env(DEGUBUG=(bool, False))
    environ.Env.read_env()
    DEBUG = env('DEBUG')
    username = env('DB_USERNAME')
    password = env('DB_PASSWORD')
    database = env('DB_DATABASE')
    server = env('DB_SERVER')
    url = 'mssql+pyodbc://'+username+':'+password+'@'+server+'/'+database+'?driver=ODBC+Driver+17+for+SQL+Server'
    
    try:
        engine = create_engine(url)
        Session = sessionmaker(engine)
        session = Session()
    except SQLAlchemyError as e:
        print(e)