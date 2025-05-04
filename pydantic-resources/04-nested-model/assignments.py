# TODO: Create Course model with fields:
# - course_id (Integer)
# - Course hass modules
# - Module has lessons

from pydantic import BaseModel
from typing import List, Optional

class Lesson(BaseModel):
    id:str
    title:str
    content:str
    duration:int
    
class Module(BaseModel):
    id:str
    title:str
    lessons:List[Lesson]

class Course(BaseModel):
    id:str
    title:str
    description:str
    modules:List[Module]
    


    
    
    

