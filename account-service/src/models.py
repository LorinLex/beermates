from sqlalchemy import ARRAY, Column, String
from sqlmodel import Field, SQLModel


class Auth(SQLModel, table=True):
    id: int = Field(primary_key=True)
    tg_username: str


class Resume(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    age: int
    description: str
    images: list[str] = Field(default=None, sa_column=Column(ARRAY(String())))
