import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base # declarative_base sirve para manipular todas las tablas de la base de datos

sqlite_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__)) # Para leer el directorio actual del archivo

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}" # Para conectar y crear la url d ela base de datos

engine = create_engine(database_url, echo=True) # Engine para el motor de la base de datos

Session = sessionmaker(bind=engine) # Estamos creando la sesion y enlazandola al motor de la base de datos

Base = declarative_base()