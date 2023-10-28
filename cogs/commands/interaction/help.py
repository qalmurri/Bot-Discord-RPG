import discord

import variable as var
from cogs.activity.logging import logging

async def basic(self, interaction, language):
    embed = discord.Embed(title=language["name_commands_basic"], description=language["commands_basic"])
    latency = round(self.bot.latency * 1000)
    embed.set_footer(text=language["latency"] + " " + str(latency) + language["ms"])
    await interaction.response.send_message(embed=embed, ephemeral=var.basic_ephemeral, delete_after=var.basic_delete)
    logging.info(f"{interaction.guild.id}/{interaction.channel.id}/{interaction.id}: /help -> Basic")
    
async def rpg(self, interaction, language):
    embed = discord.Embed(title="RPG", description=language["commands_rpg"])
    latency = round(self.bot.latency * 1000)
    embed.set_footer(text=language["latency"] + " " + str(latency) + language["ms"])
    await interaction.response.send_message(embed=embed, ephemeral=var.rpg_ephemeral, delete_after=var.rpg_delete)
    logging.info(f"{interaction.guild.id}/{interaction.channel.id}/{interaction.id}: /help -> RPG")