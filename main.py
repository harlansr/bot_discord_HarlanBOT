import discord
import json
from discord.ext import commands
from keep_alive import keep_alive

secret_f = open('secret.json')
secret_data = json.load(secret_f)

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print("BOT is now ready for use!")
    print("-------------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am the youtube bot")


client.run(secret_data['discord-bot']['token'])
keep_alive()

# https://www.youtube.com/watch?v=cCiqcu2NP8I&list=PL-7Dfw57ZZVRB4N7VWPjmT0Q-2FIMNBMP