from pydantic import BaseModel, field_validator,model_validator,computed_field


class User(BaseModel):
    username: str 
    
    
    @field_validator("username")
    def valifate_username(cls,v):
        if len(v)<3:
            raise ValueError("Username must be at least 3 characters long")
        return v
    
class SignUp(BaseModel):
    password:str
    confirm_password:str
    
    @model_validator(mode="after")
    def validate_password(cls,values):
        if values["password"] != values["confirm_password"]:
            raise ValueError("Password and confirm password do not match")
        return values
    
    
class Product(BaseModel):
    price:float
    quantity:int
    
    @computed_field
    @property
    def total_price(self)->float:
        return self.price * self.quantity
    