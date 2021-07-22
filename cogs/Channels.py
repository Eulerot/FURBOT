import discord
from discord.ext import commands

import datetime

class Channels(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.command(aliases=['cs'])
    @commands.has_permissions(view_audit_log=True)
    async def channelstats(self, ctx):
        channel = ctx.channel
        embed = discord.Embed(title=f"Информация о канале",
                              description=f"{'Категория: {}'.format(channel.category.name) if channel.category else 'Канал без категории'}",
                              colour=discord.Color.purple())
        embed.add_field(name="Название", value=channel.mention, inline=False)
        embed.add_field(name="Айди канала", value=channel.id, inline=False)
        embed.add_field(name="Задержка на канале", value=channel.slowmode_delay, inline=False)
        embed.add_field(name="Канал NSFW:", value=channel.is_nsfw(), inline=False)
        embed.add_field(name="Время создания канала", value=channel.created_at.strftime("%#d %B %Y,%I:%M %p"),
                        inline=False)
        await ctx.send(embed=embed)

    @commands.command(aliases=['ld'])
    @commands.has_permissions(view_audit_log=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    async def lockdown(self, ctx, channel: discord.TextChannel = None):
        channel_logs = self.bot.get_channel(864868876897353778)
        channel = channel or ctx.channel

        if ctx.guild.default_role not in channel.overwrites:
            overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False)
            }
            await channel.edit(overwrites=overwrites)
            emb = discord.Embed(title=f"ЛОКДАУН",
                                description=f"Значит я, {ctx.author.mention}, запрещаю вам писать сюда {ctx.channel.mention}",
                                colour=discord.Color.purple())
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            emb.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=emb)
            await channel_logs.send(embed=emb)
        elif channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[ctx.guild.default_role].send_messages == None:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            emb = discord.Embed(title=f"ЛОКДАУН",
                                description=f"Значит я, {ctx.author.mention}, запрещаю вам писать сюда {ctx.channel.mention}",
                                colour=discord.Color.purple())
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            emb.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=emb)
            await channel_logs.send(embed=emb)
        else:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = 1
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            emb = discord.Embed(title=f"ЛОКДАУН",
                                description=f"Значит я, {ctx.author.mention}, разрешаю вам писать сюда {ctx.channel.mention}",
                                colour=discord.Color.purple())
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            emb.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=emb)
            await channel_logs.send(embed=emb)


def setup(bot):
    bot.add_cog(Channels(bot))
