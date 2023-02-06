from fastapi import FastAPI
from api.controllers import restaurant_controller
from fastapi import FastAPI
import logging, uvicorn, asyncio
from api.models.app_config import get_app_config
from api.models.db_inserts import insert_test_data
from fastapi.middleware.cors import CORSMiddleware

practica_01 = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:3000",
    "http://0.0.0.0:3000",
    "http://frontend:3000",
]

practica_01.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

practica_01.include_router(restaurant_controller.router, prefix="/restaurant")

@practica_01.get("/ping", description="Check if the server is up and running.")
async def show_status():
    return {"message": "Pong"}


async def main():
    logging.basicConfig(format='%(asctime)s-%(process)d-%(levelname)s- %(message)s', level=logging.INFO)
    # Initializing PGSQL connection
    practica_01_config = get_app_config()
    # insert_test_data()

    config = uvicorn.Config("main:practica_01", port=practica_01_config["practica_01"]["port"], log_level="info", host=practica_01_config["practica_01"]["host"])
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())