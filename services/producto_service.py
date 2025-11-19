from sqlalchemy.orm import Session
from models import Producto
import schemas

def get_productos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Producto).offset(skip).limit(limit).all()

def get_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def create_producto(db: Session, producto: schemas.ProductoCreate):
    db_producto = Producto(**producto.dict()) 
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def update_producto(db: Session, producto_id: int, producto: schemas.ProductoUpdate):
    db_producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if db_producto:
        for key, value in producto.dict(exclude_unset=True).items():
            setattr(db_producto, key, value)
        db.commit()
        db.refresh(db_producto)
        return db_producto
    return None

def delete_producto(db: Session, producto_id: int):
    db_producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if db_producto:
        db.delete(db_producto)
        db.commit()
        return db_producto
    return None
