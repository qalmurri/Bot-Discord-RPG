import discord
from discord.ext import commands

import database as db
import variable as var
from cogs.activity.logging import logging

import datetime
from bson import ObjectId

class pve_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(case_insensitive=True)
    @commands.cooldown(1, var.attack_cooldown, commands.BucketType.user)
    async def attack(self, ctx):
        guild = await db.SPAWN.find_one({"_id": ctx.guild.id})
        channel = guild.get("channel_id", {})
        pve = guild.get("pve", {})

        if str(ctx.channel.id) == channel:
            await ctx.message.delete()
            player = await db.PLAYER_USER.find_one({"_id": ctx.author.id})
            if player is None:
                await ctx.channel.send("belum set profile")
            else:
                check = player.get("game", {}).get("rpg", None)
                if check is None:
                    await ctx.channel.send("belum join rpg")
                else:
                    if pve is None:
                        await ctx.channel.send("belum spawn monster woi")
                    else:
                        #stats player
                        head_stats = player.get("game", {}).get("rpg", {}).get("use", {}).get("head", {}).get("stats", {})
                        head_str, head_vit, head_int, head_agi, head_fire, head_water, head_wind, head_earth = (head_stats.get(key, 0) for key in ("str", "vit", "int", "agi", "fire", "water", "wind", "earth"))

                        #stats_environment
                        environment_profile = pve.get("profile", {})
                        environment_name = environment_profile.get("name", {})
                        environment_class = environment_profile.get("class", {})
                        environment_stats = pve.get("stats", {})
                        environment_hp = environment_stats.get("hp", {})

                        #mekanisme stats

                        #HP_envirinment
                        total_hp = environment_hp - head_str

                        lobby = pve.get("lobby", {}).get("user", {}).get(str(ctx.author.id), None)
                        if lobby is None:
                            await db.SPAWN.update_one(
                                    {"_id": ctx.guild.id}, {"$set": {f"pve.lobby.user.{str(ctx.author.id)}": datetime.datetime.now()}})
                            
                            embed = discord.Embed()
                            embed.set_author(name=ctx.author.name + f" bergabung untuk menyerang {environment_name} ({environment_class})", icon_url=ctx.author.display_avatar)

                            await  ctx.message.channel.send(embed=embed)
                            logging.info(f"{ctx.author.name} joined {environment_name}")
                        else:
                            await db.SPAWN.update_one(
                                {"pve.status": "active"}, {
                                    "$set": {
                                        "pve.stats.hp": total_hp,
                                        }
                                    }
                                )
                            await db.SPAWN.update_one(
                                {"_id": ctx.guild.id}, {"$set": {f"pve.lobby.log.attacker.{ctx.author.id}_{ObjectId()}": head_str }}
                                )
                            
                            if environment_hp <= 1:
                                await ctx.channel.send(f"```c\nini adalah kemenangan kalian, yeay!```")
                                await self.result_pve(ctx, pve)
                            else:
                                await ctx.channel.send(f"```c\n{ctx.author.name} menyerang {environment_name}({environment_class}) dengan damage serangan {head_str}, Monster mempunyai {total_hp} hp```")
                                logging.info(f"{ctx.author.name} .attack {environment_name}")
        else:
            print("channel tidak ada")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            pass

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.message.delete()
            await ctx.send(f"This command is on cooldown for another " + str("%.2f" % error.retry_after) + " seconds!", delete_after=4)

    async def result_pve(self, ctx, pve):
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

            await ctx.channel.send(total_damage_message)
            await db.SPAWN.update_one(
                    {"_id": ctx.guild.id}, {"$set": {"pve": None, }}
                    )

async def setup(bot):
    await bot.add_cog(pve_commands(bot))