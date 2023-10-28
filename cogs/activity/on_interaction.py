import discord
from discord.ext import commands

from cogs.function import load_cogs
from cogs.commands.interaction.help import basic, rpg
from rpg.commands.interaction.remove_rpg import remove_rpg

class interaction_id(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        language =  load_cogs(self).language(str(interaction.guild.id))
        data = interaction.data
        custom_id = data.get('custom_id')

        if custom_id is not None:
            if custom_id == "remove_rpg":
                await remove_rpg(interaction, language)

            elif custom_id == "basic":
                await basic(self, interaction, language)

            elif custom_id == "rpg":
                await rpg(self, interaction, language)
                
            else:
                await interaction.response.send_message("custom_id tidak ditemukan")

async def setup(bot):
    await bot.add_cog(interaction_id(bot))