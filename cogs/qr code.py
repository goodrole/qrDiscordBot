# QR Code generator
# imported modules
import discord
import os
import qrcode
import time
from discord.ext import commands


class QR(commands.Cog):

    def __init__(self, client):
        self.client = client

    # tells us if the qr generator is working
    @commands.Cog.listener()
    async def on_ready(self):
        print('QR generator working')

    @commands.command()
    async def qr(self, ctx, arg, color='black'):
        # what colors the qr code can be
        color_list = ['black', 'red', 'yellow', 'orange', 'purple', 'green', 'blue']
        qr = qrcode.QRCode(
            version=3,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=15,
            border=5,
        )
        # color chosen must be in the list
        if color in color_list:
            qr.add_data(arg)
            qr.make(fit=True)
            img = qr.make_image(fill_color=color, back_color='white')
            img.save('qrcode.png')

            await ctx.send('Processing...')
            time.sleep(2)
            # sends the image onto discord
            await ctx.send(file=discord.File('qrcode.png'))
            # deletes the image from the directory
            os.remove('qrcode.png')
        else:
            await ctx.send(f'You can only choose these colors: {color_list}')


def setup(client):
    client.add_cog(QR(client))
