from sqlalchemy import Column, Integer, String
from database import Base

class Producto(Base):
    __tablename__ = "producto"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    cantidad = Column(Integer)

from sqlalchemy import Column, Integer, String
from database import Base

class Cliente(Base):
    __tablename__ = "clientes"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True)
    direccion = Column(String) 

