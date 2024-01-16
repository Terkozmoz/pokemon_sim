# Main.py
# Made by @Terkozmoz (GitHub)
# Last Update: 2024-01-04
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

    # Generate quest spots, ensuring they don't overlap with other objects or the player
    num_quests = random.randint(0, 10)
    quest_pos = []
    if num_quests == 10:
        pos = (random.randint(0, 9), random.randint(0, 9))
        while pos in occupied_positions:
            pos = (random.randint(0, 9), random.randint(0, 9))
        quest_pos.append(pos)
        occupied_positions.append(pos)

    # Generate buttons, ensuring they don't overlap with walls
    num_buttons = random.randint(0, 10)
    button_pos = []
    button_pos_item = []
    button_pos_battle = []
    button_pos_quest = []
    button_pos_shard = []
    button_pos_craft = []
    for _ in range(num_buttons):
        pos = (random.randint(0, 9), random.randint(0, 9))
        while pos in wall_positions:
            pos = (random.randint(0, 9), random.randint(0, 9))
        if pos in occupied_positions:
            if pos in item_pos:
                button_pos_item.append(pos)
            elif pos in battle_pos:
                button_pos_battle.append(pos)
            elif pos in quest_pos:
                button_pos_quest.append(pos)
            elif pos in shard_pos:
                button_pos_shard.append(pos)
            elif pos in craft_pos:
                button_pos_craft.append(pos)
        else:
            button_pos.append(pos)
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

    for pos in quest_pos:
        area[pos[0]][pos[1]] = '[ ? ]' # Place quests in the game area

    ### BUTTONS (Yeah, they need their own category) ###

    for pos in button_pos:
        area[pos[0]][pos[1]] = '[ _ ]' # Place buttons in the game area

    for pos in button_pos_item:
        area[pos[0]][pos[1]] = '[ X̲ ]' # Place items buttons in the game area

    for pos in button_pos_battle:
        area[pos[0]][pos[1]] = '[ #̲ ]' # Place battles buttons in the game area

    for pos in button_pos_quest:
        area[pos[0]][pos[1]] = '[ ?̲ ]' # Place quests buttons in the game area

    for pos in button_pos_shard:
        area[pos[0]][pos[1]] = '[\̲-̲/̲]' # Place shard buttons in the game area

    for pos in button_pos_craft:
        area[pos[0]][pos[1]] = '[ ⚒_]' # Place craft buttons in the game area

    return area, player_pos


# Function to display the game area
def display_area(area):
    for row in area:
        for cell in row:
            if cell == '[ X ]' or cell == '[ OX ]'  or cell == '[ X̲ ]' or cell == '[ OX̲ ]':
                print('\033[94m' + cell + '\033[0m', end='')                                     # Blue for items
            elif cell == '[ # ]'  or cell == '[ #̲ ]' or cell == '[ O# ]' or cell == '[ O#̲ ]':
                print('\033[91m' + cell + '\033[0m', end='')                                     # Red for battles
            elif cell == '[---]':
                print('\033[90m' + cell + '\033[0m', end='')                                     # Gray for walls
            elif cell == '[\-/]' or cell == '[\̲-̲/̲]':
                print('\033[93m' + cell + '\033[0m', end='')                                     # Yellow for shards
            elif cell == '[ ⚒ ]' or cell == '[ ⚒_]' :
                print('\033[95m' + cell + '\033[0m', end='')                                     # Purple for craft
            elif cell == '[ O ]' or cell == '[ O̲ ]':
                print('\033[92m' + cell + '\033[0m', end='')                                     # Green for player
            elif cell == '[ ? ]' or cell == '[ ?̲ ]' :
                print('\033[96m' + cell + '\033[0m', end='')                                     # Cyan for quests
            elif cell == '[ _ ]': 
                print('\033[97m' + cell + '\033[0m', end='')                                     # White for buttons
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
        'as': (1, -1), 'qs': (1, -1), 'sd': (1, 1), 'ds': (1, 1),
        'ww': (-2, 0), 'zz': (-2, 0), 'aa': (0, -2), 'qq': (0, -2),
        'dd': (0, 2), 'ss': (2, 0)
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
                elif area[new_player_pos[0]][new_player_pos[1]] == '[ ? ]':
                    area[new_player_pos[0]][new_player_pos[1]] = '[ O? ]'
                
                ### BUTTONS ###

                elif area[new_player_pos[0]][new_player_pos[1]] == '[ _ ]':
                    area[new_player_pos[0]][new_player_pos[1]] = '[ O̲ ]'
                elif area[new_player_pos[0]][new_player_pos[1]] == '[ X̲ ]':
                    area[new_player_pos[0]][new_player_pos[1]] = '[ OX̲ ]'
                elif area[new_player_pos[0]][new_player_pos[1]] == '[ #̲ ]':
                    area[new_player_pos[0]][new_player_pos[1]] = '[ O#̲ ]'
                elif area[new_player_pos[0]][new_player_pos[1]] == '[ ?̲ ]':
                    area[new_player_pos[0]][new_player_pos[1]] = '[ O?̲ ]'
                elif area[new_player_pos[0]][new_player_pos[1]] == '[\̲-̲/̲]':
                    area[new_player_pos[0]][new_player_pos[1]] = '[\O̲/̲]'
                elif area[new_player_pos[0]][new_player_pos[1]] == '[ ⚒_]':
                    area[new_player_pos[0]][new_player_pos[1]] = '[ O⚒_ ]'
                else:
                    area[new_player_pos[0]][new_player_pos[1]] = '[ O ]'

                player_pos = new_player_pos  # Update player's position
            else:
                area[player_pos[0]][player_pos[1]] = '[ O ]'  # Hit a wall, maintain previous position
        else:
            # Player moved off the map and all buttons are pressed, regenerate the map
            if not check_button(area, player_pos):
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
            else:
                area[player_pos[0]][player_pos[1]] = '[ O ]'
                print("You can't go out of bounds while there are still buttons to press!")

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
        print("Invalid recipe name.")

### CHECKS ###

# Function to check if the player is on an item square
def check_item(area, player_pos):
    return area[player_pos[0]][player_pos[1]] == '[ OX ]' or area[player_pos[0]][player_pos[1]] == '[ OX̲ ]'

# Function to check if the player is on a battle square
def check_battle(area, player_pos):
    return area[player_pos[0]][player_pos[1]] == '[ O# ]' or area[player_pos[0]][player_pos[1]] == '[ O#̲ ]'

# Function to check if the player is on a shard square
def check_shard(area, player_pos):
    return area[player_pos[0]][player_pos[1]] == '[\O/]' or area[player_pos[0]][player_pos[1]] == '[\O̲/̲]'

# Function to check if the player is on a craft square
def check_craft(area, player_pos):
    return area[player_pos[0]][player_pos[1]] == '[ O⚒ ]' or area[player_pos[0]][player_pos[1]] == '[ O⚒_ ]'

# Function to check if the player is on a quest square
def check_quest(area, player_pos):
    return area[player_pos[0]][player_pos[1]] == '[ O? ]' or area[player_pos[0]][player_pos[1]] == '[ O?̲ ]'

# Function to check if there are remaining buttons
def check_button(area, player_pos):
    for row in area:
        for cell in row:
            if cell == '[ _ ]' or cell == '[ X̲ ]' or cell == '[ #̲ ]' or cell == '[ ?̲ ]' or cell == '[\̲-̲/̲]' or cell == '[ ⚒_ ]':
                return True
    return False

### SHARDS ###
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
        print("Nothing... You know what, take this potion!")
        b.bonus_potion += 1
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
    print("You are the \033[92m[ O ]\033[0m, you can move with wasd or zqsd. Diagonals also work You can also jump 2 spaces with ww, zz, aa, qq, dd and ss")
    print("You can jump over pretty much anything")
    print("You can find items on the \033[94m[ X ]\033[0m spots")
    print("If you walk on a \033[91m[ # ]\033[0m spot, you will encounter an enemy")
    print(" \033[90m[---]\033[0m spots are walls, you can't walk on them")
    print(" \033[93m[\-/]\033[0m spots are shard spots, use them to improve your mons")
    print(" \033[95m[ ⚒ ]\033[0m spots allows you to craft items using items")
    print(" \033[96m[ ? ]\033[0m spots are quests, complete them then go on another one to get rewards")
    print("You can also open your inventory with e")
    print("The map is infinite, don't worry about going out of bounds, and explore as much as you want")
    print("However, you can't leave the map without pressing all the buttons")
    print("You can press buttons by walking on them")
    print("Buttons can be anywhere, besides walls, so you may have to fight enemies to get to them")
    print("You can save your progress with save")
    print("You can load your progress with load")
    print("You can also quit the game with quit")
    print("You can also see this help with help")

### FILE MANAGEMENT ###

new = True
appdata_path = os.getenv('APPDATA')
game_folder = 'Tko'
game_folder2 = 'Pkmsim'
os.makedirs(os.path.join(appdata_path, game_folder), exist_ok=True)
os.makedirs(os.path.join(appdata_path, game_folder, game_folder2), exist_ok=True)

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
        # saves the current quest
        if p.quest != None:
            file.write("True\n")
            file.write(f"{p.quest.type}\n")
            file.write(f"{p.quest.objective}\n")
            file.write(f"{p.quest.quota}\n")
            file.write(f"{p.quest.target}\n")
            file.write(f"{p.quest.reward}\n")
            file.write(f"{p.quest.reward_amount}\n")
            file.write(f"{p.quest.progress}\n")
        else:
            file.write("False\n")
        # saves the pokemons's levels, in alphabetical order
        for mon in sorted_mons:
            file.write(f"{mon.level}\n")
        
    print("Game Saved!")
    file.close()

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
        # loads the current quest
        if file.readline() == "True\n":
            p.quest = p.Quest(file.readline().strip(), file.readline(), int(file.readline().strip()), file.readline().strip(), file.readline().strip(), int(file.readline()), int(file.readline()))
        # loads the pokemons's levels, in alphabetical order
        for mon in sorted_mons:
            mon.level = int(file.readline())
    print("Game Loaded!")
    file.close()

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
    if p.quest != None and p.quest.type == "collect":
        print(f"Looking for {p.quest.target} ...")
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
            
            if p.quest != None:
                if p.quest.type == "collect":
                    if ids[i] == p.quest.target:
                        p.quest.update_progress(1)
            break

### QUESTS ###

# Function to generate quests
def generate_quest():
    objectives = random.choice(["collect", "defeat"])
    if objectives == "collect":
        target = random.choice(["pokeball", "potion", "super potion", "max potion"])
        quantity = random.randint(1, 5)
        print(f"Collect {quantity} {target}s")
        objective = f"Collect {quantity} {target}s"
    elif objectives == "defeat":
        target = None
        quantity = random.randint(1, 10)
        print(f"Defeat {quantity} enemies")
        objective = f"Defeat {quantity} enemies"
    reward_amount = random.randint(1, 5)
    reward = random.choice(["pokeball", "potion", "super potion", "max potion"])
    p.quest = p.Quest(None, objective, quantity, 0, target, reward, reward_amount)

def claim_reward():
    reward = p.quest.reward
    reward_amount = p.quest.reward_amount
    if reward == "pokeball":
        b.bonus_pball += reward_amount
    elif reward == "potion":
        b.bonus_potion += reward_amount
    elif reward == "super potion":
        b.bonus_superpotion += reward_amount
    elif reward == "max potion":
        b.bonus_potionmax += reward_amount
    p.quest = None
    print("Quest completed!")
    print(f"You got {reward_amount} {reward}s!")

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
    if p.quest != None:
        print(p.quest.objective, p.quest.progress, "/", p.quest.quota, "\n")

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

    # Check if the player is on a shard square
    if check_shard(game_area, player_position):
        is_sharded() 

    # Check if the player is on a craft square
    if check_craft(game_area, player_position):
        craft_items()

    # Check if the player is on a quest square
    if check_quest(game_area, player_position):
        print("You found a quest!")
        if p.quest == None:
            generate_quest()
        elif p.quest.check_completion():
            claim_reward()

        else:
            print("You already have a quest!")
    
    # Display the updated game area
    display_area(game_area)

### CREDITS ###

print("Thank you for playing!")
print("Made by @Terkozmoz (GitHub)")
print("Music by @Bliitzit (YouTube)")
print("Have a nice day!")
