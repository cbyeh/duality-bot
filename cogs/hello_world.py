import discord


async def on_message(message):
    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")
