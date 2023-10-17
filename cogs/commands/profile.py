




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
                        with Image.open("assets/rpg/profile/default2.jpg") as a:
                            username = interaction.user.name
                            avatar = interaction.user.display_avatar
                            ava = Image.open(requests.get(avatar, stream=True).raw)
                            a.paste(ava.resize((64, 64)), (4, 24))
                            b = ImageDraw.Draw(a)
                            e = ImageFont.truetype("assets/font/Diablo Heavy.ttf", 16)
                            c = ImageFont.truetype("assets/font/Diablo Heavy.ttf", 10)

                            head_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("head", {})
                            head_id = head_data.get("id_item", None)
                            head_name = head_data.get("name", None)
                            head_str = head_data.get("str", 0)
                            head_vit = head_data.get("vit", 0)
                            head_int = head_data.get("int", 0)
                            head_agi = head_data.get("agi", 0)
                            head_fire = head_data.get("fire", 0)
                            head_water = head_data.get("water", 0)
                            head_wind = head_data.get("wind", 0)
                            head_earth = head_data.get("earth", 0)
                            if head_id is not None:
                                head_humbnail = Image.open(f"assets/rpg/item/head/{head_id}.png")
                                head_icon = Image.open(f"assets/rpg/item/head/{head_id}.png")
                                a.paste(head_humbnail.resize((80, 80)), (394, 6))
                                a.paste(head_icon.resize((22, 22)), (5, 153))
                                b.text((34, 151), f"{head_name}\nSTR{head_str}|VIT{head_vit}|INT{head_int}|AGI{head_agi}|F{head_fire}|W{head_water}|W{head_wind}|E{head_earth}", font=c, fill="white")
                            else:
                                pass

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
                                necklace1_thumbnail = Image.open(f"assets/rpg/item/necklace/{head_id}.png")
                                necklace1_icon = Image.open(f"assets/rpg/item/necklace/{head_id}.png")
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

                            usebody = player.get("game", {}).get("rpg", {}).get("use", {}).get("body", {}).get("name", None)
                            usehand1 = player.get("game", {}).get("rpg", {}).get("use", {}).get("hand1", {}).get("name", None)
                            usehand2 = player.get("game", {}).get("rpg", {}).get("use", {}).get("hand2", {}).get("name", None)
                            usebelt = player.get("game", {}).get("rpg", {}).get("use", {}).get("belt", {}).get("name", None)
                            usegloves = player.get("game", {}).get("rpg", {}).get("use", {}).get("gloves", {}).get("name", None)
                            usering1 = player.get("game", {}).get("rpg", {}).get("use", {}).get("ring1", {}).get("name", None)
                            usering2 = player.get("game", {}).get("rpg", {}).get("use", {}).get("ring2", {}).get("name", None)
                            useboots = player.get("game", {}).get("rpg", {}).get("use", {}).get("boots", {}).get("name", None)
                            
                            bar = player.get("game", {}).get("rpg", {}).get("bar", {})
                            exp = bar.get("exp", {})
                            hp = bar.get("hp", {})
                            mana = bar.get("mana", {})

                            stats = player.get("game", {}).get("rpg", {}).get("stats", {})
                            vitality = stats.get("vit", {})
                            agility = stats.get("agi", {})
                            inteligent = stats.get("int", {})
                            strength = stats.get("str", {})

                            attribut = player.get("game", {}).get("rpg", {}).get("attribut", {})
                            fire = attribut.get("fire", {})
                            water = attribut.get("water", {})
                            earth = attribut.get("earth", {})
                            wind = attribut.get("wind", {})

                            body = player.get("game", {}).get("rpg", {}).get("use", {}).get("body", {})
                            bodystr = body.get("str", 0)
                            bodyvit = body.get("vit", 0)
                            bodyint = body.get("int", 0)
                            bodyagi = body.get("agi", 0)
                            bodyfire = body.get("fire", 0)
                            bodywater = body.get("water", 0)
                            bodywind = body.get("wind", 0)
                            bodyearth = body.get("earth", 0)
                            hand1 = player.get("game", {}).get("rpg", {}).get("use", {}).get("hand1", {})
                            hand1str = hand1.get("str", 0)
                            hand1vit = hand1.get("vit", 0)
                            hand1int = hand1.get("int", 0)
                            hand1agi = hand1.get("agi", 0)
                            hand1fire = hand1.get("fire", 0)
                            hand1water = hand1.get("water", 0)
                            hand1wind = hand1.get("wind", 0)
                            hand1earth = hand1.get("earth", 0)
                            hand2 = player.get("game", {}).get("rpg", {}).get("use", {}).get("hand2", {})
                            hand2str = hand2.get("str", 0)
                            hand2vit = hand2.get("vit", 0)
                            hand2int = hand2.get("int", 0)
                            hand2agi = hand2.get("agi", 0)
                            hand2fire = hand2.get("fire", 0)
                            hand2water = hand2.get("water", 0)
                            hand2wind = hand2.get("wind", 0)
                            hand2earth = hand2.get("earth", 0)
                            belt = player.get("game", {}).get("rpg", {}).get("use", {}).get("belt", {})
                            beltstr = belt.get("str", 0)
                            beltvit = belt.get("vit", 0)
                            beltint = belt.get("int", 0)
                            beltagi = belt.get("agi", 0)
                            beltfire = belt.get("fire", 0)
                            beltwater = belt.get("water", 0)
                            beltwind = belt.get("wind", 0)
                            beltearth = belt.get("earth", 0)
                            gloves = player.get("game", {}).get("rpg", {}).get("use", {}).get("belt", {})
                            glovesstr = gloves.get("str", 0)
                            glovesvit = gloves.get("vit", 0)
                            glovesint = gloves.get("int", 0)
                            glovesagi = gloves.get("agi", 0)
                            glovesfire = gloves.get("fire", 0)
                            gloveswater = gloves.get("water", 0)
                            gloveswind = gloves.get("wind", 0)
                            glovesearth = gloves.get("earth", 0)
                            ring1 = player.get("game", {}).get("rpg", {}).get("use", {}).get("ring1", {})
                            ring1str = ring1.get("str", 0)
                            ring1vit = ring1.get("vit", 0)
                            ring1int = ring1.get("int", 0)
                            ring1agi = ring1.get("agi", 0)
                            ring1fire = ring1.get("fire", 0)
                            ring1water = ring1.get("water", 0)
                            ring1wind = ring1.get("wind", 0)
                            ring1earth = ring1.get("earth", 0)
                            ring2 = player.get("game", {}).get("rpg", {}).get("use", {}).get("ring2", {})
                            ring2str = ring2.get("str", 0)
                            ring2vit = ring2.get("vit", 0)
                            ring2int = ring2.get("int", 0)
                            ring2agi = ring2.get("agi", 0)
                            ring2fire = ring2.get("fire", 0)
                            ring2water = ring2.get("water", 0)
                            ring2wind = ring2.get("wind", 0)
                            ring2earth = ring2.get("earth", 0)
                            boots = player.get("game", {}).get("rpg", {}).get("use", {}).get("boots", {})
                            bootsstr = boots.get("str", 0)
                            bootsvit = boots.get("vit", 0)
                            bootsint = boots.get("int", 0)
                            bootsagi = boots.get("agi", 0)
                            bootsfire = boots.get("fire", 0)
                            bootswater = boots.get("water", 0)
                            bootswind = boots.get("wind", 0)
                            bootsearth = boots.get("earth", 0)

                            statsvitality = head_vit + bodyvit + hand1vit + hand2vit + beltvit + glovesvit + ring1vit + ring2vit + bootsvit + necklace1_vit + necklace2_vit
                            statsagility = head_agi + bodyagi + hand1agi + hand2agi + beltagi + glovesagi + ring1agi + ring2agi + bootsagi + necklace1_agi + necklace2_agi
                            statsinteligent = head_int + bodyint + hand1int + hand2int + beltint + glovesint + ring1int + ring2int + bootsint + necklace1_int + necklace2_int
                            statsstrength = head_str + bodystr + hand1str + hand2str + beltstr + glovesstr + ring1str + ring2str + bootsstr + necklace1_str + necklace2_str
                            statsfire = head_fire + bodyfire + hand1fire + hand2fire + beltfire + glovesfire + ring1fire + ring2fire + bootsfire + necklace1_fire + necklace2_fire
                            statswater = head_water + bodywater + hand1water + hand2water + beltwater + gloveswater + ring1water + ring2water + bootswater + necklace1_water + necklace2_water
                            statswind = head_wind + bodywind + hand1wind + hand2wind + beltwind + gloveswind + ring1wind + ring2wind + bootswind + necklace1_wind + necklace2_wind
                            statsearth = head_earth + bodyearth +hand1earth + hand2earth + beltearth + glovesearth + ring1earth + ring2earth + bootsearth + necklace1_earth  + necklace2_earth

                            attack = statsagility*(1+(2/100))+statsstrength*(1+(4/100))

                            b.text((4, 2), f"LVL 10 | {username}", font=e, fill="white")
                            b.text((4, 89), f"HP\n{hp}/1200\nMANA\n{mana}/2000", font=c, fill="white")
                            b.text((72, 33), f"VIT\nAGI\nINT\nSTR\nFIRE\nWIND\nWATER\nEARTH", font=c, fill="white")
                            b.text((115, 33), ":\n:\n:\n:\n:\n:\n:\n:", font=c, fill="white")
                            b.text((120, 33), f"{vitality}+{statsvitality}\n{agility}+{statsagility}\n{inteligent}+{statsinteligent}\n{strength}+{statsstrength}\n{fire}+{statsfire}\n{wind}+{statswind}\n{water}+{statswater}\n{earth}+{statsearth}", font=c, fill="white")
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