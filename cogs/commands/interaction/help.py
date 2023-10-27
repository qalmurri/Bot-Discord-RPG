import discord

async def basic(self, interaction, language):
    embed = discord.Embed(title="Basic", description=language["commands_basic"])

    latency = round(self.bot.latency * 1000)
    embed.set_footer(text=language["latency"] + " " + str(latency) + language["ms"])

    await interaction.response.send_message(embed=embed, ephemeral=True)
    
async def rpg(interaction):
    await interaction.response.send_message("buton rpg")