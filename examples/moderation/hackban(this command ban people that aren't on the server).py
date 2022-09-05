import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.ext import commands

from helpers import checks


class Hackban(commands.Cog, name="hackban-slash"): # cog name
    def __init__(self, bot):
        self.bot = bot


   @commands.slash_command(
        name="hackban",
        description="Bans a user without the user having to be in the server.",
        options=[
            Option(
                name="user_id",
                description="The ID of the user that should be banned.",
                type=OptionType.string,
                required=True
            ),
            Option(
                name="reason",
                description="The reason you banned the user.",
                type=OptionType.string,
                required=False
            )
        ]
    )
    @commands.has_permissions(ban_members=True) #check user permission
    @checks.not_blacklisted()
    async def hackban(self, interaction: ApplicationCommandInteraction, user_id: str,
                      reason: str = "Not specified") -> None:
        """
        Bans a user without the user having to be in the server.
        :param interaction: The application command interaction.
        :param user_id: The ID of the user that should be banned.
        :param reason: The reason for the ban. Default is "Not specified".
        """
        try:
            await self.bot.http.ban(user_id, interaction.guild.id, reason=reason)
            user = await self.bot.get_or_fetch_user(int(user_id))
            embed = disnake.Embed(
                title="User Banned!",
                description=f"**{user} (ID: {user_id}) ** was banned by **{interaction.author}**!",
                color=0x9C84EF
            )
            embed.add_field(
                name="Reason:",
                value=reason
            )
            await interaction.send(embed=embed)
        except Exception as e:
            embed = disnake.Embed(
                title="Error!",
                description="An error occurred while trying to ban the user. Make sure ID is an existing ID that belongs to a user.",
                color=0xE02B2B
            )
            await interaction.send(embed=embed)
            print(e)
