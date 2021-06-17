from discord.ext import commands


class HelloWorld(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("We are online")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f"Welcome {member}.")

    @commands.command(aliases=["hi", "bonjour"])
    async def hello(self, message):
        await message.channel.send("Why hello :)")


def setup(bot):
    bot.add_cog(HelloWorld(bot))
