# TODO: Create Employee model with fields:
# - id (Integer)
# - name str (min 3 char)
# - department Optional str default "General"
# - salary float (must be >= 1000.0)


from pydantic import BaseModel, Field

from typing import Optional


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        description="Name of the employee, must be at least 3 characters long.",
        examples="John Doe",
    )
    department: Optional[str] = "General"
    salary:float = Field(
        ...,
        ge=1000.0,
        description="Salary of the employee, must be greater than or equal to 1000.0.",
        examples=1500.0,
    )