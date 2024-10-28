
from pydantic import BaseModel

class MovieSchema(BaseModel):
    name: str
    year: str
    duration: str
    director: str
    clasification: str
    gender: str
 