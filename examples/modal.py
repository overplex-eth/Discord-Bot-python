

 @commands.slash_command(name="profilo", description="crea il tuo profilo", guild_ids=[865717588684570634])
    async def test_command(self, interaction: disnake.ApplicationCommandInteraction):

        embed = disnake.Embed(title="Crea il tuo profilo", description="Crea un tuo profilo con il nostro bot")

        await interaction.response.send_message(embed=embed, ephemeral=True)


class MyModal(disnake.ui.Modal):
    def __init__(self) -> None:
        components = [
            disnake.ui.TextInput(
                label="Nome",
                placeholder="il tuo nome social",
                custom_id="nome",
                style=disnake.TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Descrizione",
                placeholder="Descrivi il tuo canale",
                custom_id="descrizione",
                style=disnake.TextInputStyle.short,
                min_length=5,
                max_length=50,
            ),
        ]
        super().__init__(
            title="Profilo", custom_id="profile_tag", components=components
        )

    async def callback(self, inter: disnake.ModalInteraction) -> None:
        embed = disnake.Embed(title="Profilo")
        for key, value in inter.text_values.items():
            embed.add_field(name=key.capitalize(), value=value, inline=False)
        await inter.response.send_message(embed=embed)

    async def on_error(self, error: Exception, inter: disnake.ModalInteraction) -> None:
        await inter.response.send_message("Oops, something went wrong.", ephemeral=True)

def setup(bot):
    bot.add_cog(MyModal(bot))
