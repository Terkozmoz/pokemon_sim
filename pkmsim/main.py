# Main.py
# Made by @Terkozmoz (GitHub)
# Last Update: 2023-12-06
# Music by @Bliitzit (YouTube)
# Date: 2020-06-27

import random
import os
import battle as b
import pokemons as p

all_pkms = p.all_pokemon.copy()
# Function to generate the game area
def generate_area(player_pos=None):
    area = [['[   ]' for _ in range(8)] for _ in range(8)]
    if not player_pos:
        player_pos = (random.randint(0, 7), random.randint(0, 7))
    
    occupied_positions = [player_pos]  # Store occupied positions

    # Generate walls
    num_walls = random.randint(5, 10)
    wall_positions = []
    for _ in range(num_walls):
        pos = (random.randint(0, 7), random.randint(0, 7))
        while pos in occupied_positions:
            pos = (random.randint(0, 7), random.randint(0, 7))
        occupied_positions.append(pos)
        wall_positions.append(pos)

    # Generate items, making sure they don't overlap with other objects or the player
    num_items = random.randint(1, 2)
    item_pos = []
    for _ in range(num_items):
        pos = (random.randint(0, 7), random.randint(0, 7))
        while pos in occupied_positions:
            pos = (random.randint(0, 7), random.randint(0, 7))
        item_pos.append(pos)
        occupied_positions.append(pos)

    # Generate battles, ensuring they don't overlap with other objects or the player
    num_battles = random.randint(1, 5)
    battle_pos = []
    for _ in range(num_battles):
        pos = (random.randint(0, 7), random.randint(0, 7))
        while pos in occupied_positions:
            pos = (random.randint(0, 7), random.randint(0, 7))
        battle_pos.append(pos)
        occupied_positions.append(pos)

    area[player_pos[0]][player_pos[1]] = '[ O ]'  # Place the player in the game area

    for pos in wall_positions:
        area[pos[0]][pos[1]] = '[---]'  # Place walls in the game area

    for pos in item_pos:
        area[pos[0]][pos[1]] = '[ X ]'

    for pos in battle_pos:
        area[pos[0]][pos[1]] = '[ # ]'

    return area, player_pos

# Function to display the game area
def display_area(area):
    for row in area:
        for cell in row:
            if cell == '[ X ]' or cell == '[ OX ]':
                print('\033[94m' + cell + '\033[0m', end='')  # Blue for items
            elif cell == '[ # ]':
                print('\033[91m' + cell + '\033[0m', end='')  # Red for battles
            elif cell == '[---]':
                print('\033[90m' + cell + '\033[0m', end='') # Gray for walls
            elif cell == '[ O ]':
                print('\033[92m' + cell + '\033[0m', end='') # Green for player
            else:
                print(cell, end='')
        print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to check if the player's position is within the map boundaries
def within_boundaries(player_pos):
    return 0 <= player_pos[0] < 8 and 0 <= player_pos[1] < 8

# Function to handle player movement and map regeneration if player goes off the map
def move_player(area, player_pos, direction):
    area[player_pos[0]][player_pos[1]] = '[   ]' # Reset previous position

    # Update player position based on direction
    new_player_pos = player_pos  # Initialize new player position

    # Straights
    if direction == 'w' or direction == 'z':
        new_player_pos = (player_pos[0] - 1, player_pos[1])
    elif direction == 's':
        new_player_pos = (player_pos[0] + 1, player_pos[1])
    elif direction == 'a' or direction == 'q':
        new_player_pos = (player_pos[0], player_pos[1] - 1)
    elif direction == 'd':
        new_player_pos = (player_pos[0], player_pos[1] + 1)
    # Diagonals
    elif direction == 'wa' or direction == 'zq' or direction == 'aw' or direction == 'qz':
        new_player_pos = (player_pos[0] - 1, player_pos[1] - 1)
    elif direction == 'wd' or direction == 'zd' or direction == 'dw' or direction == 'dz':
        new_player_pos = (player_pos[0] - 1, player_pos[1] + 1)
    elif direction == 'sa' or direction == 'sq' or direction == 'as' or direction == 'qs':
        new_player_pos = (player_pos[0] + 1, player_pos[1] - 1)
    elif direction == 'sd' or direction == 'ds':
        new_player_pos = (player_pos[0] + 1, player_pos[1] + 1)

    elif direction == 'e':
        inventory()
    # Else, the player didn't enter a valid direction
    else:
        new_player_pos = player_pos
    
    if not (0 <= new_player_pos[0] < 8 and 0 <= new_player_pos[1] < 8):
        # Player moved off the map
        # Calculate new position based on where they left from
        if new_player_pos[0] < 0:
            new_player_pos = (7, player_pos[1])
        elif new_player_pos[0] > 7:
            new_player_pos = (0, player_pos[1])
        elif new_player_pos[1] < 0:
            new_player_pos = (player_pos[0], 7)
        elif new_player_pos[1] > 7:
            new_player_pos = (player_pos[0], 0)

        player_pos = new_player_pos  # Update player's position
        area, player_pos = generate_area(player_pos)  # Regenerate the map

    else:
        # Check if the new position is not a wall before updating the map
        if area[new_player_pos[0]][new_player_pos[1]] != '[---]':
            if area[new_player_pos[0]][new_player_pos[1]] == '[ X ]':
                area[new_player_pos[0]][new_player_pos[1]] = '[ OX ]'
            elif area[new_player_pos[0]][new_player_pos[1]] == '[ # ]':
                area[new_player_pos[0]][new_player_pos[1]] = '[ O# ]'
            else:
                area[new_player_pos[0]][new_player_pos[1]] = '[ O ]'

            player_pos = new_player_pos  # Update player's position
    
    return area, player_pos



# Function to check if the player is on an item square
def check_item(area, player_pos):
    return area[player_pos[0]][player_pos[1]] == '[ OX ]'

# Function to check if the player is on a battle square
def check_battle(area, player_pos):
    return area[player_pos[0]][player_pos[1]] == '[ O# ]'

def inventory():
    print("You have:")
    print(f"{b.bonus_potion} potions")
    print(f"{b.bonus_superpotion} super potions")
    print(f"{b.bonus_potionmax} max potions")
    print("And that's it for now!")

# Generate initial game area and get player position
game_area, player_position = generate_area()

# Display the initial game area
display_area(game_area)

# Game loop for player movement
while True:
    move = input("Enter direction (wasd / zqsd)(diagonals also work) or 'quit' to exit: ").lower()
    if move == 'quit':
        break

    # Move the player and update the game area
    clear_screen()
    game_area, player_position = move_player(game_area, player_position, move)

    # Check if the player is on an item square
    if check_item(game_area, player_position):
        print("You found an item!")
        id = random.randint(1, 100)
        if id <= 10:
            print("You found a pokeball!")
            b.bonus_pball += 1
        elif id <= 80:
            print("You found a potion!")
            b.bonus_potion += 1
        elif id <= 95:
            print("You found a super potion!")
            b.bonus_superpotion += 1
        else:
            print("WOW! You found a max potion!")
            b.bonus_potionmax += 1

    # Check if the player is on a battle square
    if check_battle(game_area, player_position):
        print("You encountered an enemy!")
        b.start(all_pkms)
        print("End of the encounter!")
        # shows leveled up pokemons
        for lvlup in p.leveled_ups:
            print(f"{lvlup[0]} leveled up to level {lvlup[1]}!")

    # Display the updated game area
    display_area(game_area)
