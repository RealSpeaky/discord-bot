import discord
from discord.ext import commands
import os
import random
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def greet(ctx):
    await ctx.send(f"Hello {ctx.author.name}, I'm alive and ready to help!")

@client.command()
async def joke(ctx):
    jokes = [
        "Why did the programmer quit his job? Because he didn't get arrays!",
        "Why do Java developers wear glasses? Because they can't C#!",
        "Debugging: Being the detective in a crime movie where you're also the murderer."
    ]
    await ctx.send(random.choice(jokes))

@client.command()
async def flip(ctx):
    result = random.choice(['Heads', 'Tails'])
    await ctx.send(f"The coin landed on **{result}**!")

@client.command()
async def eightball(ctx, *, question):
    responses = [
        "It is certain.", "Without a doubt.", "You may rely on it.",
        "Yes – definitely.", "Most likely.", "Ask again later.",
        "Cannot predict now.", "Don’t count on it.", "Very doubtful."
    ]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

keep_alive()
client.run(os.getenv('DISCORD_TOKEN'))
