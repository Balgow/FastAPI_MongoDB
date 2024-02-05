from fastapi import FastAPI
from .databases import DATABASE_URL, collection_name, client
import asyncio
from .schemas import list_of_persons
from .models import Person
from bson import ObjectId

app = FastAPI()



@app.get("/")
async def home():
    return list_of_persons(collection_name.find({},{'_id': 0}))

@app.post("/add")
async def add_person(person: Person):
    collection_name.insert_one(person.dict())
    return person.dict()