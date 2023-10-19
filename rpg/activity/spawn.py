from discord.ext import commands
import database as db

class spawn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        pass
            
            

async def setup(bot):
    await bot.add_cog(spawn(bot))