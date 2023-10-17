import discord
from discord import app_commands
from discord.ext import commands

import database as db

class equip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="equip_head", description="equip_head")
    async def equip_head(self, interaction:discord.Interaction):
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
                                "id_item": "co001",
                                "name": "HELM SNI",
                                "class": "rare",
                                "price": 1200,
                                "str": 23,
                                "vit": 21,
                                "int": 32,
                                "agi": 33,
                                "fire": 20,
                                "wind": 41,
                                "water": 12,
                                "earth": 44,
                                }
                            }
                        }
                    )
            await interaction.response.send_message("item head di kepala sudah terpasang")

    @app_commands.command(name="equip_necklace1", description="equip_necklace1")
    async def equip_necklace1(self, interaction:discord.Interaction):
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
                            "game.rpg.use.necklace1": {
                                "id_item": "co001",
                                "name": "KALUNG MBAH SURIP",
                                "class": "rare",
                                "price": 1200,
                                "str": 44,
                                "vit": 31,
                                "int": 32,
                                "agi": 21,
                                "fire": 20,
                                "wind": 44,
                                "water": 66,
                                "earth": 11,
                                }
                            }
                        }
                    )
            await interaction.response.send_message("necklace1 sudah terpasang")

    @app_commands.command(name="equip_necklace2", description="equip_necklace2")
    async def equip_necklace2(self, interaction:discord.Interaction):
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
                            "game.rpg.use.necklace2": {
                                "id_item": "co001",
                                "name": "KALUNG SAKAROTUL MAUT",
                                "class": "rare",
                                "price": 1200,
                                "str": 44,
                                "vit": 31,
                                "int": 32,
                                "agi": 21,
                                "fire": 20,
                                "wind": 44,
                                "water": 66,
                                "earth": 11,
                                }
                            }
                        }
                    )
            await interaction.response.send_message("necklace2 sudah terpasang")

async def setup(bot):
    await bot.add_cog(equip(bot))

