import discord
import urbandictionary as ud
from udpy import UrbanClient
from discord.ext import commands

client = commands.Bot(command_prefix='.')
uClient = UrbanClient()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

'''
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
'''


@client.command()
async def randomword(random):
    rand = ud.random()
    for w in rand[:3]:
        await random.send(w.word)
        await random.send(w.definition)
        await random.send('\n****************************************\n')

@client.command()
async def define(ctx, word):
    defs = uClient.get_definition(word)
    for d in defs:
        await ctx.send(d.definition)


client.run('ODQwNjQ2NjQzMjMzOTgwNDQ4.YJbPMg.Nl-4_F66_BeP03vWml_e6YetVjo')
