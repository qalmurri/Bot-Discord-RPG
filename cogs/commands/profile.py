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
                        with Image.open("assets/rpg/profile/default.png") as a:
                            avatar = interaction.user.display_avatar
                            username = interaction.user.name

                            usehead = player.get("game", {}).get("rpg", {}).get("use", {}).get("head", {}).get("name", None)
                            usebody = player.get("game", {}).get("rpg", {}).get("use", {}).get("body", {}).get("name", None)
                            usehand1 = player.get("game", {}).get("rpg", {}).get("use", {}).get("hand1", {}).get("name", None)
                            usehand2 = player.get("game", {}).get("rpg", {}).get("use", {}).get("hand2", {}).get("name", None)
                            usebelt = player.get("game", {}).get("rpg", {}).get("use", {}).get("belt", {}).get("name", None)
                            usegloves = player.get("game", {}).get("rpg", {}).get("use", {}).get("gloves", {}).get("name", None)
                            usering1 = player.get("game", {}).get("rpg", {}).get("use", {}).get("ring1", {}).get("name", None)
                            usering2 = player.get("game", {}).get("rpg", {}).get("use", {}).get("ring2", {}).get("name", None)
                            useboots = player.get("game", {}).get("rpg", {}).get("use", {}).get("boots", {}).get("name", None)
                            usenecklace = player.get("game", {}).get("rpg", {}).get("use", {}).get("necklace", {}).get("name", None)

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

                            head = player.get("game", {}).get("rpg", {}).get("use", {}).get("head", {})
                            headstr = head.get("str", 0)
                            headvit = head.get("vit", 0)
                            headint = head.get("int", 0)
                            headagi = head.get("agi", 0)
                            headfire = head.get("fire", 0)
                            headwater = head.get("water", 0)
                            headwind = head.get("wind", 0)
                            headearth = head.get("earth", 0)

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

                            necklace = player.get("game", {}).get("rpg", {}).get("use", {}).get("necklace", {})
                            necklacestr = necklace.get("str", 0)
                            necklacevit = necklace.get("vit", 0)
                            necklaceint = necklace.get("int", 0)
                            necklaceagi = necklace.get("agi", 0)
                            necklacefire = necklace.get("fire", 0)
                            necklacewater = necklace.get("water", 0)
                            necklacewind = necklace.get("wind", 0)
                            necklaceearth = necklace.get("earth", 0)

                            statsvitality = headvit + bodyvit + hand1vit + hand2vit + beltvit + glovesvit + ring1vit + ring2vit + bootsvit + necklacevit
                            statsagility = headagi + bodyagi + hand1agi + hand2agi + beltagi + glovesagi + ring1agi + ring2agi + bootsagi + necklaceagi
                            statsinteligent = headint + bodyint + hand1int + hand2int + beltint + glovesint + ring1int + ring2int + bootsint + necklaceint
                            statsstrength = headstr + bodystr + hand1str + hand2str + beltstr + glovesstr + ring1str + ring2str + bootsstr + necklaceagi
                            statsfire = headfire + bodyfire + hand1fire + hand2fire + beltfire + glovesfire + ring1fire + ring2fire + bootsfire + necklacefire
                            statswater = headwater + bodywater + hand1water + hand2water + beltwater + gloveswater + ring1water + ring2water + bootswater + necklacewater
                            statswind = headwind + bodywind + hand1wind + hand2wind + beltwind + gloveswind + ring1wind + ring2wind + bootswind + necklacewind
                            statsearth = headearth + bodyearth +hand1earth + hand2earth + beltearth + glovesearth + ring1earth + ring2earth + bootsearth + necklaceearth

                            c = ImageFont.truetype("arial.ttf", 10)
                            e = ImageFont.truetype("arial.ttf", 16)
                            d = Image.open(requests.get(avatar, stream=True).raw)
                            b = ImageDraw.Draw(a)
                            
                            a.paste(d.resize((70, 70)), (4, 24))

                            b.text((4, 2), username, font=e, fill="blue")
                            b.text((80, 23), f"Exp\nVit\nAgi\nInt\nStr", font=c, fill="red")
                            b.text((98, 23), ":\n:\n:\n:\n:", font=c, fill="red")
                            b.text((103, 23), f"{exp}\n{vitality}+{statsvitality}\n{agility}+{statsagility}\n{inteligent}+{statsinteligent}\n{strength}+{statsstrength}", font=c, fill="red")

                            b.text((160, 23), f"Lvl\nFire\nWind\nWater\nEarth", font=c, fill="red")
                            b.text((188, 23), ":\n:\n:\n:\n:", font=c, fill="red")
                            b.text((193, 23), f"100\n{fire}+{statsfire}\n{wind}+{statswind}\n{water}+{statswater}\n{earth}+{statsearth}", font=c, fill="red")

                            b.text((4, 95), f"HP\nMana", font=c, fill="red")
                            b.text((45, 95), ":\n:", font=c, fill="red")
                            b.text((50, 95), f"{hp}\n{mana}", font=c, fill="red")

                            b.text((250, 5), f"Head: {usehead}\nBody: {usebody}\nHand1: {usehand1}\nHand2: {usehand2}\nBelt: {usebelt}\nGloves: {usegloves}\nRing1: {usering1}\nRing2: {usering2}\nBoots: {useboots}\nNecklace: {usenecklace}", font=c, fill="red")

                            a.save(f"stats/rpg/profile/{interaction.guild.id}.png")
                            await interaction.response.send_message(file=discord.File(f"stats/rpg/profile/{interaction.guild.id}.png"))
                            #await interaction.response.send_message("user sudah punya game rpg")
                    else:
                        await interaction.response.send_message("user belum punya game rpg")
            elif game.value == "1":
                await interaction.response.send_message("Unknown")

async def setup(bot):
    await bot.add_cog(profile(bot))