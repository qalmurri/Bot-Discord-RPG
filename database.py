from motor.motor_asyncio import AsyncIOMotorClient

import os
from dotenv import load_dotenv
load_dotenv()

MONGO_CLIENT = AsyncIOMotorClient(os.getenv("URI"))

#Databases
MESSAGE = MONGO_CLIENT["message"]
PLAYER = MONGO_CLIENT["player"]
ENVIRONMENT = MONGO_CLIENT["environment"]

#Collection
MESSAGE_USER = MESSAGE["user"]
PLAYER_USER = PLAYER["user"]
SPAWN = ENVIRONMENT["spawn"]