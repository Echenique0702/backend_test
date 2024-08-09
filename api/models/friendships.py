from pydantic import BaseModel, Field, validator
from bson import ObjectId, errors

class FriendshipModel(BaseModel):
    first_user_id: str = Field(..., description="First User ID in a friendship", example=str(ObjectId()))
    second_user_id: str = Field(..., description="Second User ID in a friendship", example=str(ObjectId()))

    @validator("first_user_id", "second_user_id", pre=True, always=True)
    def validate_objectid(cls, value):
        if value:
            try:
                ObjectId(value)
            except errors.InvalidId:
                raise ValueError("Invalid ObjectId format")
        return value