import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Base {bot.user.name} ({bot.user.id}) on {len(bot.guilds)} Server, Online!')

@bot.event
async def setup_hook() -> None:
    extensions = [
        'cogs.activity.message',

        'cogs.commands.profile',
        'cogs.commands.join',
        
        'rpg.commands.equip',
        'rpg.commands.equip1',
        'rpg.commands.unequip',
        'rpg.commands.unequip1',
        ]
    
    for extension in extensions:
        await bot.load_extension(extension)

bot.run("OTY3MTcwODYxNTA3NDQwNjUw.Gt_s_3.ptw1JtxeYERmeoALBXiCwyPlPIIZ9c__boRBPY")