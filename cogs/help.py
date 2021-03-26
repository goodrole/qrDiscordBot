import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def help(self, ctx):
        # list of commands that bot has
        command_list = '''
        Woc command start with .

        Help:  this window
        Ban:   ban someone from the server
        Kick:  kicks someone from the server
        clear: clear messages
               ex. .clear 5
        qr: makes a qr code from website or message'''

        embed = discord.Embed(
            colour=discord.Colour.blue()
        )
        embed.set_author(name=f'Server: {ctx.message.guild.name}')
        embed.add_field(name='Commands', value=f'{command_list}', inline=True)

        await ctx.send(embed=embed)


def setup(client):
    # passing the client
    client.add_cog(Help(client))
