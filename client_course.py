# client_course.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


client = discord.Client()

# New user notification
@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    # members = '\n - '.join([member.name for member in guild.members])
    # print(f'Guild Members:\n - {members}')

# MP New user
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to {guild.name}!'
    )


# User's messages reader
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    test_quotes = [
        'Juste un petit test...',
        'test, test, test',
        (
            'Un, deux, un, deux...'
            ' Est-ce que vous me recevez?'
        ),
    ]

    if message.content == 'test!':
        response = random.choice(test_quotes)
        await message.channel.send(response)

    elif message.content == 'raise-exception':
        raise discord.DiscordException

# Error message
@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

"""
class CustomClient(discord.Client):
    async def on_ready(self):
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
            )

client = CustomClient()
"""
client.run(TOKEN)
