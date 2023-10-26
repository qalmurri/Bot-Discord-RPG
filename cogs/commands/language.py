import discord
from discord import app_commands
from discord.ext import commands

from cogs.function import load

import typing

class lang(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="setlanguage", description="Set language for your guild")
    @app_commands.describe(new_language="choice language")
    @app_commands.choices(new_language=[app_commands.Choice(name="English", value="0"), app_commands.Choice(name="Indonesian", value="1")])
    async def set_language(self, interaction:discord.interactions, new_language: typing.Optional[app_commands.Choice[str]]):

        guild_id = str(interaction.guild.id)
        language =  load(self).language(guild_id)
        language_config = load(self).load_language(guild_id)

        if "language" in language_config:
            language_config["language"] = new_language.value
        else:
            language_config["language"] = new_language.value
            
        load(self).save_language(language_config, guild_id)
        await interaction.response.send_message(language["change_language"] + f" {new_language.name}")

async def setup(bot):
    await bot.add_cog(lang(bot))