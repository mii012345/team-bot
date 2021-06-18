import discord
from discord.ext import commands
import setting
from radb import Radb

token = setting.get_token()

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

radb = Radb()

@bot.event
async def on_ready():
    print("Logged in")

@bot.command()
async def member(ctx, specified_num=2):
    auth = ctx.author.voice
    mem = [i.name for i in auth.channel.members]
    await ctx.channel.send(mem)

@bot.command()
async def team(ctx, specified_num=2):
    auth = ctx.author.voice
    mem = [i.name for i in auth.channel.members]
    ct = len(mem)

@bot.command()
async def ready(ctx):
    mes = await ctx.channel.send("@everyone 紅白戦参加する人は押してください！")
    await mes.add_reaction("👍")
    radb.set_ready_mes(mes)

@bot.command()
async def go(ctx, specified_num=2):
    await radb.get_battle_member(ctx)
    if radb.red_and_white():
        #await ctx.channel.send()
        print(radb.red_team)
        print(radb.white_team)
    else:
        await ctx.channel.send("エラーが発生しました。最初からやり直してください。")
        

@bot.command()
async def ref(ctx, arg):
    """引数のユーザの勝敗を閲覧
    """
    print(arg)
    

bot.run(token)