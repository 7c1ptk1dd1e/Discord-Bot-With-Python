from typing import Text
import discord
from discord import embeds
from discord import channel
from discord.colour import Color
from discord.ext import commands

TOKEN = 'Your Token'

#This is your Bots Prefix 
bot = commands.Bot(command_prefix='.')

#This is the name Of the Command 
@bot.command()
async def YourCommandName(ctx):
  print('Ready...')

  channel = bot.get_channel(The channel ID)



  embed = discord.Embed(title="Photo", url="Your URL", description="Your description\n\n[Click Me](Your URL)", Color=0xf976)
  embed.set_thumbnail(url="Your URL")
  embed.set_footer(text="Your Text")
  await channel.send(content=None, embed=embed)


  @bot.command()
  async def Ole (ctx):
    print('Ready...')
    embed = discord.Embed(title="Your Text",url="Your URL", description="Your Text \n\n[Click Me](Your URL)", Color=0xf976)
    embed.set_thumbnail(url="Your URL")
    embed.set_footer(text="Your Text")
    await channel.send(content=None, embed=embed)






bot.run(TOKEN, bot=True)



