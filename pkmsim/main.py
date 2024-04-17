# Main.py
# Made by @Terkozmoz (GitHub)
# Last Update: 2024-04-17 yyyy-mm-dd
# Music by @Bliitzit (YouTube)
# Date: 2020-06-27

import random
import os
import sys
import pygame as pg
import battle as b
import pokemons as p
import pyramid as py

# Initialize the differnt variables
all_pkms = p.all_pokemon.copy()
biome = "plains"
previous_biome = None
fishing_rod = False
music = None
plains_music = ["assets\\theme\\Route201.mp3", "assets\\theme\\Route120.mp3"]
acts = 0
Tem_colleg = False
On_Water = False

### GAME AREA ###
# Function to generate the game area
def generate_area(player_pos=None):
    """Generates the game area with the player and other objects."""

    global biome
    global previous_biome
    # Creates a 10x10 area with empty cells
    area = [['[   ]' for _ in range(10)] for _ in range(10)]

    # Generate the player's position randomly if not provided
    if not player_pos:
        player_pos = (random.randint(0, 9), random.randint(0, 9))
    
    occupied_positions = [player_pos]  # Store occupied positions

    previous_biome = biome

    # Define the current biome, based on the previous one (for a better coherence in the map generation)
    
    if previous_biome == 'sea':
        # Post-sea biomes
        biomes = ['plains','sea','desert','island']
        r = random.randint(0, 100)
        if r < 40:
            biome = biomes[1]
        elif r < 80 and not On_Water or r < 60 and On_Water:
            biome = biomes[0]
        elif On_Water and r > 60:
            biome = biomes[3]
        else:
            biome = biomes[2]

    elif previous_biome == 'desert':
        # Post-desert biomes
        biomes = ['plains','sea','desert']
        r = random.randint(0, 100)
        if r < 40:
            biome = biomes[2]
        elif r < 80:
            biome = biomes[0]
        else:
            biome = biomes[1]

    elif previous_biome == 'island':
        # Post-island biomes
        biomes = ['sea','island']
        r = random.randint(1, 2)
        if r == 1:
            biome = biomes[0]
        else:
            biome = biomes[1]

    elif previous_biome == 'clouds':
        # Post-clouds biomes
        biomes = ['plains','corruption']
        r = random.randint(0, 100)
        if r < 95:
            biome = biomes[0]
        else:
            biome = biomes[1] # 0.05% chance total to get the corruption biome (1% chance to get the clouds biome, then 5% to get the corruption biome after that)

    else: #plains
        biomes = ['plains','sea','desert','clouds']
        # Post-plains biomes
        r = random.randint(0, 100)
        if r < 50:
            biome = biomes[0]
        elif r < 75:
            biome = biomes[1]
        elif r == 100:
            biome = biomes[3] # 1% chance to get the clouds biome
        else:
            biome = biomes[2]

    p.biome = biome

    if pg.mixer.music.get_busy() == True: # If music is on
        if biome != previous_biome:
            previous_biome = biome
            pg.mixer.music.stop() # Stop the music
            player_action(game_area, player_position, 'music') # updates the music

    # Generate walls if the biome isn't the sea or island
    if biome not in ['sea','island']:
        num_walls = random.randint(10, 30)
        wall_positions = []
        for _ in range(num_walls):
            pos = (random.randint(0, 9), random.randint(0, 9))
            while pos in occupied_positions:
                pos = (random.randint(0, 9), random.randint(0, 9))
            occupied_positions.append(pos)
            wall_positions.append(pos)
    else:
        # Makes an empty list if there shouldn't be any walls
        wall_positions = []

    # Generate water tiles predominantly on one side with some puddles on the sand area
    if biome in ['sea', 'corruption','island']:
        water_side = random.choice(['left', 'right', 'top', 'bottom'])
        if biome == 'island':
            water_rows = random.randint(2, 3) # Number of rows of water on each side for the island biome
        else:
            water_rows = random.randint(4, 5)  # Number of rows of water on each side
        water_positions = []

        # Calculate player's side based on the player's position
        player_sides = []
        player_x, player_y = player_pos
        player_side = 'left' if player_x <= 4 else 'right'
        player_sides.append(player_side)
        player_side = 'top' if player_y <= 4 else 'bottom'
        player_sides.append(player_side)
        if biome == 'island':
            player_sides == [] # Reset the player's sides if the biome is the island (so water spawns on all sides)

        # Ensure water doesn't spawn on the same side as the player
        if biome != 'island':
            while water_side in player_sides:
                water_side = random.choice(['left', 'right', 'top', 'bottom'])

        if On_Water:
            water_side = random.choice(player_sides)

        if water_side == 'left' or biome == 'island':
            water_positions.extend([(x, y) for x in range(water_rows) for y in range(10)])
            water_positions.extend([(water_rows, y) for y in range(random.randint(1, 6))])
        if water_side == 'right' or biome == 'island':
            water_positions.extend([(x, y) for x in range(10 - water_rows, 10) for y in range(10)])
            water_positions.extend([(10 - water_rows - 1, y) for y in range(9, 9 - random.randint(1, 6), -1)])
        if water_side == 'top' or biome == 'island':
            water_positions.extend([(x, y) for x in range(10) for y in range(water_rows)])
            water_positions.extend([(x, water_rows) for x in range(random.randint(1, 6))])
        if water_side == 'bottom' or biome == 'island':
            water_positions.extend([(x, y) for x in range(10) for y in range(10 - water_rows, 10)])
            water_positions.extend([(x, 10 - water_rows - 1) for x in range(9, 9 - random.randint(1, 6), -1)])

        # Generate some puddles on the sand area
        num_puddles = random.randint(5, 10)
        puddle_positions = []
        if biome != 'island':
            for _ in range(num_puddles):
                pos = (random.randint(2, 7), random.randint(2, 7))
                while pos in occupied_positions or pos in water_positions:
                    pos = (random.randint(2, 7), random.randint(2, 7))
                occupied_positions.append(pos)
                puddle_positions.append(pos)
    else:
        water_positions = []  # Make an empty list for water and puddles if the biome is not the sea
        puddle_positions = []

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

    # Generate a shop, ensuring it doesn't overlap with other objects or the player
    shop_odds = 10 if biome in ['desert', 'sea'] else 5 # 10% chance to spawn a shop in in desert and sea, 20% in other biomes
    shop_pos = []
    if random.randint(0, shop_odds) == 1:
        pos = (random.randint(0, 9), random.randint(0, 9))
        while pos in occupied_positions:
            pos = (random.randint(0, 9), random.randint(0, 9))
        shop_pos.append(pos)
        occupied_positions.append(pos)

    # If the biome is a desert, chance to generate a pyramid
    if biome in ['desert', 'corruption']:
        pyramid_pos = []
        if random.randint(0, 10) == 10: # 10% chance to spawn a pyramid
            pos = (random.randint(0, 9), random.randint(0, 9))
            while pos in occupied_positions:
                pos = (random.randint(0, 9), random.randint(0, 9))
            pyramid_pos.append(pos)
            occupied_positions.append(pos)
    else:
        pyramid_pos = []

    # Generates Gyms
    gym_pos = []
    if random.randint(0, 10) == 10: # 10% chance to spawn a gym
        pos = (random.randint(0, 9), random.randint(0, 9))
        while pos in occupied_positions:
            pos = (random.randint(0, 9), random.randint(0, 9))
        gym_pos.append(pos)
        occupied_positions.append(pos)

    # Generate buttons, ensuring they don't overlap with walls or pyramids, if any
    num_buttons = random.randint(0, 10)
    button_pos = []
    button_pos_item = []
    button_pos_battle = []
    button_pos_quest = []
    button_pos_shard = []
    button_pos_craft = []
    for _ in range(num_buttons):
        pos = (random.randint(0, 9), random.randint(0, 9))
        while pos in wall_positions or pos in pyramid_pos or pos in water_positions:
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

    for pos in shop_pos:
        area[pos[0]][pos[1]] = '[ $ ]' # Place shops in the game area

    for pos in pyramid_pos:
        area[pos[0]][pos[1]] = '[ Δ ]' # Place pyramids in the game area


    for pos in water_positions:
        area[pos[0]][pos[1]] = '[ ~ ]' # Place water tiles in the game area

    for pos in puddle_positions:
        area[pos[0]][pos[1]] = '[ ~ ]' # Place puddles in the game area
    
    for pos in gym_pos:
        area[pos[0]][pos[1]] = '[ G ]' # Place gyms in the game area

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
        for cell in row:    # For each cell in the area
            if biome != 'clouds':
                match cell:
                    case '[ X ]' | '[ OX ]' | '[ X̲ ]' | '[ OX̲ ]':
                        print('\033[94m' + cell + '\033[0m', end='')                                     # Blue for items
                    case '[ # ]' | '[ #̲ ]' | '[ O# ]' | '[ O#̲ ]':
                        print('\033[91m' + cell + '\033[0m', end='')                                     # Red for battles
                    case '[---]':
                        print('\033[90m' + cell + '\033[0m', end='')                                     # Gray for walls
                    case '[\-/]' | '[\̲-̲/̲]' | '[ Δ ]':
                        print('\033[93m' + cell + '\033[0m', end='')                                     # Yellow for shards & pyramids
                    case '[ ⚒ ]' | '[ ⚒_]' :
                        print('\033[95m' + cell + '\033[0m', end='')                                     # Purple for craft
                    case '[ O ]' | '[ O̲ ]':
                        print('\033[92m' + cell + '\033[0m', end='')                                     # Green for player
                    case '[ ? ]' | '[ ?̲ ]' :
                        print('\033[96m' + cell + '\033[0m', end='')                                     # Cyan for quests
                    case '[ $ ]' | '[ O$ ]':
                        print('\033[92m' + cell + '\033[0m', end='')                                     # Green for shop
                    case '[ _ ]' if biome in ['desert', 'sea', 'island'] :
                        print('\033[93m' + cell + '\033[0m', end='')                                     # Yellow for buttons (other biomes)
                    case '[ _ ]' if biome in ['plains', 'corruption', 'island']:
                            print('\033[97m' + cell + '\033[0m', end='')                                 # White for buttons (plains)
                    case '[ ~ ]' | '[ 🛥 ]':
                        print('\033[94m' + cell + '\033[0m', end='')                                     # Blue for water & boat
                    case '[ G ]':
                        print('\033[92m' + cell + '\033[0m', end='')                                     # Green for gym
                    case _:
                        if biome in ['desert', 'sea', 'island']:
                            print('\033[93m' + cell + '\033[0m', end='')                                 # Changes the cells to be sand
                        elif biome == 'corruption':
                            print('\033[95m' + cell + '\033[0m', end='')                                 # Changes the cells to be corrupted
                        else:
                            print(cell, end='')
            else:
                print(cell, end='')                                                                      # In the cloud biome, everything is white
        print()

def cls():
    # Clear_screen for Thonny
    print("\n" * 100)

def clear_screen():
    if "Thonny" in sys.executable:
        cls()
        b.vsc = False
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

# Function to check if the player's position is within the map boundaries
def within_boundaries(player_pos):
    return 0 <= player_pos[0] < 10 and 0 <= player_pos[1] < 10

def move_enemies(area):
    # Moves all enemies in the area
    for i in range(len(area)):
        for j in range(len(area[0])):
            if area[i][j] == '[ # ]':
                possible_moves = [(i+1, j), (i-1, j), (i, j+1), (i, j-1), (i+1, j+1), (i-1, j-1), (i+1, j-1), (i-1, j+1)]
                move = random.choice(possible_moves)
                while not (0 <= move[0] < len(area) and 0 <= move[1] < len(area[0]) and ( area[move[0]][move[1]] == '[   ]' or area[move[0]][move[1]] == '[ _ ]') ): # Check if the move is within boundaries and is an empty cell or a button
                    move = random.choice(possible_moves)
                area[i][j] = '[   ]'  # Clear previous position
                if area[move[0]][move[1]] == '[ _ ]':
                    area[move[0]][move[1]] = '[ #̲ ]' # Move enemy to a button and make the enemy protect it
                else:
                    area[move[0]][move[1]] = '[ # ]'  # Move enemy
    return area


### PLAYER ACTION ###

# Function to handle player action and map regeneration if player goes off the map
def player_action(area, player_pos, action):
    global On_Water
    movement = {
        'w': (-1, 0), 'z': (-1, 0), 's': (1, 0), 'a': (0, -1),
        'q': (0, -1), 'd': (0, 1), 'wa': (-1, -1), 'zq': (-1, -1),
        'aw': (-1, -1), 'qz': (-1, -1), 'wd': (-1, 1), 'zd': (-1, 1),
        'dw': (-1, 1), 'dz': (-1, 1), 'sa': (1, -1), 'sq': (1, -1),
        'as': (1, -1), 'qs': (1, -1), 'sd': (1, 1), 'ds': (1, 1),
        'ww': (-2, 0), 'zz': (-2, 0), 'aa': (0, -2), 'qq': (0, -2),
        'dd': (0, 2), 'ss': (2, 0)
    } # Define the possible movements for the player
    
    player = area[player_pos[0]][player_pos[1]]      # Get the player's current position
    area[player_pos[0]][player_pos[1]] = '[   ]'     # Reset previous position
    if player == '[ 🛥 ]':
        On_Water = True
        area[player_pos[0]][player_pos[1]] = '[ ~ ]' # Reset previous position if the player is on water, and keeps the on water status

    if action in movement:                           # If the action is a movement
        move = movement[action]
        new_player_pos = (player_pos[0] + move[0], player_pos[1] + move[1])

        # If the new position is within boundaries, update the player position
        if within_boundaries(new_player_pos):
            if ( area[new_player_pos[0]][new_player_pos[1]] != '[---]' or "Earth Badge" in b.badges ) and ( area[new_player_pos[0]][new_player_pos[1]] != '[ ~ ]' or "Marsh Badge" in b.badges ):
                match area[new_player_pos[0]][new_player_pos[1]]: # Check the new position
                    case '[ X ]':
                        area[new_player_pos[0]][new_player_pos[1]] = '[ OX ]'
                    case '[ # ]':
                        area[new_player_pos[0]][new_player_pos[1]] = '[ O# ]'
                    case '[\-/]':
                        area[new_player_pos[0]][new_player_pos[1]] = '[\O/]'
                    case '[ ⚒ ]':
                        area[new_player_pos[0]][new_player_pos[1]] = '[ O⚒ ]'
                    case '[ ? ]':
                        area[new_player_pos[0]][new_player_pos[1]] = '[ O? ]'
                    case '[ Δ ]':
                        area[new_player_pos[0]][new_player_pos[1]] = '[ OΔ ]'
                    case '[ $ ]':
                        area[new_player_pos[0]][new_player_pos[1]] = '[ O$ ]'
                    case '[ G ]':
                        area[new_player_pos[0]][new_player_pos[1]] = '[ OG ]'
                    case '[ ~ ]':
                        area[new_player_pos[0]][new_player_pos[1]] = '[ 🛥 ]' # Boat if Marsh Badge
                    
                    ### BUTTONS ###

                    case '[ _ ]':
                        area[new_player_pos[0]][new_player_pos[1]] = '[ O̲ ]'
                    case '[ X̲ ]':
                        area[new_player_pos[0]][new_player_pos[1]] = '[ OX̲ ]'
                    case '[ #̲ ]':
                        area[new_player_pos[0]][new_player_pos[1]] = '[ O#̲ ]'
                    case '[ ?̲ ]':
                        area[new_player_pos[0]][new_player_pos[1]] = '[ O?̲ ]'
                    case '[\̲-̲/̲]':
                        area[new_player_pos[0]][new_player_pos[1]] = '[\O̲/̲]'
                    case '[ ⚒_]':
                        area[new_player_pos[0]][new_player_pos[1]] = '[ O⚒_ ]'

                    
                    case _:
                        area[new_player_pos[0]][new_player_pos[1]] = '[ O ]' # Empty cell ( or anywehere else the player isn't supposed to be )

                player_pos = new_player_pos                                  # Update player's position
                return area, player_pos
            
            else:
                area[player_pos[0]][player_pos[1]] = '[ O ]'                 # Hit a wall or water, maintain previous position ( oof )

        else:
            # Player moved off the map and all buttons are pressed, regenerate the map
            if not check_button(area) or player_pos[0] == player_pos[1] == 1 or "Earth Badge" in b.badges:  # all buttons
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
            else:                                                                                           # not all buttons
                area[player_pos[0]][player_pos[1]] = '[ O ]'
                print("You can't leave this room while there are still buttons to press!")

    # Check for special actions ( not movements )
    match action:

        case 'e':
            inventory()
            area[player_pos[0]][player_pos[1]] = '[ O ]'

        case 'help':
            help()
            area[player_pos[0]][player_pos[1]] = '[ O ]'

        case 'save':
            save()
            area[player_pos[0]][player_pos[1]] = '[ O ]'

        case 'load':
            load()
            area[player_pos[0]][player_pos[1]] = '[ O ]'

        case 'skip':
            for _ in range(8):
                b.badges.append(b.all_badges.pop())

        case 'music' | 'm':
            global music
            if pg.mixer.music.get_busy(): # Stop the music if it's playing
                pg.mixer.music.stop()
                print("Music stopped!")
                area[player_pos[0]][player_pos[1]] = '[ O ]'
            else:                         # Play the music if it's not playing

                # Choose the music based on the biome
                match biome:
                    case 'plains':
                        music = random.choice(plains_music)
                    case 'sea' | 'island':
                        music = "assets\\theme\\Surf.mp3"
                    case 'desert':
                        print("Desert music isn't implemented yet, so it will play the plains music, sorry!")
                        music = random.choice(plains_music)
                    case 'clouds' | 'corruption':
                        music == "assets\\theme\\Route26_27.mp3"    

                pg.mixer.init()
                pg.mixer.music.load(music)
                pg.mixer.music.play(-1)
                print("Music is playing!")
                print(f"Playing: {music[13:len(music)-4]}, by Bliitzit")
                area[player_pos[0]][player_pos[1]] = '[ O ]'

        case 'f':
            if check_near_water(area, player_pos): # Check if the player is near water
                print("You are near water!, you can fish here!")
                if fishing_rod:
                    fishing()

                else:
                    print("You need a fishing rod to fish here!")
                    print("Maybe someone will give you one if you complete a quest...")

            else:
                print("What are you trying to fish? Rocks? Dirt? Sand? You need to be near water to fish!")
            area[player_pos[0]][player_pos[1]] = '[ O ]'

        case _: # Any other action ( like "efiu" by example )
            if area[player_pos[0]][player_pos[1]] == '[ 🛥 ]' or area[player_pos[0]][player_pos[1]] == '[ ~ ]':
                area[player_pos[0]][player_pos[1]] = '[ 🛥 ]'
                On_Water = True
            else:
                area[player_pos[0]][player_pos[1]] = '[ O ]'
                On_Water = False

    return area, player_pos

def craft_items():
    # Define crafting recipes: 'result': ( [ required items ], crafted item )
    crafting_recipes = {
        1: (['potion', 'potion', 'potion', 'potion', 'potion'], 'super_potion'),
        2: (['pokeball', 'pokeball', 'pokeball'], 'max_potion'),
        3: (['potion', 'potion', 'potion', 'potion', 'potion','potion', 'potion', 'potion', 'potion', 'potion'], 'max_potion'),
        4: (['r_shard', 'b_shard', 'g_shard', 'y_shard', 'w_shard'], 'shard')
    }

    # Display available recipes
    print("Available Recipes:")
    for recipe_id, (required_items, crafted_item) in crafting_recipes.items():
        print(f"Recipe number: {recipe_id} - Required: {', '.join(required_items).capitalize()} -> Crafted: {crafted_item.capitalize()}")

    # Get user input for chosen recipe
    chosen_recipe_id = int(input("Enter the number of the item you want to craft: "))

    # Check if the chosen recipe ID exists
    if chosen_recipe_id in crafting_recipes:
        required_items, crafted_item = crafting_recipes[chosen_recipe_id]
        can_craft = True

        # Check if the player has required items for crafting
        for item in required_items:
            match item:
                case 'pokeball':
                    if b.bonus_pball < 3:
                        print(f"You don't have enough {item}s.")
                        can_craft = False
                        break
                case 'potion':
                    if b.bonus_potion < 5:
                        print(f"You don't have enough {item}s.")
                        can_craft = False
                        break
                case 'r_shard':
                    if b.r_shards < 1:
                        print(f"You don't have enough {item}s.")
                        can_craft = False
                        break
                case 'b_shard':
                    if b.b_shards < 1:
                        print(f"You don't have enough {item}s.")
                        can_craft = False
                        break
                case 'g_shard':
                    if b.g_shards < 1:
                        print(f"You don't have enough {item}s.")
                        can_craft = False
                        break
                case 'y_shard':
                    if b.y_shards < 1:
                        print(f"You don't have enough {item}s.")
                        can_craft = False
                        break
                case 'w_shard':
                    if b.w_shards < 1:
                        print(f"You don't have enough {item}s.")
                        can_craft = False
                        break

        # If the player has required items, perform crafting
        if can_craft:
            print(f"Crafting {crafted_item.capitalize()}...")
            # Remove required items from the inventory (deduct the necessary counts)
            for item in required_items:
                match item:
                    case 'pokeball':
                        b.bonus_pball -= 3
                    case 'potion':
                        b.bonus_potion -= 5
                    case 'r_shard':
                        b.r_shards -= 1
                    case 'b_shard':
                        b.b_shards -= 1
                    case 'g_shard':
                        b.g_shards -= 1
                    case 'y_shard':
                        b.y_shards -= 1
                    case 'w_shard':
                        b.w_shards -= 1

            # Add crafted item to the inventory
            match crafted_item:
                case 'super_potion':
                    b.bonus_superpotion += 1
                case 'max_potion':
                    b.bonus_potionmax += 1
                case 'shard':
                    b.shards += 1

            print(f"You crafted a {crafted_item.capitalize()}!")

    else:
        print("Invalid recipe number.")

def is_sharded():
    if b.shards > 0:
        print("Choose a Pokemon to power up using shards.")
        for i, pokemon in enumerate(p.all_pokemon):
            print(f"{i + 1}. {pokemon.name}")
        while True:
            try:
                choice = int(input("Enter the number of the Pokemon you want to shard: "))
                break
            except ValueError:
                print("Please enter a valid integer number.")
        print("\n")
        
        if 0 <= choice < len(p.all_pokemon):
            # If the target is valid, power it up using shards
            selected = p.all_pokemon[choice]
            
            # Check if there are enough shards
            selected.name = '\033[92m' + selected.name + '\033[0m'
            selected.attack += 20
            selected.defense += 20
            selected.max_hp += 10
            
            # Deducts one shard
            b.shards -= 1
                
            print("Pokemon upgraded successfully!")

    else:
        print("Not enough shards available.")

def fishing():
    print("How did you even got a fishing rod?!")
    fishing = input("Do you want to fish? (yes/no): ").lower()
    if fishing == "yes":
        catch = random.randint(0, 100) # Random chance to catch an item, a pokemon or a fishing rod ( for some reason )

        if catch < 20:  # 20% chance to catch an item
            print("You fished an item!")
            id = random.randint(1, 100)
            items(id)

        elif catch < 59 or catch == 100: # 39% chance to catch a pokemon
            print("You fished an enemy!")
            start_battle()

        elif catch == 99: # 1% chance to catch a fishing rod ( and get 1000 pokecoins if you keep it )
            print("You caught a... fishing rod?")
            print("That's not very usefull, you aleardy have one...")
            choice = input("Throw it back? (yes/no): ").lower()
            if choice == "yes":
                print("You threw the fishing rod back into the water")
            else:
                print("You kept the fishing rod and sold it for 1000 pokecoins!")
                b.pokecoins += 1000

        else:   # 40% chance to catch nothing
            print("You didn't catch anything...")

### CHECKS ###

# Function to check if the player is on an item square
def check_item(area, player_pos):
    return area[player_pos[0]][player_pos[1]] == '[ OX ]' or area[player_pos[0]][player_pos[1]] == '[ OX̲ ]'

# Function to check if the player is on a battle square
def check_battle(area, player_pos):
    return area[player_pos[0]][player_pos[1]] == '[ O# ]' or area[player_pos[0]][player_pos[1]] == '[ O#̲ ]' or area[player_pos[0]][player_pos[1]] == '[ # ]'

# Function to check if the player is on a shard square
def check_shard(area, player_pos):
    return area[player_pos[0]][player_pos[1]] == '[\O/]' or area[player_pos[0]][player_pos[1]] == '[\O̲/̲]'

# Function to check if the player is on a craft square
def check_craft(area, player_pos):
    return area[player_pos[0]][player_pos[1]] == '[ O⚒ ]' or area[player_pos[0]][player_pos[1]] == '[ O⚒_ ]'

# Function to check if the player is on a quest square
def check_quest(area, player_pos):
    return area[player_pos[0]][player_pos[1]] == '[ O? ]' or area[player_pos[0]][player_pos[1]] == '[ O?̲ ]'

# Function to check if the player is on a pyramid square
def check_pyramid(area, player_pos):
    return area[player_pos[0]][player_pos[1]] == '[ OΔ ]'

# Function to check if the player is on a gym square
def check_gym(area, player_pos):
    return area[player_pos[0]][player_pos[1]] == '[ OG ]' 

# Function to check if the player is on a shop square
def check_shop(area, player_pos):
    return area[player_pos[0]][player_pos[1]] == '[ O$ ]'

def check_near_water(area, player_pos):
    # Checks is any of the 8 cells around the player is water
    for i in range(-1, 2):
        for j in range(-1, 2):
            if player_pos[0] + i >= 0 and player_pos[0] + i < 10 and player_pos[1] + j >= 0 and player_pos[1] + j < 10: # Check if the cell is within the map
                if area[player_pos[0] + i][player_pos[1] + j] == '[ ~ ]':
                    return True

# Function to check if there are remaining buttons
def check_button(area):
    if biome != 'corruption':
        for row in area:
            for cell in row:
                if cell == '[ _ ]' or cell == '[ X̲ ]' or cell == '[ #̲ ]' or cell == '[ ?̲ ]' or cell == '[\̲-̲/̲]' or cell == '[ ⚒_ ]':
                    return True
    return False

### MENUS ###

# Shows the player's inventory
def inventory():
    print("You have:")
    if b.bonus_pball == 0 and b.bonus_potion == 0 and b.bonus_superpotion == 0 and b.bonus_potionmax == 0:
        print("Not much... You know what, take this potion!")
        b.bonus_potion += 1 # Gives the player a potion if they don't have any pokeballs or potions ( shards and badges are not accounted for )
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
    if b.badges != []:
        print("Badges:")
        for badge in b.badges:
            print(badge)
    print("And that's it for now!")

def start_battle(arena = None):
    if not arena:
        print("You encountered an enemy!")
        b.start(all_pkms)
    if arena == 'Gym':
        print("You encountered a gym leader!")
        p.gym = True
        b.start(all_pkms,None,'Gym')
        p.gym = False
    print("End of the encounter!")
    # shows leveled up pokemons
    for mon in p.leveled_ups:
        print(f"{mon[0]} leveled up to level {mon[1]}!")
        p.leveled_ups.remove(mon)
    # Updates music, if any
    if pg.mixer.music.get_busy() and music != None:
        pg.mixer.music.stop()
        pg.mixer.music.load(music)
        pg.mixer.music.play(-1)
    # Back to the board
        
def shop():
    in_shop = True
    shop_id = random.randint(0, 33)
    if shop_id == 27:
        global Tem_colleg

        items = {
            1: ('pokeball (On SaLe!!)', 50),
            2: ('pokeball', 100),
            3: ('pokeball (ExPenSiv)', 500),
            4: ('PaY 4 TeM ColLeG', 10000),
            5: ('Master Ball', 1000000)
        }

        print("WelCOm To tEm ShoP!!")
        while in_shop:
            print("YoU hAvE", b.pokecoins, "pOkeCoiNs!")
            print("You caNN buI:")
            for (item, price) in items.items():
                if item != 'Master Ball' or Tem_colleg == True:
                    print(f"{item.capitalize()} - {price} pOkeCoiNs")
            while True:
                try:
                    choice = int(input("EnTEr tHe NumBR of tHe iTm Yu wNt To bUy!:"))
                    break
                except ValueError:
                    print("Please enter a valid integer number.")
            if choice in items:
                chosen_item, item_price = items[choice]
                if b.pokecoins >= item_price:
                    b.pokecoins -= item_price
                    print(f"You bought a {chosen_item}!")
                    if chosen_item == 'pokeball' or chosen_item == 'pokeball (On SaLe!!)' or chosen_item == 'pokeball (ExPenSiv)':
                        b.bonus_pball += 1
                    elif chosen_item == 'PaY 4 TeM ColLeG':
                        Tem_colleg = True
                    elif chosen_item == 'Master Ball' and Tem_colleg == True:
                        b.bonus_masterball += 1
                else:
                    print("You don't have enough pokecoins!")
            else:
                print("Invalid item ID")
            choice = input("Do Yu wnT! Bui sMtIng eLz YaAYA? (yes/no): ").lower()
            if choice == "no" or choice == "n" or choice == "nope" or choice == "nah" or choice == "no thanks" or choice == "no mony leaft :(":
                in_shop = False

    else:

        items = {
            1: ('pokeball', 100),
            2: ('potion', 200),
            3: ('superpotion', 500),
            4: ('potionmax', 1000)
        }

        print("Welcome to the shop!")
        while in_shop:
            print("You have", b.pokecoins, "pokecoins")
            print("You can buy:")
            for (item, price) in items.items():
                print(f"{item.capitalize()} - {price} pokecoins")
            while True:
                try:
                    choice = int(input("Enter the number of the item you want to buy: "))
                    break
                except ValueError:
                    print("Please enter a valid integer number.")
            if choice in items:
                chosen_item, item_price = items[choice]
                if b.pokecoins >= item_price:
                    b.pokecoins -= item_price
                    print(f"You bought a {chosen_item}!")
                    if chosen_item == 'pokeball':
                        b.bonus_pball += 1
                    elif chosen_item == 'potion':
                        b.bonus_potion += 1
                    elif chosen_item == 'superpotion':
                        b.bonus_superpotion += 1
                    elif chosen_item == 'potionmax':
                        b.bonus_potionmax += 1
                else:
                    print("You don't have enough pokecoins!")
            else:
                print("Invalid item ID")
            choice = input("Do you want to buy something else? (yes/no): ").lower()
            if choice == "no" or choice == "n" or choice == "nope" or choice == "nah" or choice == "no thanks" or choice == "no mony leaft :(": # I doubt anyone will write most of these, but I'm adding them anyways cuz why not
                in_shop = False

# Shows some help for the player

def help():
    global acts
    acts = 10
    print("You are the \033[92m[ O ]\033[0m, you can move with wasd or zqsd. Diagonals also work You can also jump 2 spaces with 'ww', 'zz', 'aa', 'qq', 'dd' and 'ss'")
    print("You can jump over pretty much anything")
    print("You can fish near water with 'f'")
    print("You can find items on the \033[94m[ X ]\033[0m spots")
    print("If you walk on a \033[91m[ # ]\033[0m spot, you will encounter an enemy")
    print(" \033[90m[---]\033[0m spots are walls, you can't walk on them")
    print(" \033[94m[ ~ ]\033[0m spots are water, you can't walk on them either... unless you have a certain badge")
    print(" \033[93m[\-/]\033[0m spots are shard spots, use them to improve your mons, if you have shards")
    print(" \033[95m[ ⚒ ]\033[0m spots allows you to craft items using items")
    print(" \033[96m[ ? ]\033[0m spots are quests, complete them then go on another one to get rewards")
    print(" \033[92m[ $ ]\033[0m spots are shops, you can buy items there")
    print(" \033[92m[ G ]\033[0m spots are gyms, you can fight the gym leader there")
    print("You can also open your inventory with 'e'")
    print("You can also play music with 'music' or 'm'")
    print("The map is infinite, don't worry about going out of bounds, and explore as much as you want")
    print("However, you can't leave the current room without pressing all the buttons - \033[93m[ _ ]\033[0m")
    print("You can press buttons by walking on them")
    print("Buttons can be anywhere, besides walls, so you may have to fight enemies to get to them ex: \033[94m[ X̲ ]\033[0m")
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
        file.write(f"{b.shards}\n")
        file.write(f"{b.bonus_masterball}\n")
        file.write("True\n" if fishing_rod else "False\n")
        # saves the current quest
        if p.quest != None:
            file.write("True\n")
            file.write(f"{p.quest.type}\n")
            file.write(f"{p.quest.objective}\n")
            file.write(f"{p.quest.quota}\n")
            file.write(f"{p.quest.progress}\n")
            file.write(f"{p.quest.target}\n")
            file.write(f"{p.quest.reward}\n")
            file.write(f"{p.quest.reward_amount}\n")
        else:
            file.write("False\n")
        file.write(f"{Tem_colleg}\n")
        # saves the pokemons, in alphabetical order
        for mon in sorted_mons:
            file.write(f"{mon.level}\n")
            file.write(f"{mon.attack}\n")
            file.write(f"{mon.defense}\n")
            file.write(f"{mon.max_hp}\n")
            file.write(f"{mon.kos}\n")
        
        file.write(f"{b.pokecoins}\n")
        if b.badges != []:
            file.write("True\n")
            for badge in b.badges:
                file.write(f"{badge}\n")
        
    print("Game Saved!")
    file.close()

def load():
    global fishing_rod
    global Tem_colleg
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
        b.shards = int(file.readline())
        b.bonus_masterball = int(file.readline())
        fishing_rod = file.readline().strip() == "True"
        # loads the current quest
        if file.readline() == "True\n":
            p.quest = p.Quest(file.readline().strip(), file.readline(), file.readline().strip(), file.readline().strip(), file.readline().strip(), file.readline(), file.readline())

        # Loads the current Tem College status
        Tem_colleg = file.readline().strip() == "True"
        # loads the pokemons, in alphabetical order
        for mon in sorted_mons:
            mon.level = int(file.readline())
            mon.attack = int(file.readline())
            mon.defense = int(file.readline())
            mon.max_hp = int(file.readline())
            mon.kos = int(file.readline())
        
        b.pokecoins = int(file.readline())
        if file.readline().strip() == "True":  # Read the first line and strip newline characters
                b.badges = []
                for _ in range(8):
                    badge_line = str(file.readline().strip())  # Read the next line and strip newline characters
                    if badge_line in b.all_badges:
                        b.badges.append(badge_line)
                        print(f"Badge {badge_line} loaded!")
                        b.all_badges.remove(badge_line)  # Remove the badge from the list of available badges
    print("Game Loaded!")
    file.close()

def is_new():
    if os.path.exists(os.path.join(appdata_path, 'Tko', 'Pkmsim', 'save.txt')):
        global new
        new = False


### Items ###

# Function to store items ids and give them to the player
def items(id):
    ids = {
        1: "red shard",     #1%
        2: "blue shard",    #1%
        3: "yellow shard",  #1%
        4: "green shard",   #1%
        5: "white shard",   #1%
        20: "pokeball",     #15%
        70: "potion",       #50%
        90: "super potion", #20%
        100: "max potion"   #10%
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
    if not fishing_rod:
        reward = random.choice(["pokeball", "potion", "super potion", "max potion", "fishing rod"])
        if reward == "fishing rod":
            reward_amount = 1
    else:
        reward = random.choice(["pokeball", "potion", "super potion", "max potion"])
    p.quest = p.Quest(None, objective, quantity, 0, target, reward, reward_amount)

def claim_reward():
    reward = p.quest.reward[:-1]
    reward_amount = p.quest.reward_amount
    match reward:
        case "pokeball":
            b.bonus_pball += reward_amount
        case "potion":
            b.bonus_potion += reward_amount
        case "super potion":
            b.bonus_superpotion += reward_amount
        case "max potion":
            b.bonus_potionmax += reward_amount
        case "fishing rod":
            global fishing_rod
            fishing_rod = True
        case _:
            print("Error. I am a Teapot.") # Teapot error (418)
    p.quest = None
    print("Quest completed!")
    print(f"You got {reward_amount} {reward}s!")

### GAME START ###

# Inits the status of the Warning Message
shown = False
fly_popup = False

# Generate initial game area and get player position
game_area, player_position = generate_area()

print(f'You are currently in the {biome} biome')
# Display the initial game area
display_area(game_area)

is_new()
# Shows help if the player is playing for the first time
if new == True:
    help()

### MAIN LOOP ###

# Game loop for player movement

while True:
    if b.vsc == False and shown != True:
        print("\033[91m/!\ Warning. You might want to switch to VSC for better use.\033[0m")
        shown = True
    
    if acts < 10:
        print("Type help to get a list of commands, and learn the basics of the game!")

    if "Earth Badge" in b.badges and fly_popup == False:
        print("You can now use fly to skip the buttons and walls, you are free to ignore them now! (finally!)")
        print("For now, you can only use it to skip the buttons, but more features will be added soon!")
        print("Also, you kinda finished the game... For now, stay tuned!")
        fly_popup = True
    
    act = input("Enter action: ").lower()
    if act == 'quit':
        break

    # Takes into account the player's act and update the game area
    clear_screen()
    game_area, player_position = player_action(game_area, player_position, act)
    acts += 1
    move_enemies(game_area)

    if p.quest != None:
        print(p.quest.objective, p.quest.progress, "/", p.quest.quota, "\n")

    # Check if the player is on an item square
    if check_item(game_area, player_position):
        print("You found an item!")
        id = random.randint(1, 100)
        items(id)

    # Check if the player is on a battle square
    if check_battle(game_area, player_position):
        start_battle()
        game_area, player_position = player_action(game_area, player_position, 'a')

    # Check if the player is on a gym square
    if check_gym(game_area, player_position):
        print("You found a gym!")
        start_battle("Gym")

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

    if check_pyramid(game_area, player_position):
        py.main()
        pg.mixer.music.stop() # Stop the music
        player_action(game_area, player_position, 'music') # updates the music

    
    if check_shop(game_area, player_position):
        print("You found a shop!")
        shop()

    # Display the updated game area
    display_area(game_area)
    print(f'You are currently in the {biome} biome')

### CREDITS ###

print("Thank you for playing!")
print("Made by @Terkozmoz (GitHub)")
print("Music by @Bliitzit (YouTube)")
print("Have a nice day!")
