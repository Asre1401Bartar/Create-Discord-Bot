import discord
from discord.ext import commands
Prefix = "+"
client = commands.Bot(help_command=None,prefix_command=Prefix,intents=discord.Intents.all())
client.run(TOKEN)
