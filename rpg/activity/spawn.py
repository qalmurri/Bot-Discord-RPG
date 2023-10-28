from discord.ext import commands

import database as db
import variable as var
from rpg.function import load_rpg
from cogs.activity.logging import logging

import asyncio
from datetime import datetime


class spawn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.loop.create_task(self.spawn())

    async def spawn(self):
        while not self.bot.is_closed():
            cursor = db.SPAWN.find({}, {"_id": 1, "channel_id": 1, "pve": 1})

            async for document in cursor:
                pve = document.get("pve")

                if pve is None:
                    channel = self.bot.get_channel(int(document.get("channel_id")))

                    if channel:
                        guild = document.get("_id")
                        Environment = load_rpg(self).spawn_environment(str(guild))
                        expire = Environment.get("expire_at")

                        await db.SPAWN.update_many({"pve": None}, {"$set": {"pve": Environment}})
                        
                        await channel.send(expire)
                        logging.info(f"Data Environment dikirim ke channel {channel.id} - expired_at: {expire}")

                if pve is not None:
                    channel = self.bot.get_channel(int(document.get("channel_id")))

                    if channel:
                        expired_date = pve.get("expire_at")
                        current_time = datetime.utcnow()

                        if expired_date < current_time:
                            await db.SPAWN.update_many({"pve.expire_at": {"$lt": current_time}}, {"$set": {"pve": None}})
                            logging.info(f"Data Environment expired_date {channel.id}")

                else:
                    pass

            await asyncio.sleep(var.spawn_environment)

async def setup(bot):
    await bot.add_cog(spawn(bot))