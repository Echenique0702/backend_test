from pymongo.errors import PyMongoError
from fastapi import HTTPException

from database.api import CRUD

from helpers.users import basic_user_helper

from bson import ObjectId



class UsersDB(CRUD):
    def __init__(self):
        super().__init__(collection_name='users_collection')

    async def check_if_users_exist(self, users_id_list: str):
        '''
        Function to check if users exist in DB

        Params:
            users_id_list (List[str]): List with all string users id

        Return:
            bool indicating if both users exist
        '''
        collection = await self.get_collection()
        try:
            users_ids = [ObjectId(id) for id in users_id_list]
            count = await collection.count_documents({"_id": {"$in": users_ids}})
            return count == len(users_ids)
        except PyMongoError as e:
            raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


    async def get_user_by_list_ids(self, users_id_list: list) -> list:
        '''
        Get all basic information for users in list id

        Params:
            users_id_list (List[str]): List with all string users id
        
        Return:
            A list with all Objects
        '''
        collection = await self.get_collection()
        try:
            users = collection.find(
                {'_id': {
                    '$in': [
                        ObjectId(id) for id in users_id_list
                    ]
                }}
            )
            return [
                basic_user_helper(user) async for user in users
            ]
        except PyMongoError as e:
            raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


 