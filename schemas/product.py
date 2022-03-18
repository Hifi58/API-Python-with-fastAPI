from pydantic import BaseModel

class Product(BaseModel):
    pk_id: int
    name: str
    category: str
    quantity: float
    gencore: int
    fk_food_id: int
    fk_user_id: int