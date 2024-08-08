from pydantic import BaseModel, Field


class NewObjectCreatedSchema(BaseModel):
    id: str = Field(..., description="The unique identifier Object's Id")