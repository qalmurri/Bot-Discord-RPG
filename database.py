from motor.motor_asyncio import AsyncIOMotorClient

import os
from dotenv import load_dotenv
load_dotenv()

MONGO_CLIENT = AsyncIOMotorClient(os.getenv("URI"))

#Databases
MESSAGE = MONGO_CLIENT["message"]
PLAYER = MONGO_CLIENT["player"]
SETTING = MONGO_CLIENT["setting"]
ENVIRONMENT = MONGO_CLIENT["environment"]

#Collection
MESSAGE_USER = MESSAGE["user"]
PLAYER_USER = PLAYER["user"]
GUILD = SETTING["guild"]
ENV20 = ENVIRONMENT["20"]
ENV40 = ENVIRONMENT["40"]
ENV60 = ENVIRONMENT["60"]
ENV80 = ENVIRONMENT["80"]
ENV100 = ENVIRONMENT["100"]