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

class trigger(commands.Cog):
    def __init__(self, commands):
        self.commands = commands

    

    #echo command >> echo the message
    @commands.command()
    async def echo(self, ctx, *,args):
        output = ''
        for words in args:
            output += words
            output += ''
        await ctx.send(output)

        #_8ball command >> used for fortune telling or seeking advice
    @commands.command(aliases = ['8ball'])
    async def _8ball(self, ctx, *,ques):
        response = ['Signs point to yes.', 
                    'Yes.', 
                    'Reply hazy, try again.', 
                    'My sources say no.', 
                    'You may rely on it.', 
                    'Concentrate and ask again.', 
                    'Outlook not so good.', 
                    'It is decidedly so.', 
                    'Better not tell you now.', 
                    'Very doubtful.', 
                    'Yes - definitely.', 
                    'It is certain.', 
                    'Cannot predict now.', 
                    'Most likely.', 
                    'Ask again later.', 
                    'My reply is no.', 
                    'Outlook good.', 
                    "Don't count on it."]
        await ctx.send(f'Question : {ques} \nAnswer : {random.choice(response)}')


    #command to clear messages
    @commands.command()
    async def clear(self, ctx, amount = 5):
        valid_users = ["Ichan#5787"]
        if str(ctx.author) in valid_users:
            await ctx.channel.purge(limit = amount)

    #user info command
    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member

        roles = [role for role in member.roles] #for loop
        

        embed = discord.Embed(colour = member.colour, timestamp = ctx.message.created_at)
        
        embed.set_author(name = f"User info = {member}")
        embed.set_thumbnail(url = member.avatar_url)
        embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        embed.add_field(name = "ID:", value = member.id)
        embed.add_field(name = "Guild name:", value = member.display_name)
        embed.add_field(name = "Created at:",value = member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name = "Joined at:",value = member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name = f"Roles ({len(roles)})", value = " ".join([role.mention for role in roles]))
        embed.add_field(name = "Top roles:", value = member.top_role.mention)
        embed.add_field(name = "Bot?", value = member.bot)
        await ctx.send(embed = embed)

    #command to kick
    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason = None): #we are passing discord.Member object to member variable
        await member.kick(reason = reason)
        await ctx.send(f'{member.mention} has been kicked from Server.')
        print(f'{member} has been kicked from server')


    #ban
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason = None): 
        await member.ban(reason = reason)

    #unban
    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return
        
    
    @commands.command()
    async def mute(self, ctx, member : discord.Member):
        guild = ctx.guild
        for role in guild.roles:
            if role.name == 'muted':
                await member.add_roles(role)
                await ctx.send(f'{ctx.author.mention} has mute {member.mention}.')
                #await ctx.send('{} has {} has been muted.' .format(member.mention,ctx.author.mention))
                return

                over_write = discord.PermissionOverwrite(send_message = False)
                new_role = await guild.create_role(name = 'muted')
                for channel in guild.text_channels:
                    await ctx.send(f'{ctx.author.mention} has mute {member.mention}.')


                await member.add_roles(new_role)
                await ctx.send(f'{ctx.author.mention} has mute {member.mention}.')
                #await ctx.send('{} has {} has been muted.' .format(member.mention,ctx.author.mention))

    @commands.command()
    async def unmute(self, ctx, member : discord.Member):
        guild = ctx.guild
        for role in guild.roles:
            if role.name == 'muted':
                await member.remove_roles(role)
                await ctx.send(f'{ctx.author.mention} has unmute {member.mention}.')
                #await ctx.send('{} has {} has been unmuted.' .format(member.mention,ctx.author.mention))
                return
    
def setup(client):
    client.add_cog(trigger(client))