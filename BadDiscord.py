# {
# Libs Check
from cgi import test
from cmath import log
from linecache import checkcache
from platform import freedesktop_os_release

try:
    import time
    import platform
    import discord
    from discord.ext import commands
    import os
    import colorama
    from colorama import Fore, Back, Style
    colorama.init(autoreset=True) 
    library_check = 1
except:
    try:
        print("")
        import os
        os.system('pip install -r requirements')
        import platform
        import time
        import discord
        from discord.ext import commands
        import os
        import colorama
        from colorama import Fore, Back, Style
        colorama.init(autoreset=True) 
        print(f"{Fore.CYAN} The required libraries are loaded automatically")
        print("")
        library_check = 1
    except:
        print("BadDiscord libraries cannot install their own...")
        os.system('python System/LibEror.py')
##############################
# }

# Platform catcher
print("")
print("")
platform = platform.system()
try:
    if(platform=="Windows"):
        print(f"{Fore.CYAN} The platform was captured => Windows")
    elif(platform=="Linux"):
        print(f"{Fore.CYAN} The platform was captured => Windows")
    else:
        print(f"{Fore.YELLOW} Platform unidentified, platform => unknown")
except: 
    platform = "no_info"
    print(f"{Fore.YELLOW} For an unknown reason, the platform was not found")
time.sleep(2)
print("")

def redirect_1():

    with open("System/login.dll", 'r') as file:
        temp_login_check = file.read()
        login_check = int(temp_login_check)

    print(f"{Fore.CYAN} > Data is checking")
    print(f"{Fore.CYAN} ------------------")
    time.sleep(2)
    print("")

    if(connection_check==1):
        print(f"{Fore.GREEN} Connection [ok]")
    else:
        print(f"{Fore.RED} Connection [-]")
    
    if(library_check==1):
        print(f"{Fore.GREEN} Lib [ok]")
    else:
        print(f"{Fore.RED} Lib [ok]")

    if(login_check==1):
        print(f"{Fore.GREEN} Login [ok]")
    else:
        print(f"{Fore.RED} Login [-]")

    print("")

    if(connection_check==1):
        if(login_check==1):
            print(f"{Fore.CYAN} > Redirecting")   
            os.system('python System/main.py')
        else:
            print(f"{Fore.RED} eror_2881: Login error")
            print(f"{Fore.YELLOW} make sure the token is correct and bot 'intents' are turned on")
            input("")
    else:
        print(f"{Fore.RED} eror_210: Connection error")        
        print(f"{Fore.YELLOW} make sure the token is correct and bot 'intents' are turned on")
        input("")

    
print("")

# Token Check
with open("System/TempToken.pd", 'r') as file: # ***
    temp_token = file.read()

print("")
temp_token = input(" Please enter token >> ")
with open("System/TempToken.pd", 'w') as file:
    file.write(temp_token)

print("")
print(f"{Fore.CYAN} > Data is pulled")

# Connection Check
from fileinput import close
import os
from tokenize import Token
import urllib.request
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

if connect():
    connection_check = 1 # 1=True/On | 0=False/Off
else:
    connection_check = 0

# Login Check
try:
    with open("System/TempToken.pd", 'r') as file:
        check_temp_token = file.read()

    intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
    Bot = commands.Bot(command_prefix='admint --', intents=intents)
    
    @Bot.event
    async def on_ready():
        login_check = "1"
        with open("System/login.dll", 'w') as file:
            file.write(login_check)

        redirect_1()

    Bot.run(check_temp_token)
except: 
    login_check = "0"
    with open("System/login.dll", 'w') as file:
        file.write(login_check)

redirect_1()