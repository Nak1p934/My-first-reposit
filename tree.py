import random
import os
from time import sleep
from colorama import Fore
tree = ["     *",
"    ***",
"   *****",
"  *******",
" *********",
"    |#|"]
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
def lights():
    for _ in range(20):
        for lines in tree:
            for simbol in lines:
                if simbol == "*" or simbol == "|" or simbol == "#":
                    print(random.choice(colors) + simbol, end = "")
                else:
                    print(simbol, end = "")
            print()
        sleep(0.7)
        os.system("cls") 

lights()