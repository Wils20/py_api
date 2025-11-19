# apis/cliente_api.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas
import services.cliente_service as cliente_service
from database import get_db

router = APIRouter()

# Crear un cliente
@router.post("/clientes/", response_model=schemas.Cliente)
def create_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return cliente_service.create_cliente(db=db, cliente=cliente)

# Obtener todos los clientes
@router.get("/clientes/", response_model=list[schemas.Cliente])
def read_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clientes = cliente_service.get_clientes(db, skip=skip, limit=limit)
    return clientes

@router.get("/clientes/{cliente_id}", response_model=schemas.Cliente)
def read_cliente(cliente_id: int, db: Session = Depends(get_db)):
    db_cliente = cliente_service.get_cliente(db, cliente_id=cliente_id)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")
    return db_cliente

@router.put("/clientes/{cliente_id}", response_model=schemas.Cliente)
def update_cliente(cliente_id: int, cliente: schemas.ClienteUpdate, db: Session = Depends(get_db)):
    db_cliente = cliente_service.update_cliente(db, cliente_id, cliente)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")
    return db_cliente

@router.delete("/clientes/{cliente_id}", response_model=schemas.Cliente)
def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    db_cliente = cliente_service.delete_cliente(db, cliente_id)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")
    return db_cliente
