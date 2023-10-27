import discord
from discord import app_commands
from discord.ext import commands

from cogs.function import load_cogs

class basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="Magerpol Help")
    async def help(self, interaction:discord.Interaction):
        language =  load_cogs(self).language(str(interaction.guild.id))
        
        embed = discord.Embed(description=language["help"])
        embed.set_author(name=language["hello"] + " " + interaction.user.name, icon_url=interaction.user.display_avatar)

        latency = round(self.bot.latency * 1000)
        embed.set_footer(text=language["latency"] + " " + str(latency) + language["ms"])

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="Basic", custom_id="basic"))
        view.add_item(discord.ui.Button(label="RPG", custom_id="rpg"))
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True, delete_after=20)

    @app_commands.command(name="avatar", description="Get user avatar")
    async def avatar(self, interaction:discord.Interaction, member:discord.Member):
        await interaction.response.send_message(member.display_avatar)

async def setup(bot):
    await bot.add_cog(basic(bot))