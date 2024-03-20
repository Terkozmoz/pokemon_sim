# firework.py

import time
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fireworks():
    i = 0
    clear_screen()

    try:
        term_columns, term_lines = os.get_terminal_size()
    except OSError:
        term_columns, term_lines = 80, 24  # Définir des dimensions par défaut

    while i < 100:
        burst = ["*", ".", "+", "x", "o", "O", "@"]
        colors = ["\033[91m", "\033[93m", "\033[95m", "\033[96m"]
        for _ in range(200):
            x = random.randint(1, term_columns)
            y = random.randint(1, term_lines)
            color = random.choice(colors)
            print("\033[{};{}H{}{}".format(y, x, color, random.choice(burst)), end='', flush=True)
        time.sleep(0.01)
        clear_screen()
        i += 1

    clear_screen()
