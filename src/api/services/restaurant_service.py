from fastapi import Depends, HTTPException, status
from api.models.restaurant import Restaurant, Restaurant_type
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlmodel import Session
from api.models.postgresql import engine
from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, select

async def add_rest(restaurant: Restaurant):
    
    new_rest = Restaurant(restaurant.name, restaurant.address, restaurant.rest_type)
    session = Session(engine)
    # 5 - persists data
    session.add(new_rest)
    print(new_rest)

    # 6 - commit and close session
    session.commit()
    session.close()

async def get_all_restaurants():
    with Session(engine) as session:
        statement = select(Restaurant, Restaurant_type).join(Restaurant_type)
        rests = session.exec(statement).all()
        session.close()
        res: list = []

        for restaurant, rest_type in rests:
            res.append({"id": restaurant.id, "name": restaurant.name, "address": restaurant.address, "rest_type": rest_type.name})

        return res

async def get_rest_types():
    with Session(engine) as session:
        statement = select(Restaurant_type)
        rest_types = session.exec(statement).all()
        session.close()

        return rest_types