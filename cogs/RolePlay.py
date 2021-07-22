import discord
from discord.ext import commands
from discord_components import Button, ButtonStyle


class RolePlay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.command()
    async def rps(self, ctx, member: discord.Member, *, message=None):
        emb = discord.Embed(title='ОПА,РП !!!', description=f"Ого, {member.mention}, кажется {ctx.author.mention} вызывает тебя для рп! 😺", colour=discord.Color.purple())
        if message != None:
            emb.add_field(name="Сообщение", value=f"`{message}`")
        comps = [Button(style=ButtonStyle.URL, label="тык для перехода", url=f"{ctx.message.jump_url}")]
        await member.send(embed=emb, components=comps)

    @commands.command(aliases=["кусь"])
    async def bite(self, ctx, member: discord.Member, *, words=None):
        boy_role = discord.utils.get(member.guild.roles, id=866390060614025216)
        girl_role = discord.utils.get(member.guild.roles, id=866389932402933770)
        await ctx.channel.purge(limit=1)
        name = "Кусь"
        if boy_role in ctx.author.roles and girl_role not in ctx.author.roles:
            gender = "кусьнул"
        elif girl_role in ctx.author.roles and boy_role not in ctx.author.roles:
            gender = "кусьнула"
        else:
            gender = "кусьнул/a"
        if words != None:
            emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} {member.mention}",
                                colour=discord.Color.purple())
            emb.add_field(name="Со словами:", value=f"{words}")
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} {member.mention}",
                                colour=discord.Color.purple())
            await ctx.send(embed=emb)

    @commands.command(aliases=["обнять"])
    async def hug(self, ctx, member: discord.Member, *, words=None):
        boy_role = discord.utils.get(member.guild.roles, id=866390060614025216)
        girl_role = discord.utils.get(member.guild.roles, id=866389932402933770)
        await ctx.channel.purge(limit=1)
        name = "Обнимашки"
        if boy_role in ctx.author.roles and girl_role not in ctx.author.roles:
            gender = "обнял"
        elif girl_role in ctx.author.roles and boy_role not in ctx.author.roles:
            gender = "обняла"
        else:
            gender = "обнял/а"
        if words != None:
            emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} {member.mention}",
                                colour=discord.Color.purple())
            emb.add_field(name="Со словами:", value=f"{words}")
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} {member.mention}",
                                colour=discord.Color.purple())
            await ctx.send(embed=emb)

    @commands.command(aliases=["кис", "поцеловать"])
    async def kiss(self, ctx, member: discord.Member, *, words=None):
        boy_role = discord.utils.get(member.guild.roles, id=866390060614025216)
        girl_role = discord.utils.get(member.guild.roles, id=866389932402933770)
        await ctx.channel.purge(limit=1)
        name = "Целовашки"
        if boy_role in ctx.author.roles and girl_role not in ctx.author.roles:
            gender = "поцеловал"
        elif girl_role in ctx.author.roles and boy_role not in ctx.author.roles:
            gender = "поцеловала"
        else:
            gender = "поцеловал/а"
        if words != None:
            emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} {member.mention}",
                                colour=discord.Color.purple())
            emb.add_field(name="Со словами:", value=f"{words}")
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} {member.mention}",
                                colour=discord.Color.purple())
            await ctx.send(embed=emb)

    @commands.command(aliases=["погладить"])
    async def pat(self, ctx, member: discord.Member, *, words=None):
        boy_role = discord.utils.get(member.guild.roles, id=866390060614025216)
        girl_role = discord.utils.get(member.guild.roles, id=866389932402933770)
        await ctx.channel.purge(limit=1)
        name = "Погладить"
        if boy_role in ctx.author.roles and girl_role not in ctx.author.roles:
            gender = "погладил"
        elif girl_role in ctx.author.roles and boy_role not in ctx.author.roles:
            gender = "погладила"
        else:
            gender = "погладил/а"
        if words != None:
            emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} {member.mention}",
                                colour=discord.Color.purple())
            emb.add_field(name="Со словами:", value=f"{words}")
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} {member.mention}",
                                colour=discord.Color.purple())
            await ctx.send(embed=emb)

    @commands.command(aliases=["тык"])
    async def touch(self, ctx, member: discord.Member = None, *, words=None):
        boy_role = discord.utils.get(member.guild.roles, id=866390060614025216)
        girl_role = discord.utils.get(member.guild.roles, id=866389932402933770)
        await ctx.channel.purge(limit=1)
        name = "Тык"
        if boy_role in ctx.author.roles and girl_role not in ctx.author.roles:
            gender = "тыкнул"
        elif girl_role in ctx.author.roles and boy_role not in ctx.author.roles:
            gender = "тыкнула"
        else:
            gender = "тыкнул/а"
        if member != None:
            if words != None:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} {member.mention}",
                                    colour=discord.Color.purple())
                emb.add_field(name="Со словами:", value=f"{words}")
                await ctx.send(embed=emb)
            else:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} {member.mention}",
                                    colour=discord.Color.purple())
                await ctx.send(embed=emb)
        else:
            if words != None:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}",
                                    colour=discord.Color.purple())
                emb.add_field(name="Со словами:", value=f"{words}")
                await ctx.send(embed=emb)
            else:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}",
                                    colour=discord.Color.purple())
                await ctx.send(embed=emb)

    @commands.command(aliases=["буп"])
    async def boop(self, ctx, member: discord.Member = None, *, words=None):
        boy_role = discord.utils.get(member.guild.roles, id=866390060614025216)
        girl_role = discord.utils.get(member.guild.roles, id=866389932402933770)
        await ctx.channel.purge(limit=1)
        name = "Бупь"
        if boy_role in ctx.author.roles and girl_role not in ctx.author.roles:
            gender = "сделал буп"
        elif girl_role in ctx.author.roles and boy_role not in ctx.author.roles:
            gender = "сделала буп"
        else:
            gender = "сделал/а буп"
        if member != None:
            if words != None:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} {member.mention}",
                                    colour=discord.Color.purple())
                emb.add_field(name="Со словами:", value=f"{words}")
                await ctx.send(embed=emb)
            else:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} {member.mention}",
                                    colour=discord.Color.purple())
                await ctx.send(embed=emb)
        else:
            if words != None:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}",
                                    colour=discord.Color.purple())
                emb.add_field(name="Со словами:", value=f"{words}")
                await ctx.send(embed=emb)
            else:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}",
                                    colour=discord.Color.purple())
                await ctx.send(embed=emb)

    @commands.command(aliases=["лизь"])
    async def lick(self, ctx, member: discord.Member = None, *, words=None):
        boy_role = discord.utils.get(member.guild.roles, id=866390060614025216)
        girl_role = discord.utils.get(member.guild.roles, id=866389932402933770)
        await ctx.channel.purge(limit=1)
        name = "Лизь"
        if boy_role in ctx.author.roles and girl_role not in ctx.author.roles:
            gender = "лизнул"
        elif girl_role in ctx.author.roles and boy_role not in ctx.author.roles:
            gender = "лизнула"
        else:
            gender = "лизнул/а"
        if member != None:
            if words != None:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} {member.mention}",
                                    colour=discord.Color.purple())
                emb.add_field(name="Со словами:", value=f"{words}")
                await ctx.send(embed=emb)
            else:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} {member.mention}",
                                    colour=discord.Color.purple())
                await ctx.send(embed=emb)
        else:
            if words != None:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}",
                                    colour=discord.Color.purple())
                emb.add_field(name="Со словами:", value=f"{words}")
                await ctx.send(embed=emb)
            else:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}",
                                    colour=discord.Color.purple())
                await ctx.send(embed=emb)

    @commands.command(aliases=["хвост", "хвостик"])
    async def tail(self, ctx, *, words=None):
        await ctx.channel.purge(limit=1)
        boy_role = discord.utils.get(ctx.guild.roles, id=866390060614025216)
        girl_role = discord.utils.get(ctx.guild.roles, id=866389932402933770)
        await ctx.channel.purge(limit=1)
        name = "Пождать хвостик"
        if boy_role in ctx.author.roles and girl_role not in ctx.author.roles:
            gender = "поджал хвостик"
        elif girl_role in ctx.author.roles and boy_role not in ctx.author.roles:
            gender = "поджала хвостик"
        else:
            gender = "поджал/а хвостик"
        if words != None:
            emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}", colour=discord.Color.purple())
            emb.add_field(name="Со словами:", value=f"{words}")
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}", colour=discord.Color.purple())
            await ctx.send(embed=emb)

    @commands.command(aliases=["ррр", "рав", "гав"])
    async def roar(self, ctx, member: discord.Member = None, *, words=None):
        boy_role = discord.utils.get(ctx.guild.roles, id=866390060614025216)
        girl_role = discord.utils.get(ctx.guild.roles, id=866389932402933770)
        name = "Ррр"
        await ctx.channel.purge(limit=1)
        if boy_role in ctx.author.roles and girl_role not in ctx.author.roles:
            gender = "зарычал"
        elif girl_role in ctx.author.roles and boy_role not in ctx.author.roles:
            gender = "зарычала"
        else:
            gender = "зарычал/а"
        if member != None:
            if words != None:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} на {member.mention}",
                                    colour=discord.Color.purple())
                emb.add_field(name="Со словами:", value=f"{words}")
                await ctx.send(embed=emb)
            else:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} на {member.mention}",
                                    colour=discord.Color.purple())
                await ctx.send(embed=emb)
        else:
            if words != None:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}",
                                    colour=discord.Color.purple())
                emb.add_field(name="Со словами:", value=f"{words}")
                await ctx.send(embed=emb)
            else:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}",
                                    colour=discord.Color.purple())
                await ctx.send(embed=emb)

    @commands.command(aliases=["мур", "мурр", "mur"])
    async def murr(self, ctx, member: discord.Member = None, *, words=None):
        boy_role = discord.utils.get(ctx.guild.roles, id=866390060614025216)
        girl_role = discord.utils.get(ctx.guild.roles, id=866389932402933770)
        name = "Мурьк"
        await ctx.channel.purge(limit=1)
        if boy_role in ctx.author.roles and girl_role not in ctx.author.roles:
            gender = "помурчал"
        elif girl_role in ctx.author.roles and boy_role not in ctx.author.roles:
            gender = "помурчала"
        else:
            gender = "помурчал/а"
        if member != None:
            if words != None:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} для {member.mention}",
                                    colour=discord.Color.purple())
                emb.add_field(name="Со словами:", value=f"{words}")
                await ctx.send(embed=emb)
            else:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} для {member.mention}",
                                    colour=discord.Color.purple())
                await ctx.send(embed=emb)
        else:
            if words != None:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}",
                                    colour=discord.Color.purple())
                emb.add_field(name="Со словами:", value=f"{words}")
                await ctx.send(embed=emb)
            else:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}",
                                    colour=discord.Color.purple())
                await ctx.send(embed=emb)

    @commands.command(aliases=["чмок"])
    async def smooch(self, ctx, member: discord.Member = None, *, words=None):
        boy_role = discord.utils.get(member.guild.roles, id=866390060614025216)
        girl_role = discord.utils.get(member.guild.roles, id=866389932402933770)
        await ctx.channel.purge(limit=1)
        name = "Чмок"
        if boy_role in ctx.author.roles and girl_role not in ctx.author.roles:
            gender = "чмокнул"
        elif girl_role in ctx.author.roles and boy_role not in ctx.author.roles:
            gender = "чмокнула"
        else:
            gender = "чмокнул/а"
        if words != None:
            emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} {member.mention}",
                                colour=discord.Color.purple())
            emb.add_field(name="Со словами:", value=f"{words}")
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} {member.mention}",
                                colour=discord.Color.purple())
            await ctx.send(embed=emb)

    @commands.command(aliases=["понюхать", "снифф", "сниф"])
    async def sniff(self, ctx, member: discord.Member = None, *, words=None):
        boy_role = discord.utils.get(ctx.guild.roles, id=866390060614025216)
        girl_role = discord.utils.get(ctx.guild.roles, id=866389932402933770)
        name = "Sniff"
        await ctx.channel.purge(limit=1)
        if boy_role in ctx.author.roles and girl_role not in ctx.author.roles:
            gender = "понюхал"
        elif girl_role in ctx.author.roles and boy_role not in ctx.author.roles:
            gender = "понюхала"
        else:
            gender = "понюхал/а"
        if member != None:
            if words != None:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} {member.mention}",
                                    colour=discord.Color.purple())
                emb.add_field(name="Со словами:", value=f"{words}")
                await ctx.send(embed=emb)
            else:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} {member.mention}",
                                    colour=discord.Color.purple())
                await ctx.send(embed=emb)
        else:
            if words != None:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}",
                                    colour=discord.Color.purple())
                emb.add_field(name="Со словами:", value=f"{words}")
                await ctx.send(embed=emb)
            else:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}",
                                    colour=discord.Color.purple())
                await ctx.send(embed=emb)

    @commands.command(aliases=["йифф", "йиф"])
    async def yiff(self, ctx, member: discord.Member = None, *, words=None):
        boy_role = discord.utils.get(member.guild.roles, id=866390060614025216)
        girl_role = discord.utils.get(member.guild.roles, id=866389932402933770)
        await ctx.channel.purge(limit=1)
        name = "Йифф"
        if boy_role in ctx.author.roles and girl_role not in ctx.author.roles:
            gender = "йиффнул"
        elif girl_role in ctx.author.roles and boy_role not in ctx.author.roles:
            gender = "йиффнула"
        else:
            gender = "йиффнул/а"
        if member != None:
            if words != None:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} {member.mention}",
                                    colour=discord.Color.purple())
                emb.add_field(name="Со словами:", value=f"{words}")
                await ctx.send(embed=emb)
            else:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} {member.mention}",
                                    colour=discord.Color.purple())
                await ctx.send(embed=emb)
        else:
            if words != None:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}",
                                    colour=discord.Color.purple())
                emb.add_field(name="Со словами:", value=f"{words}")
                await ctx.send(embed=emb)
            else:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}",
                                    colour=discord.Color.purple())
                await ctx.send(embed=emb)

    @commands.command(aliases=["раздеться", "раздеть"])
    async def dressoff(self, ctx, member: discord.Member, *, words=None):
        boy_role = discord.utils.get(member.guild.roles, id=866390060614025216)
        girl_role = discord.utils.get(member.guild.roles, id=866389932402933770)
        await ctx.channel.purge(limit=1)
        name = "Раздеться"
        if boy_role in ctx.author.roles and girl_role not in ctx.author.roles:
            gender_ = "раздел"
        elif girl_role in ctx.author.roles and boy_role not in ctx.author.roles:
            gender_ = "раздела"
        else:
            gender_ = "раздел/а"
        if boy_role in ctx.author.roles and girl_role not in ctx.author.roles:
            gender = "разделся"
        elif girl_role in ctx.author.roles and boy_role not in ctx.author.roles:
            gender = "разделась"
        else:
            gender = "разделся/ась"
        if member != None:
            if words != None:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender_} {member.mention}",
                                    colour=discord.Color.purple())
                emb.add_field(name="Со словами:", value=f"{words}")
                await ctx.send(embed=emb)
            else:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender_} {member.mention}",
                                    colour=discord.Color.purple())
                await ctx.send(embed=emb)
        else:
            if words != None:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}",
                                    colour=discord.Color.purple())
                emb.add_field(name="Со словами:", value=f"{words}")
                await ctx.send(embed=emb)
            else:
                emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}",
                                    colour=discord.Color.purple())
                await ctx.send(embed=emb)

    @commands.command(aliases=["грусть"])
    async def sad(self, ctx, *, words=None):
        await ctx.channel.purge(limit=1)
        gender = "грустит..."
        name = "Грусть("
        if words != None:
            emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}", colour=discord.Color.darker_grey())
            emb.add_field(name="Со словами:", value=f"{words}")
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}", colour=discord.Color.darker_grey())
            await ctx.send(embed=emb)

    @commands.command(aliases=["плак"])
    async def cry(self, ctx, *, words=None):
        await ctx.channel.purge(limit=1)
        name = "Плак"
        gender = "плачет"
        if words != None:
            emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}", colour=discord.Color.darker_grey())
            emb.add_field(name="Со словами:", value=f"{words}")
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}", colour=discord.Color.darker_grey())
            await ctx.send(embed=emb)

    @commands.command(aliases=["спать", "уснуть"])
    async def sleep(self, ctx, *, words=None):
        await ctx.channel.purge(limit=1)
        name = "Сон"
        gender = "засыпает"
        if words != None:
            emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}",
                                colour=discord.Color.darker_grey())
            emb.add_field(name="Со словами:", value=f"{words}")
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}",
                                colour=discord.Color.darker_grey())
            await ctx.send(embed=emb)

    @commands.command(aliases=["лещ"])
    async def slap(self, ctx, member: discord.Member, *, words=None):
        await ctx.channel.purge(limit=1)
        name = "Пощечина"
        gender = "дает леща"
        if words != None:
            emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} {member.mention}",
                                colour=discord.Color.darker_grey())
            emb.add_field(name="Со словами:", value=f"{words}")
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender} {member.mention}",
                                colour=discord.Color.darker_grey())
            await ctx.send(embed=emb)

    @commands.command(aliases=["курить"])
    async def smoke(self, ctx, *, words=None):
        await ctx.channel.purge(limit=1)
        name = "Курение"
        gender = "курит"
        if words != None:
            emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}", colour=discord.Color.darker_grey())
            emb.add_field(name="Со словами:", value=f"{words}")
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title=f"{name}", description=f"{ctx.author.mention} {gender}", colour=discord.Color.darker_grey())
            await ctx.send(embed=emb)


def setup(bot):
    bot.add_cog(RolePlay(bot))
