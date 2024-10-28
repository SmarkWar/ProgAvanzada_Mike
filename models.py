
from sqlmodel import SQLModel, Field

class MovieModel(SQLModel, table = True):
    __tablename__ = "movies"
    
    id: int = Field(primary_key = True)
    name: str
    year: str
    duration: str
    director: str
    clasification: str
    gender: str
 