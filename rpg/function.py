from discord.ext import commands

import variable as var
from cogs.function import load_cogs

import random
import json
from datetime import datetime, timedelta

class load_rpg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def language_enemy(self, guild, random_common):
        language = load_cogs.config(self, guild)
        directory = "assets/rpg/enemy"
        file_language = f"{directory}/english/{random_common}.json" if language == "0" else f"{directory}/indonesian/{random_common}.json"

        with open(file_language, 'r') as json_file:
            language_enemy = json.load(json_file)
        return language_enemy

    def logic_spawn(self, guild):
        common = ["co001", "co002"]
        random_common = random.choice(common)
        enemy_result = self.language_enemy(guild, random_common)

        return enemy_result, random_common

    def spawn_enemy(self, guild):
        enemy_result, random_common = self.logic_spawn(guild)

        name = enemy_result['name']
        class_value = enemy_result['class']
        description = enemy_result['description']
        
        hp = enemy_result['hp']
        hp_result = random.randint(hp, hp*2)
        mana = enemy_result['mana']
        mana_result = random.randint(mana, mana*2)

        enemy = {
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
                "bar": {
                    "hp": hp_result,
                    "mana": mana_result,
                    },
                    "expire_at": datetime.utcnow() + timedelta(minutes=var.expired_enemy)
                }
    
        return enemy