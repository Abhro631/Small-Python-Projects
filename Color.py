#pip install coloroma if not present
#coloroma is a module which helps us to get various background colours for our subject text
#a small experimental code to show the usage of coloroma
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.GREEN+Back.YELLOW+"Abhro Kumar Roy,this side "+ Fore.YELLOW+ Back.BLUE+"I am a 3rd year engineering student")
print(Back.RED+"Mai yha aaya hun sirf seekhne aaya hun")
print(Fore.CYAN + Back.YELLOW+ "Chalo Bye Saionara , Bas dua mein yaad rakhna")
