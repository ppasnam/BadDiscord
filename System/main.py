# {
import  platform
from fileinput import close
import time
import discord
from discord.ext import commands
import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True) 
import webbrowser
# }

# App..
print("")

# Platform catcher
try:
    platform = platform.system()
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




# Banner(for-linux)
if(platform=="Linux"):
    print("")
    print("")
    print("")
    print("")
    print(f"{Fore.RED}⠀⠀⠀⣠⠞⠉⢉⠩⢍⡙⠛⠋⣉⠉⠍⢉⣉⣉⣉⠩⢉⠉⠛⠲⣄{Fore.YELLOW}            »»————[♦BadDiscord♦]————««                                      ")
    print(f"{Fore.RED}⠀⠀⡴⡴⠁⠀⠂⡠⠑⠀⠀⠀⠂⠀⠀⠀⠀⠠⠀⠀⠐⠁⢊⠀⠄⠈⢦⢦{Fore.YELLOW}                 → 3.0 <B-> ←                                               ")
    print(f"{Fore.RED}⠀⣠⡾⠁⠀⠀⠄⣴⡪⠽⣿⡓⢦⠀⠀⡀⠀⣠⢖⣻⣿⣒⣦⠀⡀⢀⣈⢦⡀{Fore.YELLOW}                               ")
    print(f"{Fore.RED}⣰⠑⢰⠋⢩⡙⠒⠦⠖⠋⠀⠈⠁⠀⠀⠀⠀⠈⠉⠀⠘⠦⠤⠴⠒⡟⠲⡌⠛⣆{Fore.YELLOW}   ---------------------------------                            ")
    print(f"{Fore.RED}⢹⡰⡸⠈⢻⣈⠓⡦⢤⣀⡀⢾⠩⠤⠀⠀⠤⠌⡳⠐⣒⣠⣤⠖⢋⡟⠒⡏⡄⡟{Fore.YELLOW}  → github.com/ppasnam/BadDiscord ←                                       ")
    print(f"{Fore.RED}⠀⠙⢆⠀⠀⠻⡙⡿⢦⣄⣹⠙⠒⢲⠦⠴⡖⠒⠚⣏⣁⣤⣾⢚⡝⠁⠀⣨⠞{Fore.YELLOW}    ---------------------------------                                            ")
    print(f"{Fore.RED}⠀⠀⠈⢧⠀⠀⠙⢧⡀⠈⡟⠛⠷⡾⣶⣾⣷⠾⠛⢻⠉⢀⡽⠋⠀⠀⣰⠃{Fore.YELLOW}                                                     ")
    print(f"{Fore.RED}⠀⠀⠀⠀⠑⢤⡠⢂⠌⡛⠦⠤⣄⣇⣀⣀⣸⣀⡤⠼⠚⡉⢄⠠⣠⠞⠁{Fore.YELLOW}    MIT License-Copyright (c) 2022 ppasnam                                        ")
    print(f"{Fore.RED}⠀⠀⠀⠀⠀⠀⠉⠓⠮⣔⡁⠦⠀⣤⠤⠤⣤⠄⠰⠌⣂⡬⠖⠋{Fore.YELLOW}  Please do not use this tool for unethical purposes                                      ")
    print(f"{Fore.RED}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠤⢤⣀⣀⡤⠴⠒⠉{Fore.YELLOW}                   No liability is accepted ←←←            ")
elif(platform=="no_info"):
    print("")
    print("")
    print("")
    print("")
    print(f"{Fore.RED}⠀⠀⠀⣠⠞⠉⢉⠩⢍⡙⠛⠋⣉⠉⠍⢉⣉⣉⣉⠩⢉⠉⠛⠲⣄{Fore.YELLOW}            »»————[♦BadDiscord♦]————««                                      ")
    print(f"{Fore.RED}⠀⠀⡴⡴⠁⠀⠂⡠⠑⠀⠀⠀⠂⠀⠀⠀⠀⠠⠀⠀⠐⠁⢊⠀⠄⠈⢦⢦{Fore.YELLOW}                 → 3.0 <B-> ←                                               ")
    print(f"{Fore.RED}⠀⣠⡾⠁⠀⠀⠄⣴⡪⠽⣿⡓⢦⠀⠀⡀⠀⣠⢖⣻⣿⣒⣦⠀⡀⢀⣈⢦⡀{Fore.YELLOW}                               ")
    print(f"{Fore.RED}⣰⠑⢰⠋⢩⡙⠒⠦⠖⠋⠀⠈⠁⠀⠀⠀⠀⠈⠉⠀⠘⠦⠤⠴⠒⡟⠲⡌⠛⣆{Fore.YELLOW}   ---------------------------------                            ")
    print(f"{Fore.RED}⢹⡰⡸⠈⢻⣈⠓⡦⢤⣀⡀⢾⠩⠤⠀⠀⠤⠌⡳⠐⣒⣠⣤⠖⢋⡟⠒⡏⡄⡟{Fore.YELLOW}  → github.com/ppasnam/BadDiscord ←                                       ")
    print(f"{Fore.RED}⠀⠙⢆⠀⠀⠻⡙⡿⢦⣄⣹⠙⠒⢲⠦⠴⡖⠒⠚⣏⣁⣤⣾⢚⡝⠁⠀⣨⠞{Fore.YELLOW}    ---------------------------------                                            ")
    print(f"{Fore.RED}⠀⠀⠈⢧⠀⠀⠙⢧⡀⠈⡟⠛⠷⡾⣶⣾⣷⠾⠛⢻⠉⢀⡽⠋⠀⠀⣰⠃{Fore.YELLOW}                                                     ")
    print(f"{Fore.RED}⠀⠀⠀⠀⠑⢤⡠⢂⠌⡛⠦⠤⣄⣇⣀⣀⣸⣀⡤⠼⠚⡉⢄⠠⣠⠞⠁{Fore.YELLOW}    MIT License-Copyright (c) 2022 ppasnam                                        ")
    print(f"{Fore.RED}⠀⠀⠀⠀⠀⠀⠉⠓⠮⣔⡁⠦⠀⣤⠤⠤⣤⠄⠰⠌⣂⡬⠖⠋{Fore.YELLOW}  Please do not use this tool for unethical purposes                                      ")
    print(f"{Fore.RED}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠤⢤⣀⣀⡤⠴⠒⠉{Fore.YELLOW}                   No liability is accepted ←←←            ")
elif(platform=="Windows"):
    print("")
    print("")
    print("")
    print("")
    print(f"{Fore.RED}           »»————[♦BadDiscord♦]————««")
    print(f"{Fore.RED}                  → 3.0 <B-> ← ")
    print(f"{Fore.RED} ")
    print(f"{Fore.RED}        ---------------------------------")
    print(f"{Fore.RED}        → github.com/ppasnam/BadDiscord ←")
    print(f"{Fore.RED}        ---------------------------------")
    print(f"{Fore.RED} ")
    print(f"{Fore.RED}      MIT License-Copyright (c) 2022 ppasnam")
    print(f"{Fore.RED} Please do not use this tool for unethical purposes")
    print(f"{Fore.RED}           No liability is accepted ←←←  ")
    print(f"{Fore.RED} ")
    print(f"{Fore.RED} ")



time.sleep(5)
print("")
print("")
print("")

# Menu
try:
    def menu_loop():
        print(f"{Fore.CYAN} ↓")
        print(f"{Fore.CYAN} 1 :{Fore.YELLOW} Start the attack")
        print(f"{Fore.CYAN} 2 :{Fore.YELLOW} Take Help")
        print(f"{Fore.CYAN} 3 :{Fore.YELLOW} Read the alert")
        print(f"{Fore.CYAN} 4 :{Fore.YELLOW} Give up")
        print(f"{Fore.CYAN} 5 :{Fore.YELLOW} customize the attack")
        print(f"{Fore.CYAN} ------------------------")
        temp_reply = input(" option > ")
        print("")
        if(temp_reply=="1"):
            print("")
            os.system('python System/Attack.py')
        elif(temp_reply=="2"):
            print("")
            print(f"{Fore.CYAN} >You are being redirected")
            webbrowser.open('https://github.com/ppasnam/BadDiscord', new = 2)
            time.sleep(5)
            print("")
            print("")
            menu_loop()
        elif(temp_reply=="3"):
            print("")
            os.system('python System/Alert.py')
        elif(temp_reply=="4"):
            print("")
            close()
        elif(temp_reply=="5"):
            os.system('python System/Attack/CusAttack.py')
        else:
            print(f"{Fore.YELLOW} You have not made a valid choice")
            print(f"{Fore.YELLOW} Please try again")
            menu_loop()
except:
    os.system('python BadDiscord.py')

print(f"{Fore.YELLOW} — Welcome —")
menu_loop()

print("")