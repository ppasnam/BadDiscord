def normal():
    print(" error_1516: Missing libraries")
    print(" Try: pip install -r requirements.txt")
    input("")

def with_color():
    import colorama
    from colorama import Fore, Back, Style
    colorama.init()
    print(f"{Fore.RED} error_1516: Missing libraries")
    print(f"{Fore.YELLOW} Try: pip install -r requirements.txt")
    input("")

try:
    import colorama
    with_color()
except:
    normal()