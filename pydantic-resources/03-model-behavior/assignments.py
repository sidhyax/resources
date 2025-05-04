# TODO: Create Booking model with fields:
# - user_id (Integer)
# - hotel_id (Integer)
# - nights: int (must be > 1)
# - rate per night: float 

# also add computed field total_cost (nights * rate per night)


from pydantic import BaseModel, Field, computed_field

class Booking(BaseModel):
    user_id:int
    hotel_id:int
    nights:int = Field(
        ...,
        gt=1,
        description="Number of nights, must be greater than 1.",
    )
    rate_per_night:float
    
    
    @computed_field
    @property
    def total_cost(self)->float:
        return self.nights * self.rate_per_night
