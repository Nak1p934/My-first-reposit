import random
import sys
from colorama import Fore
tree = '''     *
    ***
   *****
  *******
 *********
    |#|'''
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
def lights():
    for j in range(30):
        print("\r")
        for i in tree:
            if i == "*" or i == "|" or i == "#":
                print(random.choice(colors) + i, end = "")
            else:
                print(i, end = "")
            sys.stdout.flush()
lights()