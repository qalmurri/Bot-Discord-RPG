from discord.ext import commands
import database as db

class pve(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
     
        if message.content  == "attack":
            setting = await db.setting["guild"].find_one({"_id": message.guild.id})
            pve = setting.get("pve", {})
            channel_pve = pve.get("channel_id", {})
            if str(message.channel.id) == channel_pve:
                await message.delete()
                player = await db.player[f"{message.guild.id}"].find_one({"_id": message.author.id})
                if player is None:
                    await message.channel.send("belum set profile")
                else:
                    check = player.get("game", {}).get("rpg", None)
                    if check is None:
                        await message.channel.send("belum join rpg")
                    else:
                        environment = await db.environment[str(message.guild.id)].find_one({"status": True})
                        if environment is None:
                            await message.channel.send("belum spawn monster woi")
                        else:
                            head_stats = player.get("game", {}).get("rpg", {}).get("use", {}).get("head", {}).get("stats", {})
                            head_str, head_vit, head_int, head_agi, head_fire, head_water, head_wind, head_earth = (head_stats.get(key, 0) for key in ("str", "vit", "int", "agi", "fire", "water", "wind", "earth"))
                            
                            environment_stats = environment.get("stats", {})
                            environment_hp = environment_stats.get("hp", {})

                            total_hp = environment_hp - head_str

                            lobby_user = await db.environment[str(message.guild.id)].find_one({"_id": message.channel.id})
                            if lobby_user is None:
                                print("channel tidak ada")
                            else:
                                print("channel ada")
                            #    await db.environment[f"{message.guild.id}"].update_one({"status": True}, {
                            #        "$push": {
                            #                "lobby.user": message.author.id,
                            #            }})
                            #else:
                            #    pass

                            #await db.environment[f"{message.guild.id}"].update_one(
                            #    {"status": True}, {
                            #        "$set": {
                            #            "stats.hp": total_hp,
                            #            }
                            #        }
                            #    )
                            #await message.channel.send(f"{message.author.name} menyerang monster, mengurangi {head_str} point dari {environment_hp}hp monster")
            else:
                pass
        else:
            print("bukan serang")
            
            

async def setup(bot):
    await bot.add_cog(pve(bot))