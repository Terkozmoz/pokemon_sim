# Pokemon_Main.py
# made by @Terkozmoz (github)
# 2023-10-18
# Music by @Bliitzit (Youtube)
# 2020-06-27

import random
import pygame
import pokemons as pkms

# Initialize Pygame and load the music
pygame.init()
pygame.mixer.music.load("assets\\theme\\battle_theme.mp3")

class Player:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.potion = 1
        self.superpotion = 1
        self.potionmax = random.randint(0, 1)

    def choose_attack(self):
        print("Choose an attack:")
        for i, attack in enumerate(self.pokemon.attacks):
            print(f"{i + 1}. {attack.name} ;\n Power: {attack.power} Accuracy: {attack.accuracy}")
            if attack.effect:
                print(f"Effect: {attack.effect} ; Probability: {attack.effect_probability}%")

        choice = int(input("Enter the attack number: ")) - 1
        if 0 <= choice < len(self.pokemon.attacks):
            return self.pokemon.attacks[choice]
        else:
            print("Invalid choice. Try again.")
            return self.choose_attack()

    def use_potion(self, target, potion_choice):
        if potion_choice == 0 and self.potion >= 1:
            self.potion -= 1
            target.drink_potion(20)
            print(f"You have {self.potion} Potions remaining")
        elif potion_choice == 1 and self.superpotion >= 1:
            self.superpotion -= 1
            target.drink_potion(50)
            print(f"You have {self.superpotion} Super Potions remaining")
        elif potion_choice == 2 and self.potionmax >= 1:
            self.potionmax -= 1
            target.drink_max_potion()
            print(f"You have {self.potionmax} Max Potions remaining")
        else:
            print("Invalid potion type.")
            self.use_potion(target, potion_choice)

def battle_loop(all_pokemon, player=None):
    current_turn = 1
    healed_pokemon = []
    all_pokemon.sort(key=lambda x: x.speed, reverse=True)
    player_turn = all_pokemon.index(player.pokemon) + 1

    def all_pokemon_fainted():
        alive_pokemon = [pokemon for pokemon in all_pokemon if pokemon.is_alive()]
        return len(alive_pokemon) == 1

    while True:
        print("\n")
        if current_turn == player_turn:
            if player.pokemon.hp > 0:
                # Player's turn
                print(f"You have {player.pokemon.hp}/{player.pokemon.max_hp} HP")
                player_choice = input("Choose an action for your Pokémon:\n1. Attack\n2. Use a Potion\n3. Skip Turn\n4. Flee: ")

                if player_choice == "1":
                    # Player chooses to attack
                    attack_player = player.choose_attack()
                    print(f"Choose a target for the attack {attack_player.name}:")

                    # Display target options
                    for i, pokemon in enumerate(all_pokemon):
                        if pokemon != player.pokemon and pokemon.is_alive():
                            print(f"{i + 1}. {pokemon.name}")

                    # Ask the player to choose a target
                    target_choice = int(input("Enter the target number: ")) - 1
                    print("\n")
                    if 0 <= target_choice < len(all_pokemon) and all_pokemon[target_choice].is_alive() and all_pokemon[target_choice] != player.pokemon:
                        opponent = all_pokemon[target_choice]
                        player.pokemon.attack(opponent, attack_player)
                        current_turn += 1
                    else:
                        print("Invalid target choice. The attack failed.")
                        current_turn += 1

                elif player_choice == "2":
                    # Player chooses to use a potion
                    print(f"Choose a potion:\n0. Potion ({player.potion})\n1. Super Potion ({player.superpotion})\n2. Max Potion ({player.potionmax})\n")
                    potion_choice = int(input("Enter the potion number: "))
                    player.use_potion(player.pokemon, potion_choice)
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
            current_pokemon = all_pokemon[current_turn - 1]

            if current_pokemon.is_alive() and current_pokemon != player.pokemon:
                # Variable to track if a significant change has occurred

                # Find a random living Pokémon target
                if current_pokemon not in healed_pokemon and current_pokemon.hp < current_pokemon.max_hp - 10 and random.randint(1, 5) == 1:
                    # The Pokémon has a 1 in 5 chance of healing by 10 HP
                    if random.randint(1, 10) == 1:
                        # The Pokémon has a 1 in 10 chance of using a max potion
                        current_pokemon.drink_max_potion()
                        healed_pokemon.append(current_pokemon)
                    current_pokemon.drink_potion(10)
                    healed_pokemon.append(current_pokemon)
                else:
                    available_targets = [pokemon for pokemon in all_pokemon if pokemon.is_alive() and pokemon != current_pokemon]
                    if available_targets:
                        target = random.choice(available_targets)
                        current_pokemon.attack(target, current_pokemon.choose_attack())

            current_turn = (current_turn + 1) % len(all_pokemon)

            if all_pokemon_fainted() or current_turn > 10000:
                pygame.mixer.music.stop()
                print("The battle is over.")
                break

    winner = [pokemon for pokemon in all_pokemon if pokemon.is_alive()]
    if winner and len(winner) == 1:
        print(f"The winning Pokémon is: {winner[0].name}")
        if winner[0] == player.pokemon:
            print("\033[93mYou won the battle!\033[0m")
        else:
            print("\033[91mYou lost the battle!\033[0m")
    else:
        print("There is no winning Pokémon.")

def choose_pokemon():
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

    chosen_pokemon = all_pokemon[choice]
    print(f"You chose {chosen_pokemon.name}!")

    return chosen_pokemon

def number_of_opponents():
    global all_pokemon
    print(f"Set the number of opponent Pokémons:")
    choice = int(input(f"Choose a number between 3 and {len(all_pokemon)}: "))
    if choice >= 3:
        for i in range(0, len(all_pokemon) - choice):
            opponent = random.choice(all_pokemon)
            all_pokemon.remove(opponent)
    else:
        print("Invalid choice.")
        number_of_opponents()

def play_music():
    if input("Do you want to play music? (y/n) ") == "y":
        pygame.mixer.music.play(-1)

if __name__ == '__main__':
    # Create Pokémons and add them to the list
    print("\033[93mWelcome!\033[0m")
    all_pokemon = pkms.all_pokemon
    number_of_opponents()
    player = Player(choose_pokemon())
    all_pokemon.sort(key=lambda x: x.speed, reverse=True)
    play_music()
    battle_loop(all_pokemon, player)
