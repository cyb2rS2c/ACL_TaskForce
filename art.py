import os
import random
import pyfiglet
from termcolor import colored

def create_ascii_text():
    color_list = ['red', 'green', 'grey', 'blue', 'magenta', 'cyan', 'white']
    default_text = "ACL TaskForce"
    os.system("clear")
    color_choice = random.choice(color_list)

    ascii_art = pyfiglet.figlet_format(default_text, font='smascii12')
    print(colored(ascii_art, color_choice))
    print(colored("Author: cyb2rS2c", 'red', attrs=['blink']))
