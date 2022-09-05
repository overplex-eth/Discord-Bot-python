import platform
import random

import aiohttp
import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.ext import commands

from helpers import checks


class General(commands.Cog, name="help-slash"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="help",
        description="Full list of commands.",
    )
    @checks.not_blacklisted()
    async def botinfo(self, interaction: ApplicationCommandInteraction) -> None:
        """
        Get help.
        :param interaction: The application command interaction.
        """
        embed = disnake.Embed(
            description="Commands list",
            color=0x9C84EF
        )
        embed.set_author(
            name= "Help"
        )
        embed.add_field(
            name="**/help**",
            value=f"Vedi questo",
            inline=True
        )
        embed.add_field(
            name="**/8Ball**",
            value="Fai una domanda al bot",
            inline=True
        )
        embed.add_field(
            name="**/admins**",
            value=f"Scopri gli admin del server",
            inline=True
        )
        embed.add_field(
            name="**/bitcoin**",
            value=f"Scopri il prezzo di Bitcoin in tempo reale",
            inline=True
	)
        embed.add_field(
            name="**/candidatura**",
            value=f"Scopri come candidarti sul server Discord di Sirius",
            inline=True
	)
        embed.add_field(
            name="**/coinflip**",
            value=f"lancia una moneta",
            inline=True
	)
        embed.add_field(
            name="**/ethereum**",
            value=f"Scopri il prezzo di ethereum in tempo reale",
            inline=True
	)
        embed.add_field(
            name="**/founders**",
            value=f"Scopri i founders  del server",
            inline=True
        )
        embed.add_field(
            name="**/heads**",
            value=f"Scopri gli heads del server",
            inline=True
        )
        embed.add_field(
            name="**/invite**",
            value=f"invitami nel tuo server",
            inline=True
        )
        embed.add_field(
            name="**/nick**",
            value=f"cambia il tuo nickname",
            inline=True
        )
        embed.add_field(
            name="**/minecraftinfo**",
            value=f"info sul minecraft server",
            inline=True
        )
        embed.add_field(
            name="**/mods**",
            value=f"ti mostra i mods",
            inline=True
        )
        embed.add_field(
            name="**/owner**",
            value=f"ti mostra l'owner",
            inline=True
        )
        embed.add_field(
            name="**/randomfact**",
            value=f"ti dice un fatto random",
            inline=True
        )
        embed.add_field(
            name="**/rps**",
            value=f"gioca sasso, carta, forbice",
            inline=True
        )
        embed.add_field(
            name="**/supporto**",
            value=f"Ti da informazioni per eventuali problemi con il bot",
            inline=True
        )
        embed.add_field(
             name="**/cofounders**",
             value=f"Ti dice chi sono i cofounders",
             inline=True
        )
        embed.add_field(
            name="**/play**",
            value=f"Play a song with the bot",
            inline=True
	    )
        embed.add_field(
            name="**/userinfo**",
            value=f"Le tue informazioni?!",
            inline=True
        )
        embed.set_footer(
            text=f"Requested by {interaction.author}"
        )
        await interaction.send(embed=embed)
def setup(bot):
    bot.add_cog(General(bot))