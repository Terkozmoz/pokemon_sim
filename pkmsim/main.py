# Main.py
# Made by @Terkozmoz (GitHub)
# Last Update: 2023-12-21
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

    # Generate shard spots, ensuring they don't overlap with other objects or the player
    num_shards = random.randint(0,10)
    shard_pos = []
    if num_shards == 10:
        pos = (random.randint(0, 9), random.randint(0, 9))
        while pos in occupied_positions:
            pos = (random.randint(0, 9), random.randint(0, 9))
        shard_pos.append(pos)
        occupied_positions.append(pos)

    # Generate crafting spots, ensuring they don't overlap with other objects or the player
    num_craft = random.randint(0,10)
    craft_pos = []
    if num_craft == 10:
        pos = (random.randint(0, 9), random.randint(0, 9))
        while pos in occupied_positions:
            pos = (random.randint(0, 9), random.randint(0, 9))
        craft_pos.append(pos)
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

    for pos in shard_pos:
        area[pos[0]][pos[1]] = '[\-/]' # Places shard spots in the game area

    for pos in craft_pos:
        area[pos[0]][pos[1]] = '[ ⚒ ]' # Places shard spots in the game area

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
            elif cell == '[\-/]':
                print('\033[93m' + cell + '\033[0m', end='') # Yellow for shards
            elif cell == '[ ⚒ ]':
                print('\033[95m' + cell + '\033[0m', end='') # Purple for craft
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
                elif area[new_player_pos[0]][new_player_pos[1]] == '[\-/]':
                    area[new_player_pos[0]][new_player_pos[1]] = '[\O/]'
                elif area[new_player_pos[0]][new_player_pos[1]] == '[ ⚒ ]':
                    area[new_player_pos[0]][new_player_pos[1]] = '[ O⚒ ]'
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

def craft_items():
    # Define crafting recipes: 'result': (required items, crafted item)
    crafting_recipes = {
        'super_potion': (['potion', 'potion', 'potion', 'potion', 'potion'], 'super_potion'),
        'max_potion': (['pokeball', 'pokeball', 'pokeball'], 'max_potion'),
        'max_potion2' : (['potion', 'potion', 'potion', 'potion', 'potion','potion', 'potion', 'potion', 'potion', 'potion'], 'max_potion')
    }

    # Display available recipes
    print("Available Recipes:")
    for recipe, (required_items, crafted_item) in crafting_recipes.items():
        print(f"{recipe.capitalize()} - Required: {', '.join(required_items).capitalize()} -> Crafted: {crafted_item.capitalize()}")

    # Get user input for chosen recipe
    chosen_recipe = input("Enter the name of the item you want to craft: ").lower()

    # Check if the chosen recipe exists and if the player has required items
    if chosen_recipe in crafting_recipes:
        required_items, crafted_item = crafting_recipes[chosen_recipe]
        can_craft = True

        # Check if the player has required items for crafting
        for item in required_items:
            if item == 'pokeball':
                if b.bonus_pball < 3:  # Adjust the quantity as per the recipe
                    print(f"You don't have enough {item}s.")
                    can_craft = False
                    break
            elif item == 'potion':
                if b.bonus_potion < 5:  # Adjust the quantity as per the recipe
                    print(f"You don't have enough {item}s.")
                    can_craft = False
                    break
            # Add more conditions for other items here

        # If the player has required items, perform crafting
        if can_craft:
            print(f"Crafting {crafted_item.capitalize()}...")
            # Remove required items from the inventory (deduct the necessary counts)
            for item in required_items:
                if item == 'pokeball':
                    b.bonus_pball -= 3  # Adjust the deduction as per the recipe
                elif item == 'potion':
                    b.bonus_potion -= 5  # Adjust the deduction as per the recipe
                # Deduct counts for other items here

            # Add crafted item to the inventory (increase the count)
            if crafted_item == 'super_potion':
                b.bonus_superpotion += 1  # Adjust the increase as per the recipe
            elif crafted_item == 'max_potion':
                b.bonus_potionmax += 1  # Adjust the increase as per the recipe
            # Add more conditions for other crafted items here

            print(f"You crafted a {crafted_item.capitalize()}!")

    else:
        print("Invalid recipe name. Please choose a valid recipe.")

### CHECKS ###

# Function to check if the player is on an item square
def check_item(area, player_pos):
    return area[player_pos[0]][player_pos[1]] == '[ OX ]'

# Function to check if the player is on a battle square
def check_battle(area, player_pos):
    return area[player_pos[0]][player_pos[1]] == '[ O# ]'

# Function to check if the player is on a shard square
def check_shard(area, player_pos):
    return area[player_pos[0]][player_pos[1]] == '[\O/]'

def check_craft(area, player_pos):
    return area[player_pos[0]][player_pos[1]] == '[ O⚒ ]'


def is_sharded():
    if b.r_shards != 0 and b.b_shards != 0 and b.g_shards != 0 and b.y_shards != 0 and b.w_shards != 0:
        print("Choose a Pokemon to power up using shards.")
        for i, pokemon in enumerate(p.all_pokemon):
            print(f"{i + 1}. {pokemon.name}")
        target_choice = int(input("Enter the target number: ")) - 1
        print("\n")
        
        if 0 <= target_choice < len(p.all_pokemon):
            # If the target is valid, power it up using shards
            selected = p.all_pokemon[target_choice]
            
            # Check if there are enough shards of each color
            selected.name = '\033[92m' + selected.name + '\033[0m'
            selected.attack += 20
            selected.defense += 20
            selected.hp += 10
            
            # Deduct one shard of each color
            b.r_shards -= 1
            b.b_shards -= 1
            b.g_shards -= 1
            b.y_shards -= 1
            b.w_shards -= 1
                
            print("Pokemon upgraded successfully!")

    else:
        print("Not enough shards available.")


### MENUS ###

# Shows the player's inventory
def inventory():
    print("You have:")
    if b.bonus_pball == 0 and b.bonus_potion == 0 and b.bonus_superpotion == 0 and b.bonus_potionmax == 0:
        print("Nothing")
    if b.bonus_pball >= 1:
        print(f"{b.bonus_pball} pokeball")
    if b.bonus_potion >= 1:
        print(f"{b.bonus_potion} potions")
    if b.bonus_superpotion >= 1:
        print(f"{b.bonus_superpotion} super potions")
    if b.bonus_potionmax >= 1:
        print(f"{b.bonus_potionmax} max potions")
    if b.r_shards >= 1:
        print(f"{b.r_shards} red shards")
    if b.b_shards >= 1:
        print(f"{b.b_shards} blue shards")
    if b.y_shards >= 1:
        print(f"{b.y_shards} yellow shards")
    if b.g_shards >= 1:
        print(f"{b.g_shards} green shards")
    if b.w_shards >= 1:
        print(f"{b.w_shards} white shards")
    print("And that's it for now!")

# Shows some help for the player

def help():
    print("You are the \033[92m[ O ]\033[0m, you can move with wasd or zqsd. Diagonals also work")
    print("You can find items on the \033[94m[ X ]\033[0m spots")
    print("If you walk on a \033[91m[ # ]\033[0m spot, you will encounter an enemy")
    print(" \033[90m[---]\033[0m spots are walls, you can't walk on them")
    print(" \033[93m[\-/]\033[0m spots are shard spots, use them to improve your mons")
    print(" \033[95m[ ⚒ ]\033[0m spots allows you to craft items using items")
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
        file.write(f"{b.r_shards}\n")
        file.write(f"{b.b_shards}\n")
        file.write(f"{b.y_shards}\n")
        file.write(f"{b.g_shards}\n")
        file.write(f"{b.w_shards}\n")
        # saves the pokemons's levels, in alphabetical order
        for mon in sorted_mons:
            file.write(f"{mon.level}\n")
        
    print("Game Saved!")

def load():
    path = os.path.join(appdata_path, 'Tko', 'Pkmsim', 'save.txt')
    sorted_mons = sorted(p.all_pokemon, key=lambda x: x.name)
    print(path)

    with open(path, 'r') as file:
        # loads the player's inventory
        b.bonus_pball = int(file.readline())
        b.bonus_potion = int(file.readline())
        b.bonus_superpotion = int(file.readline())
        b.bonus_potionmax = int(file.readline())
        b.r_shards = int(file.readline())
        b.b_shards = int(file.readline())
        b.y_shards = int(file.readline())
        b.g_shards = int(file.readline())
        b.w_shards = int(file.readline())
        # loads the pokemons's levels, in alphabetical order
        for mon in sorted_mons:
            mon.level = int(file.readline())
    print("Game Loaded!")

def is_new():
    if os.path.exists(os.path.join(appdata_path, 'Tko', 'Pkmsim', 'save.txt')):
        global new
        new = False


### IDs ###

# Function to store items ids and give them to the player
def items_id(id):
    ids = {
        10: "pokeball",
        11: "red shard",
        12: "blue shard",
        13: "yellow shard",
        14: "green shard",
        15: "white shard",
        80: "potion",
        95: "super potion",
        100: "max potion"
    }
    for i in ids:
        if id <= i:
            print(f"You found a {ids[i]}!")
            if ids[i] == "pokeball":
                b.bonus_pball += 1
            elif ids[i] == "red shard":
                b.r_shards += 1
            elif ids[i] == "blue shard":
                b.b_shards += 1
            elif ids[i] == "yellow shard":
                b.y_shards += 1
            elif ids[i] == "green shard":
                b.g_shards += 1
            elif ids[i] == "white shard":
                b.w_shards += 1
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

    # Inside the while loop, after checking for item and battle squares
    if check_shard(game_area, player_position):
        is_sharded() 

    if check_craft(game_area, player_position):
        craft_items()

### CREDITS ###

print("Thank you for playing!")
print("Made by @Terkozmoz (GitHub)")
print("Music by @Bliitzit (YouTube)")
print("Have a nice day!")
