from discord.ext import commands
import database as db
import datetime
from bson import ObjectId

class pve(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
     
        if message.content  == "attack":
            setting = await db.GUILD.find_one({"_id": message.guild.id})
            pve = setting.get("pve", {})
            channel_pve = pve.get("channel_id", {})
            if str(message.channel.id) == channel_pve:
                await message.delete()
                player = await db.PLAYER_USER.find_one({"_id": message.author.id})
                if player is None:
                    await message.channel.send("belum set profile")
                else:
                    check = player.get("game", {}).get("rpg", None)
                    if check is None:
                        await message.channel.send("belum join rpg")
                    else:
                        environment = await db.ENV20.find_one({"_id": message.guild.id})
                        if environment is None:
                            await message.channel.send("belum spawn monster woi")
                        else:
                            #stats player
                            head_stats = player.get("game", {}).get("rpg", {}).get("use", {}).get("head", {}).get("stats", {})
                            head_str, head_vit, head_int, head_agi, head_fire, head_water, head_wind, head_earth = (head_stats.get(key, 0) for key in ("str", "vit", "int", "agi", "fire", "water", "wind", "earth"))

                            #stats_environment
                            environment_profile = environment.get("profile", {})
                            environment_name = environment_profile.get("name", {})
                            environment_class = environment_profile.get("class", {})

                            environment_stats = environment.get("stats", {})
                            environment_hp = environment_stats.get("hp", {})

                            #mekanisme stats

                            #HP_envirinment
                            total_hp = environment_hp - head_str

                            lobby = environment.get("lobby", {}).get("user", {}).get(str(message.author.id), None)
                            if lobby is None:
                                await db.ENV20.update_one(
                                    {"_id": message.guild.id}, {"$set": {f"lobby.user.{str(message.author.id)}": datetime.datetime.now()}}
                                    )
                                await message.channel.send(f"```c\n{message.author.name} bergabung untuk menyerang {environment_name}({environment_class})```")
                            else:
                                await db.ENV20.update_one(
                                    {"status": "active"}, {
                                        "$set": {
                                            "stats.hp": total_hp,
                                            }
                                        }
                                    )
                                await db.ENV20.update_one(
                                    {"_id": message.guild.id}, {"$set": {f"lobby.log.attacker.{message.author.id}_{ObjectId()}": head_str }}
                                    )
                                
                                if total_hp <= 1:
                                    await message.channel.send(f"```c\nini adalah kemenangan kalian, yeay!```")
                                    await self.result_pve(message, environment)
                                else:
                                    await message.channel.send(f"```c\n{message.author.name} menyerang {environment_name}({environment_class}) dengan damage serangan {head_str}, Monster mempunyai {total_hp} hp```")
            else:
                print("channel tidak di temukan")
        elif message.content  == "magic":
            setting = await db.GUILD.find_one({"_id": message.guild.id})
            pve = setting.get("pve", {})
            channel_pve = pve.get("channel_id", {})
            if str(message.channel.id) == channel_pve:
                await message.channel.send("Attack magic masi cooming soon")
                await message.delete()
        else:
            print("bukan serang")

    async def result_pve(self, message, environment):
        environment_attacker = environment.get("lobby", {}).get("log", {}).get("attacker", {})
        if isinstance(environment_attacker, dict):
            code_sum = {}
            for key, value in environment_attacker.items():
                code = key.split("_")[0]
                if code in code_sum:
                    code_sum[code] += value
                else:
                    code_sum[code] = value
            for code, total_value in code_sum.items():
                await message.channel.send(f"Total Damage:\n<@{code}>: {total_value}")
                await db.ENV20.delete_many({"_id": message.guild.id})

async def setup(bot):
    await bot.add_cog(pve(bot))