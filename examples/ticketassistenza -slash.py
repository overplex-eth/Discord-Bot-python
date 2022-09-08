import disnake
from disnake.ext import commands

import disnake
from disnake import ApplicationCommandInteraction

from disnake.enums import ButtonStyle

class assistenza(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.slash_command(name="assistenza", description="crea un ticket assistenza")
    async def ticket(self, interaction: ApplicationCommandInteraction):
        embed=disnake.Embed(title="Ticket", color=0x00ccff, description="Crea un Ticket Assistenza")
        embed.add_field(name="Clicca qui per creare un ticket!\nRicordo le seguenti regole:\n 1) Non spammare i ticket, timeout 3 giorni;\n2) Non aprire ticket a caso, warn;\n3) Non fare ticket troll,  warn + timeout 1 giorno.", value=f"{interaction.guild}", inline=False)

        await interaction.send(embed=embed, components=disnake.ui.Button(style=ButtonStyle.blurple, label='Apri un ticket assistenza', custom_id='ticket_button', emoji="🎫")
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
            guild.get_role(865872103081508896): disnake.PermissionOverwrite(view_channel=True),
            inter.author: disnake.PermissionOverwrite(view_channel=True),
        }  
       
            if inter.component.custom_id == "ticket_button":
                embed=disnake.Embed(color=0x00ccff)
                embed.add_field(name="Ticket", value="Ciao Benvenuto al ticket! Aspetta che uno staffer ti risponda e sii rispettoso, grazie! \nNel mentre ti preghiamo di scrivere qual'è il tuo probelma.", inline=False)
                category = disnake.utils.get(guild.categories, name="──  💼ￜ Staff・・・")
                ticket = await guild.create_text_channel(f"ticket-{author}", topic=f"{inter.author.id}", category=category, overwrites=overwrites)
                msg =  await inter.send(f"Ho creato il <#{ticket.id}>", ephemeral=True)
                await ticket.send(f"Hey {inter.author.mention}! Aspetta uno <@&865872103081508896>", embed=embed, 
                 components= [
                 disnake.ui.Button(style=ButtonStyle.blurple, label='Chiudi il ticket', custom_id='chiudi', emoji="❌"),             
                 disnake.ui.Button(style=ButtonStyle.green, label="Claim", custom_id="claim", emoji="🙋‍♂️")
                 ]
                                 )
            
            
            elif inter.component.custom_id == "chiudi":
                channel = inter.channel
                if channel.name.startswith("ticket-"):
                    autor1 = inter.author
                chiudi = await channel.delete(reason="Ticket chiuso")
                await autor1.send("Ticket Chiuso, se vuoi riaprirlo creane un altro!")

                return
            
            elif inter.component.custom_id == "claim":
                channel = inter.channel
                if channel.name.startswith("ticket-"):
                    autorl = inter.author
                claim = await inter.send(f"Your ticket will be handled by <@{inter.author.id}>")
                
                return
            
            elif inter.component.custom_id == "close":
                channel = inter.channel
                if channel.name.startswith("ticket-"):
                    autorl = inter.author
                btn_response = await self.bot.wait_for(
                "on_button_click", check=lambda i: i.author == interaction.author
                )
                close = await btn_response.response.send_modal(modal=MyModal())
                
                return
                                    
def setup(bot):
    bot.add_cog(assistenza(bot))

