import discord
from discord import app_commands
from discord.ext import commands

import database as db

class unequip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="unequip", description="unequip item")
    async def unequip(self, interaction:discord.Interaction):
        await db.player[f"{interaction.guild.id}"].update_one({"_id": interaction.user.id}, {"$unset": {"game.rpg.use.head": 1}})
        await interaction.response.send_message("Tengkorak di kepala sudah di lepas")

async def setup(bot):
    await bot.add_cog(unequip(bot))

