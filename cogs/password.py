from discord.ext import commands
import secrets


class PasswordGenerator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def password(self, message, num_bytes=10):
        if num_bytes not in range(3, 201):
            # The text is Base64 encoded so each byte results in ~1.3 characters.
            return await message.reply("Password must be between 3-200 bytes in length")
        if hasattr(message, "guild") and message.guild is not None:
            await message.reply(f"Password🔑 on the way, check your **messages**")
        await message.author.send(
            f"Random password:\n```{secrets.token_urlsafe(num_bytes)}```"
        )


def setup(bot):
    bot.add_cog(PasswordGenerator(bot))
