from fastapi import FastAPI, HTTPException, status
from database import create_db_and_tables, SessionDep
from models import MovieModel
from random import randint
from sqlmodel import select
from schemas import MovieSchema

app = FastAPI()

#? fastapi dev .\main.py

create_db_and_tables()

@app.post("/movies")
async def create_movie(movie_data: MovieSchema, database: SessionDep):
    print("Datos recibidos:", movie_data)
    movie = MovieModel(
        name = movie_data.name,
        year = movie_data.year,
        duration = movie_data.duration,
        director = movie_data.director,
        clasification = movie_data.clasification,
        gender = movie_data.gender
    )

    database.add(movie)
    database.commit()
    database.refresh(movie)
    print("Película creada:", movie)

    return movie

@app.get("/movies")
async def get_movies(database: SessionDep):
    statement = select(MovieModel)
    results = database.exec(statement)
    items = results.all()

    return items

@app.get("/movies/{movie_id}")
async def get_movie_by_id(movie_id: int, database: SessionDep):
    movie = database.get(MovieModel, movie_id)

    if not movie:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Pelicula no encontrado")

    return movie
 