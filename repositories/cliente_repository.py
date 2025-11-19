from sqlalchemy.orm import Session
import models
import schemas

# Crear un nuevo cliente
def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente = models.Cliente(**cliente.dict())  # Convertir el esquema a modelo
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

# Obtener todos los clientes con paginación
def get_clientes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cliente).offset(skip).limit(limit).all()

# Obtener un cliente por ID
def get_cliente(db: Session, cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

# Actualizar un cliente
def update_cliente(db: Session, cliente_id: int, cliente: schemas.ClienteUpdate):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    if db_cliente:
        update_data = cliente.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_cliente, key, value)
        db.commit()
        db.refresh(db_cliente)
    return db_cliente

# Eliminar un cliente
def delete_cliente(db: Session, cliente_id: int):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    if db_cliente:
        db.delete(db_cliente)
        db.commit()
    return db_cliente
