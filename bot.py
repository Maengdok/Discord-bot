# bot.py

import os
import random
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='¤')

"""
    EVENTS
"""

# New user
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')



"""
    COMMANDS SECTION
"""

# Channel creation
@bot.command(name='create-channel', help="-- Command to create a new textual channel.")
@commands.has_role('Python')

async def create_channel(context, channel_name='new-channel'):
    guild = context.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

# Permission
@bot.event
async def on_command_error(context, error):
    if isinstance(error, commands.errors.CheckFailure):
        await context.send('You do not have the correct role for this command')

# Test command
@bot.command(name='test', help='-- A testing command line.')
async def test_quotes(context):
    test_quotes = [
        'Juste un petit test...',
        'test, test, test',
        (
            'Un, deux, un, deux...'
            ' Est-ce que vous me recevez?'
        ),
    ]

    response = random.choice(test_quotes)
    await context.send(response)

# Rolling dice command
@bot.command(name="roll_dice", help="-- Simulates a rolling dice.")
async def roll(context, n_dice: int, n_sides: int):
    dice = [
        str(random.choice(range(1, n_sides + 1)))
        for _ in range(n_dice)
    ]
    await context.send(', '.join(dice))

# Rolling a single dice with 100 sides
@bot.command(name="roll", help="-- Simulates a 100 sides rolling dice.")
async def roll(context, n_dice=1, n_sides=100):
    dice = [
        str(random.choice(range(1, n_sides + 1)))
        for _ in range(n_dice)
    ]
    response = "Sur un jet de 100, tu as obtenu: {}.".format(''.join(dice))
    await context.send(response)

bot.run(TOKEN)
