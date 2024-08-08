from pydantic import BaseModel, Field


class UsersSchema(BaseModel):
    id: str = Field(..., description="User ID")
    img: str = Field(..., description="Avatar Pic for user profile" )
    first_name: str = Field(..., description="User First Name")
    last_name: str = Field(..., description="User Last Name")
    phone: str = Field(..., description="Personal User Phone Number")
    address: str = Field(..., description="Address FIeld for User Profile")
    city: str = Field(..., description="City Field for User Profile")
    state: str = Field(..., description="State Field for User Profile")
    zipcode: int = Field(..., description="Zip code Field for User Profile", gt=9999, lt=100000)
    available: bool = Field(..., description='User Availability')


class BasicUserSchema(BaseModel):
    id: str = Field(..., description="User ID")
    first_name: str = Field(..., description="User First Name")
    last_name: str = Field(..., description="User Last Name")
