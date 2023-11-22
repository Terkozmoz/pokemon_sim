# Pokemon_Main.py
# Made by @Terkozmoz (GitHub)
# Date: 2023-11-20
# Music by @Bliitzit (YouTube)
# Date: 2020-06-27

import random
import pygame
import pokemons as pkms
import firework as fw
import time as t

# Initialize Pygame and load the music
pygame.init()
pygame.mixer.music.load("assets\\theme\\battle_theme.mp3")

# Initialize the list of all Pokémon
all_pokemon = pkms.all_pokemon

# Define the Player class

class Player:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.potion = 1
        self.superpotion = 1
        self.potionmax = random.randint(0, 1)

    def Choose_attack(self):
        self.pokemon.Zero_pp()

        for i, attack in enumerate(self.pokemon.attacks):
            print(f"{i + 1}. {attack.name} ;\n Power: {attack.power} Accuracy: {attack.accuracy} \nPP: {self.pokemon.attack_pp[i]}")
            if attack.effect:
                print(f"Effect: {attack.effect} ; Probability: {attack.effect_probability}%")

        choice = int(input("Enter the attack number: ")) - 1
        if 0 <= choice < len(self.pokemon.attacks) and self.pokemon.attacks[choice].pp > 0:
            return self.pokemon.attacks[choice]
        else:
            print("Invalid choice. Try again.")
            return self.Choose_attack()

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

# Define the battle loop (the main game loop)

def battle_loop(all_pokemon, player=None):
    current_turn = 1
    healed_pokemon = []
    all_pokemon.sort(key=lambda x: x.speed, reverse=True)
    player_turn = all_pokemon.index(player.pokemon)
    print("\n")

    def all_pokemon_fainted():
        alive_pokemon = [pokemon for pokemon in all_pokemon if pokemon.Is_alive()]
        return len(alive_pokemon) == 1

    while True:
        if current_turn == player_turn:
            if player.pokemon.hp > 0:
                print("\n")
                # Display the all Pokémon's statuses
                for pokemon in all_pokemon:
                    if pokemon.status and pokemon != player.pokemon and pokemon.Is_alive():
                        if pokemon.status != "protect":
                            
                            print("\033[91mThe ennemy " + pokemon.name + " is " + pokemon.status + "!\033[0m")
                        else:
                            
                            print("\033[91mThe ennemy " + pokemon.name + " protects itself!\033[0m")
                
                if player.pokemon.status:
                    if player.pokemon.status != "protect":
                        
                        print("\033[94mYour Pokémon is " + player.pokemon.status + "!\033[0m")
                    else:
                        
                        print("\033[94mYour Pokémon protects itself!\033[0m")
                
                # Player's turn
                print(f"You have {player.pokemon.hp}/{player.pokemon.max_hp} HP")
                player_choice = input("Choose an action for your Pokémon:\n1. Attack\n2. Use a Potion\n3. Skip Turn\n4. Flee: ")
                print("\n")

                if player_choice == "1":
                    # Player chooses to attack
                    attack_player = player.Choose_attack()
                    print(f"\n Choose a target for the attack {attack_player.name}:")

                    # Display target options
                    for i, pokemon in enumerate(all_pokemon):
                        if pokemon != player.pokemon and pokemon.Is_alive():
                            print(f"{i + 1}. {pokemon.name}")

                    # Ask the player to choose a target
                    target_choice = int(input("Enter the target number: ")) - 1
                    print("\n")
                    if 0 <= target_choice < len(all_pokemon) and all_pokemon[target_choice].Is_alive() and all_pokemon[target_choice] != player.pokemon:
                        opponent = all_pokemon[target_choice]
                        player.pokemon.Attack(opponent, attack_player)
                        current_turn += 1
                    else:
                        print("Invalid target choice. The attack failed.")
                        current_turn += 1

                elif player_choice == "2":
                    # Player chooses to use a potion
                    print(f"Choose a potion:\n0. Potion ({player.potion})\n1. Super Potion ({player.superpotion})\n2. Max Potion ({player.potionmax})\n")
                    potion_choice = int(input("Enter the potion number: "))
                    player.Use_potion(player.pokemon, potion_choice)
                    current_turn += 1

                elif player_choice == "3":
                    # Player chooses to skip their turn
                    print("You have skipped your turn.")
                    current_turn += 1

                elif player_choice == "4":
                    # Player chooses to flee the battle
                    print("You have fled the battle.")
                    break
            else:
                current_turn += 1

        else:
            # Opponent's turn
            if current_turn < len(all_pokemon):
                current_pokemon = all_pokemon[current_turn]
            else:
                # In case the current turn is greater than the number of Pokémon
                current_pokemon = all_pokemon[current_turn % len(all_pokemon)]

            # Makes sure the current Pokémon is alive and isn't the player's Pokémon
            if current_pokemon.Is_alive() and current_pokemon != player.pokemon:
                print("\n")

                # Find a random living Pokémon target
                if current_pokemon not in healed_pokemon and current_pokemon.hp < current_pokemon.max_hp - 10 and random.randint(1, 5) == 1:
                    # The Pokémon has a 1 in 5 chance of using a potion
                    if random.randint(1, 10) == 1:
                        # The Pokémon has a 1 in 10 (total of 1 in 50) chance of using a Max Potion
                        current_pokemon.DrinkPotionMax()
                        healed_pokemon.append(current_pokemon)
                    current_pokemon.DrinkPotion(10)
                    healed_pokemon.append(current_pokemon)
                else:
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
                pygame.mixer.music.stop()
                print("\n")
                print("The battle is over.")
                break

    winner = [pokemon for pokemon in all_pokemon if pokemon.Is_alive()]
    # Define and display the winner
    if winner and len(winner) == 1:
        print(f"The winning Pokémon is: {winner[0].name}")
        if winner[0] == player.pokemon:
            print("\033[93mYou won the battle!\033[0m")
            t.sleep(1)
            fw.fireworks()
        else:
            print("\033[91mYou lost the battle!\033[0m")

    else:
        print("There is no winning Pokémon.")

    t.sleep(1)
    exit()

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
            print("Please enter a valid number.")

    if choice == 0:
        """
        print("You found a secret Pokémon!")
        chosen_pokemon = pkms.Mewthree
        all_pokemon.append(chosen_pokemon)
        """
 
    chosen_pokemon = all_pokemon[choice]
    print(f"You chose {chosen_pokemon.name}!")

    return chosen_pokemon

def number_of_opponents():
    #allows the player to choose the number of opponents
    global all_pokemon
    print(f"Set the number of opponent Pokémons:")
    choice = int(input(f"Choose a number between 4 and {len(all_pokemon)}: "))
    if len(all_pokemon) >= choice >= 4:
        for i in range(0, len(all_pokemon) - choice):
            opponent = random.choice(all_pokemon)
            all_pokemon.remove(opponent)
    else:
        print("Invalid choice.")
        number_of_opponents()

def main():
    # Create Pokémons and add them to the list
    fw.clear_screen
    print("\033[93mWelcome!\033[0m")
    number_of_opponents()
    player = Player(choose_pokemon())
    all_pokemon.sort(key=lambda x: x.speed, reverse=True)
    pkms.play_music()
    battle_loop(all_pokemon, player)
    
if __name__ == '__main__':
    main()
