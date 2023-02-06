from fastapi import Depends, APIRouter
from api.services.restaurant_service import get_all_restaurants, Restaurant
import api.services.restaurant_service as restaurant_service

router = APIRouter()


@router.get("/getAll/")
async def get_restaurants():
    rests = await restaurant_service.get_all_restaurants()
    return rests

@router.get("/getRestTypes/")
async def get_restaurants_types():
    types = await restaurant_service.get_rest_types()
    return types

@router.post("/add/")
async def add_user(new_rest: Restaurant):
    await restaurant_service.add_rest(new_rest)
    return {"message": "New restaurant saved successfully"}
