import discord
from discord import app_commands
from discord.ext import commands

import database as db

class equip1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="equip1", description="Equip item")
    async def equip(self, interaction:discord.Interaction):
        player = await db.player[f"{interaction.guild.id}"].find_one({"game.rpg.status": True})
        if player is None:
            await interaction.response.send_message("Kamu belum mempunyai game rpg")
        else:
            await db.player[f"{interaction.guild.id}"].update_one(
                {
                    "_id": interaction.user.id
                    },
                    {
                        "$set": {
                            "game.rpg.use.body": {
                                "id": 21,
                                "name": "Body Posaidon",
                                "class": "rare",
                                "str": 123,
                                "vit": 44,
                                "int": 2223,
                                "agi": 12,
                                "fire": 2222,
                                "wind": 43,
                                "water": 22,
                                "earth": 44,
                                }
                            }
                        }
                    )
            await interaction.response.send_message("Body dibadan  sudah terpasang")

async def setup(bot):
    await bot.add_cog(equip1(bot))

