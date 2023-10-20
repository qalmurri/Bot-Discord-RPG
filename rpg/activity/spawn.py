from discord.ext import commands
import asyncio

import database as db

class spawn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_background_task()

    async def background_task(self):
        while True:
            guild_collection = db.setting["guild"]
            async for document in guild_collection.find({}):
                guild_id = document["_id"]
                
                pve = document.get("pve")
                channel_pve = pve.get("channel_id")
                duration_pve = pve.get("channel_id")
                print(f"Guild: {guild_id} Channel: {channel_pve} Dur: {duration_pve}")
            await asyncio.sleep(2)

    def start_background_task(self):
        self.bot.loop.create_task(self.background_task())

            #if guild_id and channel_pve_id:
            #    guild = self.bot.get_guild(guild_id)
            #    channel_pve = self.bot.get_channel(channel_pve_id)
#
            #    if guild is not None and channel_pve is not None:
            #        await channel_pve.send(f"{self.bot.user.name} sedang menyerang monster di server {guild.name}")
            #    else:
            #        print(f"Guild or channel not found for guild ID: {guild_id}")
            #else:
            #    print("Missing guild or channel information in the document.")

            #channel_pve = self.bot.get_channel(document["channel_pve"])
            #await channel_pve.send(f"{self.bot.user.name} sedang menyerang monster")
            #if channel_pve is None:
            #    return
            #
            #while True:
            #    try:
            #        if self.last_message:
            #            await self.last_message.delete()
#
            #        self.last_message = await channel_pve.send(f"{self.bot.user.name} sedang menyerang monster")
            #        await asyncio.sleep(2)
            #    except discord.errors.NotFound:
            #        pass

async def setup(bot):
    await bot.add_cog(spawn(bot))