import discord
from discord.ext import commands

import requests
import asyncio
import os
import json
from dotenv import load_dotenv


steam_api_url = 'https://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/'
steam_app_id = '892970'

load_dotenv()
client = commands.Bot(command_prefix = '!') # What the bot listens for in discord to calls it's functionality.

@client.event
async def on_ready():
    print('bot is ready!')

@client.command()
async def update_discord(ctx):
    await ctx.send("Here is the latest update" + )



previous_update = []

def fetch_valheim_update():
    url = 'https://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=892970&count=1&maxlength=20000&format=json'
    response = requests.get(url)
    data = json.loads(response.text)
    latest_update = data['appnews']['newsitems'][0]
    title = latest_update['title']
    contents = latest_update['contents']
    return title + ' - ' + contents

result = fetch_valheim_update()
previous_update = result

async def check_for_new_update(previous_update):
    new_update = fetch_valheim_update()
    if new_update != previous_update:
        previous_update = new_update
        print('New update posted to Discord!')
    else:
        if previous_update:
            print('Previous update posted to Discord.')
        else:
            print('No previous update available.')

async def main():
    while True:
        await check_for_new_update(previous_update)
        await asyncio.sleep(3600)

asyncio.run(main())









