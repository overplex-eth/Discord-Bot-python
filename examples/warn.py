import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.ext import commands

from helpers import checks


class Warn(commands.Cog, name="warn-slash"):
    def __init__(self, bot):
        self.bot = bot
        
  @commands.slash_command( # name of the slash
        name="warn",
        description="Warns a user in the server.",
        options=[ #otpions for the command
            Option(
                name="user",
                description="The user you want to warn.",
                type=OptionType.user,
                required=True
            ),
            Option(
                name="reason",
                description="The reason you warned the user.",
                type=OptionType.string,
                required=False
            )
        ],
    )
    @commands.has_permissions(manage_messages=True) # required permission for run this command
    @checks.not_blacklisted() # check if the user that's running thios bot is not blacklisted
    async def warn(self, interaction: ApplicationCommandInteraction, user: disnake.User,
                   reason: str = "Not specified") -> None:
        """
        Warns a user in his private messages.
        :param interaction: The application command interaction.
        :param user: The user that should be warned.
        :param reason: The reason for the warn. Default is "Not specified".
        """
        member = await interaction.guild.get_or_fetch_member(user.id)
        embed = disnake.Embed(
            title="User Warned!",
            description=f"**{member}** was warned by **{interaction.author}**!",
            color=0x9C84EF
        )
        embed.add_field(
            name="Reason:",
            value=reason
        )
        await interaction.send(embed=embed)
        try:
            await member.send(f"You were warned by **{interaction.author}**!\nReason: {reason}")
        except disnake.Forbidden:
            # Couldn't send a message in the private messages of the user
            await interaction.send(f"{member.mention}, you were warned by **{interaction.author}**!\nReason: {reason}")
            
def setup(bot):
    bot.add_cog(Warn(bot))
