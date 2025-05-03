from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool = True
    age: int = 0
    
input_data = {
    "id": 1,
    "name": "John Doe",
    "is_active": True,
    "age": 30
}

user = User(**input_data)
print(user.model_dump_json())