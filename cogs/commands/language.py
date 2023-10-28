import discord
from discord import app_commands
from discord.ext import commands

import variable  as var
from cogs.function import load_cogs
from cogs.activity.logging import logging

import typing

class lang(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="language", description="Set language for your guild")
    @app_commands.describe(languages="choice language")
    @app_commands.choices(languages=[app_commands.Choice(name="English", value="0"), app_commands.Choice(name="Indonesian", value="1")])
    async def set_language(self, interaction:discord.interactions, languages: typing.Optional[app_commands.Choice[str]]):
        language =  load_cogs(self).language(str(interaction.guild.id))
        latency = round(self.bot.latency * 1000)

        if languages is not None:
            language_config = load_cogs(self).load_language(str(interaction.guild.id))

            if "language" in language_config:
                language_config["language"] = languages.value

            else:
                language_config["language"] = languages.value

            load_cogs(self).save_language(language_config, str(interaction.guild.id))

            embed = discord.Embed(description=language["change_language"] + f"```{languages.name}```")
            embed.set_footer(text=language["latency"] + " " + str(latency) + language["ms"])

            await interaction.response.send_message(embed=embed, ephemeral=var.language_ephemeral, delete_after=var.language_delete)
            logging.info(f"{interaction.guild.id}/{interaction.channel.id}/{interaction.id}: Change language {languages.name}")

        else:
            await interaction.response.send_message("pilih bahasa dulu ya")

async def setup(bot):
    await bot.add_cog(lang(bot))