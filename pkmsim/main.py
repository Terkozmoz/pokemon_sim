# Main.py
# Made by @Terkozmoz (GitHub)
# Last Update: 2023-12-14
# Music by @Bliitzit (YouTube)
# Date: 2020-06-27

import random
import os
import battle as b
import pokemons as p

all_pkms = p.all_pokemon.copy()

### GAME AREA ###
# Function to generate the game area
def generate_area(player_pos=None):
    area = [['[   ]' for _ in range(10)] for _ in range(10)]
    if not player_pos:
        player_pos = (random.randint(0, 9), random.randint(0, 9))
    
    occupied_positions = [player_pos]  # Store occupied positions

    # Generate walls
    num_walls = random.randint(10, 30)
    wall_positions = []
    for _ in range(num_walls):
        pos = (random.randint(0, 9), random.randint(0, 9))
        while pos in occupied_positions:
            pos = (random.randint(0, 9), random.randint(0, 9))
        occupied_positions.append(pos)
        wall_positions.append(pos)

    # Generate items, making sure they don't overlap with other objects or the player
    num_items = random.randint(0, 4)
    item_pos = []
    for _ in range(num_items):
        pos = (random.randint(0, 9), random.randint(0, 9))
        while pos in occupied_positions:
            pos = (random.randint(0, 9), random.randint(0, 9))
        item_pos.append(pos)
        occupied_positions.append(pos)

    # Generate battles, ensuring they don't overlap with other objects or the player
    num_battles = random.randint(1, 9)
    battle_pos = []
    for _ in range(num_battles):
        pos = (random.randint(0, 9), random.randint(0, 9))
        while pos in occupied_positions:
            pos = (random.randint(0, 9), random.randint(0, 9))
        battle_pos.append(pos)
        occupied_positions.append(pos)

    area[player_pos[0]][player_pos[1]] = '[ O ]'  # Place the player in the game area

    for pos in wall_positions:
        area[pos[0]][pos[1]] = '[---]'  # Place walls in the game area

    for pos in item_pos:
        area[pos[0]][pos[1]] = '[ X ]' # Place items in the game area

    for pos in battle_pos:
        area[pos[0]][pos[1]] = '[ # ]' # Place battles in the game area

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
    return 0 <= player_pos[0] < 10 and 0 <= player_pos[1] < 10

### PLAYER ACTION ###

# Function to handle player action and map regeneration if player goes off the map
def player_action(area, player_pos, action):
    movement = {
        'w': (-1, 0), 'z': (-1, 0), 's': (1, 0), 'a': (0, -1),
        'q': (0, -1), 'd': (0, 1), 'wa': (-1, -1), 'zq': (-1, -1),
        'aw': (-1, -1), 'qz': (-1, -1), 'wd': (-1, 1), 'zd': (-1, 1),
        'dw': (-1, 1), 'dz': (-1, 1), 'sa': (1, -1), 'sq': (1, -1),
        'as': (1, -1), 'qs': (1, -1), 'sd': (1, 1), 'ds': (1, 1)
    }

    area[player_pos[0]][player_pos[1]] = '[   ]'  # Reset previous position

    if action in movement:
        move = movement[action]
        new_player_pos = (player_pos[0] + move[0], player_pos[1] + move[1])

        # If the new position is within boundaries, update the player position
        if within_boundaries(new_player_pos):
            if area[new_player_pos[0]][new_player_pos[1]] != '[---]':
                if area[new_player_pos[0]][new_player_pos[1]] == '[ X ]':
                    area[new_player_pos[0]][new_player_pos[1]] = '[ OX ]'
                elif area[new_player_pos[0]][new_player_pos[1]] == '[ # ]':
                    area[new_player_pos[0]][new_player_pos[1]] = '[ O# ]'
                else:
                    area[new_player_pos[0]][new_player_pos[1]] = '[ O ]'

                player_pos = new_player_pos  # Update player's position
            else:
                area[player_pos[0]][player_pos[1]] = '[ O ]'  # Hit a wall, maintain previous position
        else:
            # Player moved off the map, regenerate the map
            if new_player_pos[0] < 0:
                new_player_pos = (9, player_pos[1])
            elif new_player_pos[0] > 9:
                new_player_pos = (0, player_pos[1])
            elif new_player_pos[1] < 0:
                new_player_pos = (player_pos[0], 9)
            elif new_player_pos[1] > 9:
                new_player_pos = (player_pos[0], 0)

            player_pos = new_player_pos  # Update player's position
            area, player_pos = generate_area(player_pos)  # Regenerate the map

    # Check for special actions
    elif action == 'e':
        inventory()
        area[player_pos[0]][player_pos[1]] = '[ O ]'

    elif action == 'help':
        help()
        area[player_pos[0]][player_pos[1]] = '[ O ]'

    elif action == 'save':
        save()
        area[player_pos[0]][player_pos[1]] = '[ O ]'

    elif action == 'load':
        load()
        area[player_pos[0]][player_pos[1]] = '[ O ]'

    else:
        area[player_pos[0]][player_pos[1]] = '[ O ]'

    return area, player_pos

### CHECKS ###

# Function to check if the player is on an item square
def check_item(area, player_pos):
    return area[player_pos[0]][player_pos[1]] == '[ OX ]'

# Function to check if the player is on a battle square
def check_battle(area, player_pos):
    return area[player_pos[0]][player_pos[1]] == '[ O# ]'

### MENUS ###

# Shows the player's inventory
def inventory():
    print("You have:")
    if b.bonus_pball == 0 and b.bonus_potion == 0 and b.bonus_superpotion == 0 and b.bonus_potionmax == 0:
        print("Nothing")
    if b.bonus_pball >= 1:
        print(f"{b.bonus_pball} pokeball")
    if b.bonus_potion >= 1:
        print(f"{b.bonus_potion} potion")
    if b.bonus_superpotion >= 1:
        print(f"{b.bonus_superpotion} super potion")
    if b.bonus_potionmax >= 1:
        print(f"{b.bonus_potionmax} max potions")
    print("And that's it for now!")

# Shows some help for the player

def help():
    print("You are the \033[92m[ O ]\033[0m, you can move with wasd or zqsd. Diagonals also work")
    print("You can find items on the \033[94m[ X ]\033[0m spots")
    print("If you walk on a \033[91m[ # ]\033[0m spot, you will encounter an enemy")
    print(" \033[90m[---]\033[0m spots are walls, you can't walk on them")
    print("You can also open your inventory with e")
    print("The map is infinite, don't worry about going out of bounds, and explore as much as you want")
    print("You can save your progress with save")
    print("You can load your progress with load")
    print("You can also quit the game with quit")
    print("You can also see this help with help")

### FILE MANAGEMENT ###
new = True
appdata_path = os.getenv('APPDATA')
game_folder = 'Tko/Pkmsim'
os.makedirs(os.path.join(appdata_path, game_folder), exist_ok=True)

def save():
    path = os.path.join(appdata_path, 'Tko', 'Pkmsim', 'save.txt')
    sorted_mons = sorted(p.all_pokemon, key=lambda x: x.name)

    with open(path, 'w') as file:
        # saves the player's inventory
        file.write(f"{b.bonus_pball}\n")
        file.write(f"{b.bonus_potion}\n")
        file.write(f"{b.bonus_superpotion}\n")
        file.write(f"{b.bonus_potionmax}\n")
        # saves the pokemons's levels, in alphabetical order
        for mon in sorted_mons:
            file.write(f"{mon.level}\n")

def load():
    path = os.path.join(appdata_path, 'Tko', 'Pkmsim', 'save.txt')
    sorted_mons = sorted(p.all_pokemon, key=lambda x: x.name)

    with open(path, 'r') as file:
        # loads the player's inventory
        b.bonus_pball = int(file.readline())
        b.bonus_potion = int(file.readline())
        b.bonus_superpotion = int(file.readline())
        b.bonus_potionmax = int(file.readline())
        # loads the pokemons's levels, in alphabetical order
        for mon in sorted_mons:
            mon.level = int(file.readline())

def is_new():
    if os.path.exists(os.path.join(appdata_path, 'Tko', 'Pkmsim', 'save.txt')):
        global new
        new = False


### IDs ###

# Function to store items ids and give them to the player
def items_id(id):
    ids = {
        10: "pokeball",
        80: "potion",
        95: "super potion",
        100: "max potion"
    }
    for i in ids:
        if id <= i:
            print(f"You found a {ids[i]}!")
            if ids[i] == "pokeball":
                b.bonus_pball += 1
            elif ids[i] == "potion":
                b.bonus_potion += 1
            elif ids[i] == "super potion":
                b.bonus_superpotion += 1
            elif ids[i] == "max potion":
                b.bonus_potionmax += 1
            break

### GAME START ###

# Generate initial game area and get player position
game_area, player_position = generate_area()

# Display the initial game area and show help
display_area(game_area)

is_new()
# Shows help if the player is playing for the first time
if new == True:
    help()

### MAIN LOOP ###

# Game loop for player movement
while True:
    act = input("Enter direction (wasd / zqsd)(diagonals also work), 'e' to open your inventory, 'help' for help or 'quit' to exit: ").lower()
    if act == 'quit':
        break

    # Move the player and update the game area
    clear_screen()
    game_area, player_position = player_action(game_area, player_position, act)

    # Check if the player is on an item square
    if check_item(game_area, player_position):
        print("You found an item!")
        id = random.randint(1, 100)
        items_id(id)

    # Check if the player is on a battle square
    if check_battle(game_area, player_position):
        print("You encountered an enemy!")
        b.start(all_pkms)
        print("End of the encounter!")
        # shows leveled up pokemons
        for mon in p.leveled_ups:
            print(f"{mon[0]} leveled up to level {mon[1]}!")
            p.leveled_ups.remove(mon)
        # Back to the board

    # Display the updated game area
    display_area(game_area)

### CREDITS ###

print("Thank you for playing!")
print("Made by @Terkozmoz (GitHub)")
print("Music by @Bliitzit (YouTube)")
print("Have a nice day!")
