import uvicorn
from fastapi import FastAPI
from database import engine, Base
from app.routers import empresa as e, book as b, user as u, borrow as brw
from app.models import user, empresa, borrow, book

app = FastAPI()

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


@app.get("/")
def check_api():
    return {"response": "Api Online!"}


app.include_router(e.router)
app.include_router(b.router)
app.include_router(u.router)
app.include_router(brw.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
