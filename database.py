from motor.motor_asyncio import AsyncIOMotorClient

import os
from dotenv import load_dotenv
load_dotenv()

mc = AsyncIOMotorClient(os.getenv("URI"))

msg = mc["message"]
player = mc["player"]
setting = mc["setting"]
environment = mc["environment"]