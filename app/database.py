import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

class Database:
    client: AsyncIOMotorClient = None

    @classmethod
    def initialize(cls):
        mongo_connection = os.getenv("MONGO_CONNECTION")
        if not mongo_connection:
            raise ValueError("MONGO_CONNECTION is not set in the environment variables")
        
        cls.client = AsyncIOMotorClient(mongo_connection)
        print("MongoDB client initialized.")

    @classmethod
    def close_connection(cls):
        if cls.client:
            cls.client.close()
            print("MongoDB client connection closed.")

    @classmethod
    def get_database(cls, db_name: str):
        if not cls.client:
            raise RuntimeError("MongoDB client not initialized")
        return cls.client[db_name]
