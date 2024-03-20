# battle.py

import random
import pygame
import pokemons as pkms
import firework as fw
import time as t
import abilities as a

# Initialize Pygame
pygame.init()

# Inventory

bonus_potion = 0
bonus_superpotion = 0
bonus_potionmax = 0

bonus_pball = 0
r_shards = 0
b_shards = 0
y_shards = 0
g_shards = 0
w_shards = 0
pokecoins = 0

badges = []

all_badges = ["Earth Badge", "Volcano Badge", "Marsh Badge", "Soul Badge", "Rainbow Badge", "Thunder Badge", "Cascade Badge", "Boulder Badge"] # Reverse order for pop()

vsc = True
# Define the Player class

class Player:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        # Items
        self.potion = 1 + bonus_potion
        self.superpotion = 1 + bonus_superpotion
        self.potionmax = random.randint(0, 1) + bonus_potionmax
        self.pball = 1 + bonus_pball # allows the player to catch (and instantly defeat) a pokemon

    """
    Initialize the player's Pokémon and the number of potions
    The number of potions is randomized between 0 and 1 for the Max Potion, so they aren't guaranteed to have one
    ### Methods ###
    Choose_attack() allows the player to choose an attack
    Use_potion() allows the player to use a potion
    They are borh used in the battle.by's battle loop
    """

    def Choose_attack(self):
        self.pokemon.Zero_pp()

        for i, attack in enumerate(self.pokemon.attacks):
            print(f"{i + 1}. {attack.name} ;\n Power: {attack.power} Accuracy: {attack.accuracy} \nPP: {self.pokemon.attack_pp[i]}")
            if attack.effect:
                print(f"Effect: {attack.effect} ; Probability: {attack.effect_probability}%")

        try:
            choice = int(input("Enter the attack number: ")) - 1

        except ValueError:
            print("Please enter a valid number.")
            return self.Choose_attack()  # Recursive call for invalid input

        if 0 <= choice < len(self.pokemon.attacks):
            attack = self.pokemon.attacks[choice]
            if self.pokemon.attack_pp[self.pokemon.attacks.index(attack)] > 0:
                return attack
            else:
                print("Attack out of PP. Choose another.")
                return self.Choose_attack()  # Recursive call for attack out of PP
        else:
            print("Invalid choice. Try again.")
            return self.Choose_attack()  # Recursive call for invalid index

    def Use_potion(self, target, potion_choice):
        if potion_choice == 0 and self.potion >= 1:
            self.potion -= 1
            target.DrinkPotion(20)
            print(f"You have {self.potion} Potions remaining")
        elif potion_choice == 1 and self.superpotion >= 1:
            self.superpotion -= 1
            target.DrinkPotion(50)
            print(f"You have {self.superpotion} Super Potions remaining")
        elif potion_choice == 2 and self.potionmax >= 1:
            self.potionmax -= 1
            target.DrinkPotionMax()
            print(f"You have {self.potionmax} Max Potions remaining")
        else:
            print("Invalid potion type.")

    def Use_pball(self):
        if self.pball >= 1:
            print("choose a pokemon to catch:")
            for i, pokemon in enumerate(all_pokemon):
                if pokemon.Is_alive() and pokemon != self.pokemon:
                    print(f"{i + 1}. {pokemon.name}")
            choice = int(input("Enter the pokemon number: ")) - 1
            if 0 <= choice < len(all_pokemon):
                print(f"You throw a Pokeball at {all_pokemon[choice].name}!")
                self.pball -= 1
                print(f"You have {self.pball} Pokeballs remaining")
                if random.randint(1, 10) == 1:
                    print("The pokemon was caught! It won't be able to fight anymore.")
                    all_pokemon[choice].hp = 0
                else:
                    print("The pokemon broke free!")
        else:
            print("No Pokeballs left.")

# Define the battle loop (the main game loop)

def battle_loop(all_pokemon, player=None, Arena=None):
    global pokecoins
    global badges
    for pkm in all_pokemon:
        pkm.defeated = 0
    current_turn = 1
    healed_pokemon = []
    all_pokemon.sort(key=lambda x: x.speed, reverse=True)
    player_turn = all_pokemon.index(player.pokemon)
    print("\n")

    # Gives each pokemon an ability
    a.give_abilities(all_pokemon)

    """
    The battle loop is the main game loop
    It is used to run the battle
    ### Variables ###
    current_turn is the current turn number
    healed_pokemon is a list of Pokémon that have been healed by a potion
    all_pokemon is the list of all Pokémon in the battle
    player_turn is the turn number of the player's Pokémon
    ### Methods ###
    all_pokemon_fainted() checks if all Pokémon are fainted
    It is used to end the battle
    """

    def all_pokemon_fainted():
        alive_pokemon = [pokemon for pokemon in all_pokemon if pokemon.Is_alive()]
        return len(alive_pokemon) == 1

    while True:
        if current_turn == player_turn:
            # Player's turn
            if player.pokemon.hp > 0:
                # If the player's Pokémon is alive
                print("\n")
                # Display the all Pokémon's statuses
                for pokemon in all_pokemon:
                    # Print the status of the Pokémon if it has one
                    if pokemon.status and pokemon != player.pokemon and pokemon.Is_alive():
                        if pokemon.status != "protect":
                            
                            print("\033[91mThe ennemy " + pokemon.name + " is " + pokemon.status + "!\033[0m")
                        else:
                            
                            print("\033[91mThe ennemy " + pokemon.name + " protects itself!\033[0m")
                
                if player.pokemon.status:
                    # Print the status of the player's Pokémon if it has one
                    if player.pokemon.status != "protect":
                        
                        print("\033[94mYour Pokémon is " + player.pokemon.status + "!\033[0m")
                    else:
                        
                        print("\033[94mYour Pokémon protects itself!\033[0m")

                print(f"Your ability is: {player.pokemon.ability} (Name - Effect -- Trigger)")
                
                # Player's turn menu
                print(f"You have {player.pokemon.hp}/{player.pokemon.max_hp} HP")
                player_choice = input("Choose an action for your Pokémon:\n1. Attack\n2. Use an item\n3. Skip Turn\n4. Flee: ")
                print("\n")

                match player_choice:

                    case "1":
                        # Player chooses to attack
                        attack_player = player.Choose_attack()
                        print(f"\n Choose a target for the attack {attack_player.name}:")

                        # Display target options
                        for i, pokemon in enumerate(all_pokemon):
                            if pokemon != player.pokemon and pokemon.Is_alive():
                                print(f"{i + 1}. {pokemon.name}")

                        # Ask the player to choose a target ( loops while invalid input )
                                
                        while True:
                            try:
                                target_choice = int(input("Enter the number of the target: ")) - 1
                                break
                            except ValueError:
                                # If the input is not a number
                                print("Please enter a valid number.")
                        
                        print("\n")
                        if 0 <= target_choice < len(all_pokemon) and all_pokemon[target_choice].Is_alive() and all_pokemon[target_choice] != player.pokemon:
                            # If the target is valid, attack it
                            opponent = all_pokemon[target_choice]
                            player.pokemon.Attack(opponent, attack_player, True)
                            current_turn += 1
                        else:
                            # If the target is invalid, the attack fails
                            print("Invalid target choice. The attack failed.")
                            current_turn += 1

                    case "2":
                        # Player chooses to use a item
                        print(f"Do you want to use a potion or a pokeball?\n0. Potion ({player.potion})\n1. Super Potion ({player.superpotion})\n2. Max Potion ({player.potionmax})\n3. Pokeball ({player.pball})\n")

                        while True:
                            try:
                                choice = int(input("Enter the number of the item you want to use: "))
                                break
                            except ValueError:
                                # If the input is not a number
                                print("Please enter a valid number.")

                        if choice <= 2:
                            player.Use_potion(player.pokemon, choice)
                        elif choice == 3:
                            Player.Use_pball(self=player)
                        else:
                            print("Invalid choice. Your turn is skipped.")
                        current_turn += 1

                    case "3":
                        # Player chooses to skip their turn
                        print("You have skipped your turn.")
                        current_turn += 1

                    case "4":
                        # Player chooses to flee the battle
                        print("You have fled the battle.")
                        break

                    case _:
                        # If the player's choice is invalid, skip their turn
                        print("Invalid choice. Your turn is skipped.")
                        current_turn += 1
            else:
                # If the player's Pokémon is fainted, skip their turn
                current_turn += 1

        else:
            # Opponent's turn
            if current_turn < len(all_pokemon):
                current_pokemon = all_pokemon[current_turn]
            else:
                if len(all_pokemon) > 0: # In case all pokemons are fainted (because of statuses)
                    # In case the current turn is greater than the number of Pokémon
                    current_pokemon = all_pokemon[current_turn % len(all_pokemon)]

            # Makes sure the current Pokémon is alive and isn't the player's Pokémon
            if current_pokemon.Is_alive() and current_pokemon != player.pokemon:
                print("\n")

                # Check for ability
                if current_pokemon.ability.name == "Intimidate":
                    player.pokemon.attack -= 10
                    current_pokemon.ability.name = None # ability only works once
                if current_pokemon.ability.name == "Galvanize":
                    for pkm in all_pokemon:
                        if pkm.type == "Normal":
                            pkm.type = "Electric"
                    current_pokemon.ability.name = None # Ability only works once
                
                if current_pokemon.hp < current_pokemon.max_hp / 3:
                    if current_pokemon.ability.name == "Overgrow" or current_pokemon.ability.name == "Swarm" or current_pokemon.ability.name == "Torrent" or current_pokemon.ability.name == "Blaze":
                        current_pokemon.attack += 10
                if current_pokemon not in healed_pokemon and current_pokemon.hp < current_pokemon.max_hp - 10 and random.randint(1, 5) == 1:
                    # The Pokémon has a 1 in 5 chance of using a potion
                    if random.randint(1, 10) == 1:
                        # The Pokémon has a 1 in 10 (total of 1 in 50) chance of using a Max Potion
                        current_pokemon.DrinkPotionMax()
                        healed_pokemon.append(current_pokemon)
                    current_pokemon.DrinkPotion(10)
                    healed_pokemon.append(current_pokemon)
                else:
                    # The Pokémon attacks a random living Pokémon
                    available_targets = [pokemon for pokemon in all_pokemon if pokemon.Is_alive() and pokemon != current_pokemon]
                    if available_targets:
                        target = random.choice(available_targets)
                        current_pokemon.Attack(target, current_pokemon.Choose_attack())

            current_turn = (current_turn + 1) % len(all_pokemon)

            all_pokemon = [pokemon for pokemon in all_pokemon if pokemon.Is_alive()]
            for i, pokemon in enumerate(all_pokemon):
                pokemon.number = i + 1

            if all_pokemon_fainted() or current_turn > len(all_pokemon)*100:
                # If all Pokémon are fainted, the battle is over or if the battle lasts too long, it ends (in case of normal vs ghost type situation)
                print("\n")
                print("The battle is over.")
                break

    winner = [pokemon for pokemon in all_pokemon if pokemon.Is_alive()]
    # Define and display the winner
    if winner and len(winner) == 1:
        print(f"The winning Pokémon is: {winner[0].name}")
        if winner[0] == player.pokemon:
            print("\033[93mYou won the battle!\033[0m")
            if Arena:
                if Arena == "Gym":
                    if len(all_badges) > 0:
                        print("You won a badge!")
                        badges.append(all_badges.pop())
                        print(f"You got the {badges[-1]}!")
                    else:
                        print("You have all the badges!")      
                
            if vsc == True:
                print("Fireworks? (might not work in some cases)")
                if input("y/n: ") == "y":
                    t.sleep(1)
                    fw.fireworks()

        else:
            print("\033[91mYou lost the battle!\033[0m")

        # Gives pokecoins to the player, based on the amount of pokemons defeated
        pokecoins = 50 * player.pokemon.defeated

    else:
        print("There is no winning Pokémon.")

    t.sleep(1)
    fw.clear_screen()
    reset_game()

def choose_pokemon():
    # allows the player to choose a pokemon
    global all_pokemon
    print("Choose a Pokémon from the following:")
    for i, pokemon in enumerate(all_pokemon):
        print(f"{i + 1}. {pokemon.name}")

    choice = None
    while choice is None:
        try:
            choice = int(input("Enter the number of the Pokémon you want: ")) - 1
            if choice < 0 or choice >= len(all_pokemon):
                print("Invalid Pokémon number. Try again.")
                choice = None
        except ValueError:
            # If the input is not a number
            print("Please enter a valid number.")
 
    chosen_pokemon = all_pokemon[choice]
    print(f"You chose {chosen_pokemon.name}!")

    return chosen_pokemon

def number_of_opponents(all_pokemon):
    #allows the player to choose the number of opponents
    choice = None
    
    print(f"Set the number of opponent Pokémons between 4 and {len(all_pokemon)}:")
    while choice is None:
        try:
            choice = int(input("Enter the number of opponents: "))
            if choice < 4 or choice > len(all_pokemon):
                print("Invalid number. Try again.")
                choice = None
            else: # Leave only the chosen number of opponents
                n = len(all_pokemon) - choice
                for i in range(n):
                    all_pokemon.pop(random.randint(0, len(all_pokemon) - 1)) # Remove a random pokemon
        except ValueError:
            # If the input is not a number
            print("Please enter a valid number.")

def reset_game():
    global all_pokemon
    pkms.reset_pokemon()
    all_pokemon.clear()  # Clear the existing list instead of reassigning
    all_pokemon.extend(pkms.base_all_pokemon)  # Extend with the updated list of pokemons

def start(pokes = None, player = None, gym = None):
    if pygame.mixer.music.get_busy() == True:
        pygame.mixer.music.stop()
    if not pokes:
        global all_pokemon
        all_pokemon = pkms.all_pokemon
    else:
        all_pokemon = pokes
    fw.clear_screen
    print("\033[93mWelcome!\033[0m")
    number_of_opponents(all_pokemon)
    player = Player(choose_pokemon())
    all_pokemon.sort(key=lambda x: x.speed, reverse=True)
    pkms.play_music()
    battle_loop(all_pokemon, player, gym)
    
if __name__ == '__main__':
    while True:
        start()
        if input("Do you want to play again? (y/n): ") == "n":
            break
