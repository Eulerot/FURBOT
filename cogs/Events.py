import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.roles, id=864881407230083112)
        await member.add_roles(role)
        try:
            if self.bot.muted_users[member.id]:
                muted_role = discord.utils.get(member.guild.roles, id=864857776110174228)
                if muted_role:
                    await member.add_roles(muted_role)
        except KeyError:
            pass
        try:
            if self.bot.banned_users[member.id]:
                banned_role = discord.utils.get(member.guild.roles, id=865323020541624401)
                if banned_role:
                    await member.add_roles(banned_role)
        except KeyError:
            pass

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Упс, {ctx.author.mention}, данной команды не сущетсвует")
        if isinstance(error, commands.CheckFailure):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Упс, {ctx.author.mention},у тебя нет прав для использования этой команды")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Кажется, {ctx.author.mention}, ты ввел неверный аргумент,пропиши {self.bot.DEFAULTPREFIX}help")
        if isinstance(error, commands.BadArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Кажется, {ctx.author.mention}, ты ввел неверный аргумент,пропиши {self.bot.DEFAULTPREFIX}help")
        raise error


def setup(bot):
    bot.add_cog(Events(bot))
