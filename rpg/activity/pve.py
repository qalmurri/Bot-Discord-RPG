import discord
from discord.ext import commands
import database as db
import datetime
from bson import ObjectId

class pve_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(case_insensitive=True)
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
                        print(pve)
                        if lobby is None:
                            await db.SPAWN.update_one(
                                    {"_id": ctx.guild.id}, {"$set": {f"pve.lobby.user.{str(ctx.author.id)}": datetime.datetime.now()}})
                            
                            embed = discord.Embed()
                            embed.set_author(name=ctx.author.name + f" bergabung untuk menyerang {environment_name} ({environment_class})", icon_url=ctx.author.display_avatar)

                            await  ctx.message.channel.send(embed=embed)
                        else:
                            print("player menyerang monster")
                                


        
        #await ctx.send(f"{ctx.author.mention} menyerang!")

async def setup(bot):
    await bot.add_cog(pve_commands(bot))