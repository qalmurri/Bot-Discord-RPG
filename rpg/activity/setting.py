import discord
from discord import app_commands
from discord.ext import commands

import database as db

class setting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="setting", description="setting")
    async def setting(self, interaction:discord.Interaction, channel_pve: str):
        setting = await db.setting["guild"].find_one({"_id": interaction.guild.id})
        if setting is None:
            await db.setting["guild"].insert_one(
                {
                    "_id": interaction.guild.id,
                    "channel_pve": channel_pve
                    }
                )
            await interaction.response.send_message(f"channel pve sudah di atur {channel_pve}")
        else:
            await db.setting["guild"].update_one(
                {"_id": interaction.guild.id},
                    {
                        "$set": {
                            "channel_pve": channel_pve,
                            }
                        }
                    )
            await interaction.response.send_message(f"channel pve sudah di perbarui {channel_pve}")

async def setup(bot):
    await bot.add_cog(setting(bot))

