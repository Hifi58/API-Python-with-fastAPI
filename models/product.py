from sqlalchemy import Table, Column, Integer, Float, String, Boolean
from config.db import meta

products = Table(
    'products', meta,
    Column('pk_id', Integer,primary_key=True),
    Column('name', String(255)),
    Column('category', String(255)),
    Column('quantity', Float),
    Column('gencode', Integer),
    Column('fk_food_id', Integer),
    Column('fk_user_id', Integer),
)