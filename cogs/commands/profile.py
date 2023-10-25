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

    @app_commands.command(name="profile", description="Profile")
    @app_commands.describe(game="Refreshing")
    @app_commands.choices(game=[app_commands.Choice(name="RPG", value="0")])
    async def profile(self, interaction:discord.Interaction, member:discord.Member, game: typing.Optional[app_commands.Choice[str]] = None):
        if member is None and game is None:
            await interaction.response.send_message("ya kamu harus milih dulu dong dengan pilihan yang sudah tersedia")
        elif game is None:
            await interaction.response.send_message(f"ini profilmu {member}")
        elif member is None:
            await interaction.response.send_message(f"Kamu harus memilih membernya terlebih dulu")
        else:
            if game.value == "0":
                player = await db.PLAYER_USER.find_one({"_id": member.id})
                if player is None:
                    await interaction.response.send_message("User belum register")
                else:
                    check = player.get("game", {}).get("rpg", {})
                    if check is not None and check :
                        with Image.open("assets/rpg/profile/default.jpg") as a:
                            username = member.name
                            avatar = member.display_avatar
                            ava = Image.open(requests.get(avatar, stream=True).raw)
                            a.paste(ava.resize((64, 64)), (4, 24))
                            b = ImageDraw.Draw(a)
                            e = ImageFont.truetype("assets/font/Diablo Heavy.ttf", 16)
                            c = ImageFont.truetype("assets/font/Diablo Heavy.ttf", 10) 

                            head_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("head", {})
                            if head_data :
                                head_stats = head_data.get("stats", {})
                                head_image, head_name, head_class = (head_data.get(key, None) for key in ("id_image", "name", "class"))
                                head_str, head_vit, head_int, head_agi, head_fire, head_water, head_wind, head_earth = (head_stats.get(key, 0) for key in ("str", "vit", "int", "agi", "fire", "water", "wind", "earth"))
                                a.paste(Image.open(f"assets/rpg/class/{head_class}.jpg").resize((281, 26)), (3, 151)) #Class
                                a.paste(Image.open(f"assets/rpg/item/head/{head_image}.png").resize((80, 80)), (394, 6)) #Thumbnail
                                a.paste(Image.open(f"assets/rpg/item/head/{head_image}.png").resize((22, 22)), (5, 153)) #Icon
                                b.text((34, 151),f"{head_name}\nSTR{head_str}|VIT{head_vit}|INT{head_int}|AGI{head_agi}|F{head_fire}|W{head_water}|W{head_wind}|E{head_earth}", font=c, fill="white")
                            else:
                                head_str = head_vit = head_int = head_agi = head_fire = head_water = head_wind = head_earth = 0    

                            necklace1_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("necklace1", {})
                            if necklace1_data :
                                necklace1_stats = necklace1_data.get("stats", {})
                                necklace1_image, necklace1_name, necklace1_class = (necklace1_data.get(key, None) for key in ("id_image", "name", "class"))
                                necklace1_str, necklace1_vit, necklace1_int, necklace1_agi, necklace1_fire, necklace1_water, necklace1_wind, necklace1_earth = (necklace1_stats.get(key, 0) for key in ("str", "vit", "int", "agi", "fire", "water", "wind", "earth"))
                                a.paste(Image.open(f"assets/rpg/class/{necklace1_class}.jpg").resize((281, 26)), (3, 179)) #Class
                                a.paste(Image.open(f"assets/rpg/item/necklace/{necklace1_image}.png").resize((80, 80)), (295, 77)) #Thumbnail
                                a.paste(Image.open(f"assets/rpg/item/necklace/{necklace1_image}.png").resize((22, 22)), (5, 181)) #Icon
                                b.text((34, 179), f"{necklace1_name}\nSTR{necklace1_str}|VIT{necklace1_vit}|INT{necklace1_int}|AGI{necklace1_agi}|F{necklace1_fire}|W{necklace1_water}|W{necklace1_wind}|E{necklace1_earth}", font=c, fill="white")
                            else:
                                necklace1_str = necklace1_vit = necklace1_int = necklace1_agi = necklace1_fire = necklace1_water = necklace1_wind = necklace1_earth = 0    

                            necklace2_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("necklace2", {})
                            if necklace2_data :
                                necklace2_stats = necklace2_data.get("stats", {})
                                necklace2_image, necklace2_name, necklace2_class = (necklace2_data.get(key, None) for key in ("id_image", "name", "class"))
                                necklace2_str, necklace2_vit, necklace2_int, necklace2_agi, necklace2_fire, necklace2_water, necklace2_wind, necklace2_earth = (necklace2_stats.get(key, 0) for key in ("str", "vit", "int", "agi", "fire", "water", "wind", "earth"))
                                a.paste(Image.open(f"assets/rpg/class/{necklace2_class}.jpg").resize((281, 26)), (3, 207)) #Class
                                a.paste(Image.open(f"assets/rpg/item/necklace/{necklace2_image}.png").resize((80, 80)), (491, 77)) #Thumbnail
                                a.paste(Image.open(f"assets/rpg/item/necklace/{necklace2_image}.png").resize((22, 22)), (5, 209)) #Icon
                                b.text((34, 207), f"{necklace2_name}\nSTR{necklace2_str}|VIT{necklace2_vit}|INT{necklace2_int}|AGI{necklace2_agi}|F{necklace2_fire}|W{necklace2_water}|W{necklace2_wind}|E{necklace2_earth}", font=c, fill="white")
                            else:
                                necklace2_str = necklace2_vit = necklace2_int = necklace2_agi = necklace2_fire = necklace2_water = necklace2_wind = necklace2_earth = 0   

                            body_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("body", {})
                            if body_data :
                                body_stats = body_data.get("stats", {})
                                body_image, body_name, body_class = (body_data.get(key, None) for key in ("id_image", "name", "class"))
                                body_str, body_vit, body_int, body_agi, body_fire, body_water, body_wind, body_earth = (body_stats.get(key, 0) for key in ("str", "vit", "int", "agi", "fire", "water", "wind", "earth"))
                                a.paste(Image.open(f"assets/rpg/class/{body_class}.jpg").resize((281, 26)), (3, 235)) #Class
                                a.paste(Image.open(f"assets/rpg/item/body/{body_image}.png").resize((100, 142)), (384, 94)) #Thumbnail
                                a.paste(Image.open(f"assets/rpg/item/body/{body_image}.png").resize((16, 22)), (8, 237)) #Icon
                                b.text((34, 235), f"{body_name}\nSTR{body_str}|VIT{body_vit}|INT{body_int}|AGI{body_agi}|F{body_fire}|W{body_water}|W{body_wind}|E{body_earth}", font=c, fill="white")
                            else:
                                body_str = body_vit = body_int = body_agi = body_fire = body_water = body_wind = body_earth = 0        

                            gloves1_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("gloves1", {})
                            if gloves1_data :
                                gloves1_stats = gloves1_data.get("stats", {})
                                gloves1_image, gloves1_name, gloves1_class = (gloves1_data.get(key, None) for key in ("id_image", "name", "class"))
                                gloves1_str, gloves1_vit, gloves1_int, gloves1_agi, gloves1_fire, gloves1_water, gloves1_wind, gloves1_earth = (gloves1_stats.get(key, 0) for key in ("str", "vit", "int", "agi", "fire", "water", "wind", "earth"))
                                a.paste(Image.open(f"assets/rpg/class/{gloves1_class}.jpg").resize((281, 26)), (3, 263)) #Class
                                a.paste(Image.open(f"assets/rpg/item/gloves/{gloves1_image}.png").resize((80, 111)), (295, 164)) #Thumbnail
                                a.paste(Image.open(f"assets/rpg/item/gloves/{gloves1_image}.png").resize((16, 22)), (8, 265)) #Icon
                                b.text((34, 263), f"{gloves1_name}\nSTR{gloves1_str}|VIT{gloves1_vit}|INT{gloves1_int}|AGI{gloves1_agi}|F{gloves1_fire}|W{gloves1_water}|W{gloves1_wind}|E{gloves1_earth}", font=c, fill="white")
                            else:
                                gloves1_str = gloves1_vit = gloves1_int = gloves1_agi = gloves1_fire = gloves1_water = gloves1_wind = gloves1_earth = 0  

                            gloves2_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("gloves2", {})
                            if gloves2_data :
                                gloves2_stats = gloves2_data.get("stats", {})
                                gloves2_image, gloves2_name, gloves2_class = (gloves2_data.get(key, None) for key in ("id_image", "name", "class"))
                                gloves2_str, gloves2_vit, gloves2_int, gloves2_agi, gloves2_fire, gloves2_water, gloves2_wind, gloves2_earth = (gloves2_stats.get(key, 0) for key in ("str", "vit", "int", "agi", "fire", "water", "wind", "earth"))
                                a.paste(Image.open(f"assets/rpg/class/{gloves2_class}.jpg").resize((281, 26)), (3, 291)) #Class
                                a.paste(Image.open(f"assets/rpg/item/gloves/{gloves2_image}.png").resize((80, 111)), (491, 164)) #Thumbnail
                                a.paste(Image.open(f"assets/rpg/item/gloves/{gloves2_image}.png").resize((16, 22)), (8, 293)) #Icon
                                b.text((34, 291), f"{gloves2_name}\nSTR{gloves2_str}|VIT{gloves2_vit}|INT{gloves2_int}|AGI{gloves2_agi}|F{gloves2_fire}|W{gloves2_water}|W{gloves2_wind}|E{gloves2_earth}", font=c, fill="white")
                            else:
                                gloves2_str = gloves2_vit = gloves2_int = gloves2_agi = gloves2_fire = gloves2_water = gloves2_wind = gloves2_earth = 0 

                            belt_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("belt", {})
                            if belt_data :
                                belt_stats = belt_data.get("stats", {})
                                belt_image, belt_name, belt_class = (belt_data.get(key, None) for key in ("id_image", "name", "class"))
                                belt_str, belt_vit, belt_int, belt_agi, belt_fire, belt_water, belt_wind, belt_earth = (belt_stats.get(key, 0) for key in ("str", "vit", "int", "agi", "fire", "water", "wind", "earth"))
                                a.paste(Image.open(f"assets/rpg/class/{belt_class}.jpg").resize((281, 26)), (3, 319)) #Class
                                a.paste(Image.open(f"assets/rpg/item/belt/{belt_image}.png").resize((98, 40)), (384, 243)) #Thumbnail
                                a.paste(Image.open(f"assets/rpg/item/belt/{belt_image}.png").resize((22, 10)), (5, 327)) #Icon
                                b.text((34, 319), f"{belt_name}\nSTR{belt_str}|VIT{belt_vit}|INT{belt_int}|AGI{belt_agi}|F{belt_fire}|W{belt_water}|W{belt_wind}|E{belt_earth}", font=c, fill="white")
                            else:
                                belt_str = belt_vit = belt_int = belt_agi = belt_fire = belt_water = belt_wind = belt_earth = 0        

                            ring1_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("ring1", {})
                            if ring1_data :
                                ring1_stats = ring1_data.get("stats", {})
                                ring1_image, ring1_name, ring1_class = (ring1_data.get(key, None) for key in ("id_image", "name", "class"))
                                ring1_str, ring1_vit, ring1_int, ring1_agi, ring1_fire, ring1_water, ring1_wind, ring1_earth = (ring1_stats.get(key, 0) for key in ("str", "vit", "int", "agi", "fire", "water", "wind", "earth"))
                                a.paste(Image.open(f"assets/rpg/class/{ring1_class}.jpg").resize((281, 26)), (3, 347)) #Class
                                a.paste(Image.open(f"assets/rpg/item/ring/{ring1_image}.png").resize((50, 50)), (310, 280)) #Thumbnail
                                a.paste(Image.open(f"assets/rpg/item/ring/{ring1_image}.png").resize((22, 22)), (5, 349)) #Icon
                                b.text((34, 347), f"{ring1_name}\nSTR{ring1_str}|VIT{ring1_vit}|INT{ring1_int}|AGI{ring1_agi}|F{ring1_fire}|W{ring1_water}|W{ring1_wind}|E{ring1_earth}", font=c, fill="white")
                            else:
                                ring1_str = ring1_vit = ring1_int = ring1_agi = ring1_fire = ring1_water = ring1_wind = ring1_earth = 0 

                            ring2_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("ring2", {})
                            if ring2_data :
                                ring2_stats = ring2_data.get("stats", {})
                                ring2_image, ring2_name, ring2_class = (ring2_data.get(key, None) for key in ("id_image", "name", "class"))
                                ring2_str, ring2_vit, ring2_int, ring2_agi, ring2_fire, ring2_water, ring2_wind, ring2_earth = (ring2_stats.get(key, 0) for key in ("str", "vit", "int", "agi", "fire", "water", "wind", "earth"))
                                a.paste(Image.open(f"assets/rpg/class/{ring2_class}.jpg").resize((281, 26)), (3, 375)) #Class
                                a.paste(Image.open(f"assets/rpg/item/ring/{ring2_image}.png").resize((50, 50)), (505, 280)) #Thumbnail
                                a.paste(Image.open(f"assets/rpg/item/ring/{ring2_image}.png").resize((22, 22)), (5, 377)) #Icon
                                b.text((34, 375), f"{ring2_name}\nSTR{ring2_str}|VIT{ring2_vit}|INT{ring2_int}|AGI{ring2_agi}|F{ring2_fire}|W{ring2_water}|W{ring2_wind}|E{ring2_earth}", font=c, fill="white")
                            else:
                                ring2_str = ring2_vit = ring2_int = ring2_agi = ring2_fire = ring2_water = ring2_wind = ring2_earth = 0  

                            pants_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("pants", {})
                            if pants_data :
                                pants_stats = pants_data.get("stats", {})
                                pants_image, pants_name, pants_class = (pants_data.get(key, None) for key in ("id_image", "name", "class"))
                                pants_str, pants_vit, pants_int, pants_agi, pants_fire, pants_water, pants_wind, pants_earth = (pants_stats.get(key, 0) for key in ("str", "vit", "int", "agi", "fire", "water", "wind", "earth"))
                                a.paste(Image.open(f"assets/rpg/class/{pants_class}.jpg").resize((281, 26)), (3, 403)) #Class
                                a.paste(Image.open(f"assets/rpg/item/pants/{pants_image}.png").resize((80, 111)), (393, 287)) #Thumbnail
                                a.paste(Image.open(f"assets/rpg/item/pants/{pants_image}.png").resize((16, 22)), (8, 405)) #Icon
                                b.text((34, 403), f"{pants_name}\nSTR{pants_str}|VIT{pants_vit}|INT{pants_int}|AGI{pants_agi}|F{pants_fire}|W{pants_water}|W{pants_wind}|E{pants_earth}", font=c, fill="white")
                            else:
                                pants_str = pants_vit = pants_int = pants_agi = pants_fire = pants_water = pants_wind = pants_earth = 0  

                            hand1_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("hand1", {})
                            if hand1_data :
                                hand1_stats = hand1_data.get("stats", {})
                                hand1_image, hand1_name, hand1_class = (hand1_data.get(key, None) for key in ("id_image", "name", "class"))
                                hand1_str, hand1_vit, hand1_int, hand1_agi, hand1_fire, hand1_water, hand1_wind, hand1_earth = (hand1_stats.get(key, 0) for key in ("str", "vit", "int", "agi", "fire", "water", "wind", "earth"))
                                a.paste(Image.open(f"assets/rpg/class/{hand1_class}.jpg").resize((281, 26)), (3, 431)) #Class
                                a.paste(Image.open(f"assets/rpg/item/hand/{hand1_image}.png").resize((80, 111)), (295, 335)) #Thumbnail
                                a.paste(Image.open(f"assets/rpg/item/hand/{hand1_image}.png").resize((16, 22)), (8, 433)) #Icon
                                b.text((34, 431), f"{hand1_name}\nSTR{hand1_str}|VIT{hand1_vit}|INT{hand1_int}|AGI{hand1_agi}|F{hand1_fire}|W{hand1_water}|W{hand1_wind}|E{hand1_earth}", font=c, fill="white")
                            else:
                                hand1_str = hand1_vit = hand1_int = hand1_agi = hand1_fire = hand1_water = hand1_wind = hand1_earth = 0  

                            hand2_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("hand2", {})
                            if hand2_data :
                                hand2_stats = hand2_data.get("stats", {})
                                hand2_image, hand2_name, hand2_class = (hand2_data.get(key, None) for key in ("id_image", "name", "class"))
                                hand2_str, hand2_vit, hand2_int, hand2_agi, hand2_fire, hand2_water, hand2_wind, hand2_earth = (hand2_stats.get(key, 0) for key in ("str", "vit", "int", "agi", "fire", "water", "wind", "earth"))
                                a.paste(Image.open(f"assets/rpg/class/{hand2_class}.jpg").resize((281, 26)), (3, 459)) #Class
                                a.paste(Image.open(f"assets/rpg/item/hand/{hand2_image}.png").resize((80, 111)), (491, 335)) #Thumbnail
                                a.paste(Image.open(f"assets/rpg/item/hand/{hand2_image}.png").resize((16, 22)), (8, 461)) #Icon
                                b.text((34, 459), f"{hand2_name}\nSTR{hand2_str}|VIT{hand2_vit}|INT{hand2_int}|AGI{hand2_agi}|F{hand2_fire}|W{hand2_water}|W{hand2_wind}|E{hand2_earth}", font=c, fill="white")
                            else:
                                hand2_str = hand2_vit = hand2_int = hand2_agi = hand2_fire = hand2_water = hand2_wind = hand2_earth = 0  

                            boots_data = player.get("game", {}).get("rpg", {}).get("use", {}).get("boots", {})
                            if boots_data :
                                boots_stats = boots_data.get("stats", {})
                                boots_image, boots_name, boots_class = (boots_data.get(key, None) for key in ("id_image", "name", "class"))
                                boots_str, boots_vit, boots_int, boots_agi, boots_fire, boots_water, boots_wind, boots_earth = (boots_stats.get(key, 0) for key in ("str", "vit", "int", "agi", "fire", "water", "wind", "earth"))
                                a.paste(Image.open(f"assets/rpg/class/{boots_class}.jpg").resize((281, 26)), (3, 487)) #Class
                                a.paste(Image.open(f"assets/rpg/item/boots/{boots_image}.png").resize((80, 111)), (393, 402)) #Thumbnail
                                a.paste(Image.open(f"assets/rpg/item/boots/{boots_image}.png").resize((16, 22)), (8, 489)) #Icon
                                b.text((34, 487), f"{boots_name}\nSTR{boots_str}|VIT{boots_vit}|INT{boots_int}|AGI{boots_agi}|F{boots_fire}|W{boots_water}|W{boots_wind}|E{boots_earth}", font=c, fill="white")
                            else:
                                boots_str = boots_vit = boots_int = boots_agi = boots_fire = boots_water = boots_wind = boots_earth = 0

                            stats_str = head_str + necklace1_str + necklace2_str + body_str + gloves1_str + gloves2_str + belt_str + ring1_str + ring2_str + pants_str + hand1_str + hand2_str + boots_str
                            stats_vit = head_vit + necklace1_vit + necklace2_vit + body_vit + gloves1_vit + gloves2_vit + belt_vit + ring1_vit + ring2_vit + pants_vit + hand1_vit + hand2_vit + boots_vit
                            stats_int = head_int + necklace1_int + necklace2_int + body_int + gloves1_int + gloves2_int + belt_int + ring1_int + ring2_int + pants_int + hand1_int + hand2_int + boots_int
                            stats_agi = head_agi + necklace1_agi + necklace2_agi + body_agi + gloves1_agi + gloves2_agi + belt_agi + ring1_agi + ring2_agi + pants_agi + hand1_agi + hand2_agi + boots_agi
                            stats_fire = head_fire + necklace1_fire + necklace2_fire + body_fire + gloves1_fire + gloves2_fire + belt_fire + ring1_fire + ring2_fire + pants_fire + hand1_fire + hand2_fire + boots_fire
                            stats_water = head_water + necklace1_water + necklace2_water + body_water + gloves1_water + gloves2_water + belt_water + ring1_water + ring2_water + pants_water + hand1_water + hand2_water + boots_water
                            stats_wind = head_wind + necklace1_wind + necklace2_wind + body_wind + gloves1_wind + gloves2_wind + belt_wind + ring1_wind + ring2_wind + pants_wind + hand1_wind + hand2_wind + boots_wind
                            stats_earth = head_earth + necklace1_earth + necklace2_earth + body_earth + gloves1_earth + gloves2_earth + belt_earth + ring1_earth + ring2_earth + pants_earth + hand1_earth + hand2_earth + boots_earth         

                            stats_atk = (stats_agi*(1+(2/100))+stats_str*(1+(4/100)))+stats_wind*(1+(4/100))
                            stats_aspd = stats_wind + stats_agi
                            stats_def = stats_earth + stats_str + stats_vit
                            stats_mdef = (stats_earth + stats_water)/2 + stats_int + stats_str
                            stats_matk = stats_fire + stats_int
                            stats_crit = stats_agi + stats_wind    

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

                            b.text((4, 2), f"{username}|LVL 38 (89%)", font=e, fill="white")
                            b.text((4, 89), f"HP\n{hp}/1200\nMANA\n{mana}/2000", font=c, fill="white")
                            b.text((72, 33), f"VIT\nAGI\nINT\nSTR\nFIRE\nWIND\nWATER\nEARTH", font=c, fill="white")
                            b.text((115, 33), ":\n:\n:\n:\n:\n:\n:\n:", font=c, fill="white")
                            b.text((120, 33), f"{vitality}+{stats_vit}\n{agility}+{stats_agi}\n{inteligent}+{stats_int}\n{strength}+{stats_str}\n{fire}+{stats_fire}\n{wind}+{stats_wind}\n{water}+{stats_water}\n{earth}+{stats_earth}", font=c, fill="white")
                            b.text((180, 33), f"ATK\nASPD\nDEF\nMDEF\nMATK\nCRIT\nPOINT\nGUILD", font=c, fill="white")
                            b.text((216, 33), ":\n:\n:\n:\n:\n:\n:\n:", font=c, fill="white")
                            b.text((221, 33), f"{stats_atk}\n{stats_aspd}\n{stats_def}\n{stats_mdef}\n{stats_matk}\n{stats_crit}\n10\n10", font=c, fill="white")           
                            a.save(f"stats/rpg/profile/{interaction.guild.id}.jpg")

                            await interaction.response.send_message(file=discord.File(f"stats/rpg/profile/{interaction.guild.id}.jpg"))
                    else:
                        await interaction.response.send_message("user belum punya game rpg")
            else:
                pass

async def setup(bot):
    await bot.add_cog(profile(bot))