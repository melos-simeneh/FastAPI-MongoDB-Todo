from fastapi import APIRouter
from models.todos import Todo
from config.db import collection_name
from schemas.schemas import list_serial
from bson import ObjectId 

router =APIRouter()

# GET Request Method
@router.get("/")
async def get_todos():
    todos=list_serial(collection_name.find())
    return todos

#POST Request Method
@router.post("/")
async def post_todo(todo:Todo):
    collection_name.insert_one(dict(todo))

#PUT Request Method
@router.put("/{id}")
async def put_tdo(id:str,todo:Todo):
    collection_name.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(todo)})