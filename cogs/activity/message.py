from discord.ext import commands
import database as db

class message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return 

        await db.MESSAGE_USER.insert_many([
            {
                "_id": message.id,
                "Info": {
                    "_ch": message.channel.id,
                    "_au": message.author.id,
                    "_gu": message.guild.id
                    },
                "msg": message.content,
            }
        ])

async def setup(bot):
    await bot.add_cog(message(bot))