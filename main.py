# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)



@client.event
async def on_ready():
        print(f'Logged on as {client.user}!')

@client.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')

    if message.author == client.user:
        return
    
    if message.content == 'Hello':
        await message.channel.send('Hello')


client.run(TOKEN)