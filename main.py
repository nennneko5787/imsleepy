import os

import dotenv
import discord
from discord.ext import commands

bot = commands.Bot("sleepy#", intents=discord.Intents.default())

@bot.event
async def setup_hook():
    pass

bot.run(os.getenv("discord"))