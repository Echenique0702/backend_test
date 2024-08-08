from pymongo.errors import DuplicateKeyError, PyMongoError
from fastapi import HTTPException
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from typing import List, Dict

from core.config import settings

# 
class CRUD():
    def __init__(self, collection_name):
        self.collection_name = collection_name

    async def cursor(self):
        """
        Establish a connection to the MongoDB database.

        This function creates a connection to the MongoDB database using the provided
        credentials and returns the database object for performing database operations.

        Returns:
            connection (Database): The connected MongoDB database object.
        """
        # Construct the MongoDB URI using the provided credentials
        mongo_uri = f'mongodb://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:27017/{settings.DB}'

        # Create a MongoDB client
        client = AsyncIOMotorClient(mongo_uri)

        # Connect to the specified database
        connection = client[settings.DB]
        
        # Return the database connection
        return connection


    async def get_collection(self):
        db = await self.cursor()
        return db[self.collection_name]


    async def create(self, data: dict) -> dict:
        """
        Create a new document in the collection.

        Args:
            data (dict): The document to be inserted.

        Returns:
            result (InsertOneResult): The result of the insertion.
        """
        try:
            collection = await self.get_collection()
            result = await collection.insert_one(data)
            return {
                'id': str(result.inserted_id)
                }
        except DuplicateKeyError:
            raise HTTPException(status_code=400, detail="Document with the same key already exists.")
        except PyMongoError as e:
            raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


    async def get_all(self) -> List[Dict]:
        """
        Read all documents from the collection.
        
        Returns:
            documents (List[Dict]): A list with all documents in collection, None otherwise.
        """
        try:
            collection = await self.get_collection()
            documents = collection.find()
            if not documents:
                raise HTTPException(status_code=404, detail="Documents not found.")
            return [{'id': str(doc.pop('_id')), **doc} async for doc in documents]
        except PyMongoError as e:
            raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


    async def get_by_id(self, object_id: str) -> Dict:
        """
        Read all documents from the collection.
        
        Params:
            object_id (str): The unique identifier for the object in collection

        Returns:
            document (Dict): A specific documents in collection, None otherwise.
        """
        collection = await self.get_collection()
        try:
            document = await collection.find_one({
                '_id': ObjectId(object_id)
            })
            if not document:
                raise HTTPException(status_code=404, detail="Documents not found.")
            document['id'] = str(document.pop('_id'))
            return document
        except PyMongoError as e:
            raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


    async def update_by_id(self, object_id: str, data: dict) -> Dict:
        """
        Update a specific object in the collection by its id.

        Params:
            object_id (str): The unique identifier for the object in the collection
            data (dict): Dict data to be updated in the object

        Returns:
            document (Dict): The updated document, None otherwise.
        """
        collection = await self.get_collection()
        try:
            document = await collection.find_one_and_update(
                {
                    '_id': ObjectId(object_id)
                },
                {
                    '$set': data
                },
                return_document=True
            )
            if not document:
                raise HTTPException(status_code=404, detail="Document not found.")
            document['id'] = str(document.pop('_id'))
            return document
        except PyMongoError as e:
            raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


    async def delete_by_id(self, object_id: str) -> Dict:
        """
        Delete a specific object in the collection by its id.

        Params:
            object_id (str): The unique identifier for the object in the collection

        Returns:
            result (Dict): The result of the delete operation.
        """
        collection = await self.get_collection()
        try:
            result = await collection.delete_one(
                {
                    '_id': ObjectId(object_id)
                }
            )
            if result.deleted_count == 0:
                raise HTTPException(status_code=404, detail="Document not found.")
            return {
                'id': object_id
                }
        except PyMongoError as e:
            raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
