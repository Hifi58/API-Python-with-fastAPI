from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User

user = APIRouter

#getall
@user.get("/users")
async def get_users():
    return conn.execute(users.select()).fetchall()

#getbyid
@user.get("/users{pk_id}")
async def get_user(pk_id: int):
    return conn.execute(users.select().where(users.c.pk_id == pk_id)).fetchall()

#create
@user.post("/users")
async def add_user(user: User):
    conn.execute(users.insert().values(
        mail= user.mail,
        password= user.password,
        premium= user.premium
    ))
    return conn.execute(users.select()).fetchall()

#edit
@user.put("/users{pk_id}")
async def update_user(pk_id: int, user:User):
    conn.execute(users.update().values(
        mail= user.mail,
        password= user.password,
        premium= user.premium
    ).where(users.c.pk_id == pk_id))

    return conn.execute(users.select()).fetchall()

#delete
@user.delete("/users")
async def delete_user():
    conn.execute(users.delete().where(users.c.pk_id == pk_id))
    return conn.execute(users.select()).fetchall()