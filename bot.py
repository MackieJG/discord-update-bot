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
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents) 

@client.event
async def on_ready():
    print(f'Logged on as {client.user}!')

previous_update = []
client.event
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

@client.event
async def on_message(message):
    if message.content == "Update":
        result = fetch_valheim_update()
        print("Length of result:" , len(result))
        if len(result) > 1067:
            chunks = [result[i:i+1067] for i in range(0, len(result), 1067)]
            for chunk in chunks:
                await message.channel.send(chunk)
        await message.channel.send("Here is the latest update" + result)


print(len(result))

# async def main():
#     while True:
#         await check_for_new_update(previous_update)
#         await asyncio.sleep(3600)

# asyncio.run(main())

client.run(TOKEN)









