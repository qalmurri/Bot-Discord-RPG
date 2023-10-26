import discord
from discord import app_commands
from discord.ext import commands

from cogs.function import load
import database as db

import datetime

class register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="register", description="Bot ini perlu register dulu, buat sebuah 'About Me' di perintah ini")
    async def register(self, interaction: discord.Interaction, about_me: str):
        
        guild_id = str(interaction.guild.id)
        language =  load(self).language(guild_id)

        player = await db.PLAYER_USER.find_one({"_id": interaction.user.id})
        if player is None:
            await db.PLAYER_USER.insert_one(
                {
                    "_id": interaction.user.id,
                    "jinfo": {
                        "jdate" : datetime.datetime.now(),
                        "jguild" : interaction.guild.id
                    },
                    "profile": {
                        "udate": datetime.datetime.now(),
                        "about_me": about_me
                        },
                    "game": {}
                    }
                )
            await interaction.response.send_message(language["create_register"])
        else:
            await db.PLAYER_USER.update_one(
                {"_id": interaction.user.id},
                    {
                        "$set": {
                            "profile.udate": datetime.datetime.now(),
                            "profile.about_me": about_me
                            }
                        }
                    )
            await interaction.response.send_message(language["update_register"])

async def setup(bot):
    await bot.add_cog(register(bot))