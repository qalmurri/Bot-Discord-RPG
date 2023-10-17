import discord
from discord import app_commands
from discord.ext import commands

import database as db

class unequip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="unequip_head", description="unequip_head")
    async def unequip_head(self, interaction:discord.Interaction):
        await db.player[f"{interaction.guild.id}"].update_one({"_id": interaction.user.id}, {"$unset": {"game.rpg.use.head": 1}})
        await interaction.response.send_message("Tengkorak di kepala sudah di lepas")

    @app_commands.command(name="unequip_necklace1", description="unequip_necklace1")
    async def unequip_necklace1(self, interaction:discord.Interaction):
        await db.player[f"{interaction.guild.id}"].update_one({"_id": interaction.user.id}, {"$unset": {"game.rpg.use.necklace1": 1}})
        await interaction.response.send_message("kalung di badan sudah di lepas")

    @app_commands.command(name="unequip_necklace2", description="unequip_necklace2")
    async def unequip_necklace2(self, interaction:discord.Interaction):
        await db.player[f"{interaction.guild.id}"].update_one({"_id": interaction.user.id}, {"$unset": {"game.rpg.use.necklace2": 1}})
        await interaction.response.send_message("kalung di badan sudah di lepas")

async def setup(bot):
    await bot.add_cog(unequip(bot))

