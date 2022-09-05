"""
Making an application from the message is not that different that a normal command
now I will show you why
"""

import os

import disnake
from disnake.ext import commands

class Apps(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

@commands.user_command(name="Avatar")  #here you put the name of the application and in that case "avatar" 
 async def avatar(inter: disnake.ApplicationCommandInteraction, user: disnake.User): #here you put the async and can be every async you want
    emb = disnake.Embed(title=f"{user}'s avatar") # working part
    emb.set_image(url=user.display_avatar.url) # working part
    await inter.response.send_message(embed=emb) # send the message, in this case an embed


@commands.message_command(name="Reverse") # another app with the name of "Reverse" 
 async def reverse(inter: disnake.ApplicationCommandInteraction, message: disnake.Message): #async
    # Let's reverse it and send back
    await inter.response.send_message(message.content[::-1]) # send the message, in this case a normal message
    
def setup(bot):
    bot.add_cog(Apps(bot))
   
 """
 So in the end the only thing that you have to change is from @commands.command/@commands.slash_command to @commands.user_command 
 (also modify the await of what you are doing)
 
 still remember @commands.message_command for cogs and @bot.message_command for put it on the main
 """
