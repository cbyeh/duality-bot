from discord.ext import commands


class GetAvatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["getavatar"])
    async def avatar(self, message):
        await message.channel.send("Getting avatar...")


def setup(bot):
    bot.add_cog(GetAvatar(bot))
