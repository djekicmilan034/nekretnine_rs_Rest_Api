from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
import psycopg2

#-----------------------------------Creating table:-----------------------------
engine=create_engine('postgresql://postgres:root@localhost:5432/demo',echo=False) #Konekcija sa bazom "demo"
Session=sessionmaker(bind=engine)
session=Session()
Base=declarative_base()


class Oglas(Base):
    __tablename__='neks' #kreiranje tabele 'neks'

    id=Column(Integer,primary_key=True) #kreiranje kolona pocev od id do naselja u kom se nekretnina nalazi.
    transakcija=Column(String(50))
    vrsta = Column(String(50))
    cenaNek = Column(Float)
    kvadratura = Column(Float)
    grad = Column(String(50))
    naselje = Column(String(50))

#Provera da li postoji konekcija sa bazom demo, sto znaci da je pre pokretanja programa potrebno napraviti bazu demo u pgAdmin-u.
try:
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="demo")
    print("Connection established")
except (Exception, psycopg2.Error) as error:
    print("Connection not established", error)

#Provera da li postoji tabela 'neks' u bazi demo.
cursor = connection.cursor()
cursor.execute(f"SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name='neks')")
if bool(cursor.fetchone()[0]):
    print(f'Table neks exists.')
#Ukoliko ne postoji tabela 'neks' u bazi, program ce je kreirati.
else:
    print(f'Table neks does not exist. Creating the Table neks now.')
    Base.metadata.create_all(engine)

