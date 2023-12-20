import discord
from discord.ext import commands
import random

# Your list of random phrases
random_phrases = []
with open('bohdi_quotes', encoding="utf8") as f:
    random_phrases = f.readlines()


# Function to select a random phrase
def select_random_phrase():
    return random.choice(random_phrases)

# Discord bot setup
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} new message test')

@bot.command(name='bohdi')
async def bohdi_command(ctx):
    # Send a random phrase as a reply
    await ctx.send(select_random_phrase())

@bot.command(name='Bohdi')
async def bohdi_uppercase_command(ctx):
    # Send a random phrase as a reply
    await ctx.send(select_random_phrase())


# run the bot with the key from key.file
f = open("key.file", "r")
f = f.read()
print('reading key from file....')
bot.run(f)
print('starting server....')