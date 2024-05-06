from pydantic import BaseModel

class TodoModel(BaseModel):
    name: str
    description: str
    status: bool
    created_by: str
    