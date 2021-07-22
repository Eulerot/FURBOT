import discord
from discord.ext import commands


import random
class Funs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def fursonaimage(self, ctx, image):
        pass

    @commands.command()
    async def roll(self, ctx, dice: str):
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

def setup(bot):
    bot.add_cog(Funs(bot))