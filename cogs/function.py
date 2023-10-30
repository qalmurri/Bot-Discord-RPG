from discord.ext import commands
import json

class load_cogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def load_language(self, guild):
        try:
            with open('config/' + guild + '.json', 'r') as file:
                language_config = json.load(file)
        except FileNotFoundError:
            language_config = {}
        return language_config

    def save_language(self, language_config, guild):
        with open('config/' + guild + '.json', 'w') as file:
            json.dump(language_config, file)

    def config(self, guild):
        try:
            with open('config/' + guild + '.json', 'r') as file:
                data = json.load(file)
                if isinstance(data.get("language"), str):
                    language = data.get("language", "0")
        except FileNotFoundError:
            language = "0"

        return language

    def language_commands(self, guild):
        language = self.config(guild)
        directory = "assets/language"
        file_language = f"{directory}/english.json" if language == "0" else f"{directory}/indonesian.json"
        
        with open(file_language, 'r') as json_file:
            language_commands = json.load(json_file)
        return language_commands