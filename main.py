import discord
from discord.ext import commands

import logging
import os

from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix="$")

# Register cogs
for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

# Set up logger
logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
logger.addHandler(handler)

# Run bot
bot.run(os.getenv("TOKEN"))
