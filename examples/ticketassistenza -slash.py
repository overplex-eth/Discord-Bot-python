import disnake
from disnake.ext import commands

import disnake
from disnake import ApplicationCommandInteraction

from disnake.enums import ButtonStyle

class assistenza(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.slash_command(name="<command-slash-name>", description="<command-slash-description>") # put a name and a description for this ticket system
    async def ticket(self, interaction: ApplicationCommandInteraction):
        embed=disnake.Embed(title="Ticket", color=0x00ccff, description="Open a Ticket")
        embed.add_field(name="Open a support ticket!.", value=f"{interaction.guild}", inline=False) # put a name for this ticket

        await interaction.send(embed=embed, components=disnake.ui.Button(style=ButtonStyle.blurple, label='Open a Ticket', custom_id='ticket_button', emoji="🎫") # the button for open a ticket
            )


    @commands.Cog.listener("on_button_click")
    async def bottonilistener(self, inter: disnake.MessageInteraction):
            guild = inter.guild
            print(guild)
            author = inter.author.name
            print(author)
            print(guild.default_role)
            overwrites = {
            guild.default_role: disnake.PermissionOverwrite(view_channel=False),
            guild.get_role("staffroleid"): disnake.PermissionOverwrite(view_channel=True), # put the id of the staff role
            inter.author: disnake.PermissionOverwrite(view_channel=True),
        }  
       
            if inter.component.custom_id == "ticket_button":
                embed=disnake.Embed(color=0x00ccff)
                embed.add_field(name="Ticket", value"hello! and welcome to the ticket!", inline=False)
                category = disnake.utils.get(guild.categories, name="") # put here the name of your category for the ticket
                ticket = await guild.create_text_channel(f"ticket-{author}", topic=f"{inter.author.id}", category=category, overwrites=overwrites)
                msg =  await inter.send(f"Ho creato il <#{ticket.id}>", ephemeral=True)
                await ticket.send(f"Hey {inter.author.mention}! wait for a staffer <@id>", embed=embed, # put the id of the staff role so they will get notified
                 components= [
                 disnake.ui.Button(style=ButtonStyle.blurple, label='Close the ticket', custom_id='chiudi', emoji="❌"),             # close button
                 disnake.ui.Button(style=ButtonStyle.green, label="Claim", custom_id="claim", emoji="🙋‍♂️") # claim button
                 ]
                                 )
            
            
            elif inter.component.custom_id == "chiudi": # button id
                channel = inter.channel
                if channel.name.startswith("ticket-"):
                    autor1 = inter.author
                chiudi = await channel.delete(reason="Ticket closed")
                await autor1.send("Ticket Closed! Open a new one for more support") # Send a DM to the author

                return
            
            elif inter.component.custom_id == "claim": # button id for the claim
                channel = inter.channel
                if channel.name.startswith("ticket-"):
                    autorl = inter.author
                claim = await inter.send(f"Your ticket will be handled by <@{inter.author.id}>") # the reply for the moderator
                
                return
                                    
def setup(bot):
    bot.add_cog(Ticket (bot))

