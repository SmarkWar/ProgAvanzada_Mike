from fastapi import FastAPI, HTTPException, status
from database import create_db_and_tables, SessionDep
from user import UserModel
from random import randint
from sqlmodel import select
from schemas import UserSchema

app = FastAPI()

#? fastapi dev .\main.py

create_db_and_tables()

@app.post("/users")
async def create_user(user_data: UserSchema, database: SessionDep):
    user = UserModel(
        name = user_data.name,
        last_name = user_data.last_name,
        email = user_data.email,
        phone = user_data.phone
    )
    
    database.add(user)
    database.commit()
    database.refresh(user)
    
    return user

@app.get("/users")
async def get_users(database: SessionDep):
    statement = select(UserModel)
    results = database.exec(statement)
    items = results.all()
    return items

@app.get("/users/{user_id}")
async def get_user_by_id(user_id: int, database: SessionDep):
    user = database.get(UserModel, user_id)
    
    if not user:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Usuario no encontrado")
    
    return user

#! Crear tabla en la base de datos donde se puedan registrar peliculas, nombre, duracion, genero, etc.
#! Esto esto guardarlo en una tabla para consultar peliculas y poder cosultarlo por id