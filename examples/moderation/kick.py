import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.ext import commands

from helpers import checks


class Kick(commands.Cog, name="kick-slash"): # class name
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command( # name for the slash comman (kick)
        name="kick",
        description="Kick a user out of the server.",
        options=[ # options for the command
            Option( 
                name="user",
                description="The user you want to kick.",
                type=OptionType.user,
                required=True
            ),
            Option(
                name="reason",
                description="The reason you kicked the user.",
                type=OptionType.string,
                required=False
            )
        ]
    )
    @commands.has_permissions(kick_members=True) # this is necessary because the bot checks if you have the permission for kick members (don't put False, trust me)
    @checks.not_blacklisted() #check if the member tha is using the command is not blöacklisted
    async def kick(self, interaction: ApplicationCommandInteraction, user: disnake.User,
                   reason: str = "Not specified") -> None:
        """
        Kick a user out of the server.
        :param interaction: The application command interaction.
        :param user: The user that should be kicked from the server.
        :param reason: The reason for the kick. Default is "Not specified".
        """
        member = await interaction.guild.get_or_fetch_member(user.id)
        if member.guild_permissions.administrator: # if the member you are trying to kick the member is administrator you can't kick him
            embed = disnake.Embed(
                title="Error!",
                description="User has Admin permissions.",
                color=0xE02B2B
            )
            await interaction.send(embed=embed)
        else:
            try:
                embed = disnake.Embed(
                    title="User Kicked!",
                    description=f"**{member}** was kicked by **{interaction.author}**!",
                    color=0x9C84EF
                )
                embed.add_field(
                    name="Reason:",
                    value=reason
                )
                await interaction.send(embed=embed)
                try:
                    await member.send(
                        f"You were kicked by **{interaction.author}**!\nReason: {reason}"
                    )
                except disnake.Forbidden:
                    # Couldn't send a message in the private messages of the user
                    pass
                await member.kick(reason=reason)
            except:
                embed = disnake.Embed(
                    title="Error!",
                    description="An error occurred while trying to kick the user. Make sure my role is above the role of the user you want to kick.",
                    color=0xE02B2B
                )
                await interaction.send(embed=embed)
                
  def setup(bot):
    bot.add_cog(Kick(bot))

