from fastapi import FastAPI
from apis import producto_api, cliente_api  
from database import engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(producto_api.router)

app.include_router(cliente_api.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
