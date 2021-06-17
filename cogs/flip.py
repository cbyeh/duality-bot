from discord.ext import commands
import random


class CoinToss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def flip(self, message):
        res = "**Heads**"
        flip = random.randint(0, 1)
        if flip == 0:
            res = "**Tails**"
        await message.reply(f"{message.author.name} landed on {res}")


def setup(bot):
    bot.add_cog(CoinToss(bot))
