import datetime
import discord
from discord.ext import commands


class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["хелп", "h"])
    async def help(self, ctx):
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title="Команды", description=f"Запрос для {ctx.author.mention}",
                            color=discord.Color.purple())
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        emb.timestamp = datetime.datetime.utcnow()
        emb.add_field(name="●", value="ㅤ")
        emb.add_field(name="Вид", value="`{}kick @user ~причина`".format(self.bot.DEFAULTPREFIX))
        emb.add_field(name="Фунцкия", value="`Исключает участника сервера`")

    @commands.command(aliases=["a"])
    @commands.has_permissions(view_audit_log=True)
    async def admin(self, ctx):
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title="Команды", description=f"Запрос для {ctx.author.mention}",
                            color=discord.Color.purple())
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        emb.timestamp = datetime.datetime.utcnow()
        emb.add_field(name="●", value="ㅤ")
        emb.add_field(name="Вид", value="`{}kick @user ~причина`".format(self.bot.DEFAULTPREFIX))
        emb.add_field(name="Фунцкия", value="`Исключает участника сервера`")
        emb.add_field(name="●", value="ㅤ")
        emb.add_field(name="Вид", value="`{}ban @user ~причина ~time`".format(self.bot.DEFAULTPREFIX))
        emb.add_field(name="Фунцкия", value="`Банит участника сервера`")
        emb.add_field(name="●", value="ㅤ")
        emb.add_field(name="Вид", value="`{}unban @user`".format(self.bot.DEFAULTPREFIX))
        emb.add_field(name="Фунцкия", value="`Разбанивает участника сервера`")
        emb.add_field(name="●", value="ㅤ")
        emb.add_field(name="Вид", value="`{}mute @user ~причина ~time`".format(self.bot.DEFAULTPREFIX))
        emb.add_field(name="Фунцкия", value="`Мутит участника сервера`")
        emb.add_field(name="●", value="ㅤ")
        emb.add_field(name="Вид", value="`{}unmute @user`".format(self.bot.DEFAULTPREFIX))
        emb.add_field(name="Фунцкия", value="`Размучивает участника сервера`")
        emb.add_field(name="●", value="ㅤ")
        emb.add_field(name="Вид", value="`{}clear ~n`".format(self.bot.DEFAULTPREFIX))
        emb.add_field(name="Фунцкия", value="`Удаляет сообщения`")
        await ctx.send(embed=emb)

    @commands.command(aliases=["as"])
    async def rp(self, ctx, page=1):
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title="Команды рп(3 страницы)", description=f"Запрос для {ctx.author.mention}",
                            color=discord.Color.purple())
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        if page == 1:
            emb.timestamp = datetime.datetime.utcnow()
            emb.add_field(name="●", value=f"Страница {page}")
            emb.add_field(name="ㅤ", value=f"ㅤ")
            emb.add_field(name="ㅤ", value=f"ㅤ")
            emb.add_field(name="●", value="ㅤ")
            emb.add_field(name="Вид", value="`{}rps @user ~сообщение`".format(self.bot.DEFAULTPREFIX))
            emb.add_field(name="Фунцкия", value="`Уведомляет участника о рп`")
            emb.add_field(name="●", value="ㅤ")
            emb.add_field(name="Вид", value="`{}обнять @user ~слова`".format(self.bot.DEFAULTPREFIX))
            emb.add_field(name="Фунцкия", value="`*Обнимает*`")
            emb.add_field(name="●", value="ㅤ")
            emb.add_field(name="Вид", value="`{}поцеловать @user ~слова`".format(self.bot.DEFAULTPREFIX))
            emb.add_field(name="Фунцкия", value="`*Целует*`")
            emb.add_field(name="●", value="ㅤ")
            emb.add_field(name="Вид", value="`{}чмок @user ~слова`".format(self.bot.DEFAULTPREFIX))
            emb.add_field(name="Фунцкия", value="`*Чмокает*`")
            emb.add_field(name="●", value="ㅤ")
            emb.add_field(name="Вид", value="`{}погладить @user ~слова`".format(self.bot.DEFAULTPREFIX))
            emb.add_field(name="Фунцкия", value="`*Гладит*`")
            emb.add_field(name="●", value="ㅤ")
            emb.add_field(name="Вид", value="`{}буп ~@user ~слова`".format(self.bot.DEFAULTPREFIX))
            emb.add_field(name="Фунцкия", value="`*Бупь*`")
            emb.add_field(name="●", value="ㅤ")
            emb.add_field(name="Вид", value="`{}тык ~@user ~слова`".format(self.bot.DEFAULTPREFIX))
            emb.add_field(name="Фунцкия", value="`*Тык*`")
        elif page == 2:
            emb.add_field(name="●", value=f"Страница {page}")
            emb.add_field(name="ㅤ", value=f"ㅤ")
            emb.add_field(name="ㅤ", value=f"ㅤ")
            emb.add_field(name="●", value="ㅤ")
            emb.add_field(name="Вид", value="`{}лизь ~@user ~слова`".format(self.bot.DEFAULTPREFIX))
            emb.add_field(name="Фунцкия", value="`*Лизь*`")
            emb.add_field(name="●", value="ㅤ")
            emb.add_field(name="Вид", value="`{}кусь @user ~слова`".format(self.bot.DEFAULTPREFIX))
            emb.add_field(name="Фунцкия", value="`*Кусь*`")
            emb.add_field(name="●", value="ㅤ")
            emb.add_field(name="Вид", value="`{}снифф ~@user ~слова`".format(self.bot.DEFAULTPREFIX))
            emb.add_field(name="Фунцкия", value="`*Нюхает*`")
            emb.add_field(name="●", value="ㅤ")
            emb.add_field(name="Вид", value="`{}хвост ~слова`".format(self.bot.DEFAULTPREFIX))
            emb.add_field(name="Фунцкия", value="`*Поджать хвост*`")
            emb.add_field(name="●", value="ㅤ")
            emb.add_field(name="Вид", value="`{}ррр ~@user ~слова`".format(self.bot.DEFAULTPREFIX))
            emb.add_field(name="Фунцкия", value="`*Рык*`")
            emb.add_field(name="●", value="ㅤ")
            emb.add_field(name="Вид", value="`{}мур ~@user ~слова`".format(self.bot.DEFAULTPREFIX))
            emb.add_field(name="Фунцкия", value="`*Муррр*`")
            emb.add_field(name="●", value="ㅤ")
            emb.add_field(name="Вид", value="`{}йифф ~@user ~слова`".format(self.bot.DEFAULTPREFIX))
            emb.add_field(name="Фунцкия", value="`*Йифф*`")
        elif page == 3:
            emb.add_field(name="●", value=f"Страница {page}")
            emb.add_field(name="ㅤ", value=f"ㅤ")
            emb.add_field(name="ㅤ", value=f"ㅤ")
            emb.add_field(name="●", value="ㅤ")
            emb.add_field(name="Вид", value="`{}плак ~слова`".format(self.bot.DEFAULTPREFIX))
            emb.add_field(name="Фунцкия", value="`*Плак*`")
            emb.add_field(name="●", value="ㅤ")
            emb.add_field(name="Вид", value="`{}грусть ~слова`".format(self.bot.DEFAULTPREFIX))
            emb.add_field(name="Фунцкия", value="`*Грусть(*`")
            emb.add_field(name="●", value="ㅤ")
            emb.add_field(name="Вид", value="`{}спать ~слова`".format(self.bot.DEFAULTPREFIX))
            emb.add_field(name="Фунцкия", value="`*Спать*`")
            emb.add_field(name="●", value="ㅤ")
            emb.add_field(name="Вид", value="`{}лещ ~слова`".format(self.bot.DEFAULTPREFIX))
            emb.add_field(name="Фунцкия", value="`*Пощечина*`")
            emb.add_field(name="●", value="ㅤ")
            emb.add_field(name="Вид", value="`{}курить ~слова`".format(self.bot.DEFAULTPREFIX))
            emb.add_field(name="Фунцкия", value="`*Курить*`")
        else:
            emb = discord.Embed(description=f"{ctx.author.mention},кажется такой страницы нет :/")
        await ctx.send(embed=emb)

    @commands.command()
    async def info(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        else:
            pass
        show_roles = ", ".join(
            [f"<@&{x.id}>" for x in sorted(member.roles, key=lambda x: x.position, reverse=True) if x.id != ctx.guild.default_role.id]
        ) if len(member.roles) > 1 else "None"
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title=f'Информация о {member.name}', description=f'Запрос для {ctx.author.mention}', colour=discord.Color.purple())
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        emb.timestamp = datetime.datetime.utcnow()
        emb.add_field(name=f"ID", value=member.id, inline=False)
        emb.add_field(name=f"Аккаунт пользователя был создан", value=member.created_at.strftime("%#d %B %Y,%I:%M %p"),
                      inline=False)
        emb.add_field(name=f"{member.name} присоединился к нам:", value=member.joined_at.strftime("%#d %B %Y,%I:%M %p"),inline=False)
        emb.add_field(name=f"Роли", value=show_roles, inline=False)
        emb.add_field(name=f"Высшая роль:", value=member.top_role.mention, inline=False)
        emb.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=emb)

    @commands.command(aliases=["rep"])
    async def report(self, ctx, member: discord.Member, *, reason=None):
        await ctx.channel.purge(limit=1)
        channel = self.bot.get_channel(866368831994855455)
        if reason != None:
            await ctx.send(
                f"Жалоба на участника {member.mention} отправлена.\nАдминистрация в ближайшее время рассмотрит жалобу.")
            emb = discord.Embed(title=f"Жалоба на игрока", description=f"{member.mention}",
                                colour=discord.Color.purple())
            emb.add_field(name="Причина", value=f"{reason}")
            emb.add_field(name="Отправитель", value=f"{ctx.author.mention}")
            emb.timestamp = datetime.datetime.utcnow()
        else:
            await ctx.send(
                f"Жалоба на участника {member.mention} отправлена.\nАдминистрация в ближайшее время рассмотрит жалобу.")
            emb = discord.Embed(title=f"Жалоба на игрока", description=f"{member.mention}",
                                colour=discord.Color.purple())
            emb.add_field(name="Причина", value="Без причины")
            emb.add_field(name="Отправитель", value=f"{ctx.author.mention}")
            emb.timestamp = datetime.datetime.utcnow()
        await channel.send(embed=emb)

def setup(bot):
    bot.add_cog(HelpCommands(bot))
