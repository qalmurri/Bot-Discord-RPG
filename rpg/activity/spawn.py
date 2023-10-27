import discord
from discord.ext import commands

import variable as var

import database as db
import asyncio

from datetime import datetime, timedelta
import random

class spawn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.loop.create_task(self.spawn())



    async def spawn(self):
        while not self.bot.is_closed():
            expire_time = datetime.utcnow() + timedelta(seconds=8)
            random_number = random.randint(1, 100)
            Environment = {
                        "number":random_number,
                    "id_image": "co001",
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
            
            cursor = db.SPAWN.find({}, {"channel_id": 1, "pve": 1})
            async for document in cursor:
                pve = document.get("pve")
                if pve is None:
                    channel_id = document.get("channel_id")
                    channel = self.bot.get_channel(int(channel_id))
                    print(channel)
                    if channel:
                        await db.SPAWN.update_many({}, {"$set": {"pve": Environment}})

                        await channel.send(Environment)
                else:
                    print("tidak ada update")

            await asyncio.sleep(var.spawn_environment)

async def setup(bot):
    await bot.add_cog(spawn(bot))