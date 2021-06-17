from discord.ext import commands


class Cat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cat(self, message):
        await message.channel.send("Cat")


def setup(bot):
    bot.add_cog(Cat(bot))
