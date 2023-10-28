import discord
from discord import app_commands
from discord.ext import commands

import database as db
from cogs.activity.logging import logging

class pve_activity(commands.Cog):
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
                logging.info(f"{interaction.guild.id}/{interaction.channel.id}/{interaction.id}: Create channel PVE {channel_pve}")

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
                logging.info(f"{interaction.guild.id}/{interaction.channel.id}/{interaction.id}: Update channel PVE {channel_pve}")

        else:
            environment = await db.SPAWN.find_one({"_id": interaction.guild.id})

            if environment is not None:
                pve = environment.get("pve", {})
                profile_env = pve.get("profile", {})
                stats_env = pve.get("stats", {})

                id_image, status = (pve.get(key, 0) for key in ("id_image", "status"))
                name_env, desc_env  = (profile_env.get(key, 0) for key in ("name", "description"))
                hp_env, mana_env  = (stats_env.get(key, 0) for key in ("hp", "mana"))

                environment_attacker = pve.get("lobby", {}).get("log", {}).get("attacker", {})
                
                if isinstance(environment_attacker, dict):
                    code_sum = {}
                    for key, value in environment_attacker.items():
                        code = key.split("_")[0]
                        if code in code_sum:
                            code_sum[code] += value
                        else:
                            code_sum[code] = value

                    total_damage_message = ""
                    for code, total_value in code_sum.items():
                        total_damage_message += f"<@{code}>: {total_value}\n"

                embed = discord.Embed(title=name_env, description=desc_env)
                embed.add_field(name="Stats", value=f"HP: {hp_env}\nMana: {mana_env}", inline=False)
                embed.add_field(name="Attacker Damage", value=total_damage_message, inline=False)
    
                await interaction.response.send_message(embed=embed)
            else:
                await interaction.response.send_message("belum set channel pve")


async def setup(bot):
    await bot.add_cog(pve_activity(bot))
