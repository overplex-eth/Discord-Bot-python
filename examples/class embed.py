import platform
import random

import aiohttp
import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.ext import commands

from helpers import checks

class General(commands.Cog, name="name-slash"): #name the cog
    def __init__(self, bot):
        self.bot = bot
    
  @commands.slash_command(name="<slash command name>", description="<slash command description>") #change the name + description
    async def test_command(self, interaction: disnake.ApplicationCommandInteraction):
      
  @checks.not_blacklisted() #check if the user is banned (config.json)
    async def botinfo(self, interaction: ApplicationCommandInteraction) -> None:
        """
        Get help.
        :param interaction: The application command interaction.
        """
        embed = disnake.Embed(
            description="<embed name>", # change the embed name
            color=0x9C84EF
        )
        embed.set_author(
            name= "<embed author>" # big name 
        )
        embed.add_field(
            name="<name of the field>", # first field name (bigger than value)
            value=f"<value of the field>", # smaller than the name
            inline=True # for inline the filed (for remove it change the True with False)
        )
        embed.add_field(
            name="<name of the field>", # first field name (bigger than value)
            value=f"<value of the field>", # smaller than the name
            inline=True # for inline the filed (for remove it change the True with False)
        )
        
        # for add more field just alline they with this
        
        await interaction.send(embed=embed) # send the embed

def setup(bot):
    bot.add_cog(General(bot))
