




import discord
from discord import app_commands
from discord.ext import commands

import database as db

import typing
from PIL import Image, ImageDraw, ImageFont
import requests

class profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="set_profile", description="Setting Profile bio")
    async def set_profile(self, interaction: discord.Interaction, bio: str):
        player = await db.player[f"{interaction.guild.id}"].find_one({"_id": interaction.user.id})
        if player is None:
            await db.player[f"{interaction.guild.id}"].insert_one(
                {
                    "_id": interaction.user.id,
                    "profile": {
                        "bio": bio
                        },
                    "game": {}
                    }
                )
            await interaction.response.send_message(f"Yeay! Kamu sudah mengatur biomu, sekarang kamu bisa join Game dari server ini")
        else:
            await db.player[f"{interaction.guild.id}"].update_one(
                {"_id": interaction.user.id},
                    {
                        "$set": {
                            "profile.bio": bio
                            }
                        }
                    )
            await interaction.response.send_message(f"Kamu sudah memperbarui bio kamu")
        
    @app_commands.command(name="profile", description="Profile")
    @app_commands.describe(game="Refreshing")
    @app_commands.choices(
        game=[
            app_commands.Choice(name="RPG", value="0"),
            app_commands.Choice(name="Unknown", value="1")
            ]
        )
    async def profile(self, interaction:discord.Interaction, member:discord.Member, game: typing.Optional[app_commands.Choice[str]] = None,):
        if member is None and game is None:
            await interaction.response.send_message("ya kamu harus milih dulu dong dengan pilihan yang sudah tersedia")
        elif game is None:
            await interaction.response.send_message(f"ini profilmu {member}")
        elif member is None:
            await interaction.response.send_message(f"Kamu harus memilih membernya terlebih dulu")
        else:
            if game.value == "0":
                player = await db.player[f"{interaction.guild.id}"].find_one({"_id": member.id})
                if player is None:
                    await interaction.response.send_message("User belum set_profile")
                else:
                    check = player.get("game", {}).get("rpg", {})
                    if check is not None and check :
                        with Image.open("assets/rpg/profile/default.jpg") as a:
                            username = interaction.user.name
                            avatar = interaction.user.display_avatar
                            ava = Image.open(requests.get(avatar, stream=True).raw)
                            a.paste(ava.resize((64, 64)), (4, 24))
                            b = ImageDraw.Draw(a)
                            e = ImageFont.truetype("assets/font/Diablo Heavy.ttf", 16)
                            c = ImageFont.truetype("assets/font/Diablo Heavy.ttf", 10)

                            head_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("head", {})
                            if head_data :
                                head_name = head_data.get("name", None)
                                head_id, head_str, head_vit, head_int, head_agi, head_fire, head_water, head_wind, head_earth = (head_data.get(key, 0) for key in ("id_item", "str", "vit", "int", "agi", "fire", "water", "wind", "earth"))
                                head_humbnail = Image.open(f"assets/rpg/item/head/{head_id}.png")
                                head_icon = Image.open(f"assets/rpg/item/head/{head_id}.png")
                                a.paste(head_humbnail.resize((80, 80)), (394, 6))
                                a.paste(head_icon.resize((22, 22)), (5, 153))
                                b.text((34, 151),f"{head_name}\nSTR{head_str}|VIT{head_vit}|INT{head_int}|AGI{head_agi}|F{head_fire}|W{head_water}|W{head_wind}|E{head_earth}", font=c, fill="white")
                            else:
                                head_str = head_vit = head_int = head_agi = head_fire = head_water = head_wind = head_earth = 0

                            necklace1_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("necklace1", {})
                            necklace1_id = necklace1_data.get("id_item", None)
                            necklace1_name = necklace1_data.get("name", None)
                            necklace1_str = necklace1_data.get("str", 0)
                            necklace1_vit = necklace1_data.get("vit", 0)
                            necklace1_int = necklace1_data.get("int", 0)
                            necklace1_agi = necklace1_data.get("agi", 0)
                            necklace1_fire = necklace1_data.get("fire", 0)
                            necklace1_water = necklace1_data.get("water", 0)
                            necklace1_wind = necklace1_data.get("wind", 0)
                            necklace1_earth = necklace1_data.get("earth", 0)
                            if necklace1_id is not None:
                                necklace1_thumbnail = Image.open(f"assets/rpg/item/necklace/{necklace1_id}.png")
                                necklace1_icon = Image.open(f"assets/rpg/item/necklace/{necklace1_id}.png")
                                a.paste(necklace1_thumbnail.resize((80, 80)), (295, 77))
                                a.paste(necklace1_icon.resize((22, 22)), (5, 181))
                                b.text((34, 179), f"{necklace1_name}\nSTR{necklace1_str}|VIT{necklace1_vit}|INT{necklace1_int}|AGI{necklace1_agi}|F{necklace1_fire}|W{necklace1_water}|W{necklace1_wind}|E{necklace1_earth}", font=c, fill="white")
                            else:
                                pass

                            necklace2_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("necklace2", {})
                            necklace2_id = necklace2_data.get("id_item", None)
                            necklace2_name = necklace2_data.get("name", None)
                            necklace2_str = necklace2_data.get("str", 0)
                            necklace2_vit = necklace2_data.get("vit", 0)
                            necklace2_int = necklace2_data.get("int", 0)
                            necklace2_agi = necklace2_data.get("agi", 0)
                            necklace2_fire = necklace2_data.get("fire", 0)
                            necklace2_water = necklace2_data.get("water", 0)
                            necklace2_wind = necklace2_data.get("wind", 0)
                            necklace2_earth = necklace2_data.get("earth", 0)
                            if necklace2_id is not None:
                                necklace2_thumbnail = Image.open(f"assets/rpg/item/necklace/{necklace2_id}.png")
                                necklace2_icon = Image.open(f"assets/rpg/item/necklace/{necklace2_id}.png")
                                a.paste(necklace2_thumbnail.resize((80, 80)), (491, 77))
                                a.paste(necklace2_icon.resize((22, 22)), (5, 209))
                                b.text((34, 207), f"{necklace2_name}\nSTR{necklace2_str}|VIT{necklace2_vit}|INT{necklace2_int}|AGI{necklace2_agi}|F{necklace2_fire}|W{necklace2_water}|W{necklace2_wind}|E{necklace2_earth}", font=c, fill="white")
                            else:
                                pass

                            body_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("body", {})
                            body_id = body_data.get("id_item", None)
                            body_name = body_data.get("name", None)
                            body_str = body_data.get("str", 0)
                            body_vit = body_data.get("vit", 0)
                            body_int = body_data.get("int", 0)
                            body_agi = body_data.get("agi", 0)
                            body_fire = body_data.get("fire", 0)
                            body_water = body_data.get("water", 0)
                            body_wind = body_data.get("wind", 0)
                            body_earth = body_data.get("earth", 0)
                            if body_id is not None:
                                body_thumbnail = Image.open(f"assets/rpg/item/body/{body_id}.png")
                                body_icon = Image.open(f"assets/rpg/item/body/{body_id}.png")
                                a.paste(body_thumbnail.resize((100, 142)), (384, 94))
                                a.paste(body_icon.resize((16, 22)), (8, 237))
                                b.text((34, 235), f"{body_name}\nSTR{body_str}|VIT{body_vit}|INT{body_int}|AGI{body_agi}|F{body_fire}|W{body_water}|W{body_wind}|E{body_earth}", font=c, fill="white")
                            else:
                                pass

                            gloves1_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("gloves1", {})
                            gloves1_id = gloves1_data.get("id_item", None)
                            gloves1_name = gloves1_data.get("name", None)
                            gloves1_str = gloves1_data.get("str", 0)
                            gloves1_vit = gloves1_data.get("vit", 0)
                            gloves1_int = gloves1_data.get("int", 0)
                            gloves1_agi = gloves1_data.get("agi", 0)
                            gloves1_fire = gloves1_data.get("fire", 0)
                            gloves1_water = gloves1_data.get("water", 0)
                            gloves1_wind = gloves1_data.get("wind", 0)
                            gloves1_earth = gloves1_data.get("earth", 0)
                            if gloves1_id is not None:
                                gloves1_thumbnail = Image.open(f"assets/rpg/item/body/{gloves1_id}.png")
                                gloves1_icon = Image.open(f"assets/rpg/item/body/{gloves1_id}.png")
                                a.paste(gloves1_thumbnail.resize((100, 142)), (384, 94))
                                a.paste(gloves1_icon.resize((16, 22)), (8, 237))
                                b.text((34, 235), f"{gloves1_name}\nSTR{gloves1_str}|VIT{gloves1_vit}|INT{gloves1_int}|AGI{gloves1_agi}|F{gloves1_fire}|W{gloves1_water}|W{gloves1_wind}|E{gloves1_earth}", font=c, fill="white")
                            else:
                                pass

                            gloves2_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("gloves2", {})
                            gloves2_id = gloves2_data.get("id_item", None)
                            gloves2_name = gloves2_data.get("name", None)
                            gloves2_str = gloves2_data.get("str", 0)
                            gloves2_vit = gloves2_data.get("vit", 0)
                            gloves2_int = gloves2_data.get("int", 0)
                            gloves2_agi = gloves2_data.get("agi", 0)
                            gloves2_fire = gloves2_data.get("fire", 0)
                            gloves2_water = gloves2_data.get("water", 0)
                            gloves2_wind = gloves2_data.get("wind", 0)
                            gloves2_earth = gloves2_data.get("earth", 0)
                            if gloves2_id is not None:
                                gloves2_thumbnail = Image.open(f"assets/rpg/item/body/{gloves2_id}.png")
                                gloves2_icon = Image.open(f"assets/rpg/item/body/{gloves2_id}.png")
                                a.paste(gloves2_thumbnail.resize((100, 142)), (384, 94))
                                a.paste(gloves2_icon.resize((16, 22)), (8, 237))
                                b.text((34, 235), f"{gloves2_name}\nSTR{gloves2_str}|VIT{gloves2_vit}|INT{gloves2_int}|AGI{gloves2_agi}|F{gloves2_fire}|W{gloves2_water}|W{gloves2_wind}|E{gloves2_earth}", font=c, fill="white")
                            else:
                                pass

                            belt_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("belt", {})
                            belt_id = belt_data.get("id_item", None)
                            belt_name = belt_data.get("name", None)
                            belt_str = belt_data.get("str", 0)
                            belt_vit = belt_data.get("vit", 0)
                            belt_int = belt_data.get("int", 0)
                            belt_agi = belt_data.get("agi", 0)
                            belt_fire = belt_data.get("fire", 0)
                            belt_water = belt_data.get("water", 0)
                            belt_wind = belt_data.get("wind", 0)
                            belt_earth = belt_data.get("earth", 0)
                            if belt_id is not None:
                                belt_thumbnail = Image.open(f"assets/rpg/item/body/{belt_id}.png")
                                belt_icon = Image.open(f"assets/rpg/item/body/{belt_id}.png")
                                a.paste(belt_thumbnail.resize((100, 142)), (384, 94))
                                a.paste(belt_icon.resize((16, 22)), (8, 237))
                                b.text((34, 235), f"{belt_name}\nSTR{belt_str}|VIT{belt_vit}|INT{belt_int}|AGI{belt_agi}|F{belt_fire}|W{belt_water}|W{belt_wind}|E{belt_earth}", font=c, fill="white")
                            else:
                                pass

                            ring1_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("ring1", {})
                            ring1_id = ring1_data.get("id_item", None)
                            ring1_name = ring1_data.get("name", None)
                            ring1_str = ring1_data.get("str", 0)
                            ring1_vit = ring1_data.get("vit", 0)
                            ring1_int = ring1_data.get("int", 0)
                            ring1_agi = ring1_data.get("agi", 0)
                            ring1_fire = ring1_data.get("fire", 0)
                            ring1_water = ring1_data.get("water", 0)
                            ring1_wind = ring1_data.get("wind", 0)
                            ring1_earth = ring1_data.get("earth", 0)
                            if ring1_id is not None:
                                ring1_thumbnail = Image.open(f"assets/rpg/item/body/{ring1_id}.png")
                                ring1_icon = Image.open(f"assets/rpg/item/body/{ring1_id}.png")
                                a.paste(ring1_thumbnail.resize((100, 142)), (384, 94))
                                a.paste(ring1_icon.resize((16, 22)), (8, 237))
                                b.text((34, 235), f"{ring1_name}\nSTR{ring1_str}|VIT{ring1_vit}|INT{ring1_int}|AGI{ring1_agi}|F{ring1_fire}|W{ring1_water}|W{ring1_wind}|E{ring1_earth}", font=c, fill="white")
                            else:
                                pass

                            ring2_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("ring2", {})
                            ring2_id = ring2_data.get("id_item", None)
                            ring2_name = ring2_data.get("name", None)
                            ring2_str = ring2_data.get("str", 0)
                            ring2_vit = ring2_data.get("vit", 0)
                            ring2_int = ring2_data.get("int", 0)
                            ring2_agi = ring2_data.get("agi", 0)
                            ring2_fire = ring2_data.get("fire", 0)
                            ring2_water = ring2_data.get("water", 0)
                            ring2_wind = ring2_data.get("wind", 0)
                            ring2_earth = ring2_data.get("earth", 0)
                            if ring2_id is not None:
                                ring2_thumbnail = Image.open(f"assets/rpg/item/body/{ring2_id}.png")
                                ring2_icon = Image.open(f"assets/rpg/item/body/{ring2_id}.png")
                                a.paste(ring2_thumbnail.resize((100, 142)), (384, 94))
                                a.paste(ring2_icon.resize((16, 22)), (8, 237))
                                b.text((34, 235), f"{ring2_name}\nSTR{ring2_str}|VIT{ring2_vit}|INT{ring2_int}|AGI{ring2_agi}|F{ring2_fire}|W{ring2_water}|W{ring2_wind}|E{ring2_earth}", font=c, fill="white")
                            else:
                                pass

                            pants_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("pants", {})
                            pants_id = pants_data.get("id_item", None)
                            pants_name = pants_data.get("name", None)
                            pants_str = pants_data.get("str", 0)
                            pants_vit = pants_data.get("vit", 0)
                            pants_int = pants_data.get("int", 0)
                            pants_agi = pants_data.get("agi", 0)
                            pants_fire = pants_data.get("fire", 0)
                            pants_water = pants_data.get("water", 0)
                            pants_wind = pants_data.get("wind", 0)
                            pants_earth = pants_data.get("earth", 0)
                            if pants_id is not None:
                                pants_thumbnail = Image.open(f"assets/rpg/item/body/{pants_id}.png")
                                pants_icon = Image.open(f"assets/rpg/item/body/{pants_id}.png")
                                a.paste(pants_thumbnail.resize((100, 142)), (384, 94))
                                a.paste(pants_icon.resize((16, 22)), (8, 237))
                                b.text((34, 235), f"{pants_name}\nSTR{pants_str}|VIT{pants_vit}|INT{pants_int}|AGI{pants_agi}|F{pants_fire}|W{pants_water}|W{pants_wind}|E{pants_earth}", font=c, fill="white")
                            else:
                                pass

                            hand1_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("hand1", {})
                            hand1_id = hand1_data.get("id_item", None)
                            hand1_name = hand1_data.get("name", None)
                            hand1_str = hand1_data.get("str", 0)
                            hand1_vit = hand1_data.get("vit", 0)
                            hand1_int = hand1_data.get("int", 0)
                            hand1_agi = hand1_data.get("agi", 0)
                            hand1_fire = hand1_data.get("fire", 0)
                            hand1_water = hand1_data.get("water", 0)
                            hand1_wind = hand1_data.get("wind", 0)
                            hand1_earth = hand1_data.get("earth", 0)
                            if hand1_id is not None:
                                hand1_thumbnail = Image.open(f"assets/rpg/item/body/{hand1_id}.png")
                                hand1_icon = Image.open(f"assets/rpg/item/body/{hand1_id}.png")
                                a.paste(hand1_thumbnail.resize((100, 142)), (384, 94))
                                a.paste(hand1_icon.resize((16, 22)), (8, 237))
                                b.text((34, 235), f"{hand1_name}\nSTR{hand1_str}|VIT{hand1_vit}|INT{hand1_int}|AGI{hand1_agi}|F{hand1_fire}|W{hand1_water}|W{hand1_wind}|E{hand1_earth}", font=c, fill="white")
                            else:
                                pass

                            hand2_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("hand2", {})
                            hand2_id = hand2_data.get("id_item", None)
                            hand2_name = hand2_data.get("name", None)
                            hand2_str = hand2_data.get("str", 0)
                            hand2_vit = hand2_data.get("vit", 0)
                            hand2_int = hand2_data.get("int", 0)
                            hand2_agi = hand2_data.get("agi", 0)
                            hand2_fire = hand2_data.get("fire", 0)
                            hand2_water = hand2_data.get("water", 0)
                            hand2_wind = hand2_data.get("wind", 0)
                            hand2_earth = hand2_data.get("earth", 0)
                            if hand2_id is not None:
                                hand2_thumbnail = Image.open(f"assets/rpg/item/body/{hand2_id}.png")
                                hand2_icon = Image.open(f"assets/rpg/item/body/{hand2_id}.png")
                                a.paste(hand2_thumbnail.resize((100, 142)), (384, 94))
                                a.paste(hand2_icon.resize((16, 22)), (8, 237))
                                b.text((34, 235), f"{hand2_name}\nSTR{hand2_str}|VIT{hand2_vit}|INT{hand2_int}|AGI{hand2_agi}|F{hand2_fire}|W{hand2_water}|W{hand2_wind}|E{hand2_earth}", font=c, fill="white")
                            else:
                                pass

                            boots_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("boots", {})
                            boots_id = boots_data.get("id_item", None)
                            boots_name = boots_data.get("name", None)
                            boots_str = boots_data.get("str", 0)
                            boots_vit = boots_data.get("vit", 0)
                            boots_int = boots_data.get("int", 0)
                            boots_agi = boots_data.get("agi", 0)
                            boots_fire = boots_data.get("fire", 0)
                            boots_water = boots_data.get("water", 0)
                            boots_wind = boots_data.get("wind", 0)
                            boots_earth = boots_data.get("earth", 0)
                            if boots_id is not None:
                                boots_thumbnail = Image.open(f"assets/rpg/item/body/{boots_id}.png")
                                boots_icon = Image.open(f"assets/rpg/item/body/{boots_id}.png")
                                a.paste(boots_thumbnail.resize((100, 142)), (384, 94))
                                a.paste(boots_icon.resize((16, 22)), (8, 237))
                                b.text((34, 235), f"{boots_name}\nSTR{boots_str}|VIT{boots_vit}|INT{boots_int}|AGI{boots_agi}|F{boots_fire}|W{boots_water}|W{boots_wind}|E{boots_earth}", font=c, fill="white")
                            else:
                                pass
                
                            bar = player.get("game", {}).get("rpg", {}).get("bar", {})
                            exp = bar.get("exp", {})
                            hp = bar.get("hp", {})
                            mana = bar.get("mana", {})

                            stats = player.get("game", {}).get("rpg", {}).get("stats", {})
                            strength = stats.get("str", {})
                            vitality = stats.get("vit", {})
                            inteligent = stats.get("int", {})                            
                            agility = stats.get("agi", {})

                            attribut = player.get("game", {}).get("rpg", {}).get("attribut", {})
                            fire = attribut.get("fire", {})
                            water = attribut.get("water", {})
                            earth = attribut.get("earth", {})
                            wind = attribut.get("wind", {})

                            stats_str = head_str + necklace1_str + necklace2_str + body_str + gloves1_str + gloves2_str + belt_str + ring1_str + ring2_str + pants_str + hand1_str + hand2_str + boots_str
                            stats_vit = head_vit + necklace1_vit + necklace2_vit + body_vit + gloves1_vit + gloves2_vit + belt_vit + ring1_vit + ring2_vit + pants_vit + hand1_vit + hand2_vit + boots_vit
                            stats_int = head_int + necklace1_int + necklace2_int + body_int + gloves1_int + gloves2_int + belt_int + ring1_int + ring2_int + pants_int + hand1_int + hand2_int + boots_int
                            stats_agi = head_agi + necklace1_agi + necklace2_agi + body_agi + gloves1_agi + gloves2_agi + belt_agi + ring1_agi + ring2_agi + pants_agi + hand1_agi + hand2_agi + boots_agi
                            stats_fire = head_fire + necklace1_fire + necklace2_fire + body_fire + gloves1_fire + gloves2_fire + belt_fire + ring1_fire + ring2_fire + pants_fire + hand1_fire + hand2_fire + boots_fire
                            stats_water = head_water + necklace1_water + necklace2_water + body_water + gloves1_water + gloves2_water + belt_water + ring1_water + ring2_water + pants_water + hand1_water + hand2_water + boots_water
                            stats_wind = head_wind + necklace1_wind + necklace2_wind + body_wind + gloves1_wind + gloves2_wind + belt_wind + ring1_wind + ring2_wind + pants_wind + hand1_wind + hand2_wind + boots_wind
                            stats_earth = head_earth + necklace1_earth + necklace2_earth + body_earth + gloves1_earth + gloves2_earth + belt_earth + ring1_earth + ring2_earth + pants_earth + hand1_earth + hand2_earth + boots_earth

                            attack = stats_agi*(1+(2/100))+stats_str*(1+(4/100))

                            b.text((4, 2), f"LVL 10 | {username}", font=e, fill="white")
                            b.text((4, 89), f"HP\n{hp}/1200\nMANA\n{mana}/2000", font=c, fill="white")
                            b.text((72, 33), f"VIT\nAGI\nINT\nSTR\nFIRE\nWIND\nWATER\nEARTH", font=c, fill="white")
                            b.text((115, 33), ":\n:\n:\n:\n:\n:\n:\n:", font=c, fill="white")
                            b.text((120, 33), f"{vitality}+{stats_vit}\n{agility}+{stats_agi}\n{inteligent}+{stats_int}\n{strength}+{stats_str}\n{fire}+{stats_fire}\n{wind}+{stats_wind}\n{water}+{stats_water}\n{earth}+{stats_earth}", font=c, fill="white")
                            b.text((180, 33), f"ATK\nASPD\nDEF\nMDEF\nMATK\nCRIT\nPOINT\nGUILD", font=c, fill="white")
                            b.text((216, 33), ":\n:\n:\n:\n:\n:\n:\n:", font=c, fill="white")
                            b.text((221, 33), f"{attack}\n10\n10\n10\n10\n10\n10\n10", font=c, fill="white")

                            a.save(f"stats/rpg/profile/{interaction.guild.id}.jpg")
                            await interaction.response.send_message(file=discord.File(f"stats/rpg/profile/{interaction.guild.id}.jpg"))
                            #await interaction.response.send_message("user sudah punya game rpg")
                    else:
                        await interaction.response.send_message("user belum punya game rpg")
            elif game.value == "1":
                await interaction.response.send_message("Unknown")

async def setup(bot):
    await bot.add_cog(profile(bot))