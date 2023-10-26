from discord.ext import commands
import json

class load_cogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def load_language(self, guild_id):
        try:
            with open('config/' + guild_id + '.json', 'r') as file:
                language_config = json.load(file)
        except FileNotFoundError:
            language_config = {}
        return language_config

    def save_language(self, language_config, guild_id):
        with open('config/' + guild_id + '.json', 'w') as file:
            json.dump(language_config, file)

    def language(self, guild_id):
        try:
            with open('config/' + guild_id + '.json', 'r') as file:
                data = json.load(file)
                if isinstance(data.get("language"), str):
                    guild_language = data.get("language", "0")
        except FileNotFoundError:
            guild_language = "0"

        file_language = "assets/language/english.json" if guild_language == "0" else "assets/language/indonesian.json"
        with open(file_language, 'r') as json_file:
            language = json.load(json_file)
        return language