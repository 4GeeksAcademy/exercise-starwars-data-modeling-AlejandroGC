import os
import sys
from sqlalchemy import Integer, String
from sqlalchemy.orm import declarative_base
from eralchemy2 import render_er
from sqlalchemy.orm import mapped_column

from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
Base = declarative_base()



class User(Base):
    __tablename__ = "user_table"

    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(20), nullable=False)
    name = mapped_column(String(50))
    last_name = mapped_column(String(50))
    email = mapped_column(String(100))
    password = mapped_column(String(20))
    sub_date = mapped_column(String(10))
    favourites = relationship(List["Favourites"])


class Characters(Base):
    __tablename__ = "characters_table"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(50), nullable=False)
    age = mapped_column(Integer)
    favourites = relationship(List["Favourites"])

class Planets(Base):
    __tablename__ = "planets_table"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(50), nullable=False)
    size = mapped_column(Integer)
    favourites = relationship(List["Favourites"])

class Favourites(Base):
    __tablename__ = "favourites_table"

    id = mapped_column(Integer, primary_key=True)
    planet_id = mapped_column(Integer, ForeignKey("planets_table.id"))
    character_id = mapped_column(Integer, ForeignKey("characters_table.id"))
    user_id = mapped_column(Integer, ForeignKey("user_table.id"))



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')