import discord
from discord.ext import commands

import os
from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Base {bot.user.name} ({bot.user.id}) on {len(bot.guilds)} Server, Online!')

@bot.event
async def setup_hook() -> None:
    extensions = [
        'cogs.activity.on_interaction',
        'cogs.commands.basic',
        'cogs.commands.language',
        'cogs.commands.register',
        'cogs.commands.profile',
        'cogs.commands.join',
        'rpg.commands.test_equip',
        'rpg.commands.pve',
        'rpg.activity.spawn',
        ]
    
    for extension in extensions:
        await bot.load_extension(extension)

bot.run(os.getenv("TOKEN"))