import discord
from discord import app_commands
from discord.ext import commands

import database as db

class pve(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="pve", description="setting")
    async def pve(self, interaction:discord.Interaction, channel_pve: str = None):
        if channel_pve is not None:
            setting = await db.SPAWN.find_one({"_id": interaction.guild.id})
            if setting is None:
                await db.SPAWN.insert_one(
                    {
                        "_id": interaction.guild.id,
                        "channel_id": channel_pve,
                        "pve":None,
                        }
                    )
                await interaction.response.send_message(f"channel pve sudah di atur {channel_pve}")
            else:
                await db.SPAWN.update_one(
                    {"_id": interaction.guild.id},
                        {
                            "$set": {
                                "channel_id": channel_pve,
                                "pve":None,
                                }
                            }
                        )
                await interaction.response.send_message(f"channel pve sudah di perbarui {channel_pve}")
        else:
            environment = await db.SPAWN.find_one({"_id": interaction.guild.id})
            data_env = environment.get("pve", {})
            profile_env = data_env.get("profile", {})

            id_image, status = (data_env.get(key, 0) for key in ("id_image", "status"))
            name_env, class_env, desc_env  = (profile_env.get(key, 0) for key in ("name", "class", "description"))

            print(id_image)

            embed = discord.Embed(title=name_env, description=desc_env)
            embed.set_thumbnail(url="https://wiki.dfo-world.com/images/2/23/AdaptingJagos.gif")
   
            await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(pve(bot))

