from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder

# Schemas
from schemas.base import NewObjectCreatedSchema
from schemas.users import (
    BasicUserSchema,
    UsersSchema
)

# Models
from models.users import (
    UsersModel,
    UsersUpdateModel
) 

# Database
from database.users import UsersDB

from typing import List

# Initial Settings Variables
router = APIRouter()
user_db =UsersDB() 


# Endpoints Declarations
# Create a new User
@router.post(
    '',
    description="Create an User in DB",
    response_model=NewObjectCreatedSchema,
    response_description="The unique identifier for new user"
)
async def create_user(data: UsersModel = Body(...)):
    data = jsonable_encoder(data)
    try:
        new_user = await user_db.create(
            data = data
        )
        return new_user
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))


# Get all Users
@router.get(
    '',
    response_model=List[BasicUserSchema],
    description="Get basic information for all users in DB",
    response_description="A list with all documents in Users collection"
)
async def get_all_users():
    try:
        all_users = await user_db.get_all()
        return all_users
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error))


# Get user by ID
@router.get(
    '/{id}',
    response_model=UsersSchema,
    description='Get detailed information About a specific user',
    response_description='User Object in DB'
)
async def get_user_by_id(id: str):
    try:
        user = await user_db.get_by_id(
            object_id=id
        )
        return user
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error))


@router.patch(
    '/{id}',
    # response_model=UsersSchema,
    description='Update an User',
    response_description="THe user updated"

)
async def update_user(id: str, data: UsersUpdateModel = Body(...)):
    data = data.dict()
    try:
        updated_user = await user_db.update_by_id(
            object_id=id,
            data=data
        )
        return updated_user
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error))


@router.delete(
    '/{id}',
    response_model=NewObjectCreatedSchema,
    description="Delete an User for its id",
    response_description="THe user deleteed id"
)
async def delete_user(id: str):
    try:
        user = await user_db.delete_by_id(
            object_id=id
        )
        return user
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error))