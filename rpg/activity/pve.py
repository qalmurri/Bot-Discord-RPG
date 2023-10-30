import discord
from discord.ext import commands

import database as db
import variable as var
from cogs.activity.logging import logging

import datetime
from bson import ObjectId
from datetime import timedelta

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

                        enemy_profile = pve.get("profile", {})
                        enemy_name = enemy_profile.get("name", {})
                        enemy_class = enemy_profile.get("class", {})

                        #HP_envirinment
                        enemy_stats = pve.get("bar", {})
                        enemy_hp = enemy_stats.get("hp", {})
                        enemy_mana = enemy_stats.get("mana", {})

                        total_hp = enemy_hp - head_str

                        lobby = pve.get("lobby", {}).get("user", {}).get(str(ctx.author.id), None)
                        if lobby is None:
                            await db.SPAWN.update_one(
                                    {"_id": ctx.guild.id}, {"$set": {f"pve.lobby.user.{str(ctx.author.id)}": datetime.datetime.now()}})
                            
                            embed = discord.Embed()
                            embed.set_author(name=ctx.author.name + f" bergabung untuk menyerang {enemy_name} ({enemy_class})", icon_url=ctx.author.display_avatar)

                            await  ctx.message.channel.send(embed=embed)
                            logging.info(f"{ctx.author.name} joined {enemy_name}")
                        else:
                            await db.SPAWN.update_one(
                                {"pve.status": "active"}, {
                                    "$set": {
                                        "pve.bar.hp": total_hp,
                                        }
                                    }
                                )
                            
                            enemy_expire_at = pve.get("expire_at", {})
                            add_expire = enemy_expire_at + timedelta(minutes=var.expired_enemy)
                            await db.SPAWN.update_one(
                                {"_id": ctx.guild.id}, {"$set": {
                                    f"pve.lobby.log.attacker.{ctx.author.id}_{ObjectId()}": head_str,
                                    f"pve.expire_at": add_expire,
                                      }}
                                )
                            
                            if enemy_hp <= 1:
                                await ctx.channel.send(f"```c\nini adalah kemenangan kalian, yeay!```")
                                await self.result_pve(ctx, pve)
                            else:
                                await ctx.channel.send(f"```c\n{ctx.author.name} menyerang {enemy_name}({enemy_class}) dengan damage serangan {head_str}, Monster mempunyai {total_hp} hp```")
                                logging.info(f"{ctx.author.name} .attack {enemy_name}")
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
        enemy_attacker = pve.get("lobby", {}).get("log", {}).get("attacker", {})
        if isinstance(enemy_attacker, dict):
            code_sum = {}
            for key, value in enemy_attacker.items():
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