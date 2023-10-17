# Pokemon_Main.py
# made by @Terkozmoz (github)
# 2023-10-18
# Music by @Bliitzit (Youtube)
# 2020-06-27

import random
import pygame
import pokemons as pkms
pygame.init()
pygame.mixer.music.load("assets\\theme\\battle_theme.mp3")

class Joueur:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.potion = 1
        self.superpotion = 1
        self.potionmax = random.randint(0,1)

    def choisir_attaque(self):
        print("Choisissez une attaque :")
        for i, attaque in enumerate(self.pokemon.attaques):
            print(f"{i + 1}. {attaque.nom} ;\n Puissance: {attaque.puissance} Precision: {attaque.precision}")
            if attaque.effet:
                print(f"Effet: {attaque.effet} ; Probabilité: {attaque.effet_proba}%")

        choix = int(input("Entrez le numéro de l'attaque : ")) - 1
        if 0 <= choix < len(self.pokemon.attaques):
            return self.pokemon.attaques[choix]
        else:
            print("Choix invalide. Réessayez.")
            return self.choisir_attaque()
        
    def utiliser_potion(self, cible, potion_choix):
        if potion_choix == 0 and self.potion >= 1:
            self.potion -= 1
            cible.BoitPotion(20)
            print(f"il vous reste {self.potion} Potions")
        elif potion_choix == 1 and self.superpotion >= 1:
            self.superpotion -= 1
            cible.BoitPotion(50)
            print(f"il vous reste {self.superpotion} Super Potions")
        elif potion_choix == 2 and self.potionmax >= 1:
            self.potionmax -= 1
            cible.BoitPotionMax()
            print(f"il vous reste {self.potionmax} Potions Max")
        else:
            print("Type de potion invalide.")
            self.utiliser_potion(cible, potion_choix)

def battle_loop(all_pokemon, joueur = None):
    current_turn = 1
    healed_pokemon = []
    all_pokemon.sort(key=lambda x: x.vitesse, reverse=True)
    player_turn = all_pokemon.index(joueur.pokemon) + 1

    def all_pokemon_fainted():
        alive_pokemon = [pokemon for pokemon in all_pokemon if pokemon.est_vivant()]
        return len(alive_pokemon) == 1

    while True:
        print("\n")
        if current_turn == player_turn:
            if joueur.pokemon.pv > 0:
                # Tour du joueur
                print(f"Il vous reste {joueur.pokemon.pv}/{joueur.pokemon.pvmax} PV")
                choix_joueur = input("Choisissez une action pour votre Pokémon:\n1. Attaquer\n2. Utiliser une Potion\n3. Passer Son Tour\n4. Fuire : ")
                
                if choix_joueur == "1":
                    # Le joueur choisit d'attaquer
                    attaque_joueur = joueur.choisir_attaque()
                    print(f"Choisissez une cible pour l'attaque {attaque_joueur.nom}:")
                    
                    # Afficher les options de cibles
                    for i, pokemon in enumerate(all_pokemon):
                        if pokemon != joueur.pokemon and pokemon.est_vivant():
                            print(f"{i+1}. {pokemon.nom}")

                    # Demander au joueur de choisir la cible
                    choix_cible = int(input("Entrez le numéro de la cible: ")) - 1
                    print("\n")
                    if 0 <= choix_cible < len(all_pokemon) and all_pokemon[choix_cible].est_vivant() and all_pokemon[choix_cible] != joueur.pokemon:
                        adversaire = all_pokemon[choix_cible]
                        joueur.pokemon.Attaque(adversaire, attaque_joueur)
                        current_turn += 1
                    else:
                        print("Choix de cible invalide. L'attaque a échoué.")
                        current_turn += 1
            
                elif choix_joueur == "2":
                    # Le joueur choisit d'utiliser une potion
                    print(f"Choisissez une potion:\n0. Potion ({joueur.potion})\n1. Super Potion ({joueur.superpotion})\n2. Potion Max ({joueur.potionmax})\n")
                    choix_potion = int(input("Entrez le numéro de la potion: "))
                    joueur.utiliser_potion(joueur.pokemon,choix_potion)
                    current_turn += 1
                
                elif choix_joueur == "3":
                    # Le joueur choisit de skipper le tour
                    print("Vous avez passé votre tour.")
                    current_turn += 1

                elif choix_joueur == "4":
                    # Le joueur choisit de quitter le combat
                    print("Vous avez fuit le combat.")
                    break
            else:
                current_turn += 1

        else:   
            current_pokemon = all_pokemon[current_turn-1]

            if current_pokemon.est_vivant() and current_pokemon != joueur.pokemon:
                # Variable pour suivre si un changement significatif s'est produit

                # Trouver une cible Pokémon vivante aléatoire
                if current_pokemon not in healed_pokemon and current_pokemon.pv < current_pokemon.pvmax - 10 and random.randint(1, 5) == 1:
                    # Le Pokémon a une chance de 1 sur 5 de se soigner de 10 PV
                    if random.randint(1, 10) == 1:
                        # Le Pokémon a une chance de 1 sur 10 d'utiliser une potion max
                        current_pokemon.BoitPotionMax()
                        healed_pokemon.append(current_pokemon)
                    current_pokemon.BoitPotion(10)
                    healed_pokemon.append(current_pokemon)
                else:
                    available_targets = [pokemon for pokemon in all_pokemon if pokemon.est_vivant() and pokemon != current_pokemon]
                    if available_targets:
                        target = random.choice(available_targets)
                        current_pokemon.Attaque(target,current_pokemon.choisir_attaque())

            current_turn = (current_turn + 1) % len(all_pokemon)

            if all_pokemon_fainted() or current_turn > 10000:
                pygame.mixer.music.stop()
                print("Le combat est terminé.")
                break

    winner = [pokemon for pokemon in all_pokemon if pokemon.est_vivant()]
    if winner and len(winner) == 1:
        print(f"Le Pokémon gagnant est : {winner[0].nom}")
        if winner[0] == joueur.pokemon:
            print("\033[93mVous avez gagné le combat !\033[0m")
        else:
            print("\033[91mVous avez perdu le combat !\033[0m")
    else:
        print("Il n'y a pas de Pokémon gagnant.")

def choisir_pokemon():
    print("Choisissez un Pokémon parmi les suivants :")
    for i, pokemon in enumerate(all_pokemon):
        print(f"{i + 1}. {pokemon.nom}")

    choix = None
    while choix is None:
        try:
            choix = int(input("Entrez le numéro du Pokémon que vous souhaitez : ")) - 1
            if choix < 0 or choix >= len(all_pokemon):
                print("Numéro de Pokémon invalide. Réessayez.")
                choix = None
        except ValueError:
            print("Veuillez entrer un numéro valide.")

    pokemon_joueur = all_pokemon[choix]
    print(f"Vous avez choisi {pokemon_joueur.nom} !")

    return pokemon_joueur

def nombre_adversaires():
    global all_pokemon
    print(f"Definir le nombre de Pokemons:")
    choix = int(input(f"Choisir un nombre entre 3 et {len(all_pokemon)}: "))
    if choix >= 3:
        for i in range (0,len(all_pokemon) - choix):
            pkm = random.choice(all_pokemon)
            all_pokemon.remove(pkm)
    else:
        print("choix invalide.")
        nombre_adversaires()


def musique():
    if input("Voulez-vous lancer une musique ? (o/n) ") == "o":
        pygame.mixer.music.play(-1)

if __name__ == '__main__':
    # Création des pokemons et ajout dans la liste
    print("\033[93mBienvenue !\033[0m")
    pokemon_order = []
    all_pokemon = pkms.all_pokemon
    nombre_adversaires()
    a = len(all_pokemon)+1
    player = Joueur(choisir_pokemon())
    all_pokemon.sort(key=lambda x: x.vitesse, reverse=True)
    musique()
    battle_loop(all_pokemon,player)
        
    ##########################
    # a essayer hors du site #
    #   Pour des raisons de  #
    #        Couleurs        #
    # et de Choix d'attaques #
    ##########################