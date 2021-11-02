import discord
from discord.client import _ClientEventTask

Welcome_channel_id = Your channel ID
class Myclient(discord.Client):
    async def on_ready (self):
        print("TReady...")
        welcome_channel = _ClientEventTask.get_channel(Welcome_channel_id)
        await welcome_channel.send("Your Text")



        async def on_reaction_add (self, reaction, user):
            Your Role Name = discord.utils.get(user.guild.roles, name="Your Role Name")
            Your Role Name = discord.utils.get(user.guild.roles, name="Your Role Name")
            if str(reaction.emoji) == "Your Emoji":
                user.add_roles(Your Role Name)
            
            if str(reaction.emoji) == "Your Emoji":
                user.add_roles(Your Role Name)

            


        client = Myclient()
        client.run("Your Token")
