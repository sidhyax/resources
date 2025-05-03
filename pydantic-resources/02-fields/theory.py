from pydantic import BaseModel
from typing import Optional, List, Dict

class Cart(BaseModel):
    user_id:str 
    items: List[str]
    quantities: Dict[str, int]
    
class BlogPost(BaseModel):
    title: str
    content: str
    img_url: Optional[str] = None