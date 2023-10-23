import discord
from discord.ext import commands
from discord import app_commands

import database as db

class spawn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="spawn", description="spawn di db")
    async def spawn(self, interaction:discord.Interaction):
        environment = await db.ENV20.find_one({"_id": interaction.guild.id})
        if environment is None:
            await db.ENV20.insert_one(
                {
                    "_id": interaction.guild.id,
                    "id_image": None,
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
                        }
                    }
                )
            await interaction.response.send_message(f"Monster sudah ada di db, silahkan ketik attack untuk melihat reaksinya")
        else:
            pass


async def setup(bot):
    await bot.add_cog(spawn(bot))