import disnake
from disnake.ext import commands


##first thing you need to create is the button because is NOT inside of the class (modal or embed)

def create_button_view():
    view = disnake.ui.View()
    view.add_item(disnake.ui.Button(label="<button_name>", style=disnake.ButtonStyle.blurple))
    return view

  '''
  for this button the only thing you need to change is "<button_name>" and put inside the name you want to use
  
  you can also see the style, style=disnake.ButtonStlye.blurple you can change it with:
  - disnake.ButtonStyle.gray (for this you can just remove "style=disnake.ButtonStyle.blurple because is default color)
  - disnake.ButtonStyle.green (green color)
  - disnake.ButtonStyle.red (red color)
  '''

class ClassName(commands.Cog): #put a name for your class
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener() #the listener is for see what cogs are loaded when you run the bot
    async def on_ready(self):
        print(f"{self.qualified_name} loaded")

    @commands.slash_command(name="<slash_command_name>", description="<slash_command_description>", guild_ids=["<server_IDY>") # guild_ids is just for select what server this command is in
    async def test_command(self, interaction: disnake.ApplicationCommandInteraction):

        embed = disnake.Embed(title="<embed_name>", description="<embed_description>")

        view = create_button_view() # collegate the button with the embed and modal
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True) # as you can see here is for send the message and inside of () you will see what is sending: the embed, the view(button) and ephemeral, ephemeral is for put the message just for you put "False" if you don't want it

        btn_response = await self.bot.wait_for(
            "button_click", check=lambda i: i.author == interaction.author
        )

        await btn_response.response.send_modal(modal=MyModal()) #send the modal


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
        embed = disnake.Embed(title="Profilo")
        for key, value in inter.text_values.items():
            embed.add_field(name=key.capitalize(), value=value, inline=False)
        await inter.response.send_message(embed=embed)

    async def on_error(self, error: Exception, inter: disnake.ModalInteraction) -> None:
        await inter.response.send_message("Oops, something went wrong.", ephemeral=True)

def setup(bot):
    bot.add_cog(ClassName(bot))
