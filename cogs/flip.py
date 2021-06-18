from discord.ext import commands
import discord
import random


class CoinToss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def flip(self, message):
        res = "Heads"
        img = "https://raw.githubusercontent.com/heybc/files/main/heads_small.png"
        flip = random.randint(0, 1)
        if flip == 0:
            res = "Tails"
            img = "https://raw.githubusercontent.com/heybc/files/main/tails_small.png"
        e = discord.Embed(
            description=f"Coin landed on:\n**{res}**",
            colour=discord.Colour.gold(),
        )
        e.set_image(url=img)
        await message.reply(embed=e)


def setup(bot):
    bot.add_cog(CoinToss(bot))
