import discord
from discord import app_commands
from discord.ext import commands

import database as db
import variable  as var
from cogs.function import load_cogs

import datetime
import typing

class join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='join', description="Basic commands")
    @app_commands.describe(game="Refreshing", select="options")
    @app_commands.choices(game=[app_commands.Choice(name="RPG", value="0")], select=[app_commands.Choice(name="Delete", value="0")])
    async def join(self, interaction: discord.Interaction, game: typing.Optional[app_commands.Choice[str]] = None, select: typing.Optional[app_commands.Choice[str]] = None):
        language_commands =  load_cogs(self).language_commands(str(interaction.guild.id))

        if game is None and select is None:
            await interaction.response.send_message(language_commands["game_select_is_none"])
            
        elif game is None:
            await interaction.response.send_message(language_commands["game_is_none"])
        else:
            if select is None:
                if game.value == str(0):
                    await self.join_rpg(interaction, language_commands)
                else:
                    pass
            else:
                if select.value == str(0):
                    if game.value == str(0):
                        player = await db.PLAYER_USER.find_one({"game.rpg.status": "active"})
                        if player is None:
                            await interaction.response.send_message(language_commands["account_not_exist"])
                        else:
                            remove_rpg = discord.ui.View().add_item(discord.ui.Button(label="Ya", custom_id="remove_rpg"))
                            await interaction.response.send_message(language_commands["confirm_remove_rpg"], view=remove_rpg)
                    else:
                        pass
    
    async def join_rpg(self, interaction, language_commands):
        player = await db.PLAYER_USER.find_one({"_id": interaction.user.id, "game.rpg.status": "active"})
        if player is None:
            await db.PLAYER_USER.update_one(
                {
                "_id": interaction.user.id},
                {
                    "$set": {
                        "game.rpg": {
                            "status": "active",
                            "jdate": datetime.datetime.now(),
                            "pve": None,
                            "account": {
                                "point": 0,
                                "like": 0,
                                "premium": None,
                                "themes": "default",
                                "stamina": 0
                            },
                            "bar": {
                                "exp": 0,
                                "hp": 0,
                                "mana": 0
                                },
                            "bag": {
                                "coin": 0,
                                "items": {}
                                },
                            "stats": {
                                "str": 0,
                                "vit": 0,
                                "int": 0,
                                "agi": 0
                            },
                            "attribut": {
                                "fire": 0,
                                "water": 0,
                                "earth": 0,
                                "wind": 0
                                },
                            "use": {},
                            "badge": {},
                            }
                        }
                    }
                )

            check = await db.PLAYER_USER.find_one({"_id": interaction.user.id})
            if check is None:

                await interaction.response.send_message(language_commands["register_first"], ephemeral=var.register_first_ephemeral, delete_after=var.register_first_delete)
                return

            await interaction.response.send_message(language_commands["join_rpg"], ephemeral=var.join_rpg_ephemeral, delete_after=var.join_rpg_delete)
        else:
            await interaction.response.send_message(language_commands["join_rpg_again"] + f" {player['game']['rpg']['jdate'].strftime('%d/%m/%Y')}", ephemeral=var.join_rpg_again_ephemeral, delete_after=var.join_rpg_again_delete)

async def setup(bot):
    await bot.add_cog(join(bot))