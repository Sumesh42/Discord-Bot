import discord
from discord.ext import commands


class chelp(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(colour = 0xFFA500, title = 'Help!', description = 'shows information about the command') 
        embed.set_author(name = 'Author', icon_url = 'https://i.redd.it/ssp4cr2qeha11.jpg')
        embed.set_thumbnail(url = 'https://i.redd.it/ssp4cr2qeha11.jpg')
        embed.add_field(name = '🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸', value = '🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸')
        
        embed.add_field(name = '1. help', value = 'display this message.', inline = False)
        embed.add_field(name = '2. ping', value = 'reply with pong and shows latency.', inline = False)
        embed.add_field(name = '3. echo', value = 'display the same message. ( usage- *echo HI )', inline = False)
        embed.add_field(name = '4. _8ball or 8ball', value = 'use for seeking random advice that can be either YES or NO or UNCERTAIN. ( usage- *8ball will it rain today? ) ', inline = False)
        embed.add_field(name = '5. ban', value = 'use to ban a member.', inline = False)
        embed.add_field(name = '6. unban', value = 'use to unban a member.', inline = False)
        embed.add_field(name = '7. clear', value = 'use to clear message history from a channel.', inline = False)
        embed.add_field(name = '8. kick', value = 'use to kick a member from the server.', inline = False)
        embed.add_field(name = '9. mute', value = 'use to mute a member in the server.', inline = False)
        embed.add_field(name = '10. unmute', value = 'use to unmute a member in the server.', inline = False)
        embed.add_field(name = '11. join', value = 'use to join voice channel. (NOTE- without join you cannot use "play" command for playing music.)', inline = False)
        embed.add_field(name = '12. leave', value = 'use to leave voice channel', inline = False)
        embed.add_field(name = '13. play', value = 'use to play youtbe music in the voice channel. ( usage- *play <video link from youtube> )', inline = False)
        embed.add_field(name = '14. userinfo', value = 'use to display member infomation in the server.', inline = False)
        embed.add_field(name = '15. cprefix', value = 'use to change server prefix. (usage- *cprefix <new_prefix> NOTE- this is meant to be used only by the Admin.)', inline = False)

        embed.set_footer(text = 'this is a footer')

        await ctx.send(embed = embed)

    



def setup(client):
    client.add_cog(chelp(client))
