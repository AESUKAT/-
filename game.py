import pygame
import sys
import prime
from cx_Freeze import setup, Executable

def main():
    Prime = prime.main()
    Prime.run()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

base = None

if sys.platform == "win32" : base = "Win32GUI"

exe = Executable(script = "prime.py", base= base)

setup(
    name = 'prime_game',
    version = '0.1', 
    description = 'converter',
    executables = [exe]
)

import os
img3_path = os.getcwd() + "img/"
print(img3_path)