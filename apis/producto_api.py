from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas
import services.producto_service as producto_service
from database import get_db

router = APIRouter()

@router.post("/productos/", response_model=schemas.Producto)
def create_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return producto_service.create_producto(db=db, producto=producto)

@router.get("/productos/", response_model=list[schemas.Producto])
def read_productos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    productos = producto_service.get_productos(db, skip=skip, limit=limit)
    return productos

@router.get("/productos/{producto_id}", response_model=schemas.Producto)
def read_producto(producto_id: int, db: Session = Depends(get_db)):
    db_producto = producto_service.get_producto(db, producto_id=producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    return db_producto

@router.put("/productos/{producto_id}", response_model=schemas.Producto)
def update_producto(producto_id: int, producto: schemas.ProductoUpdate, db: Session = Depends(get_db)):
    db_producto = producto_service.update_producto(db, producto_id, producto)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    return db_producto

@router.delete("/productos/{producto_id}", response_model=schemas.Producto)
def delete_producto(producto_id: int, db: Session = Depends(get_db)):
    db_producto = producto_service.delete_producto(db, producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    return db_producto
