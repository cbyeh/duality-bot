import discord
import logging
import os
from dotenv import load_dotenv
from cogs import hello_world

load_dotenv()

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


# Apply decorators to other functions
client.event(hello_world.on_message)

# Set up logger
logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
logger.addHandler(handler)

# Run bot
client.run(os.getenv("TOKEN"))
