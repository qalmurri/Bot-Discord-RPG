import discord
from discord import app_commands
from discord.ext import commands

import typing
import database as db

class equip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='equip', description="Test Equip")
    @app_commands.describe(item="Change")
    @app_commands.choices(
        item=[
            app_commands.Choice(name="head", value="0"),
            app_commands.Choice(name="necklace1", value="1"),
            app_commands.Choice(name="necklace2", value="2"),
            app_commands.Choice(name="body", value="3"),
            app_commands.Choice(name="gloves1", value="4"),
            app_commands.Choice(name="gloves2", value="5"),
            app_commands.Choice(name="belt", value="6"),
            app_commands.Choice(name="ring1", value="7"),
            app_commands.Choice(name="ring2", value="8"),
            app_commands.Choice(name="pants", value="9"),
            app_commands.Choice(name="hand1", value="10"),
            app_commands.Choice(name="hand2", value="11"),
            app_commands.Choice(name="boots", value="12"),
            ],
        )
    async def equip(self, interaction: discord.Interaction, item: typing.Optional[app_commands.Choice[str]] = None):
        player = await db.PLAYER_USER.find_one({"game.rpg.status": "active"})
        if player is None:
            await interaction.response.send_message("Kamu belum mempunyai game rpg")
        elif item.value == str(0):
            await db.PLAYER_USER.update_one(
                {
                    "_id": interaction.user.id
                    },
                    {
                        "$set": {
                            "game.rpg.use.head": {
                                "id_item": 0,
                                "id_image": "co001",
                                "set_item": None,
                                "name": "HEAD",
                                "class": "common",
                                "price": 1000,
                                "stats": {
                                    "str": 10,
                                    "vit": 10,
                                    "int": 10,
                                    "agi": 10,
                                    "fire": 10,
                                    "wind": 10,
                                    "water": 10,
                                    "earth": 10,
                                    }
                                }
                            }
                        }
                    )
            await interaction.response.send_message("head sudah terpasang")
        elif item.value == str(1):
            await db.PLAYER_USER.update_one(
                {
                    "_id": interaction.user.id
                    },
                    {
                        "$set": {
                            "game.rpg.use.necklace1": {
                                "id_item": 0,
                                "id_image": "co001",
                                "set_item": None,
                                "name": "NECKLACE1",
                                "class": "common",
                                "price": 1000,
                                "stats": {
                                    "str": 10,
                                    "vit": 10,
                                    "int": 10,
                                    "agi": 10,
                                    "fire": 10,
                                    "wind": 10,
                                    "water": 10,
                                    "earth": 10,
                                    }
                                }
                            }
                        }
                    )
            await interaction.response.send_message("necklace1 sudah terpasang")
        elif item.value == str(2):
            await db.PLAYER_USER.update_one(
                {
                    "_id": interaction.user.id
                    },
                    {
                        "$set": {
                            "game.rpg.use.necklace2": {
                                "id_item": 0,
                                "id_image": "co001",
                                "set_item": None,
                                "name": "NECKLACE2",
                                "class": "common",
                                "price": 1000,
                                "stats": {
                                    "str": 10,
                                    "vit": 10,
                                    "int": 10,
                                    "agi": 10,
                                    "fire": 10,
                                    "wind": 10,
                                    "water": 10,
                                    "earth": 10,
                                    }
                                }
                            }
                        }
                    )
            await interaction.response.send_message("necklace2 sudah terpasang")
        elif item.value == str(3):
            await db.PLAYER_USER.update_one(
                {
                    "_id": interaction.user.id
                    },
                    {
                        "$set": {
                            "game.rpg.use.body": {
                                "id_item": 0,
                                "id_image": "co001",
                                "set_item": None,
                                "name": "BODY",
                                "class": "common",
                                "price": 1000,
                                "stats": {
                                    "str": 10,
                                    "vit": 10,
                                    "int": 10,
                                    "agi": 10,
                                    "fire": 10,
                                    "wind": 10,
                                    "water": 10,
                                    "earth": 10,
                                    }
                                }
                            }
                        }
                    )
            await interaction.response.send_message("body sudah terpasang")
        elif item.value == str(4):
            await db.PLAYER_USER.update_one(
                {
                    "_id": interaction.user.id
                    },
                    {
                        "$set": {
                            "game.rpg.use.gloves1": {
                                "id_item": 0,
                                "id_image": "co001",
                                "set_item": None,
                                "name": "GLOVES1",
                                "class": "common",
                                "price": 1000,
                                "stats": {
                                    "str": 10,
                                    "vit": 10,
                                    "int": 10,
                                    "agi": 10,
                                    "fire": 10,
                                    "wind": 10,
                                    "water": 10,
                                    "earth": 10,
                                    }
                                }
                            }
                        }
                    )
            await interaction.response.send_message("gloves1 sudah terpasang")
        elif item.value == str(5):
            await db.PLAYER_USER.update_one(
                {
                    "_id": interaction.user.id
                    },
                    {
                        "$set": {
                            "game.rpg.use.gloves2": {
                                "id_item": 0,
                                "id_image": "co001",
                                "set_item": None,
                                "name": "GLOVES2",
                                "class": "common",
                                "price": 1000,
                                "stats": {
                                    "str": 10,
                                    "vit": 10,
                                    "int": 10,
                                    "agi": 10,
                                    "fire": 10,
                                    "wind": 10,
                                    "water": 10,
                                    "earth": 10,
                                    }
                                }
                            }
                        }
                    )
            await interaction.response.send_message("gloves2 sudah terpasang")
        elif item.value == str(6):
            await db.PLAYER_USER.update_one(
                {
                    "_id": interaction.user.id
                    },
                    {
                        "$set": {
                            "game.rpg.use.belt": {
                                "id_item": 0,
                                "id_image": "co001",
                                "set_item": None,
                                "name": "BELT",
                                "class": "common",
                                "price": 1000,
                                "stats": {
                                    "str": 10,
                                    "vit": 10,
                                    "int": 10,
                                    "agi": 10,
                                    "fire": 10,
                                    "wind": 10,
                                    "water": 10,
                                    "earth": 10,
                                    }
                                }
                            }
                        }
                    )
            await interaction.response.send_message("belt sudah terpasang")
        elif item.value == str(7):
            await db.PLAYER_USER.update_one(
                {
                    "_id": interaction.user.id
                    },
                    {
                        "$set": {
                            "game.rpg.use.ring1": {
                                "id_item": 0,
                                "id_image": "co001",
                                "set_item": None,
                                "name": "RING1",
                                "class": "common",
                                "price": 1000,
                                "stats": {
                                    "str": 10,
                                    "vit": 10,
                                    "int": 10,
                                    "agi": 10,
                                    "fire": 10,
                                    "wind": 10,
                                    "water": 10,
                                    "earth": 10,
                                    }
                                }
                            }
                        }
                    )
            await interaction.response.send_message("ring1 sudah terpasang")
        elif item.value == str(8):
            await db.PLAYER_USER.update_one(
                {
                    "_id": interaction.user.id
                    },
                    {
                        "$set": {
                            "game.rpg.use.ring2": {
                                "id_item": 0,
                                "id_image": "co001",
                                "set_item": None,
                                "name": "RING2",
                                "class": "common",
                                "price": 1000,
                                "stats": {
                                    "str": 10,
                                    "vit": 10,
                                    "int": 10,
                                    "agi": 10,
                                    "fire": 10,
                                    "wind": 10,
                                    "water": 10,
                                    "earth": 10,
                                    }
                                }
                            }
                        }
                    )
            await interaction.response.send_message("ring2 sudah terpasang")
        elif item.value == str(9):
            await db.PLAYER_USER.update_one(
                {
                    "_id": interaction.user.id
                    },
                    {
                        "$set": {
                            "game.rpg.use.pants": {
                                "id_item": 0,
                                "id_image": "co001",
                                "set_item" : None,
                                "name": "PANTS",
                                "class": "common",
                                "price": 1000,
                                "stats": {
                                    "str": 10,
                                    "vit": 10,
                                    "int": 10,
                                    "agi": 10,
                                    "fire": 10,
                                    "wind": 10,
                                    "water": 10,
                                    "earth": 10,
                                    }
                                }
                            }
                        }
                    )
            await interaction.response.send_message("pants sudah terpasang")
        elif item.value == str(10):
            await db.PLAYER_USER.update_one(
                {
                    "_id": interaction.user.id
                    },
                    {
                        "$set": {
                            "game.rpg.use.hand1": {
                                "id_item": 0,
                                "id_image": "co001",
                                "set_item": None,
                                "name": "HAND1",
                                "class": "common",
                                "price": 1000,
                                "stats": {
                                    "str": 10,
                                    "vit": 10,
                                    "int": 10,
                                    "agi": 10,
                                    "fire": 10,
                                    "wind": 10,
                                    "water": 10,
                                    "earth": 10,
                                    }
                                }
                            }
                        }
                    )
            await interaction.response.send_message("hand1 sudah terpasang")
        elif item.value == str(11):
            await db.PLAYER_USER.update_one(
                {
                    "_id": interaction.user.id
                    },
                    {
                        "$set": {
                            "game.rpg.use.hand2": {
                                "id_item": 0,
                                "id_image": "co001",
                                "set_item": None,
                                "name": "HAND2",
                                "class": "common",
                                "price": 1000,
                                "stats": {
                                    "str": 10,
                                    "vit": 10,
                                    "int": 10,
                                    "agi": 10,
                                    "fire": 10,
                                    "wind": 10,
                                    "water": 10,
                                    "earth": 10,
                                    }
                                }
                            }
                        }
                    )
            await interaction.response.send_message("hand2 sudah terpasang")
        elif item.value == str(12):
            await db.PLAYER_USER.update_one(
                {
                    "_id": interaction.user.id
                    },
                    {
                        "$set": {
                            "game.rpg.use.boots": {
                                "id_item": 0,
                                "id_image": "co001",
                                "set_item": None,
                                "name": "BOOTS",
                                "class": "common",
                                "price": 1000,
                                "stats": {
                                    "str": 10,
                                    "vit": 10,
                                    "int": 10,
                                    "agi": 10,
                                    "fire": 10,
                                    "wind": 10,
                                    "water": 10,
                                    "earth": 10
                                    }
                                }
                            }
                        }
                    )
            await interaction.response.send_message("boots sudah terpasang")
        else:
            pass

    @app_commands.command(name='unequip', description="Test unequip")
    @app_commands.describe(item="Change")
    @app_commands.choices(
        item=[
            app_commands.Choice(name="head", value="0"),
            app_commands.Choice(name="necklace1", value="1"),
            app_commands.Choice(name="necklace2", value="2"),
            app_commands.Choice(name="body", value="3"),
            app_commands.Choice(name="gloves1", value="4"),
            app_commands.Choice(name="gloves2", value="5"),
            app_commands.Choice(name="belt", value="6"),
            app_commands.Choice(name="ring1", value="7"),
            app_commands.Choice(name="ring2", value="8"),
            app_commands.Choice(name="pants", value="9"),
            app_commands.Choice(name="hand1", value="10"),
            app_commands.Choice(name="hand2", value="11"),
            app_commands.Choice(name="boots", value="12"),
            ],
        )
    async def unequip(self, interaction: discord.Interaction, item: typing.Optional[app_commands.Choice[str]] = None):
        player = await db.PLAYER_USER.find_one({"game.rpg.status": "active"})
        if player is None:
            await interaction.response.send_message("Kamu belum mempunyai game rpg")
        elif item.value == str(0):
            await db.PLAYER_USER.update_one({"_id": interaction.user.id}, {"$unset": {"game.rpg.use.head": 1}})
            await interaction.response.send_message("head di lepas")
        elif item.value == str(1):
            await db.PLAYER_USER.update_one({"_id": interaction.user.id}, {"$unset": {"game.rpg.use.necklace1": 1}})
            await interaction.response.send_message("necklace1 di lepas")
        elif item.value == str(2):
            await db.PLAYER_USER.update_one({"_id": interaction.user.id}, {"$unset": {"game.rpg.use.necklace2": 1}})
            await interaction.response.send_message("necklace2 di lepas")
        elif item.value == str(3):
            await db.PLAYER_USER.update_one({"_id": interaction.user.id}, {"$unset": {"game.rpg.use.body": 1}})
            await interaction.response.send_message("body di lepas")
        elif item.value == str(4):
            await db.PLAYER_USER.update_one({"_id": interaction.user.id}, {"$unset": {"game.rpg.use.gloves1": 1}})
            await interaction.response.send_message("gloves1 di lepas")
        elif item.value == str(5):
            await db.PLAYER_USER.update_one({"_id": interaction.user.id}, {"$unset": {"game.rpg.use.gloves2": 1}})
            await interaction.response.send_message("gloves2 di lepas")
        elif item.value == str(6):
            await db.PLAYER_USER.update_one({"_id": interaction.user.id}, {"$unset": {"game.rpg.use.belt": 1}})
            await interaction.response.send_message("belt di lepas")
        elif item.value == str(7):
            await db.PLAYER_USER.update_one({"_id": interaction.user.id}, {"$unset": {"game.rpg.use.ring1": 1}})
            await interaction.response.send_message("ring1 di lepas")
        elif item.value == str(8):
            await db.PLAYER_USER.update_one({"_id": interaction.user.id}, {"$unset": {"game.rpg.use.ring2": 1}})
            await interaction.response.send_message("ring2 di lepas")
        elif item.value == str(9):
            await db.PLAYER_USER.update_one({"_id": interaction.user.id}, {"$unset": {"game.rpg.use.pants": 1}})
            await interaction.response.send_message("pants di lepas")
        elif item.value == str(10):
            await db.PLAYER_USER.update_one({"_id": interaction.user.id}, {"$unset": {"game.rpg.use.hand1": 1}})
            await interaction.response.send_message("hand1 di lepas")
        elif item.value == str(11):
            await db.PLAYER_USER.update_one({"_id": interaction.user.id}, {"$unset": {"game.rpg.use.hand2": 1}})
            await interaction.response.send_message("hand2 di lepas")
        elif item.value == str(12):
            await db.PLAYER_USER.update_one({"_id": interaction.user.id}, {"$unset": {"game.rpg.use.boots": 1}})
            await interaction.response.send_message("boots di lepas")
        else:
            pass

async def setup(bot):
    await bot.add_cog(equip(bot))

