from pydantic import BaseModel, Field
from bson import ObjectId


class FriendshipSchema(BaseModel):
    id: str = Field(..., description="The unique identifier Object's Id")
    first_user_id: str = Field(..., description="First User ID in a friendship")
    first_user_first_name: str = Field(..., description="First User First Name in a friendship")
    first_user_last_name: str = Field(..., description="First User Last Name in a friendship")
    second_user_id: str = Field(..., description="Second User ID in a friendship")
    second_user_first_name: str = Field(..., description="Second User FIrst Name in a friendship")
    second_user_last_name: str = Field(..., description="Second User Last Name in a friendship")
