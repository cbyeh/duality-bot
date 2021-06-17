from discord.ext import commands


class Reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def remind(self, message):
        await message.channel.send("Remind")


def setup(bot):
    bot.add_cog(Reminder(bot))
