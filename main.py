import discord
from discord.ext import commands
from keep_alive import keep_alive  # This runs the web server

# Start the Flask server for uptime monitoring
keep_alive()

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Run the bot (use your actual bot token here)
bot.run("MTM3MjU0OTQ3MTg1NDAwNjMxMw.GzxP_G._iPFrExBkBt6EdzLAsw58pVudf-cv99jApyFPs")
