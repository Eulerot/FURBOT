import discord
from discord_components import DiscordComponents ,Button, ButtonStyle
from discord.ext import commands
from pymongo import MongoClient
from discord import Activity, ActivityType
from config import settings
import string
import asyncio
import time
import json

#body
bot = commands.Bot(command_prefix=settings['prefix'], intents=discord.Intents.all())
cluster = MongoClient("mongodb+srv://FURBOT:HAm-Eb7-fsz-HzW@cluster.5jxn3.mongodb.net/FURBOT?retryWrites=true&w=majority")
mute_list = cluster.mute_list.mute_list
ban_list = cluster.ban_list.ban_list
bot.remove_command('help')
collusers = cluster.warns.collusers

#events


#status
@bot.event
async def on_ready():
    for guild in bot.guilds:
        for member in guild.members:
            values = {
                "_id": member.id,
                "warns": 0,
                "reasons": [],
                "case": 0
            }
        if collusers.count_documents({"_id": member.id}) == 0:
            collusers.insert_one(values)


    DiscordComponents(bot)
    print("""
    ************************
    *BOT HAS BEEN CONNECTED*
    ************************
    """)

    await bot.change_presence(status=discord.Status.idle, activity=Activity(name='за плохими фуррями', type=ActivityType.watching))




#errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.channel.purge(limit=1)
        await ctx.send(f"{ctx.author.mention} сорри,но кажется такой команды нет :/\nЧтобы посмотреть список всех комманда напиши !help")

#on_member_join
@bot.event
async def on_member_join(member):
    strip = len(member.name)
    strip = strip * '—'
    emb = discord.Embed(title=f'Привет!', colour=discord.Color.purple())
    emb.add_field(name='{}'.format(strip), value=f'{member.mention} - новый пушистик на нашем сервере', inline=False)
    emb.add_field(name='Поприветствуем его!', value='Чтобы узнать больше о сервере - перейди в текстовые каналы «информация» и «rules».', inline=False)

    values = {
        "_id": member.id,
        "warns": 0,
        "reasons": [],
        "case": 0
    }
    if collusers.count_documents({"_id": member.id}) == 0:
        collusers.insert_one(values)
    channel = bot.get_channel(864313018636304394)
    muted_role = discord.utils.get(member.guild.roles, id=864857776110174228)
    ban_role = discord.utils.get(member.guild.roles, id=865323020541624401)
    role = discord.utils.get(member.guild.roles, id=864881407230083112)
    if mute_list.count_documents({"_id": member.id}) == 1:
        await member.add_roles(muted_role)
        await asyncio.sleep(time)
        await member.remove_roles(muted_role)
    elif ban_list.count_documents({"_id": member.id}) == 1:
        await member.add_roles(ban_role)
    else:
        await member.add_roles(role)


    await channel.send(embed=emb)
    emb = discord.Embed(title=f'Привет!', colour=discord.Color.purple())
    emb.add_field(name='{}'.format(strip), value=f'{member.mention}, я очень рад,что ты посетил наш сервер!', inline=False)
    await member.send(embed=emb)

#on_member_remove
@bot.event
async def on_member_remove(member):
    strip = len(member.name)
    strip = strip * '—'
    channel = bot.get_channel(864313018636304394)
    emb = discord.Embed(title=f'Пока!(', colour=discord.Color.purple())
    emb.add_field(name='{}'.format(strip), value=f'{member.mention} - покинул наш сервер(', inline=False)
    await channel.send(embed=emb)

#new_voice_channel
@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel != None:
        if after.channel.id == 864316403019939860:
            for guild in bot.guilds:
                maincategory = discord.utils.get(guild.categories,id=864289583566422051)
                new_channel = await guild.create_voice_channel(name=f".{member.display_name}", category=maincategory)
                await new_channel.set_permissions(member, connect=True, move_members=True, manage_channels=True)
                await member.move_to(new_channel)
                def check(x, y, z):
                    return len(new_channel.members) == 0
                await bot.wait_for('voice_state_update', check=check)
                await new_channel.delete()

#warning_system
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.content.split(' ')}.intersection(set(json.load(open('ban_word.json')))) != set():
        await message.delete()



#commands


#help
@bot.command()
async def help(ctx):
    await ctx.channel.purge(limit=1)
    strip = len(ctx.author.name)
    strip = strip*'—'
    emb = discord.Embed(title=f'Команды: ', colour=discord.Color.purple())
    emb.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    emb.add_field(name='———————————{}'.format(strip), value=f'Запрос для {ctx.author.mention}',inline=False)
    emb.add_field(name='{}info @user'.format(settings['prefix']), value='Информация о пользователе',inline=False)
    emb.add_field(name='{}8ball question'.format(settings['prefix']), value='Волшебный шар восьмерка', inline=False)
    emb.add_field(name='{}rp'.format(settings['prefix']), value='Рп-команды', inline=False)
    await ctx.send(embed=emb)

#adminhelp
@bot.command()
@commands.has_permissions(view_audit_log=True)
async def admin(ctx):
    await ctx.channel.purge(limit=1)
    strip=len(ctx.author.name)
    strip=strip*'—'
    emb = discord.Embed(title=f'Команды: ', colour=discord.Color.purple())
    emb.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    emb.add_field(name='———————————{}'.format(strip), value=f'Запрос для {ctx.author.mention}',inline=False)
    emb.add_field(name='{}clear n(натуральное число)'.format(settings['prefix']), value='Очистка чата', inline=False)
    emb.add_field(name='{}mute @user reason time(minutes)'.format(settings['prefix']), value='Мут', inline=False)
    emb.add_field(name='{}unmute @user'.format(settings['prefix']), value='Разут(Доступно только администрации)', inline=False)
    emb.add_field(name='{}kick  @user  reason'.format(settings['prefix']), value='Кик')
    emb.add_field(name='{}ban  @user  reason'.format(settings['prefix']), value='Бан(Доступно только администрации)',inline=False)
    emb.add_field(name='{}unban @user'.format(settings['prefix']), value='Разбан(Доступно только администрации)',inline=False)
    await ctx.send(embed=emb)
#info
@bot.command()
async def info(ctx, member: discord.Member ):
    roles = [role for role in member.roles]
    strip = len(member.name)
    strip = strip * '—'
    await ctx.channel.purge(limit=1)
    emb = discord.Embed(title=f'Информация о {member.name}', colour=discord.Color.purple())
    emb.add_field(name='———————————{}'.format(strip), value=f'Запрос для {ctx.author.mention}', inline=False)
    emb.add_field(name=f"{member.name} присоединился к нам:", value=member.joined_at.strftime("%#d %B %Y,%I:%M %p"),inline=False)
    emb.add_field(name=f"ID:", value=member.id, inline=False)
    emb.add_field(name=f"Аккаунт пользователя был создан:", value=member.created_at.strftime("%#d %B %Y,%I:%M %p"),inline=False)
    emb.add_field(name=f"Роли: ({len(roles)})", value="".join([role.mention for role in roles]),inline=False)
    emb.add_field(name=f"Высшая роль:", value=member.top_role.mention, inline=False)
    emb.set_thumbnail(url=member.avatar_url)
    emb.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)


#mute
@bot.command()
@commands.has_permissions(view_audit_log=True)
async def mute(ctx, member: discord.Member, reason, time:int):
    await ctx.channel.purge(limit=1)
    channel = bot.get_channel(864868876897353778)
    muted_role = discord.utils.get(ctx.guild.roles, id=864857776110174228)

    minute = ['минуту', 'минуты', 'минут']
    if time % 10 == 1 and time % 100 != 11:
        minute = minute[0]
    elif 2 <= time % 10 <= 4 and (time % 100 < 10 or time % 100 >= 20):
        minute = minute[1]
    else:
        minute = minute[2]
    strip = len(member.name)
    strip = strip * '—'

    post = {
        "_id,": member.id,
        "time": time
    }
    mute_list.insert_one(post)


    await member.add_roles(muted_role)
    emb = discord.Embed(title=f'Плохой {member.name} получает мут!По причине: {reason.upper()} на {time} {minute}', colour=discord.Color.purple())
    emb.add_field(name='{}'.format(strip), value=f'{member.mention}',inline=False)
    emb.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)
    await channel.send(embed=emb)
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=1)
    await asyncio.sleep(time*60)
    await member.remove_roles(muted_role)

#unmute
@bot.command()
@commands.has_permissions(view_audit_log=True)
async def unmute(ctx, member: discord.Member):
    strip = len(member.name)
    strip = strip * '—'
    channel = bot.get_channel(864868876897353778)
    await ctx.channel.purge(limit=1)
    muted_role = discord.utils.get(ctx.guild.roles,id=864857776110174228)
    emb = discord.Embed(title=f'Плохой {member.name} размучен!', colour=discord.Color.purple())
    emb.add_field(name='{}'.format(strip), value=f'{member.mention}', inline=False)
    emb.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)
    await channel.send(embed=emb)
    await member.remove_roles(muted_role)
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=1)

#kick
@bot.command()
@commands.has_permissions(view_audit_log=True)
async def kick(ctx, member: discord.Member, *,reason):
    strip = len(member.name)
    strip = strip * '—'
    channel = bot.get_channel(864868876897353778)
    await ctx.channel.purge(limit=1)
    await member.kick(reason=reason)
    emb = discord.Embed(title=f'Плохой {member.name} кикнут! По причине: {reason.upper()}', colour=discord.Color.purple())
    emb.add_field(name='{}'.format(strip), value=f'{member.mention}', inline=False)
    emb.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)
    await channel.send(embed=emb)
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=1)

#ban
@bot.command()
@commands.has_permissions(view_audit_log=True)
async def ban(ctx, member: discord.Member,*,reason):
    ban_role = discord.utils.get(ctx.guild.roles,id=865323020541624401)
    strip = len(member.name)
    strip = strip * '—'
    channel = bot.get_channel(864868876897353778)
    await ctx.channel.purge(limit=1)
    emb = discord.Embed(title=f'Плохой {member.name} получает бан!', colour=discord.Color.purple())
    emb.add_field(name='{}'.format(strip), value=f'{member.mention}', inline=False)
    emb.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    await member.add_roles(ban_role)
    await ctx.send(embed=emb)
    await channel.send(embed=emb)
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=1)

#tempban
@bot.command()
@commands.has_permissions(view_audit_log=True)
async def tempban(ctx, member: discord.Member,reason,time:int):
    ban_role = discord.utils.get(ctx.guild.roles, id=865323020541624401)
    strip = len(member.name)
    strip = strip * '—'
    channel = bot.get_channel(864868876897353778)
    await ctx.channel.purge(limit=1)
    days = ['день', 'дня', 'дней']
    if time % 10 == 1 and time % 100 != 11:
        days = days[0]
    elif 2 <= time % 10 <= 4 and (time % 100 < 10 or time % 100 >= 20):
        days = days[1]
    else:
        days = days[2]
    emb = discord.Embed(title=f'Плохой {member.name} получает бан!По причине: {reason.upper()} на {time} {days}',colour=discord.Color.purple())
    emb.add_field(name='{}'.format(strip), value=f'{member.mention}', inline=False)
    emb.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    await member.add_roles(ban_role)
    await ctx.send(embed=emb)
    await channel.send(embed=emb)
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=1)
    await asyncio.sleep(time*3600*24)
    await member.remove_roles(ban_role)


#unban
@bot.command()
@commands.has_permissions(view_audit_log=True)
async def unban(ctx, member: discord.Member):
    strip = len(member.name)
    strip = strip * '—'
    channel = bot.get_channel(864868876897353778)
    await ctx.channel.purge(limit=1)
    ban_role = discord.utils.get(ctx.guild.roles, id=865323020541624401)
    emb = discord.Embed(title=f'Плохой {member.name} разбнен!', colour=discord.Color.purple())
    emb.add_field(name='{}'.format(strip), value=f'{member.mention}', inline=False)
    emb.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)
    await channel.send(embed=emb)
    await member.remove_roles(ban_role)
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=1)


#clear
@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    emb = discord.Embed(title=f':white_check_mark: Удалено {amount} сообщений', colour=discord.Color.purple())
    emb.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=1)


#rp_commands


#rp
@bot.command()
async def rp(ctx):
    await ctx.channel.purge(limit=1)
    strip = len(ctx.author.name)
    strip = strip*'—'
    emb = discord.Embed(title=f'Команды рп: ', colour=discord.Color.purple())
    emb.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    emb.add_field(name='———————————{}'.format(strip), value=f'Запрос для {ctx.author.mention}', inline=False)
    emb.add_field(name='{}rps @user'.format(settings['prefix']), value='Вызывает участника для рп в лс', inline=False)
    await ctx.send(embed=emb)


#rp_send_user
@bot.command()
async def rps(ctx,member: discord.Member):
    await ctx.channel.purge(limit=1)
    strip = len(ctx.author.name)
    strip = strip * '—'
    emb = discord.Embed(title='ОПА,РП !!!', colour=discord.Color.purple())
    emb.add_field(name='{}'.format(strip), value=f'Ого, {member.mention}, кажется {ctx.author.mention} вызывает тебя для рп! 😺\n ', inline=False)
    comps=[Button(style=ButtonStyle.URL, label="тык для перехода", url="https://discord.gg/sdTNPC4pph")]
    await member.send(embed=emb, components=comps)



#funcommands


@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    await ctx.channel.purge(limit=1)

    if question == "":
        await ctx.send(f"{ctx.author.mention},кажется у тебя пустой вопрос(")
    else:
        emb = discord.Embed(title='Волшебный шар восьмерка!',colour=discord.Color.purple())
        emb.add_field(name=f'Ответ: {response}', value=f'{ctx.author.mention} спрашивает: {question}',inline=False)
        emb.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
        emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)

#errors


#info_error
@info.error
async def info_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.mention},вы не указали @')

#info_error
@_8ball.error
async def _8ball_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.mention},кажется вопрос пуст')

#clear_error
@clear.error
async def clear_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention}, изивини, но кажется у тебя не достаточно прав(")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.mention},надо указать натуральное число!')

#mute_error
@mute.error
async def mute_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention}, изивини, но кажется у тебя не достаточно прав(")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.mention},вы не указали @ или причину, время')

#unmute_error
@unmute.error
async def unmute_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention}, изивини, но кажется у тебя не достаточно прав(")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.mention},вы не указали @')

#kick_error
@kick.error
async def kick_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error,commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention}, изивини, но кажется у тебя не достаточно прав(")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.mention},вы не указали @ или причину')

#ban_error
@ban.error
async def ban_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention}, изивини, но кажется у тебя не достаточно прав(")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.mention},вы не указали @ или причину')

#tempban_error
@tempban.error
async def tempban_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention}, изивини, но кажется у тебя не достаточно прав(")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.mention},вы не указали @ или причину,время')

#unban_error
@unban.error
async def unban_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention}, изивини, но кажется у тебя не достаточно прав(")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.mention},вы не указали @')


bot.run(settings['token'])