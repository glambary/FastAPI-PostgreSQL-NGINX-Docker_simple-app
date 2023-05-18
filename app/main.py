'this branch in test'

import databases
from fastapi import FastAPI
from fastapi.routing import APIRoute, APIRouter

from src.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from src.model import person_table
from src.schema import Person


app = FastAPI()

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
database = databases.Database(DATABASE_URL)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


async def main_page():
    return {"message": "Hello! You are on the main page."}


async def get_records():
    query = person_table.select()
    return await database.fetch_all(query)


async def create_record(person: Person):
    query = person_table.insert().values(
        first_name=person.first_name,
        last_name=person.last_name,
        date_of_birth=person.date_of_birth,
    )
    last_record_id = await database.execute(query)
    return {**person.dict(), "id": last_record_id}


routes = [
    APIRoute(path="/", endpoint=main_page, methods=["GET"]),
    APIRoute(path="/create", endpoint=create_record, methods=["POST"]),
    APIRoute(path="/get", endpoint=get_records, methods=["GET"]),
]


app.include_router(APIRouter(routes=routes))


'''
if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="localhost", port=7000)
'''
