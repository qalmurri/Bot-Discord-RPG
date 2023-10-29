import json
from discord.ext import commands
import random

import variable as var

from datetime import datetime, timedelta

class load_rpg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def language_environment(self, guild):
        try:
            with open('config/' + guild + '.json', 'r') as file:
                data = json.load(file)
                if isinstance(data.get("language"), str):
                    guild_language = data.get("language", "0")
        except FileNotFoundError:
            guild_language = "0"

        file_language = "assets/rpg/environment/english.json" if guild_language == "0" else "assets/rpg/environment/indonesian.json"
        with open(file_language, 'r') as json_file:
            language_environment = json.load(json_file)
        return language_environment

    def logic_spawn(self, guild):
        language_environment =  self.language_environment(guild)

        common = ["co001", "co002"]
        random_common = random.choice(common)

        name_environment = random_common + "_name"
        class_environment = random_common + "_class"
        desccription_environment = random_common + "_description"
        hp_environment = random_common + "_hp"
        mana_environment = random_common + "_mana"

        environment_result ={
            "id_image": random_common,
            "name": language_environment[name_environment],
            "class": language_environment[class_environment],
            "description": language_environment[desccription_environment],
            "hp": language_environment[hp_environment],
            "mana": language_environment[mana_environment]
        }
        return environment_result

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

        environment_result =  self.logic_spawn(guild)
        id_image = environment_result['id_image']
        name = environment_result['name']
        class_value = environment_result['class']
        description = environment_result['description']
        
        hp = environment_result['hp']
        hp_result = random.randint(hp, (hp+hp))
        
        mana = environment_result['mana']
        mana_result = random.randint(mana, (mana+mana))

        if spawn_env == "0":
            environment = {
                    "random_number": f"{spawn_env}_{random_number}",
                    "id_image": id_image,
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
                        "expire_at": expire_time
                    }
        
        elif spawn_env == "1":
            environment = {
                    "random_number": f"{spawn_env}_{random_number}",
                    "id_image": id_image,
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
                        "expire_at": expire_time
                    }
        
        return environment