import discord
import json
from discord.ext import commands
from keep_alive import keep_alive
import requests

secret_f = open('secret.json')
secret_data = json.load(secret_f)
TOKENBOT = secret_data['discord-bot']['token']

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='bot ', intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f"{bot.user.name} is now ready for use!")
    print("-------------------------")
    await bot.change_presence(activity=discord.Game(name="bot help"))
    # await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))
    # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))
    # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == 'puja kerang ajaib':
        await message.channel.send('lulululululululululululululululu')
    await bot.process_commands(message)


@bot.command()
async def help(ctx):
    await ctx.send(f"Belum ada command, masih sedang develop, sabar <@{ctx.author.id}>....")


@bot.command()
async def hello(ctx):
    # print(ctx.author.name)
    await ctx.send(f"Hello <@{ctx.author.id}>, Saya HarlanBOT")


@bot.command()
async def say(ctx, *args):
    pesan = ''
    for arg in args:
        pesan += arg + ' '
    print(pesan)
    await ctx.send(pesan)


@bot.command()
async def goodbye(ctx):
    await ctx.send("Ok, Bye")


@bot.command(pass_context=True)
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        # voice.play(source)
    else:
        await ctx.send("Kamu tidak di voice channel")


@bot.command(pass_context=True)
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("Kamu tidak di voice channel")


@bot.event
async def on_member_join(member):
    print(f"Hello")
    # print(f"Hello {member.guild.name}")
    # channel = client.get_channel(983383547790368808)
    # await channel.send('Hello')


@bot.event
async def on_member_remove(member):
    print("Goodbye")


def sendAPI(url):
    headers = {
        'data': "data"
    }
    response = requests.request("GET", url, headers=headers)
    return response.text


bot.run(TOKENBOT)
keep_alive()

# Tutorial YouTube
# https://www.youtube.com/watch?v=cCiqcu2NP8I&list=PL-7Dfw57ZZVRB4N7VWPjmT0Q-2FIMNBMP
# https://discordpy.readthedocs.io/en/stable/api.html
