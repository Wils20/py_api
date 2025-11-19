from pydantic import BaseModel
from typing import Optional

class ProductoBase(BaseModel):
    nombre: Optional[str] = None
    cantidad: Optional[int] = None

class ProductoCreate(ProductoBase):
    nombre: str
    cantidad: int

class ProductoUpdate(ProductoBase):
    pass

class Producto(ProductoBase):
    id: int

    class Config:
        orm_mode = True


class ClienteBase(BaseModel):
    nombre: Optional[str] = None
    direccion: Optional[str] = None

class ClienteCreate(ClienteBase):
    nombre: str
    direccion: str

class ClienteUpdate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int

    class Config:
        orm_mode = True
