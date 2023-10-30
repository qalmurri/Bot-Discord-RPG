import discord
from discord import app_commands
from discord.ext import commands

import database as db
from cogs.function import load_cogs
from cogs.activity.logging import logging

import datetime

class register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="register", description="Bot ini perlu register dulu, buat sebuah 'About Me' di perintah ini")
    async def register(self, interaction: discord.Interaction, aboutme: str):
        language =  load_cogs(self).language_commands(str(interaction.guild.id))
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
                        "about_me": aboutme
                        },
                    "game": {}
                    }
                )
            
            await interaction.response.send_message(language["create_register"])
            logging.info(f"{interaction.guild.id}/{interaction.channel.id}/{interaction.id}: Create register: {aboutme}")

        else:
            await db.PLAYER_USER.update_one(
                {"_id": interaction.user.id},
                    {
                        "$set": {
                            "profile.udate": datetime.datetime.now(),
                            "profile.about_me": aboutme
                            }
                        }
                    )
            
            await interaction.response.send_message(language["update_register"])
            logging.info(f"{interaction.guild.id}/{interaction.channel.id}/{interaction.id}: Update register: {aboutme}")

async def setup(bot):
    await bot.add_cog(register(bot))