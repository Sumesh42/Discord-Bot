import discord
import random
import time
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot, Greedy
from discord import User
import youtube_dl
import os
import json
from discord.utils import get


#client = commands.Bot(command_prefix = "*")
def get_prefix(client, message):
    with open('custpf.json', 'r') as f:
        custpf = json.load(f)

    return custpf[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix)
client.remove_command('help')

#background task event/command
#background task
@client.event
async def chngPR():
    await client.wait_until_ready()

    statuses = ["*help", "Being a good bot", "Having fun"]
    while not client.is_closed():
        status = random.choice(statuses)

        await client.change_presence(activity = discord.Game(status))
        await asyncio.sleep(7)

client.loop.create_task(chngPR())


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')



@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('')