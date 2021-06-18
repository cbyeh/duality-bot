from discord.ext import commands
import asyncio


class Reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    seconds = set(["sec", "secs", "second", "seconds"])
    minutes = set(["min", "mins", "minute", "minutes"])
    hours = set(["hr", "hrs", "hour", "hours"])
    days = set(["day", "days"])
    weeks = set(["week", "weeks"])
    months = set(["mon", "month", "months"])
    years = set(["yr", "yrs", "year", "years"])
    times = [seconds, minutes, hours, days, weeks, months, years]

    def remind_helper(self, message):
        tokens = message.message.content.split()
        return tokens

    @commands.command()
    async def remind(self, message):
        msg = self.remind_helper(message)
        await message.channel.send("Remind")

    @commands.command()
    async def remindm(self, message):
        msg = self.remind_helper(message)
        await message.author.send("Remind")


def setup(bot):
    bot.add_cog(Reminder(bot))
