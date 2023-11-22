import time
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fireworks():
    i = 0
    clear_screen()

    while i < 100:
        burst = ["*", ".", "+", "x", "o", "O", "@"]
        colors = ["\033[91m", "\033[93m", "\033[95m", "\033[96m"]
        for _ in range(200):
            x = random.randint(1, os.get_terminal_size().columns)
            y = random.randint(1, os.get_terminal_size().lines)
            color = random.choice(colors)
            print("\033[{};{}H{}{}".format(y, x, color, random.choice(burst)), end='', flush=True)
        time.sleep(0.01)
        clear_screen()
        i += 1

    print("\033[93mThank you for playing!\033[0m")
    time.sleep(1)
    exit()
