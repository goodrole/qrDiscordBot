import discord
import time
from discord.ext import commands


class Basic(commands.Cog):
    # passing into the cog
    def __init__(self, client):
        # access the client within the cog
        self.client = client

    # kick command
    @commands.command()
    async def kick(self, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    # ban command
    @commands.command()
    async def ban(self, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)

    # clear messages
    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount + 1)
        # prints out how many messages have been deleted
        await ctx.send(f'{amount} messages have been cleared!')
        time.sleep(5)
        await ctx.channel.purge(limit=1)


def setup(client):
    # passing the client
    client.add_cog(Basic(client))
