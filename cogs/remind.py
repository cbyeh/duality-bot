from discord.ext import commands
from asyncio import sleep


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
    units = [seconds, minutes, hours, days, weeks, months, years]

    def remind_helper(self, message):
        tokens = message.message.content.split()
        if len(tokens) < 4:
            raise Exception("Bad argument(s)")
        try:
            time = int(tokens[1])
            if time < 1:
                raise Exception("Bad argument(s)")
        except ValueError:
            raise Exception("Bad argument(s)")
        found = False
        for i, unit in enumerate(self.units):
            if tokens[2] in unit:
                found = True
            if unit == self.minutes:
                time *= 60
            elif unit == self.hours:
                time *= 60
            elif unit == self.days:
                time *= 24
            elif unit == self.weeks:
                time *= 7
            elif unit == self.months:
                time *= 4.34524
            elif unit == self.years:
                time *= 12
            if found:
                break
        if not found:
            raise Exception("Bad argument(s)")
        message = " ".join(tokens[3:])
        return (time, message)

    @commands.command()
    async def remind(self, message):
        try:
            msg = self.remind_helper(message)
        except:
            return await message.reply(
                "Invalid usage.\n```$remind 3 hrs Remind me to do something```"
            )
        await sleep(msg[0])
        await message.reply(f"Reminder: **{msg[1]}**")

    @commands.command()
    async def remindm(self, message):
        try:
            msg = self.remind_helper(message)
        except:
            return await message.reply(
                "Invalid usage.\n```$remind 3 hrs Remind me to do something```"
            )
        await sleep(msg[0])
        await message.author.send(f"Reminder: **{msg[1]}**")


def setup(bot):
    bot.add_cog(Reminder(bot))
