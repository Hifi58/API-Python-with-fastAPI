from pydantic import BaseModel

class User(BaseModel):
    pk_id: int
    mail: str
    password: str
    premium: bool