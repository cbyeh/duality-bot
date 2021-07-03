from discord.ext import commands
from asyncio import sleep as s


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
        if len(tokens) < 4:
            raise Exception("Bad argument(s)")
        try:
            val = int(tokens[1])
            if val < 1:
                raise Exception("Bad argument(s)")
        except ValueError:
            raise Exception("Bad argument(s)")
        return (int(tokens[1]), "Hello world")

    @commands.command()
    async def remind(self, message):
        try:
            msg = self.remind_helper(message)
        except:
            return await message.reply(
                "Invalid usage.\n```$remind 3 hrs Remind me to do something```"
            )
        await s(msg[0])
        await message.reply(f"Reminder: **{msg[1]}**")

    @commands.command()
    async def remindm(self, message):
        try:
            msg = self.remind_helper(message)
        except:
            return await message.reply(
                "Invalid usage.\n```$remind 3 hrs Remind me to do something```"
            )
        await s(msg[0])
        await message.author.send(f"Reminder: **{msg[1]}**")


def setup(bot):
    bot.add_cog(Reminder(bot))
