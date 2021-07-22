import discord
from discord.ext import commands


class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before, after):
        if after.channel != None:
            if after.channel.id == 864316403019939860:
                for guild in self.bot.guilds:
                    category = discord.utils.get(guild.categories, id=864289583566422051)
                    new_channel = await guild.create_voice_channel(name=f".{member.display_name}", category=category)
                    ChannelID = new_channel.id
                    data = {
                        '_id': member.id,
                        'ChannelID': ChannelID,
                    }
                    await self.bot.voices.upsert(data)
                    self.bot.voice_channel[member.id] = data
                    self.bot.voice_channel[ChannelID] = data
                    await member.move_to(new_channel)
                    await new_channel.set_permissions(self.bot.user, connect=True, read_messages=True)
                    await new_channel.edit(user_limit=5)
                    def check(x, y, z):
                        return len(new_channel.members) == 0
                    await self.bot.wait_for('voice_state_update', check=check)
                    await new_channel.delete()
                    await self.bot.voices.delete(member.id)
                    try:
                        self.bot.voice_channel.pop(member.id)
                    except KeyError:
                        pass

    @commands.command(aliases=["lim"])
    async def limit(self, ctx, limit: int):
        await ctx.channel.purge(limit=1)
        if limit < 0 or limit > 100:
            await ctx.send(f"{ctx.author.mention}, минимальное количество слотов - 0,максимальное - 99")
        else:
            member = ctx.author.id
            memberID = await self.bot.voices.find_by_id(member)
            if not memberID:
                await ctx.send(f"{ctx.author.mention},к сожалению,ты не владелец канала,либо он не существует")
            else:
                channelID = self.bot.get_channel(memberID["ChannelID"])
                await channelID.edit(user_limit=limit)
                await ctx.send(f"{ctx.author.mention}, {channelID.mention} изменен,количество слотов - `{limit}`")

    @commands.command(aliases=["name"])
    async def rename(self, ctx, name):
        await ctx.channel.purge(limit=1)
        member = ctx.author.id
        memberID = await self.bot.voices.find_by_id(member)
        if not memberID:
            await ctx.send(f"{ctx.author.mention},к сожалению,ты не владелец канала,либо он не существует")
        else:
            channelID = self.bot.get_channel(memberID["ChannelID"])
            await channelID.edit(name=name)
            await ctx.send(f"{ctx.author.mention}, {channelID.mention} изменен,название - `{name}`")

    @commands.command()
    async def lock(self, ctx):
        await ctx.channel.purge(limit=1)
        member = ctx.author.id
        memberID = await self.bot.voices.find_by_id(member)
        if not memberID:
            await ctx.send(f"{ctx.author.mention},к сожалению,ты не владелец канала,либо он не существует")
        else:
            role = ctx.guild.default_role
            channelID = self.bot.get_channel(memberID["ChannelID"])
            await channelID.set_permissions(role, connect=False)
            await ctx.send(f"{ctx.author.mention}, {channelID.mention} `закрыт`")

    @commands.command()
    async def unlock(self, ctx):
        await ctx.channel.purge(limit=1)
        member = ctx.author.id
        memberID = await self.bot.voices.find_by_id(member)
        if not memberID:
            await ctx.send(f"{ctx.author.mention},к сожалению,ты не владелец канала,либо он не существует")
        else:
            role = ctx.guild.default_role
            channelID = self.bot.get_channel(memberID["ChannelID"])
            await channelID.set_permissions(role, connect=None)
            await ctx.send(f"{ctx.author.mention}, {channelID.mention} `открыт`")

    @commands.command(aliases=["allow"])
    async def permit(self, ctx, user: discord.Member):
        await ctx.channel.purge(limit=1)
        member = ctx.author.id
        memberID = await self.bot.voices.find_by_id(member)
        if not memberID:
            await ctx.send(f"{ctx.author.mention},к сожалению,ты не владелец канала,либо он не существует")
        else:
            channelID = self.bot.get_channel(memberID["ChannelID"])
            await channelID.set_permissions(user, connect=True)
            await ctx.send(f'{ctx.author.mention}, {channelID.mention} изменен,{user.mention} имеет возможность подключаться к чату')

    @commands.command(aliases=["deny"])
    async def veto(self, ctx, user: discord.Member):
        await ctx.channel.purge(limit=1)
        member = ctx.author.id
        memberID = await self.bot.voices.find_by_id(member)
        if not memberID:
            await ctx.send(f"{ctx.author.mention},к сожалению,ты не владелец канала,либо он не существует")
        else:
            channelID = self.bot.get_channel(memberID["ChannelID"])
            await channelID.set_permissions(user, connect=False, read_messages=True)
            for members in channelID.members:
                if members.id == user.id:
                    kick_channel = await ctx.guild.create_voice_channel("kick")
                    await user.move_to(kick_channel)
                    await kick_channel.delete()
                    context = f'{ctx.author.mention}, {channelID.mention} изменен,{user.mention} не имеет возможность подключаться к чату'
                else:
                    context = f'{ctx.author.mention},этот пользователь не находится в {channelID.mention} '
            await ctx.send(context)

    @commands.command()
    async def vkick(self, ctx, user: discord.Member):
        await ctx.channel.purge(limit=1)
        member = ctx.author.id
        memberID = await self.bot.voices.find_by_id(member)
        if not memberID:
            await ctx.send(f"{ctx.author.mention},к сожалению,ты не владелец канала,либо он не существует")
        else:
            channelID = self.bot.get_channel(memberID["ChannelID"])
            for members in channelID.members:
                if members.id == user.id:
                    kick_channel = await ctx.guild.create_voice_channel("kick")
                    await user.move_to(kick_channel)
                    await kick_channel.delete()
                    context = f'{ctx.author.mention},{user.mention} исключен из {channelID.mention} '
                else:
                    context = f'{ctx.author.mention},этот пользователь не находится в {channelID.mention} '
            await ctx.send(context)


def setup(bot):
    bot.add_cog(Voice(bot))