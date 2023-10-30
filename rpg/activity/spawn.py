import discord
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
                        enemy = load_rpg(self).spawn_enemy(str(guild))
                        
                        expire = enemy.get("expire_at")
                        name = enemy['profile']['name']
                        description = enemy['profile']['description']
                        hp = enemy['bar']['hp']
                        mana = enemy['bar']['mana']

                        await db.SPAWN.update_many({"pve": None}, {"$set": {"pve": enemy}})
                        
                        embed = discord.Embed(title=name, description=description)
                        embed.add_field(name="Bar", value=f"HP: {hp}\nMana: {mana}", inline=False)
                        embed.set_thumbnail(url="https://wiki.dfo-world.com/images/2/23/AdaptingJagos.gif")
                        
                        await channel.send(embed=embed)
                        logging.info(f"{name} ({hp}/{mana}) Spawn {channel.id}. Expired at {expire}")

                if pve is not None:
                    channel = self.bot.get_channel(int(document.get("channel_id")))

                    if channel:
                        expired_date = pve.get("expire_at")
                        current_time = datetime.utcnow()

                        if expired_date < current_time:
                            await db.SPAWN.update_many({"pve.expire_at": {"$lt": current_time}}, {"$set": {"pve": None}})
                            logging.info(f"Spawn {channel.id}. Expired date")

                else:
                    pass

            await asyncio.sleep(var.spawn_enemy)

async def setup(bot):
    await bot.add_cog(spawn(bot))