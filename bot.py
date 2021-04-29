import discord
from discord.ext import commands
import setting

token = setting.get_token()

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Logged in")

@bot.command()
async def member(ctx, specified_num=2):
    auth = ctx.author.voice
    mem = [i.name for i in auth.channel.members]
    await ctx.channel.send(mem)

bot.run(token)