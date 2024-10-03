from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, databases

router = APIRouter()


# Маршрут для создания пользователя
@router.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(databases.get_db)):
    # Проверка наличия пользователя с таким же email
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Создаем нового пользователя
    fake_hashed_password = user.password + "notsecure"
    db_user = models.User(name=user.name, email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Маршрут для получения всех пользователей
@router.get("/users/", response_model=list[schemas.UserResponse])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(databases.get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users
