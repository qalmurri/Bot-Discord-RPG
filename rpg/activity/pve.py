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
            channel_pve = setting.get("channel_pve", {})
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
                        await message.channel.send(f"{message.author.name} menyerang monster")
            else:
                pass
        else:
            print("bukan serang")
            
            

async def setup(bot):
    await bot.add_cog(pve(bot))