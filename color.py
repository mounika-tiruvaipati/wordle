from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


def color(guess, wrong_placement, example, word):
    colors = []
    for letter in guess:
        if letter in example and guess.index(letter) == word.index(letter):  
            colors.append(Fore.GREEN + letter + Style.RESET_ALL)
        elif letter in wrong_placement:
            colors.append(Fore.YELLOW + letter + Style.RESET_ALL)
        else:
            colors.append(letter)  
    return ''.join(colors)


