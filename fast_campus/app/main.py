from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles

from sqlalchemy.orm import Session


from . import models, schemas
# ImportError: attempted relative import with no known parent package Error 발생
# python -m app.main 으로 터미널 환경에서 실행 

from .database import SessionLocal, engine

import uvicorn
models.Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existed_user = db.query(models.User).filter_by(
        email=user.email
    ).first()

    if existed_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = models.User(email=user.email, password=user.password)
    db.add(user)
    db.commit()

    return user


@app.get("/users", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}


if __name__ == "__main__":
    uvicorn.run(
    "app.main:app",
    host="localhost",
    port=8000,
    reload=True,
    # reload_excludes=["app/files/"],
    )