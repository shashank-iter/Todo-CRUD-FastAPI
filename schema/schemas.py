def individual_serializer(todo) -> dict:
    return {
        'id': str(todo["_id"]),
        'name': todo["name"],
        'description': todo["description"],
        'status': todo["status"]
    }
    
def todos_serializer(todos) -> list:
    return [individual_serializer(todo) for todo in todos]

# Path: models/todos.model.py