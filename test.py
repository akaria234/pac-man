from pacman import pacman
import sys

if len(sys.argv) >= 2:
    print(pacman(sys.argv[1]))
else:
    print("Enter the correct number of arguments")