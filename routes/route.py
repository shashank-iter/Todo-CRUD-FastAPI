from fastapi import APIRouter
from models.todos import TodoModel
from config.database import collection_name
from schema.schemas import todos_serializer, individual_serializer
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_todos():
    todos = collection_name.find()
    return todos_serializer(todos)

@router.post("/")
async def create_todos(todo: TodoModel):
    collection_name.insert_one(dict(todo))
    return {"message": "Todo created successfully"}
