# bot.py
import os

import discord
from dotenv import load_dotenv
import time
import asyncio
from datetime import datetime


now = datetime.now()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()




#Bot Stuff
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'

    )

    current = 0
    channel = client.get_channel(id=channelID)
    while True:
        now = datetime.now()
        if datetime.now().minute != current:
            current = datetime.now().minute
            currenttime = now.strftime("%I:%M %p")
            print(currenttime)
            await channel.send("<USER> It's " + currenttime)




client.run(TOKEN)
