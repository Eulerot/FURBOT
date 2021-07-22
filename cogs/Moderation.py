import asyncio
import datetime

import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await ctx.channel.purge(limit=1)
        channel = self.bot.get_channel(864868876897353778)
        await member.kick(reason=reason)
        if reason != None:
            emb = discord.Embed(title=f'{member.name} исключается!',
                                colour=discord.Color.purple())
            emb.add_field(name='Причина', value=f'{reason.upper()}', inline=False)
            emb.add_field(name='Нарушитель', value=f'{member.mention}', inline=False)
            emb.add_field(name='Администратор', value=f'{ctx.author.mention}', inline=False)
            emb.set_thumbnail(url=member.avatar_url)
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            emb.timestamp = datetime.datetime.utcnow()
        else:
            emb = discord.Embed(title=f'Плохой {member.name} исключается!',
                                colour=discord.Color.purple())
            emb.add_field(name='Причина', value=f'Без причины', inline=False)
            emb.add_field(name='Нарушитель', value=f'{member.mention}', inline=False)
            emb.add_field(name='Администратор', value=f'{ctx.author.mention}', inline=False)
            emb.set_thumbnail(url=member.avatar_url)
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            emb.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=emb)
        await channel.send(embed=emb)

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def ban(self, ctx, member: discord.Member, reason=None, time=0):
        await ctx.channel.purge(limit=1)
        time = int(time) * 60
        channel = self.bot.get_channel(864868876897353778)
        banned_role = discord.utils.get(ctx.guild.roles, id=865323020541624401)
        minute = ['минуту', 'минуты', 'минут']
        if int(time / 60) % 10 == 1 and int(time / 60) % 100 != 11:
            minute = minute[0]
        elif 2 <= int(time / 60) % 10 <= 4 and (int(time / 60) % 100 < 10 or int(time / 60) % 100 >= 20):
            minute = minute[1]
        else:
            minute = minute[2]
        try:
            if self.bot.banned_users[member.id]:
                await ctx.send(f"{member.mention} уже находится в бане")
                return
        except KeyError:
            pass
        data = {
            '_id': member.id,
            'bannedAt': datetime.datetime.now(),
            'reason': reason,
            'banDuration': time or None,
            'bannedBy': ctx.author.id
        }
        await self.bot.bans.upsert(data)
        self.bot.banned_users[member.id] = data
        await member.add_roles(banned_role)
        if reason == None:
            if time == 0:
                emb = discord.Embed(title=f'{member.name} получает бан!На неопределенный срок',
                                    colour=discord.Color.purple())
                emb.add_field(name='Причина', value=f'Без причины', inline=False)
                emb.add_field(name='Нарушитель', value=f'{member.mention}', inline=False)
                emb.add_field(name='Администратор', value=f'{ctx.author.mention}', inline=False)
                emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                emb.timestamp = datetime.datetime.utcnow()
            else:
                emb = discord.Embed(title=f'{member.name} получает бан!На {int(time / 60)} {minute}',
                                    colour=discord.Color.purple())
                emb.add_field(name='Причина', value=f'Без причины', inline=False)
                emb.add_field(name='Нарушитель', value=f'{member.mention}', inline=False)
                emb.add_field(name='Администратор', value=f'{ctx.author.mention}', inline=False)
                emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                emb.timestamp = datetime.datetime.utcnow()
        else:
            if time == 0:
                emb = discord.Embed(title=f'{member.name} получает бан!На неопределенный срок',
                                    colour=discord.Color.purple())
                emb.add_field(name='Причина', value=f'{reason.upper()}', inline=False)
                emb.add_field(name='Нарушитель', value=f'{member.mention}', inline=False)
                emb.add_field(name='Администратор', value=f'{ctx.author.mention}', inline=False)
                emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                emb.timestamp = datetime.datetime.utcnow()
            else:
                emb = discord.Embed(title=f'{member.name} получает бан!На {int(time / 60)} {minute}',
                                    colour=discord.Color.purple())
                emb.add_field(name='Причина', value=f'{reason.upper()}', inline=False)
                emb.add_field(name='Нарушитель', value=f'{member.mention}', inline=False)
                emb.add_field(name='Администратор', value=f'{ctx.author.mention}', inline=False)
                emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                emb.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=emb)
        await channel.send(embed=emb)
        if time != 0:
            await asyncio.sleep(time)
            if banned_role in member.roles:
                await member.remove_roles(banned_role)
                boy_role = discord.utils.get(member.guild.roles, id=866390060614025216)
                girl_role = discord.utils.get(member.guild.roles, id=866389932402933770)
                if boy_role in member.roles and girl_role not in member.roles:
                    await ctx.send(f"{member.mention} разбанен")
                elif girl_role in member.roles and boy_role not in member.roles:
                    await ctx.send(f"{member.mention} разбанена")
                else:
                    await ctx.send(f"{member.mention} разбанен/a")
            await self.bot.bans.delete(member.id)
            try:
                self.bot.banned_users.pop(member.id)
            except KeyError:
                pass

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def unban(self, ctx, member: discord.Member):
        await ctx.channel.purge(limit=1)
        channel = self.bot.get_channel(864868876897353778)
        banned_role = discord.utils.get(ctx.guild.roles, id=865323020541624401)
        boy_role = discord.utils.get(member.guild.roles, id=866390060614025216)
        girl_role = discord.utils.get(member.guild.roles, id=866389932402933770)
        await self.bot.bans.delete(member.id)
        try:
            self.bot.banned_users.pop(member.id)
        except KeyError:
            pass
        if banned_role not in member.roles:
            if boy_role in member.roles and girl_role not in member.roles:
                await ctx.send(f"{member.mention} не был забанен")
            elif girl_role in member.roles and boy_role not in member.roles:
                await ctx.send(f"{member.mention} не была забанена")
            else:
                await ctx.send(f"{member.mention} не был/а забанен/a")
            return
        await member.remove_roles(banned_role)
        if boy_role in member.roles and girl_role not in member.roles:
            await ctx.send(f"{member.mention} разбанен")
            await channel.send(f"{member.mention} разбанен {ctx.author.mention}")
        elif girl_role in member.roles and boy_role not in member.roles:
            await ctx.send(f"{member.mention} разбанена")
            await channel.send(f"{member.mention} разбаненa {ctx.author.mention}")
        else:
            await ctx.send(f"{member.mention} разбанен/a")
            await channel.send(f"{member.mention} разбанен/a {ctx.author.mention}")

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def mute(self, ctx, member: discord.Member, reason=None, time=0):
        await ctx.channel.purge(limit=1)
        time = int(time) * 60
        channel = self.bot.get_channel(864868876897353778)
        muted_role = discord.utils.get(ctx.guild.roles, id=864857776110174228)
        minute = ['минуту', 'минуты', 'минут']
        if int(time / 60) % 10 == 1 and int(time / 60) % 100 != 11:
            minute = minute[0]
        elif 2 <= int(time / 60) % 10 <= 4 and (int(time / 60) % 100 < 10 or int(time / 60) % 100 >= 20):
            minute = minute[1]
        else:
            minute = minute[2]
        try:
            if self.bot.muted_users[member.id]:
                await ctx.send(f"{member.mention} уже находится в муте")
                return
        except KeyError:
            pass
        data = {
            '_id': member.id,
            'mutedAt': datetime.datetime.now(),
            'muteDuration': time or None,
            'reason': reason,
            'mutedBy': ctx.author.id
        }
        await self.bot.mutes.upsert(data)
        self.bot.muted_users[member.id] = data
        await member.add_roles(muted_role)
        if reason == None:
            if time == 0:
                emb = discord.Embed(title=f'{member.name} получает мут!На неопределенный срок',
                                    colour=discord.Color.purple())
                emb.add_field(name='Причина', value=f'Без причины', inline=False)
                emb.add_field(name='Нарушитель', value=f'{member.mention}', inline=False)
                emb.add_field(name='Администратор', value=f'{ctx.author.mention}', inline=False)
                emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                emb.timestamp = datetime.datetime.utcnow()
            else:
                emb = discord.Embed(title=f'{member.name} получает мут!На {int(time / 60)} {minute}',
                                    colour=discord.Color.purple())
                emb.add_field(name='Причина', value=f'Без причины', inline=False)
                emb.add_field(name='Нарушитель', value=f'{member.mention}', inline=False)
                emb.add_field(name='Администратор', value=f'{ctx.author.mention}', inline=False)
                emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                emb.timestamp = datetime.datetime.utcnow()
        else:
            if time == 0:
                emb = discord.Embed(title=f'{member.name} получает мут!На неопределенный срок',
                                    colour=discord.Color.purple())
                emb.add_field(name='Причина', value=f'{reason.upper()}', inline=False)
                emb.add_field(name='Нарушитель', value=f'{member.mention}', inline=False)
                emb.add_field(name='Администратор', value=f'{ctx.author.mention}', inline=False)
                emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                emb.timestamp = datetime.datetime.utcnow()
            else:
                emb = discord.Embed(title=f'{member.name} получает мут!На {int(time / 60)} {minute}',
                                    colour=discord.Color.purple())
                emb.add_field(name='Причина', value=f'{reason.upper()}', inline=False)
                emb.add_field(name='Нарушитель', value=f'{member.mention}', inline=False)
                emb.add_field(name='Администратор', value=f'{ctx.author.mention}', inline=False)
                emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                emb.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=emb)
        await channel.send(embed=emb)
        if time != 0:
            await asyncio.sleep(time)
            if muted_role in member.roles:
                await member.remove_roles(muted_role)
                boy_role = discord.utils.get(member.guild.roles, id=866390060614025216)
                girl_role = discord.utils.get(member.guild.roles, id=866389932402933770)
                if boy_role in member.roles and girl_role not in member.roles:
                    await ctx.send(f"{member.mention} размучен")
                elif girl_role in member.roles and boy_role not in member.roles:
                    await ctx.send(f"{member.mention} размучена")
                else:
                    await ctx.send(f"{member.mention} размучена/a")
            await self.bot.mutes.delete(member.id)
            try:
                self.bot.muted_users.pop(member.id)
            except KeyError:
                pass

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def unmute(self, ctx, member: discord.Member):
        await ctx.channel.purge(limit=1)
        channel = self.bot.get_channel(864868876897353778)
        muted_role = discord.utils.get(ctx.guild.roles, id=864857776110174228)
        boy_role = discord.utils.get(member.guild.roles, id=866390060614025216)
        girl_role = discord.utils.get(member.guild.roles, id=866389932402933770)
        await self.bot.mutes.delete(member.id)
        try:
            self.bot.muted_users.pop(member.id)
        except KeyError:
            pass
        if muted_role not in member.roles:
            if boy_role in member.roles and girl_role not in member.roles:
                await ctx.send(f"{member.mention} не был замучен")
            elif girl_role in member.roles and boy_role not in member.roles:
                await ctx.send(f"{member.mention} не была замучена")
            else:
                await ctx.send(f"{member.mention} не был/a размучена/a")
            return
        await member.remove_roles(muted_role)
        if boy_role in member.roles and girl_role not in member.roles:
            await ctx.send(f"{member.mention} размучен")
            await channel.send(f"{member.mention} размучен {ctx.author.mention}")
        elif girl_role in member.roles and boy_role not in member.roles:
            await ctx.send(f"{member.mention} размучена")
            await channel.send(f"{member.mention} размучена {ctx.author.mention}")
        else:
            await ctx.send(f"{member.mention} размучена/a")
            await channel.send(f"{member.mention} размучен {ctx.author.mention}")

    @commands.command(aliases=["с", "c"])
    @commands.has_permissions(view_audit_log=True)
    async def clear(self, ctx, amount=15):
        await ctx.channel.purge(limit=amount + 1)
        channel = self.bot.get_channel(864868876897353778)
        message = ['сообщение', 'сообщения', 'сообщений']
        if amount % 10 == 1 and amount % 100 != 11:
            message = message[0]
        elif 2 <= amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
            message = message[1]
        else:
            message = message[2]
        emb = discord.Embed(title=f"Было удалено {amount} {message}", description=f"{ctx.channel.mention}",
                            colour=discord.Color.purple())
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        emb.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=emb)
        await channel.send(embed=emb)


def setup(bot):
    bot.add_cog(Moderation(bot))
