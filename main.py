import discord
import os
import requests
import json
import asyncio
import replit
import urbandictionary as ud
                                          # urbandictionary repo link: https://github.com/bocong/urbandictionary-py
from udpy import UrbanClient
from discord.ext import commands
from keep_alive import keep_alive         # importing keep_alive thread from the script

client = commands.Bot(command_prefix='.') # bot client, all commands start with '.'
uClient = UrbanClient()                   # UD api wrapper client, https://pypi.org/project/udpy/
token = os.environ['TOKEN']               # do not touch, replit env variable access system.
hourlyBool = 1
replit.clear()
delay = 3600


'''
async def send_interval_message():
    await client.wait_until_ready()
    interval = delay
    channel = discord.Object(id=840663367781842965)
    while not client.is_closed:
        rand = ud.random()
        for w in rand[:1]:
          message = w.definiton
        await client.send_message(channel, message)
        print(message)
        await asyncio.sleep(interval)
'''




async def send_interval_message():
  while hourlyBool == 1:
      await asyncio.sleep(3600)
      rand = ud.random()
      for w in rand[:1]:
        channel = client.get_channel(id = 840663367781842965)
        await channel.send(w.word)
        await channel.send(w.definition)
        #print(w.word)
        
      




@client.event                             # decorator for events
async def on_ready():                     # refer to discord api. on_ready used for confirmation of bot coming online
    print('logged in as {0.user}'.format(client))
    client.loop.create_task(send_interval_message())

                                          # print on console
    text_channel_list = []
    for guild in client.guilds:
        for channel in guild.text_channels:
            text_channel_list.append(channel)

    #print(client.guilds)

'''
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
'''
''''
@client.event 
async def hourly(guild):
    while hourlyBool == 1:
      await guild.text_channels[0].send("I have joined the server")
      await asyncio.sleep(3)

'''   


@client.command()
async def info(ctx):
    await ctx.send("ID: {}".format(ctx.guild.id))
    

@client.command()                         # decorator for commands
async def randomword(random):             # function name will be used as commands along with bot prefix
    rand = ud.random()
    for w in rand[:3]:
        await random.send(w.word)
        await random.send(w.definition)
        await random.send('-------------------------------------------------------------------------------------------------------------------------------------------------------------------')

@client.command()
async def define(ctx, *, word):           # define words and phrases
    defs = uClient.get_definition(word)
    for d in defs[:2]:
        await ctx.send(d.definition)

keep_alive()                             # thread to keep running
client.run(token)
