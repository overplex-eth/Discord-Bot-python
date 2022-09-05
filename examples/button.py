import disnake
from disnake.ext import commands


def create_button_view():
    view = disnake.ui.View()
    view.add_item(disnake.ui.Button(label="creazione profilo", style=disnake.ButtonStyle.blurple))
    return view

  '''simple button'''
  
  # For collegate the button to the class use view=view
