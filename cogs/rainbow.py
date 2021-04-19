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

class Rainbow(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            home = self.client.get_guild(id = 684887204480548886)
            Role= home.get_role(691934280170864680)
            while True:
                Color = [0x8A2BE2, 0x4B0082, 0x40E0D0, 0x00FA9A, 0xFFFF00, 0xFFA500, 0xFF0000]
                ran = random.choice(Color)
                Colors = discord.Color(ran)
                await Role.edit(colour = Colors)
                await asyncio.sleep(2)

        except Exception as error:
            print(error)


def setup(client):
    client.add_cog(Rainbow(client))