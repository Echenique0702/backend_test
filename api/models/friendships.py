from pydantic import BaseModel, Field, field_validator
from bson import ObjectId, errors

class FriendshipModel(BaseModel):
    first_user_id: str = Field(..., description="First User ID in a friendship", example=str(ObjectId()))
    second_user_id: str = Field(..., description="Second User ID in a friendship", example=str(ObjectId()))
   
    
    @field_validator("first_user_id", "second_user_id")
    def validate_objectid(cls, value, field):
        if value:
            try:
                ObjectId(value)
            except errors.InvalidId:
                raise ValueError(f"Invalid ObjectId format for {field.name}")
        return value