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

replit.clear()                            # clear screen


client = commands.Bot(command_prefix='.') # bot client, all commands start with '.'
uClient = UrbanClient()                   # UD api wrapper client, https://pypi.org/project/udpy/
token = os.environ['TOKEN']               # do not touch, replit env variable access system.

switch = 1                                # global variable to control word of the day
delay = 5                                 # frequency in seconds at which words are posted


async def send_interval_message_all():    # sends to all servers' first text channel it's able to
  while switch == 1:
      await asyncio.sleep(delay)
      for guild in client.guilds:
        for channel in guild.text_channels:
          try:
            # print(channel.id)
            rand = ud.random()
            for w in rand[:1]:
              await channel.send(w.word)
              await channel.send(w.definition)
          except Exception:
            continue
          else:
            break


async def send_interval_message_specific():# sends to a specific channel
  while switch == 1:
      await asyncio.sleep(delay)
      rand = ud.random()
      for w in rand[:1]:
        channel = client.get_channel(id = 840663367781842965)
        await channel.send(w.word)
        await channel.send(w.definition)


      




@client.event                             # decorator for events
async def on_ready():                     # refer to discord api. on_ready used for confirmation of bot coming online
    print('logged in as {0.user}'.format(client))
    client.loop.create_task(send_interval_message_specific())
                                          # choose method of sending random words
                                          # _specific for a specific channel with given id
                                          # _all for all available servers' first text channel it's able to


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
