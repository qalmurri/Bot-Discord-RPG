import json
from discord.ext import commands
import random

import variable as var

from datetime import datetime, timedelta

class load_rpg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def spawn_environment(self, guild):
        try:
            with open('config/' + guild + '.json', 'r') as file:
                data = json.load(file)
                if isinstance(data.get("spawn_env"), str):
                    spawn_env = data.get("spawn_env", "0")
                else:
                    spawn_env = "0"
        except FileNotFoundError:
            spawn_env = "0"


        current_time = datetime.utcnow()
        expire_time = current_time + timedelta(minutes=var.expired_environment)
        random_number = random.randint(1, 1000)

        if spawn_env == "0":
            environment = {
                    "id_image": random_number,
                    "status": "active",
                    "profile": {
                        "name": "jelangkung",
                        "class": "common",
                        "description": "jelangku adalah boneka spritirual",
                        },
                    "lobby": {
                        "user": {},
                        "log": {},
                        },
                    "stats": {
                        "hp": 300,
                        "mana": 1000,
                        },
                        "expire_at": expire_time
                    }
        
        elif spawn_env == "1":

            environment = {
                    "id_image": random_number,
                    "status": "active",
                    "profile": {
                        "name": "jelangkung",
                        "class": "common",
                        "description": "jelangku adalah boneka spritirual",
                        },
                    "lobby": {
                        "user": {},
                        "log": {},
                        },
                    "stats": {
                        "hp": 300,
                        "mana": 1000,
                        },
                        "expire_at": expire_time
                    }
        

        return environment