import discord
from discord import app_commands
from discord.ext import commands

import database as db

class equip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="equip", description="Equip item")
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
                            "game.rpg.use.head": {
                                "id": 21,
                                "name": "tengkorak",
                                "class": "rare",
                                "str": 999999,
                                "vit": 31,
                                "int": 12,
                                "agi": 2,
                                "fire": 20,
                                "wind": 41,
                                "water": 12,
                                "earth": 44,
                                }
                            }
                        }
                    )
            await interaction.response.send_message("Tengkorak di kepala sudah terpasang")

    @app_commands.command(name="unequip", description="unequip item")
    async def unequip(self, interaction:discord.Interaction):
        await db.player[f"{interaction.guild.id}"].update_one({"_id": interaction.user.id}, {"$unset": {"game.rpg.use.head": 1}})
        await interaction.response.send_message("Tengkorak di kepala sudah di lepas")

async def setup(bot):
    await bot.add_cog(equip(bot))

