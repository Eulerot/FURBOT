import os
import asyncio

import discord
from discord.ext import commands


class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.command(aliases=["cp"], usage="prefix")
    @commands.is_owner()
    async def prefix(self, ctx, *, prefix="!"):
        channel_logs = self.bot.get_channel(864868876897353778)
        await self.bot.config.upsert({"_id": ctx.guild.id, "prefix": prefix})
        await ctx.send(f"Мой новый префикc {prefix}")
        await channel_logs.send(f"Мой новый префикc {prefix} {ctx.author.mention}")
        await asyncio.sleep(15)
        await ctx.message.delete()

    @commands.command(aliases=['dp'])
    @commands.is_owner()
    async def deleteprefix(self, ctx):
        channel_logs = self.bot.get_channel(864868876897353778)
        await self.bot.config.unset({"_id": ctx.guild.id, "prefix": 1})
        await ctx.send("Префикс: По умолчанию")
        await channel_logs.send(f"Префикс: По умолчанию {ctx.author.mention}")
        await asyncio.sleep(15)
        await ctx.message.delete()

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx):
        channel_logs = self.bot.get_channel(864868876897353778)
        async with ctx.typing():
            emb = discord.Embed(
                title="Коги перезагружаются",
                color=discord.Color.purple(),
                timestamp=ctx.message.created_at)
            for ext in os.listdir("./cogs/"):
                if ext.endswith(".py") and not ext.startswith("_"):
                    try:
                        self.bot.unload_extension(f"cogs.{ext[:-3]}")
                        self.bot.load_extension(f"cogs.{ext[:-3]}")
                        emb.add_field(
                            name=f"Перезагружено: `{ext}`",
                            value='\uFEFF',
                            inline=False
                        )
                    except Exception as e:
                        emb.add_field(
                            name=f"Ошибка перезагрузки: `{ext}`",
                            value=e,
                            inline=False
                        )
                    await asyncio.sleep(0.5)
            await ctx.send(embed=emb)
            await channel_logs.send(embed=emb)
            await asyncio.sleep(15)
            await ctx.message.delete()


def setup(bot):
    bot.add_cog(Config(bot))
