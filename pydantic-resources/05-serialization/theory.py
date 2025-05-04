from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime



class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
    
class User(BaseModel):
    id: str
    name: str
    email: str
    address: Address
    created_at: datetime
    updated_at: Optional[datetime] = None
    tags:List[str] = []
    is_active: bool = True
    
    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v:v.strftime("%d-%m-%Y %H:%M:%S"),
        }
    )
        
    
    
user = User(
    id="12345",
    name="John Doe",
    email="x@gmail.com",
    address=Address(
        street="123 Main St",
        city="Anytown",
        state="CA",
        zip_code="12345"
    ),
    tags=["admin", "user"],
    is_active=True,
    created_at=datetime(2024, 3, 15, 14, 30),
    
)

# py_dict = user.model_dump()
py_dict = user.model_dump_json()
print(py_dict)