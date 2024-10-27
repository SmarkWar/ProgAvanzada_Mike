from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    last_name: str
    email: str
    phone: str