from fastapi import APIRouter
from config.db import connection
from models.index import users
from schemas.index import User

user = APIRouter

#getall
@user.get("/users")
async def get_users():
    return connection.execute(users.select()).fetchall()

#getbyid
@user.get("/user{pk_id}")
async def get_user(pk_id: int):
    return connection.execute(users.select().where(users.c.pk_id == pk_id)).fetchall()

#create
@user.post("/users")
async def add_user(user: User):
    connection.execute(users.insert().values(
        mail= user.mail,
        password= user.password,
        premium= user.premium
    ))
    return connection.execute(users.select()).fetchall()

#edit
@user.put("/user{pk_id}")
async def update_user(pk_id: int, user:User):
    connection.execute(users.update().values(
        mail= user.mail,
        password= user.password,
        premium= user.premium
    ).where(users.c.pk_id == pk_id))

    return connection.execute(users.select()).fetchall()

#delete
@user.delete("/users")
async def delete_user():
    connection.execute(users.delete().where(users.c.pk_id == pk_id))
    return connection.execute(users.select()).fetchall()