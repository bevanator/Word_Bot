import discord
import os
import requests
import json
import urbandictionary as ud  
                                          # urbandictionary repo link: https://github.com/bocong/urbandictionary-py
from udpy import UrbanClient
from discord.ext import commands
from keep_alive import keep_alive         # importing keep_alive thread

client = commands.Bot(command_prefix='.') # bot client, all commands start with '.'
uClient = UrbanClient()                   # UD api wrapper client, https://pypi.org/project/udpy/
token = os.environ['TOKEN']               # do not touch, replit env variable access system.

@client.event                             # decorator for events
async def on_ready():                     # refer to discord api. on_ready used for confirmation of bot coming online
    print('We have logged in as {0.user}'.format(client))
                                          # print on console

'''
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
'''


@client.command()                         # decorator for commands
async def randomword(random):             # function name will be used as commands along with bot prefix
    rand = ud.random()
    for w in rand[:3]:
        await random.send(w.word)
        await random.send(w.definition)
        await random.send('\n****************************************\n')

@client.command()
async def define(ctx, *, word):           # define words and phrases
    defs = uClient.get_definition(word)
    for d in defs[:2]:
        await ctx.send(d.definition)

keep_alive()                              # thread to keep running
client.run(token)
