from pydantic import BaseModel
from typing import Optional, List



class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
    
class User(BaseModel):
    username:str
    id:str
    address: Address
    
class Comments(BaseModel):
    user: User
    content:str
    likes:int = 0
    replies:Optional[List["Comments"]] = None
    
Comments.model_rebuild()

    
address = Address(
    street="123 Main St",
    city="Anytown",
    state="CA",
    zip_code="12345"
)

user = User(
    username="johndoe",
    id="123",
    address=address
)

comment = Comments(
    user=user,
    content="This is a comment.",
    likes=10,
    replies=[
        Comments(
            user=user,
            content="This is a reply.",
            likes=5
        )
    ]
)



    