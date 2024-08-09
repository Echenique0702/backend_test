from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder

# Schemas
from schemas.friendships import (
    FriendshipSchema
)
from schemas.users import BasicUserSchema
from schemas.base import NewObjectCreatedSchema

# Models
from models.friendships import (
    FriendshipModel
)

# Database
from database.friendships import FriendshipDB
from database.users import UsersDB

from typing import List
from bson import ObjectId

# Initial Settings Variables
router = APIRouter()
friendship_db = FriendshipDB()
user_db = UsersDB()

# Endpoints Declarations
@router.post(
    '/first-user/{first_user_id}/second-user/{second_user_id}',
    response_model=NewObjectCreatedSchema,
    description='Create a new friendship between two users id',
    response_description="A new frindship id created"
)
async def create_friendship(first_user_id: str, second_user_id: str):
    
    try:
        # Check if both users exist
        if not await user_db.check_if_users_exist(
            users_id_list=[first_user_id, second_user_id]
            ):
            raise HTTPException(status_code=404, detail='Users Not Found')
        # Data Creation to Store in DB
        data = FriendshipModel(
            first_user_id=first_user_id,
            second_user_id=second_user_id
        ).dict()
        # Store in DB
        new_friendship = await friendship_db.create(
            data=data
            )
        return new_friendship
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.get(
    '',
    response_model=List[FriendshipSchema],
    description='Return all friendship',
    response_description='A list with all relationshiops'
)
async def get_all_friendships():
    try:
        users = await user_db.get_all()
        friendships = await friendship_db.get_all()

        # mappign users
        users_mapping = {user['id']: user for user in users}

        return [
            {
                'id': friendship['id'],
                'first_user_id': friendship['first_user_id'],
                'first_user_first_name': users_mapping[friendship['first_user_id']]['first_name'],
                'first_user_last_name': users_mapping[friendship['first_user_id']]['last_name'],
                'second_user_id': friendship['second_user_id'],
                'second_user_first_name': users_mapping[friendship['second_user_id']]['first_name'],
                'second_user_last_name': users_mapping[friendship['second_user_id']]['last_name'],
            } for friendship in friendships
        ]
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))



@router.get(
    '/user/{user_id}',
    response_model=List[BasicUserSchema],
    description='Return all friendship by user id',
    response_description='A list with all relationshiops by user'
)
async def get_all_friendships_by_user(user_id: str):
    try:
        friendships = await friendship_db.get_all_by_user_id(
            user_id=user_id
            )
        users_ids = list(set([
            friendship[value] for friendship in friendships for value in friendship if value != 'id' and friendship[value] != user_id
        ]))

        users = await user_db.get_user_by_list_ids(
            users_id_list=users_ids
        )

        return users
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))
