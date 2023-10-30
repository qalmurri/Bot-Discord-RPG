import json
from discord.ext import commands
import random

import variable as var

from datetime import datetime, timedelta

class load_rpg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def language_environment(self, guild, random_common):
        try:
            with open('config/' + guild + '.json', 'r') as file:
                data = json.load(file)
                if isinstance(data.get("language"), str):
                    guild_language = data.get("language", "0")
        except FileNotFoundError:
            guild_language = "0"

        file_language = f"assets/rpg/environment/english/{random_common}.json" if guild_language == "0" else f"assets/rpg/environment/indonesian/{random_common}.json"
        with open(file_language, 'r') as json_file:
            language_environment = json.load(json_file)
        return language_environment

    def logic_spawn(self, guild):
        common = ["co001", "co002"]
        random_common = random.choice(common)

        environment_result = self.language_environment(guild, random_common)
        return environment_result, random_common

    def spawn_environment(self, guild):
        environment_result, random_common =  self.logic_spawn(guild)

        name = environment_result['name']
        class_value = environment_result['class']
        description = environment_result['description']
        
        hp = environment_result['hp']
        hp_result = random.randint(hp, hp*2)
        mana = environment_result['mana']
        mana_result = random.randint(mana, mana*2)

        environment = {
                "id_image": random_common,
                "status": "active",
                "profile": {
                    "name": name,
                    "class": class_value,
                    "description": description,
                    },
                "lobby": {
                    "user": {},
                    "log": {},
                    },
                "stats": {
                    "hp": hp_result,
                    "mana": mana_result,
                    },
                    "expire_at": datetime.utcnow() + timedelta(minutes=var.expired_environment)
                }
    
        return environment