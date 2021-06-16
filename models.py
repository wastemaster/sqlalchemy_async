import sqlalchemy
from db import db, metadata, sqlalchemy


users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("age", sqlalchemy.Integer),
)


class User:
    @classmethod
    async def error(cls):
        query = "SELECT wrong_field FROM public.users"
        result = await db.fetch_all(query)
        return result

    @classmethod
    async def raw(cls):
        query = "SELECT * FROM public.users"
        result = await db.fetch_all(query)
        return result

    @classmethod
    async def all(cls):
        query = users.select()
        user_list = await db.fetch_all(query)
        return user_list

    @classmethod
    async def get(cls, id):
        query = users.select().where(users.c.id == id)
        user = await db.fetch_one(query)
        return user

    @classmethod
    async def create(cls, **user):
        query = users.insert().values(**user)
        user_id = await db.execute(query)
        return user_id
