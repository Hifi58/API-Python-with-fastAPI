from sqlalchemy import Table, Column, Integer, String, Boolean
from config.db import meta

users = Table(
    'users', meta,
    Column('pk_id', Integer,primary_key=True),
    Column('mail', String(255)),
    Column('password', String(255)),
    Column('premium', Boolean, default=False),
)