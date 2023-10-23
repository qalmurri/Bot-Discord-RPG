import discord
from discord import app_commands
from discord.ext import commands

import database as db

class spawn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = 1110105612790005812

    @app_commands.command(name="spawn", description="spawn di db")
    async def spawn(self, interaction:discord.Interaction):
        environment = await db.environment[str(interaction.guild.id)].find_one({"status": "active"})
        if environment is None:
            await db.environment[str(interaction.guild.id)].insert_one(
                {
                    "_id": interaction.channel.id,
                    "id_image": None,
                    "status": True,
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