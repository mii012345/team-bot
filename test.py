import discord
import setting

TOKEN = setting.get_token()

client = discord.Client()

@client.event
async def on_ready():
    print('logged')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "/neko":
        await message.channel.send('nyaa')

async def reply(message):
    reply = f'{message.author.mention} ?'
    await message.channel.send(reply)

@client.event
async def on_message(message):
    if client.user in message.mentions:
        await reply(message)

def get_data(message):
    command = message.content
    data_table = {
        '/members': message.guild.members,
        '/roles': message.guild.roles,
        '/text_channels': message.guild.text_channels,
        '/voice_channels': message.guild.voice_channels,
        '/category_channels': message.guild.categories,
    }
    return data_table.get(command, 'error:invalid command')

@client.event
async def on_message(message):
    print(get_data(message))

async def get_members(message):
    status = message.author.voice
    print(status.channel)
    member = [i.name for i in status.channel.members]
    for i in member:
        await message.channel.send(i)

@client.event
async def on_message(message):
    if message.content == '/members':
        await get_members(message)

@
    
client.run(TOKEN)