from datetime import datetime, timedelta
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from api.models.app_config import get_app_config
from passlib.context import CryptContext
from pydantic import BaseModel
import bcrypt
from typing import Optional
from sqlalchemy.dialects.postgresql import BYTEA
from api.models.postgresql import engine
from sqlmodel import Field, Session, SQLModel, select, Relationship
from typing import List, Optional

cubox_be_config = get_app_config()

class Restaurant_type(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str
    # heroes: List["Restaurant"] = Relationship(back_populates="restaurant_type")

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

class Restaurant(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None)
    name: str
    address: str = Field(default="San Jose", unique=True)
    rest_type: int = Field(default=1, foreign_key="restaurant_type.id")
    # rest_types: Optional[Restaurant_type] = Relationship(back_populates="restaurant")

    def __init__(self, name: str, address: str, rest_type: int):
        self.name = name
        self.address = address
        self.rest_type = rest_type
