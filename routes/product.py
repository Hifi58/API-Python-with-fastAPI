from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User

product = APIRouter()

#getall
@product.get("/products")
async def get_products():
    return conn.execute(products.select()).fetchall()

#getbyid
@product.get("/product{pk_id}")
async def get_product(pk_id: int):
    return conn.execute(products.select().where(products.c.pk_id == pk_id)).fetchall()

#create
@product.post("/product")
async def add_product(product: product):
    conn.execute(products.insert().values(
        name= product.name,
        category= product.category,
        quantity= product.quantity
        gencode= product.gencode,
        fk_food_id= product.fk_food_id,
        fk_user_id= product.fk_user_id
    ))
    return conn.execute(products.select()).fetchall()

#edit
@product.put("/product{pk_id}")
async def update_product(pk_id: int, product:product):
    conn.execute(products.update().values(
        name= product.name,
        category= product.category,
        quantity= product.quantity
        gencode= product.gencode,
        fk_food_id= product.fk_food_id,
        fk_user_id= product.fk_user_id
    ).where(products.c.pk_id == pk_id))

    return conn.execute(products.select()).fetchall()

#delete
@product.delete("/product")
async def delete_product():
    conn.execute(products.delete().where(products.c.pk_id == pk_id))
    return conn.execute(products.select()).fetchall()