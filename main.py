import nextcord
from nextcord.ext import commands

TESTING_GUILD_ID = 989746611192234024

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="My first slash command", guild_ids=[TESTING_GUILD_ID])
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hello!")

bot.run("NzU4ODUyMzExODk1Mzc1ODgy.G1Bqvh.VwCR3lIpPHvGbK2Hy3wuu2u6hI9BiJESWgNHE8")