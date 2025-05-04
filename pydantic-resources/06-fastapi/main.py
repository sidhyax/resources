from pydantic import BaseModel, EmailStr
from fastapi import FastAPI, Depends
from typing import Optional, List, Dict, Any


app = FastAPI()


class UserSignUp(BaseModel):
    name: str
    email: EmailStr
    password: str
    
class Settings(BaseModel):
    app_name: str = "My App"
    admin_email: EmailStr = "sidhya@gmail.com"
    
def get_settings() -> Settings:
    return Settings()

@app.post("/signup")
async def signup(user: UserSignUp):
    return {
        "message":f"{user.name} signed up successfully!"
    }
    
@app.get("/settings")
async def get_app_settings(settings: Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email
    }
