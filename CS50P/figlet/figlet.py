from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()
font_list = figlet.getFonts()

if len(sys.argv) == 1:
    user_input = input("Input: ").strip()
    figlet.setFont(font = choice(font_list))
    print("Output: \n", figlet.renderText(user_input))
elif len(sys.argv) == 3 and sys.argv[2] in font_list and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    user_input = input("Input: ").strip()
    figlet.setFont(font = sys.argv[2])
    print("Output: \n", figlet.renderText(user_input))
else:
    sys.exit("Invalid usage")