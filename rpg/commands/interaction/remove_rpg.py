import database as db
from cogs.activity.logging import logging

async def remove_rpg(interaction, language):
    await db.PLAYER_USER.update_one({"_id": interaction.user.id}, {"$unset": {"game.rpg": {}}})
    
    await interaction.response.send_message(language["remove_rpg"])
    logging.info(f"{interaction.guild.id}/{interaction.channel.id}/{interaction.id}: Remove RPG")