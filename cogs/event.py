import discord
import json
import random
import time
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot, Greedy
from discord import User
import youtube_dl
import os
from discord.utils import get
import datetime


msg = joined = 0

class Event(commands.Cog):
    def __init__(self, client):
        self.client = client

    #getting bot ready
    @commands.Cog.listener()
    async def on_ready(self):
        print(" '---------NdroiD is Online----------' ")

    #ping command
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong! {round(self.client.latency * 1000)} ms')

    #custom guild prefix command
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('custpf.json', 'r') as f:
            custpf = json.load(f)

        custpf[str(guild.id)] = '*'


        with open('custpf.json', 'w') as f:
            json.dump(custpf, f, indent = 4)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open('custpf.json', 'r') as f:
            custpf = json.load(f)

        custpf.pop(str(guild.id))


        with open('custpf.json', 'w') as f:
            json.dump(custpf, f, indent = 4)

    @commands.command()
    async def cprefix(self, ctx, *, pre):
        with open('custpf.json') as f:
            custpf = json.load(f)

        custpf[str(ctx.guild.id)] = pre
        await ctx.send(f"New Prefix is '{pre}'")
    
        with open('custpf.json', 'w') as f:
            json.dump(custpf, f, indent = 4)

    #joining a server
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.create_dm()
        embed = discord.Embed(colour = 0x95efcc, description = f'Welcome to my discord server! You are the {len(list(member.guild.members))} member to join.')
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text = f'{member.guild}', icon_url = f'{member.guild.icon_url}')
        embed.set_author(name = f'{member.name}', icon_url = f'{member.avatar_url}')
        embed.set_thumbnail(url = f'{member.avatar_url}')
        print(f'{member} has join the server.❤️')
        await member.dm_channel.send(embed = embed)

    #auto add roles
        rol = get(member.guild.roles, name = 'basic')
        await member.add_roles(rol)
        
    #leaving server
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        embed = discord.Embed(colour = 0x95efcc, description = f'{member.mention} has left the server.')
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text = f'{member.guild}', icon_url = f'{member.guild.icon_url}')
        embed.set_author(name = f'{member.name}', icon_url = f'{member.avatar_url}')
        embed.set_thumbnail(url = f'{member.avatar_url}')
        #await member.dm_channel.send(str(f"{mention}, welcome to my server {guild}").format()
        channel = self.client.get_channel(id = 684887204480548889)
        await channel.send(embed = embed)
        print(f'{member} has left the server.☹️ ')

    #deleting bad words
    @commands.Cog.listener()
    async def on_message(self, message):
        bad_words = ["kutte", "kaminey"]
        for word in bad_words:
            if message.content.count(word) > 0:
                print('%s has used bad word(s)' % (message.author.id))
                #print("A bad word was said")
                await message.channel.purge(limit=1)
                await self.client.process_commands(message)
                

    #changing user nickname 
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        n = after.nick
        if n:
            last = before.nick
            if n.lower().count(before.nick) > 0:
                if last == before.nick:
                    await after.edit(nick = "Same_As_Before")
                    


def setup(client):
    client.add_cog(Event(client))