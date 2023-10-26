import discord
from discord import app_commands
from discord.ext import commands

import database as db
from cogs.function import load_cogs
from rpg.commands.profile import profile_rpg

import typing


class profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="profile", description="Profile")
    @app_commands.describe(game="Refreshing")
    @app_commands.choices(game=[app_commands.Choice(name="RPG", value="0")])
    async def profile(self, interaction:discord.Interaction, member:discord.Member, game: typing.Optional[app_commands.Choice[str]] = None):
        language =  load_cogs(self).language(str(interaction.guild.id))

        if member is None and game is None:
            await interaction.response.send_message(language["member_game_is_none"])
        elif game is None:
            await interaction.response.send_message(language["game_is_none"] + str(member))
        elif member is None:
            await interaction.response.send_message(language["member_is_none"])
        else:
            if game.value == "0":
                player = await db.PLAYER_USER.find_one({"_id": member.id})
                if player is None:
                    await interaction.response.send_message("User belum register")
                else:
                    check = player.get("game", {}).get("rpg", {})
                    if check is not None and check :
                        await profile_rpg(interaction, member, player)
                    else:
                        await interaction.response.send_message("user belum punya game rpg")
            else:
                pass

async def setup(bot):
    await bot.add_cog(profile(bot))