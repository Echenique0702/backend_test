from pydantic import BaseModel, Field, field_validator
import re
from typing import Optional

class UsersModel(BaseModel):
    img: str = Field(..., description="Avatar Pic for user profile", example="https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    first_name: str = Field(..., description="User First Name", example="Steph")
    last_name: str = Field(..., description="User Last Name", example="Walters")
    phone: str = Field(..., description="Personal User Phone Number", example="(820) 289-1818")
    address: str = Field(..., description="Address Field for User Profile", example="5190 Center Court Drive")
    city: str = Field(..., description="City Field for User Profile", example="Spring")
    state: str = Field(..., description="State Field for User Profile", example="TX")
    zipcode: int = Field(..., description="Zip code Field for User Profile", gt=9999, lt=100000, example=77370)
    available: bool = Field(..., description='User Availability')


    @field_validator('phone')
    def validate_phone(cls, value):
        phone_pattern = re.compile(r'^\(\d{3}\) \d{3}-\d{4}$')
        if not phone_pattern.match(value):
            raise ValueError('Phone number must be in the format (XXX) XXX-XXXX')
        return value

    @field_validator('state')
    def validate_state(cls, value):
        state_pattern = re.compile(r'^[A-Z]{2}$')
        if not state_pattern.match(value):
            raise ValueError('State must be a two-letter uppercase code')
        return value


class UsersUpdateModel(BaseModel):
    img: Optional[str] = Field(None, description="Avatar Pic for user profile", example="https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    first_name: Optional[str] = Field(None, description="User First Name", example="Steph")
    last_name: Optional[str] = Field(None, description="User Last Name", example="Walters")
    phone: Optional[str] = Field(None, description="Personal User Phone Number", example="(820) 289-1818")
    address: Optional[str] = Field(None, description="Address Field for User Profile", example="5190 Center Court Drive")
    city: Optional[str] = Field(None, description="City Field for User Profile", example="Spring")
    state: Optional[str] = Field(None, description="State Field for User Profile", example="TX")
    zipcode: Optional[int] = Field(None, description="Zip code Field for User Profile", gt=9999, lt=100000, example=77370)
    available: Optional[bool] = Field(None, description='User Availability')

    # Configuración del modelo
    class Config:
        # Excluir campos que no fueron establecidos
        use_enum_values = True
        extra = "forbid"


    # Phone validator for appropiate syntax
    @field_validator('phone')
    def validate_phone(cls, value):
        phone_pattern = re.compile(r'^\(\d{3}\) \d{3}-\d{4}$')
        if not phone_pattern.match(value):
            raise ValueError('Phone number must be in the format (XXX) XXX-XXXX')
        return value

    @field_validator('state')
    def validate_state(cls, value):
        state_pattern = re.compile(r'^[A-Z]{2}$')
        if not state_pattern.match(value):
            raise ValueError('State must be a two-letter uppercase code')
        return value


    def dict(self, **kwargs):
        """ Override the default dict method to exclude unset fields """
        exclude_unset = kwargs.pop("exclude_unset", True)
        return super().dict(exclude_unset=exclude_unset, **kwargs)