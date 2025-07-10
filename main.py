import uvicorn
from fastapi import FastAPI
from database import engine, Base
from app.routers import empresa
from contextlib import asynccontextmanager

# Lifespan substitui os eventos 'startup' e 'shutdown'
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Executa ao iniciar a aplicação
    Base.metadata.create_all(bind=engine)
    yield
    # Aqui você pode colocar ações ao finalizar (opcional)

app = FastAPI(lifespan=lifespan)

@app.get("/")
def check_api():
    return {"response": "Api Online!"}

app.include_router(empresa.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
