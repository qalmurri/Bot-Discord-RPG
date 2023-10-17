import discord
from discord import app_commands
from discord.ext import commands

import database as db

class unequip1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="unequip1", description="unequip item")
    async def unequip(self, interaction:discord.Interaction):
        await db.player[f"{interaction.guild.id}"].update_one({"_id": interaction.user.id}, {"$unset": {"game.rpg.use.body": 1}})
        await interaction.response.send_message("body di badan sudah di lepas")

async def setup(bot):
    await bot.add_cog(unequip1(bot))

