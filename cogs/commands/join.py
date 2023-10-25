import discord
from discord import app_commands
from discord.ext import commands

import database as db

import datetime
import typing

class join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='join', description="Basic commands")
    @app_commands.describe(game="Refreshing", select="options")
    @app_commands.choices(game=[app_commands.Choice(name="RPG", value="0")], select=[app_commands.Choice(name="Delete", value="0")])
    async def join(self, interaction: discord.Interaction, game: typing.Optional[app_commands.Choice[str]] = None, select: typing.Optional[app_commands.Choice[str]] = None):
        if game is None and select is None:
            await interaction.response.send_message("Ya gak bisa dong hmm")
        elif game is None:
            await interaction.response.send_message("Kamu harus memilih gamenya")
        else:
            if select is None:
                if game.value == str(0):
                    await self.join_rpg(interaction)
                else:
                    pass
            else:
                if select.value == str(0):
                    if game.value == str(0):
                        player = await db.PLAYER_USER.find_one({"game.rpg.status": "active"})
                        if player is None:
                            await interaction.response.send_message("Kamu belum buat akun woi!")
                        else:
                            remove_rpg = discord.ui.View().add_item(discord.ui.Button(label="Ya", custom_id="remove_rpg"))
                            await interaction.response.send_message("Apakah kamu akan menghapus game RPG mu?", view=remove_rpg)
                    else:
                        pass
    
    async def join_rpg(self, interaction):
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
                await interaction.response.send_message("Set your profile first here `/set_profile`")
                return

            await interaction.response.send_message("You joined")
        else:
            join_date = player["game"]["rpg"]["jdate"]
            convert_join_date = join_date.strftime("%d/%m/%Y")
            await interaction.response.send_message(f"You have joined the RPG on {convert_join_date}")

    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        data = interaction.data
        custom_id = data.get('custom_id')
        if custom_id is not None:
            if custom_id == "remove_rpg":
                await self.remove_rpg(interaction)
            else:
                await interaction.response.send_message("custom_id tidak ditemukan")

    async def remove_rpg(self, interaction):
        await db.PLAYER_USER.update_one({"_id": interaction.user.id}, {"$unset": {"game.rpg": {}}})
        await interaction.response.send_message("Game RPGmu sudah terhapus")

async def setup(bot):
    await bot.add_cog(join(bot))