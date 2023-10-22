import discord
from discord.ext import commands
from discord import app_commands

import asyncio

import database as db

class spawn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = 1110105612790005812

    @app_commands.command(name="spawn", description="spawn di db")
    async def spawn(self, interaction:discord.Interaction):
        environment = await db.environment[str(interaction.guild.id)].find_one({"status": "active"})
        if environment is None:
            await db.environment[str(interaction.guild.id)].insert_one(
                {
                    "_id": interaction.channel.id,
                    "id_image": None,
                    "status": True,
                    "profile": {
                        "name": "jelangkung",
                        "class": "common",
                        "description": "jelangku adalah boneka spritirual",
                        },
                    "lobby": {
                        "user": {},
                        "log": {},
                        },
                    "stats": {
                        "hp": 300,
                        "mana": 1000,
                        }
                    }
                )
            await interaction.response.send_message(f"Monster sudah ada di db, silahkan ketik attack untuk melihat reaksinya")
        else:
            pass

    @commands.Cog.listener()
    async def on_ready(self):
        await self.send_and_delete_loop()

    async def send_and_delete_loop(self):
        # Ambil daftar channel ID dari database (gantilah ini sesuai dengan cara Anda mengambil data dari database)
        channel_ids = [1110105612790005812, 1156074378975531079]  # Contoh daftar channel ID

        for channel_id in channel_ids:
            channel = self.bot.get_channel(channel_id)
            if not channel:
                print(f"Channel with ID {channel_id} not found")
                continue

            while True:
                # Kirim pesan
                message = await channel.send("Ini pesan yang akan dihapus nanti.")

                # Tunggu beberapa detik
                await asyncio.sleep(2)  # Ganti dengan waktu yang sesuai

                # Hapus pesan yang telah dikirim
                await message.delete()

                # Tunggu sebelum mengirim lagi
                await asyncio.sleep(2)  # Ganti dengan waktu yang sesuai


async def setup(bot):
    await bot.add_cog(spawn(bot))