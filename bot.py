import os
import logging
from pathlib import Path

import motor.motor_asyncio

import discord
from discord.ext import commands
from discord import Activity, ActivityType
from discord_components import DiscordComponents

import utils.json
from utils.mongo import Document

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")


async def get_prefix(bot, message):
    if not message.guild:
        return commands.when_mentioned_or(bot.DEFAULTPREFIX)(bot, message)

    try:
        data = await bot.config.find(message.guild.id)

        if not data or "prefix" not in data:
            return commands.when_mentioned_or(bot.DEFAULTPREFIX)(bot, message)
        return commands.when_mentioned_or(data["prefix"])(bot, message)
    except:
        return commands.when_mentioned_or(bot.DEFAULTPREFIX)(bot, message)


DEFAULTPREFIX = "!"
secret_file = utils.json.read_json('secret')

bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents=discord.Intents.all(),
                   owner_id=361101019326840844)
DiscordComponents(bot)
bot.remove_command("help")

bot.config_token = secret_file["token"]
bot.connection_url = secret_file["mongo"]
logging.basicConfig(level=logging.INFO)

bot.DEFAULTPREFIX = DEFAULTPREFIX
bot.voice_channel = {}
bot.banned_users = {}
bot.muted_users = {}
bot.cwd = cwd


@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n")
    await bot.change_presence(status=discord.Status.idle,
                              activity=Activity(name='за плохими фуррями', type=ActivityType.watching))
    bot.mongo = motor.motor_asyncio.AsyncIOMotorClient(str(bot.connection_url))
    bot.db = bot.mongo['bot_config']
    bot.config = Document(bot.db, "secret.json")
    bot.mutes = Document(bot.db, "mutes.json")
    bot.bans = Document(bot.db, "bans.json")
    bot.voices = Document(bot.db, "voices.json")

    for document in await bot.config.get_all():
        print(document)
    currentMutes = await bot.mutes.get_all()
    for mute in currentMutes:
        bot.muted_users[mute["_id"]] = mute
    print(bot.muted_users)
    currentBans = await bot.bans.get_all()
    for ban in currentBans:
        bot.banned_users[ban["_id"]] = ban
    print(bot.muted_users)
    print("Connect with Database\n-----")


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.lower().startswith("help"):
        await message.channel.send("Тебе надо написать !help")
        await message.delete()
    if message.content.lower().startswith("хелп"):
        await message.delete()
        await message.channel.send("Тебе надо написать !help")
    if message.content.startswith("OwO"):
        await message.channel.reply("UwU")
    if message.content.startswith("UwU"):
        await message.channel.reply("OwO")
    if message.content.startswith(f"<@!{bot.user.id}>") and len(message.content) == len(f"<@!{bot.user.id}>"):
        data = await bot.config.get_by_id(message.guild.id)
        if not data or "prefix" not in data:
            prefix = bot.DEFAULTPREFIX
        else:
            prefix = data["prefix"]
        await message.channel.send(f"Мой префикс - `{prefix}`")
    if message.content.lower().startswith("цирк"):
        await message.channel.reply("А Админ в нем клоун")

    await bot.process_commands(message)


if __name__ == "__main__":
    for file in os.listdir(cwd + "/cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.{file[:-3]}")

    bot.run(bot.config_token)
