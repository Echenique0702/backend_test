from database.api import CRUD
from helpers.friendships import basic_friendship_helper
from pymongo.errors import PyMongoError

class FriendshipDB(CRUD):
    def __init__(self):
        super().__init__(collection_name='friendship_collection')
    

    async def get_all_by_user_id(self, user_id: str):
        collection = await self.get_collection()
        try:
            friendships = collection.find({
                "$or": [
                    {'first_user_id': user_id},
                    {'second_user_id': user_id}
                ]
            })
            return [basic_friendship_helper(friendship) async for friendship in friendships]
        except PyMongoError as e:
            raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

