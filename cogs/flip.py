from discord.ext import commands


class CoinToss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def flip(self, message):
        await message.channel.send("Heads!")


def setup(bot):
    bot.add_cog(CoinToss(bot))
