import discord
from discord.ext import commands
import random


class React(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = ["happy", "cheery", "merry", "joy", "joyful", "jolly", "delight", "delightful", "smile", "smile", "smiley", "smiling", "blessed", "lucky", "luck"]
        em = ["🤩", "😀", "😁", "😂", "🤣", "😃", "😄", "😅", "😆", "😉", "😊"]

        msg1 = ["unhappy" "not happy", "sad", "sorrow", "sorrowful", "regret", "regretful", "deject", "dejected", "misery", "miserable", "downhearted", "down", "not happy", "funeral", "broken", "heartbroken", "tragedy", "die", "died", "dead", "death", "killed","kill"]
        em1 = ["😥", "😓", "😔", "☹️", "🙁", "😢", "😭"]

        msg2 = ["love", "loved", "lovely", "likes", "liked", "fondness", "warm", "warmth", "intimate", "intimacy", "attachment", "lust", "care", "cared", "caring", "concern", "friendship", "kind", "kindness", "sympathy", "kindliness", "affair", "love affair", "romance", "liking"]
        em2 = ["😍", "😘", "🥰", "😗", "😙", "😚"]

        msg3 = ["angry", "mad", "irritate", "disturb", "hate", "annoyed", "hot tempered", "annoying", "furious", "rage", "raging", "enraged", "outraged", "bad-tempered", "hot-tempered", "wild", "dirty"]
        em3 = ["😡", "😠", "🤬"]

        msg4 = ["plane", "aeroplane", "flight", "airport"]
        em4 = ["✈️", "🛫", "🛬", "🛩"]

        msg5 = ["music", "song", "songs", "melody", "melodic", "tuning", "tuned"]
        em5 = ["🎤", "🎧", "🎼", "🎹", "🥁", "🎷", "🎺", "🎸", "🎻"]

        for emote in msg:
            if message.channel.id == 684887204480548889 and message.content.count(emote) > 0:
                rdm = random.choice(em)
                await message.add_reaction(rdm)
        for emote in msg1:
            if message.channel.id == 684887204480548889 and message.content.count(emote) > 0:
                rdm = random.choice(em1)
                await message.add_reaction(rdm)
        
        for emote in msg2:
            if message.channel.id == 684887204480548889 and message.content.count(emote) > 0:
                rdm = random.choice(em2)
                await message.add_reaction(rdm)

        for emote in msg3:
            if message.channel.id == 684887204480548889 and message.content.count(emote) > 0:
                rdm = random.choice(em3)
                await message.add_reaction(rdm)

        for emote in msg4:
            if message.channel.id == 684887204480548889 and message.content.count(emote) > 0:
                rdm = random.choice(em4)
                await message.add_reaction(rdm)

        for emote in msg5:
            if message.channel.id == 684887204480548889 and message.content.count(emote) > 0:
                rdm = random.choice(em5)
                await message.add_reaction(rdm)

def setup(client):
    client.add_cog(React(client))
    