from colorama import init, Fore, Back, Style

init(autoreset=True)
debug = True

def log(log, level):

    if debug == False:
        return

    #1: INFO
    #2: WARN
    #3: ERROR
    #4: CRITICAL

    if level == 1:
        print(Fore.CYAN + log)
    elif level == 2:
        print(Fore.YELLOW + log)
    elif level == 3:
        print(Fore.RED + log)
    elif level == 4:
        print(Fore.RED + Back.WHITE + log)
