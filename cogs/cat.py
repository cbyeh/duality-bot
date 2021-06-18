from discord.ext import commands
import aiohttp


class Cat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cat(self, message):
        cat_url = "https://purr.objects-us-east-1.dream.io/i/2014-11-0100.22.56.jpg"
        async with aiohttp.ClientSession() as session:
            async with session.get("https://aws.random.cat/meow") as res:
                if res.status == 200:
                    data = await res.json()
                    cat_url = data["file"]
        await message.channel.send(cat_url)


def setup(bot):
    bot.add_cog(Cat(bot))
