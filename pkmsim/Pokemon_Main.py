# Pokemon_Main.py
# made by @Terkozmoz (github)
# 2023-10-25
# Musics by @Bliitzit (Youtube)
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

    def Choisir_attaque(self):
        for i, attack in enumerate(self.pokemon.attaques):
            print(f"{i + 1}. {attack.nom} ;\n Power: {attack.puissance} Accuracy: {attack.precision}")
            if attack.effet:
                print(f"Effect: {attack.effet} ; Probability: {attack.effet_proba}%")

        choice = int(input("Enter the attack number: ")) - 1
        if 0 <= choice < len(self.pokemon.attaques):
            return self.pokemon.attaques[choice]
        else:
            print("Invalid choice. Try again.")
            return self.Choisir_attaque()

    def Use_potion(self, target, potion_choice):
        if potion_choice == 0 and self.potion >= 1:
            self.potion -= 1
            target.BoitPotion(20)
            print(f"You have {self.potion} Potions remaining")
        elif potion_choice == 1 and self.superpotion >= 1:
            self.superpotion -= 1
            target.BoitPotion(50)
            print(f"You have {self.superpotion} Super Potions remaining")
        elif potion_choice == 2 and self.potionmax >= 1:
            self.potionmax -= 1
            target.BoitPotionMax()
            print(f"You have {self.potionmax} Max Potions remaining")
        else:
            print("Invalid potion type.")

def battle_loop(all_pokemon, player=None):
    current_turn = 1
    healed_pokemon = []
    all_pokemon.sort(key=lambda x: x.vitesse, reverse=True)
    player_turn = all_pokemon.index(player.pokemon)

    def all_pokemon_fainted():
        alive_pokemon = [pokemon for pokemon in all_pokemon if pokemon.Est_vivant()]
        return len(alive_pokemon) == 1

    while True:
        print("\n")
        if current_turn == player_turn:
            if player.pokemon.pv > 0:
                if player.pokemon.statut:
                    print(f"Your Pokémon is {player.pokemon.statut}!")
                # Player's turn
                print(f"You have {player.pokemon.pv}/{player.pokemon.pvmax} HP")
                player_choice = input("Choose an action for your Pokémon:\n1. Attack\n2. Use a Potion\n3. Skip Turn\n4. Flee: ")
                print("\n")

                if player_choice == "1":
                    # Player chooses to attack
                    attack_player = player.Choisir_attaque()
                    print(f"\n Choose a target for the attack {attack_player.nom}:")

                    # Display target options
                    for i, pokemon in enumerate(all_pokemon):
                        if pokemon != player.pokemon and pokemon.Est_vivant():
                            print(f"{i + 1}. {pokemon.nom}")

                    # Ask the player to choose a target
                    target_choice = int(input("Enter the target number: ")) - 1
                    print("\n")
                    if 0 <= target_choice < len(all_pokemon) and all_pokemon[target_choice].Est_vivant() and all_pokemon[target_choice] != player.pokemon:
                        opponent = all_pokemon[target_choice]
                        player.pokemon.Attaque(opponent, attack_player)
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
            current_pokemon = all_pokemon[current_turn]

            if current_pokemon.Est_vivant() and current_pokemon != player.pokemon:
                # Variable to track if a significant change has occurred

                # Find a random living Pokémon target
                if current_pokemon not in healed_pokemon and current_pokemon.pv < current_pokemon.pvmax - 10 and random.randint(1, 5) == 1:
                    # The Pokémon has a 1 in 5 chance of healing by 10 pv
                    if random.randint(1, 10) == 1:
                        # The Pokémon has a 1 in 10 chance of using a max potion
                        current_pokemon.BoitPotionMax()
                        healed_pokemon.append(current_pokemon)
                    current_pokemon.BoitPotion(10)
                    healed_pokemon.append(current_pokemon)
                else:
                    available_targets = [pokemon for pokemon in all_pokemon if pokemon.Est_vivant() and pokemon != current_pokemon]
                    if available_targets:
                        target = random.choice(available_targets)
                        current_pokemon.Attaque(target, current_pokemon.Choisir_attaque())

            current_turn = (current_turn + 1) % len(all_pokemon)

            if all_pokemon_fainted() or current_turn > len(all_pokemon)*100:
                pygame.mixer.music.stop()
                print("\n")
                print("The battle is over.")
                break

    winner = [pokemon for pokemon in all_pokemon if pokemon.Est_vivant()]
    if winner and len(winner) == 1:
        print(f"The winning Pokémon is: {winner[0].nom}")
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
        print(f"{i + 1}. {pokemon.nom}")

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
    print(f"You chose {chosen_pokemon.nom}!")

    return chosen_pokemon

def number_of_opponents():
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

if __name__ == '__main__':
    # Create Pokémons and add them to the list
    print("\033[93mWelcome!\033[0m")
    all_pokemon = pkms.all_pokemon
    number_of_opponents()
    player = Player(choose_pokemon())
    all_pokemon.sort(key=lambda x: x.vitesse, reverse=True)
    pkms.play_music()
    battle_loop(all_pokemon, player)
