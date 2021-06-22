from discord.ext import commands
import discord


class GetAvatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["getavatar"])
    async def avatar(self, message):
        tokens = message.message.content.split()
        if len(tokens) > 2:
            return await message.reply(
                "Invalid usage.\n```$avatar\n$avatar ExampleUser#1234```"
            )
        if len(tokens) == 1:
            return await message.reply(message.message.author.avatar_url)
        # user = await self.bot.fetch_user(tokens[1])
        converter = commands.MemberConverter()
        try:
            member = await converter.convert(message, tokens[1])
            await message.reply(member.avatar_url)
        except discord.ext.commands.errors.MemberNotFound:
            return await message.reply("User not found")


def setup(bot):
    bot.add_cog(GetAvatar(bot))
