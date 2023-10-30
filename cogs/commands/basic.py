import discord
from discord import app_commands
from discord.ext import commands

import variable  as var
from cogs.function import load_cogs
from cogs.activity.logging import logging

class basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="Magerpol Help")
    async def help(self, interaction:discord.Interaction):
        language =  load_cogs(self).language_commands(str(interaction.guild.id))
        latency = round(self.bot.latency * 1000)
        
        embed = discord.Embed(description=f"```\n{language['help']}```")
        embed.set_footer(text=language["latency"] + " " + str(latency) + language["ms"])

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="Basic", custom_id="basic"))
        view.add_item(discord.ui.Button(label="RPG", custom_id="rpg"))
        
        await interaction.response.send_message(embed=embed, view=view, ephemeral=var.help_ephemeral, delete_after=var.help_delete)
        logging.info(f"{interaction.guild.id}/{interaction.channel.id}/{interaction.id}: /help")

async def setup(bot):
    await bot.add_cog(basic(bot))