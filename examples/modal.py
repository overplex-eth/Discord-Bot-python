import disnake
from disnake.ext import commands

class General(commands.Cog, name="name-slash"): #name the cog
    def __init__(self, bot):
        self.bot = bot
    
 @commands.slash_command(name="<slash command name>", description="<slash command description>") #change the name + description
    async def test_command(self, interaction: disnake.ApplicationCommandInteraction):

class MyModal(disnake.ui.Modal):
    def __init__(self) -> None:
        components = [
            disnake.ui.TextInput( # imput thext for the modal
                label="<name>",
                placeholder="<under the text (uneditable text)>",
                custom_id="<id for the component>",
                style=disnake.TextInputStyle.short,
                max_length=50, # max lenght is for see how much text they can write max (you can use min_lenght for put a minimum necessary text)
            ),
            disnake.ui.TextInput(
                label="<name>",
                placeholder="<under the text (uneditable text)>",
                custom_id="descrizione",
                style=disnake.TextInputStyle.short,
                min_length=5,
                max_length=50,
            ),
        ]
        super().__init__(
            title="<title for the footer>", custom_id="<id>", components=components # to send the components you need to say it with components=components
        )

    async def callback(self, inter: disnake.ModalInteraction) -> None:
        embed = disnake.Embed(title="<name of the callback embed>") # name the callback
        for key, value in inter.text_values.items():
            embed.add_field(name=key.capitalize(), value=value, inline=False) # put here ephemeral=True for put "only see from you" (like line 37)
        await inter.response.send_message(embed=embed)

    async def on_error(self, error: Exception, inter: disnake.ModalInteraction) -> None:
        await inter.response.send_message("Oops, something went wrong.", ephemeral=True)

def setup(bot):
    bot.add_cog(General(bot))
