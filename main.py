# Modules
import logging
import os
from discord.ext import commands

#  Variables
token = 'token'
client = commands.Bot(command_prefix='.', help_command=None)


# events
# tells us if the bot is online


@client.event
async def on_ready():
    print('bot is online')


# Errors
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing required argument')


# logs errors and debug information
def discord_log():
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='discord.log', encoding='utf 8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)


# goes through all the files in cogs folder
for filename in os.listdir('./cogs'):
    # loads .py files
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

discord_log()

client.run(token)
