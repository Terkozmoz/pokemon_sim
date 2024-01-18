# pkm-old.py
# The very first version, kinda. Kept here as a souvenir.
# Yeah, it's a mess, but it's my mess.
# Plus it's a good example of how much I've improved since then, how much I've learned, and how much I've grown.
# That's crazy how much it changed in just a few months.... And i hope it will keep changing for the better.
# When i think about it, it's been a long time since i've started this project. I've learned so much since then... Welp, i guess you're here to see the code, not to read my life story. ^^'
# I had to use another version of 'Attaque', because i didn't keep the old one. I'm sorry for that. ### UPDATE ### Found the original one and put it back where it belongs.
# Also, it's in french, cause i'm french. Didn't want to translate it, to keep it as it was. (so just use google translate if you want to understand it (or learn french :p (or don't, it's a hard language (too many parenthesis (agreed.))))))

import random

class Attaque:
    def __init__(self, nom, puissance, precision, type):
        self.nom = nom
        self.puissance = puissance
        self.precision = precision
        self.type = type

    def calculer_degats(self, attaquant, defenseur, efficacite):
        # Formule de calcul des dégâts sans considération du niveau
        A = attaquant.attaque
        D = defenseur.defense
        P = self.puissance
        E = efficacite
        degats = int(int((((100+A+(15*50))*P)/(D+50)))/20)*E
        return int(degats)

impasses = 0
# Attaques pour le type "Electrique"
electric_attaques = [
    Attaque("Thunderbolt", 90, 100, "electrique"),
    Attaque("Thunder Shock", 40, 100, "electrique"),
    Attaque("Spark", 65, 100, "electrique"),
    Attaque("Thunder Wave", 1, 90, "electrique"),
]

# Attaques pour le type "Feu"
fire_attaques = [
    Attaque("Flamethrower", 90, 100, "feu"),
    Attaque("Ember", 40, 100, "feu"),
    Attaque("Fire Blast", 110, 85, "feu"),
    Attaque("Fire Spin", 35, 85, "feu"),
]

# Attaques pour le type "Eau"
water_attaques = [
    Attaque("Surf", 90, 100, "eau"),
    Attaque("Water Gun", 40, 100, "eau"),
    Attaque("Hydro Pump", 110, 80, "eau"),
    Attaque("Bubble", 20, 100, "eau"),
]

# Attaques pour le type "Plante"
grass_attaques = [
    Attaque("Solar Beam", 120, 100, "plante"),
    Attaque("Razor Leaf", 55, 95, "plante"),
    Attaque("Vine Whip", 45, 100, "plante"),
    Attaque("Bullet Seed", 25, 100, "plante"),
]

# Attaques pour le type "Normal"
normal_attaques = [
    Attaque("Tackle", 40, 100, "normal"),
    Attaque("Quick Attack", 40, 100, "normal"),
    Attaque("Hyper Beam", 150, 90, "normal"),
    Attaque("Scratch", 40, 100, "normal"),
]

# Attaques pour le type "Glace"
ice_attaques = [
    Attaque("Ice Beam", 90, 100, "glace"),
    Attaque("Aurora Beam", 65, 100, "glace"),
    Attaque("Blizzard", 110, 70, "glace"),
    Attaque("Icy Wind", 55, 95, "glace"),
]

# Attaques pour le type "Combat"
fighting_attaques = [
    Attaque("Karate Chop", 50, 100, "combat"),
    Attaque("Dynamic Punch", 100, 50, "combat"),
    Attaque("Cross Chop", 100, 80, "combat"),
    Attaque("Mach Punch", 40, 100, "combat"),
]

# Attaques pour le type "Poison"
poison_attaques = [
    Attaque("Sludge Bomb", 90, 100, "poison"),
    Attaque("Toxic", 1, 85, "poison"),
    Attaque("Poison Jab", 80, 100, "poison"),
    Attaque("Smog", 20, 70, "poison"),
]

# Attaques pour le type "Sol"
ground_attaques = [
    Attaque("Earthquake", 100, 100, "sol"),
    Attaque("Dig", 80, 100, "sol"),
    Attaque("Mud-Slap", 20, 100, "sol"),
    Attaque("Fissure", 1, 30, "sol"),
]

# Attaques pour le type "Vol"
flying_attaques = [
    Attaque("Aerial Ace", 60, 100, "vol"),
    Attaque("Fly", 90, 95, "vol"),
    Attaque("Hurricane", 110, 70, "vol"),
    Attaque("Peck", 35, 100, "vol"),
]

# Attaques pour le type "Psy"
psychic_attaques = [
    Attaque("Psychic", 90, 100, "psy"),
    Attaque("Confusion", 50, 100, "psy"),
    Attaque("Psybeam", 65, 100, "psy"),
    Attaque("Hypnosis", 1, 60, "psy"),
]

# Attaques pour le type "Insecte"
bug_attaques = [
    Attaque("Bug Buzz", 90, 100, "insecte"),
    Attaque("Pin Missile", 25, 95, "insecte"),
    Attaque("X-Scissor", 80, 100, "insecte"),
    Attaque("String Shot", 1, 95, "insecte"),
]

# Attaques pour le type "Roche"
rock_attaques = [
    Attaque("Rock Slide", 75, 90, "roche"),
    Attaque("Stone Edge", 100, 80, "roche"),
    Attaque("Rock Throw", 50, 90, "roche"),
    Attaque("Rock Polish", 1, 100, "roche"),
]

# Attaques pour le type "Spectre"
ghost_attaques = [
    Attaque("Shadow Ball", 80, 100, "spectre"),
    Attaque("Night Shade", 1, 100, "spectre"),
    Attaque("Curse", 1, 100, "spectre"),
    Attaque("Lick", 20, 100, "spectre"),
]

# Attaques pour le type "Ténèbres"
dark_attaques = [
    Attaque("Dark Pulse", 80, 100, "tenebres"),
    Attaque("Pursuit", 40, 100, "tenebres"),
    Attaque("Foul Play", 95, 100, "tenebres"),
    Attaque("Thief", 60, 100, "tenebres"),
]

# Attaques pour le type "Dragon"
dragon_attaques = [
    Attaque("Dragon Claw", 80, 100, "dragon"),
    Attaque("Dragon Rage", 40, 100, "dragon"),
    Attaque("Outrage", 120, 100, "dragon"),
    Attaque("Dragon Breath", 60, 100, "dragon"),
]

# Attaques pour le type "Acier"
steel_attaques = [
    Attaque("Iron Tail", 100, 75, "acier"),
    Attaque("Metal Claw", 50, 95, "acier"),
    Attaque("Flash Cannon", 80, 100, "acier"),
    Attaque("Iron Head", 80, 100, "acier"),
]

# Attaques pour le type "Fee"
fairy_attaques = [
    Attaque("Moonblast", 95, 100, "fee"),
    Attaque("Dazzling Gleam", 80, 100, "fee"),
    Attaque("Play Rough", 90, 90, "fee"),
    Attaque("Draining Kiss", 50, 100, "fee"),
]
class Pokemon:
    def __init__(self, nom, pv, pvmax, Att, Vitesse,Def, Type):
        """
        Initialise un Pokémon avec des attributs de base.

        Args:
            nom (str): Le nom du Pokémon.
            pv (int): Les points de vie actuels du Pokémon.
            pvmax (int): Les points de vie maximum du Pokémon.
            Att (int) : L'attaque du Pokémon
            Vitesse (int): La vitesse du Pokémon.
            Def (int): La defense duokemon.
            Type (str): Le type du Pokémon.
        """
        self.nom = nom
        self.base = pvmax
        self.attaque = Att
        self.defense = Def
        self.vitesse = Vitesse
        self.type = Type
        self.pv = self.calculate_hp()
        self.pvmax = self.pv
        self.attaques = self.generer_attaques_aleatoires()

    def generer_attaques_aleatoires(self):
        # Sélectionner 4 attaques aléatoires parmi les attaques du type du Pokémon
        attaques_disponibles = attaques_par_type.get(self.type, [])
        if len(attaques_disponibles) < 4:
            raise Exception("Pas assez d'attaques disponibles pour ce type de Pokémon.")
        return random.sample(attaques_disponibles, 4)

    def calculate_hp(self):
        if self.nom != 'Munja':
            return int(0.01 * (2 * self.base) * 50 + 50 + 10)
        return self.base
    
    TYPE_EFFECTIVENESS = {
        'electrique': {'eau': 2, 'vol': 2, 'plante': 0.5, 'dragon': 0.5, 'sol': 0},
        'feu': {'plante': 2, 'insecte': 2, 'acier': 2, 'glace': 2, 'eau': 0.5, 'roche': 0.5, 'dragon': 0.5},
        'eau': {'feu': 2, 'roche': 2, 'sol': 2, 'plante': 0.5, 'dragon': 0.5},
        'plante': {'eau': 2, 'sol': 2, 'roche': 2, 'feu': 0.5, 'poison': 0.5, 'vol': 0.5, 'insecte': 0.5, 'dragon': 0.5, 'acier': 0.5},
        'normal': {'spectre': 0, 'roche': 0.5, 'acier': 0.5},
        'glace': {'plante': 2, 'sol': 2, 'vol': 2, 'dragon': 2, 'feu': 0.5, 'eau': 0.5, 'acier': 0.5},
        'combat': {'normal': 2, 'glace': 2, 'roche': 2, 'acier': 2, 'tenebres': 2, 'poison': 0.5, 'vol': 0.5, 'psy': 0.5, 'insecte': 0.5, 'fee': 0.5, 'spectre': 0},
        'poison': {'plante': 2, 'fee': 2, 'sol': 0.5, 'roche': 0.5, 'spectre': 0.5, 'acier': 0},
        'sol': {'feu': 2, 'electrique': 2, 'poison': 2, 'roche': 2, 'acier': 2, 'plante': 0.5, 'insecte': 0.5, 'vol': 0},
        'vol': {'plante': 2, 'combat': 2, 'insecte': 2, 'electrique': 0.5, 'roche': 0.5, 'acier': 0.5},
        'psy': {'combat': 2, 'poison': 2, 'acier': 0.5, 'tenebres': 0, 'spectre': 2},
        'insecte': {'insecte': 2, 'psy': 2, 'tenebres': 2, 'feu': 0.5, 'combat': 0.5, 'poison': 0.5, 'vol': 0.5, 'spectre': 0.5, 'acier': 0.5, 'fee': 0.5},
        'roche': {'feu': 2, 'glace': 2, 'vol': 2, 'insecte': 2, 'combat': 0.5, 'sol': 0.5, 'acier': 0.5},
        'spectre': {'psy': 2, 'tenebres': 0.5, 'normal': 0},
        'dragon': {'dragon': 2, 'acier': 0.5, 'fee': 0},
        'tenebres': {'psy': 2, 'spectre': 0.5, 'combat': 0.5, 'fee': 0.5},
        'acier': {'glace': 2, 'roche': 2, 'fee': 2, 'feu': 0.5, 'eau': 0.5, 'electrique': 0.5},
        'fee': {'combat': 2, 'dragon': 2, 'tenebres': 0.5, 'feu': 0.5, 'poison': 0.5, 'acier': 0.5}
    }
        
    def learn_attack(self, attack):
        if len(self.attaques) < 4 and attack not in self.attaques:
            self.attaques.append(attack)
            print(f"{self.nom} a appris {attack.nom}")
        else:
            print(f"{self.nom} ne peux pas apprendre {attack.nom}")
    
    def est_vivant(self):
        """
        Vérifie si le Pokémon est en vie.

        Returns:
            bool: True si le Pokémon a des PV restants, False sinon.
        """
        if self.pv > 0:
            return True
        return False
    
    def BoitPotion(self, gain):
        """
        Fait boire une potion au Pokémon pour restaurer ses PV.

        Args:
            gain (int): Le nombre de PV restaurés.

        Returns:
            int: Le nombre de PV actuels du Pokémon après la restauration.
        """
        print(f"x1b[32m{self.nom} boit une potion de {gain} PVx1b[0m")
        if self.pv + gain > self.pvmax:
            self.pv = self.pvmax
        else:
            self.pv += gain
        print(f"{self.nom} a x1b[34m{self.pv} PVx1b[0m")
        return self.pv
    
    def choisir_attaque(self):
        attaque = random.choice(self.attaques)
        return attaque

    def BoitPotionMax(self):
        """
        Fait boire une potion max au Pokémon pour le soigner complètement.

        Returns:
            int: Le nombre de PV actuels du Pokémon après la restauration.
        """
        print(f" x1b[34m {self.nom} boit une potion max et est complètement soigné! x1b[0m")
        self.pv = self.pvmax
        print(f"{self.nom} a x1b[34m{self.pv} PVx1b[0m")
        return self.pv

    def Typing(self, cible) -> int:
        """
        Calcule l'efficacité d'une attaque en fonction des types.

        Args:
            cible (Pokemon): Le Pokémon cible de l'attaque.

        Returns:
            int: Le facteur d'efficacité de l'attaque.
        """
        if self.type in self.TYPE_EFFECTIVENESS:
            if cible.type in self.TYPE_EFFECTIVENESS[self.type]:
                return self.TYPE_EFFECTIVENESS[self.type][cible.type]
        return 1
                
    def Attaque(self, cible, attaque):
        global a
        print(f"{self.nom} attaque {cible.nom} avec {attaque.nom}.")
        efficacite = self.Typing(cible)
        degats = attaque.calculer_degats(self, cible, efficacite)

        if efficacite > 1:
            efficacite_message = "x1b[32mC'est super efficace!x1b[0m"
        elif efficacite < 1 and efficacite > 0:
            efficacite_message = "x1b[mCe n'est pas très efficace...x1b[0m"
        elif efficacite == 0:
            efficacite_message = f"x1b[31mÇa n'affecte pas {cible.nom}.x1b[0m"
        else:
            efficacite_message = ""

        print(f"{efficacite_message} {self.nom} inflige x1b[31m{degats} x1b[0m dégâts à {cible.nom}.")

        # S'assurer que les PV de l'adversaire ne descendent pas en dessous de 0
        cible.pv = max(cible.pv - degats, 0)

        if cible.pv == 0:
            a -= 1
            print(f"x1b[31m{cible.nom} est KO.x1b[0m")
            ko_pkm = (a, cible.nom)
            pokemon_order.append(ko_pkm)
        else:
            print(f"Il reste x1b[m{cible.pv} PVx1b[0m à {cible.nom}.")
        
    def __add__(self, pvs):
        """
        Ajoute la valeur donnée à l'attribut `pv`.
        
        Paramètres:
            pvs (int): La valeur à ajouter à `pv`.
        
        Renvoie:
            Aucun
        """
        self.pv += pvs
        
    def __sub__(self, pvs):
        """
        Soustrait la valeur de `pvs` à l'attribut `pv` actuel.
        
        Paramètres :
            pvs (int) : La valeur à soustraire à `pv`.
        
        Renvoie :
            None
        """
        self.pv -= pvs

class Joueur:
    def __init__(self, pokemon):
        self.pokemon = pokemon

    def choisir_attaque(self):
        print("Choisissez une attaque :")
        for i, attaque in enumerate(self.pokemon.attaques):
            print(f"{i + 1}. {attaque.nom}")

        choix = int(input("Entrez le numéro de l'attaque : ")) - 1
        if 0 <= choix < len(self.pokemon.attaques):
            return self.pokemon.attaques[choix]
        else:
            print("Choix invalide. Réessayez.")
            return self.choisir_attaque()
        
    def utiliser_potion(self, cible, potion_choix):
        if potion_choix == 0:
            cible.BoitPotion(20)
        elif potion_choix == 1:
            cible.BoitPotion(50)
        elif potion_choix == 2:
            cible.BoitPotionMax()
        else:
            print("Type de potion invalide.")

attaques_par_type = {
    "electrique": electric_attaques,
    "feu": fire_attaques,
    "eau": water_attaques,
    "plante": grass_attaques,
    "normal": normal_attaques,
    "glace": ice_attaques,
    "combat": fighting_attaques,
    "poison": poison_attaques,
    "sol": ground_attaques,
    "vol": flying_attaques,
    "psy": psychic_attaques,
    "insecte": bug_attaques,
    "roche": rock_attaques,
    "spectre": ghost_attaques,
    "tenebres": dark_attaques,
    "dragon": dragon_attaques,
    "acier": steel_attaques,
    "fee": fairy_attaques,
}
def battle_loop(all_pokemon, joueur):
    global impasses
    current_turn = 0
    num_turns = 0  # Ajout d'un compteur de tours
    healed_pokemon = []

    def all_pokemon_fainted():
        alive_pokemon = [pokemon for pokemon in all_pokemon if pokemon.est_vivant()]
        return len(alive_pokemon) == 1

    while True:
        if current_turn == 0:
            if joueur.pokemon.pv > 0:
                # Tour du joueur
                print(f"Il vous reste {joueur.pokemon.pv}PV")
                choix_joueur = input("""Choisissez une action pour votre Pokémon:
1. Attaquer
2. Utiliser une Potion
""")
                
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
                    if 0 <= choix_cible < len(all_pokemon) and all_pokemon[choix_cible].est_vivant():
                        adversaire = all_pokemon[choix_cible]
                        joueur.pokemon.Attaque(adversaire, attaque_joueur)
                        current_turn += 1
                    else:
                        print("Choix de cible invalide. L'attaque a échoué.")
                        current_turn += 1
            
                elif choix_joueur == "2":
                    # Le joueur choisit d'utiliser une potion
                    print("""Choisissez une potion:
0. Potion
1. Super Potion
2. Potion Max
""")
                    choix_potion = int(input("Entrez le numéro de la potion: "))
                    joueur.utiliser_potion(joueur.pokemon,choix_potion)
                    current_turn += 1
            current_turn += 1

        else:   
            current_pokemon = all_pokemon[current_turn]

            if current_pokemon.est_vivant():
                # Variable pour suivre si un changement significatif s'est produit

                # Trouver une cible Pokémon vivante aléatoire
                if current_pokemon not in healed_pokemon and current_pokemon.pv < current_pokemon.pvmax - 10 and random.randint(1, 5) == 1:
                    # Le Pokémon a une chance de 1 sur 5 de se soigner de 10 PV
                    if current_pokemon not in healed_pokemon and current_pokemon.pv < current_pokemon.pvmax - 10 and random.randint(1, 10) == 1:
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
                    # Mettre à jour le compteur de tours
                    num_turns += 1

            current_turn = (current_turn + 1) % len(all_pokemon)

            if all_pokemon_fainted() or num_turns > 100:
                print("Le combat est terminé.")
                break

    winner = [pokemon for pokemon in all_pokemon if pokemon.est_vivant()]
    if winner and len(winner) == 1:
        print("Le Pokémon gagnant est :", winner[0].nom)
        ko_pkm = (1, winner[0].nom)
        pokemon_order.append(ko_pkm)
    else:
        global impasses
        impasses += 1
        print("Il n'y a pas de Pokémon gagnant.")
    print(pokemon_order)

def simulate_battles(all_pokemon, num_battles):
    """
    Simule une série de combats entre un groupe de Pokémon.

    Args:
        all_pokemon (list): Une liste d'objets Pokémon représentant tous les Pokémon participant aux combats.
        num_battles (int): Le nombre de combats à simuler.

    Returns:
        dict: Un dictionnaire faisant correspondre les noms des Pokémon au nombre de combats qu'ils ont remportés.
    """
    pokemon_wins = {pokemon.nom: 0 for pokemon in all_pokemon}
    global impasses
    
    for y in range(num_battles):
        global a
        global pokemon_order
        a = len(all_pokemon) + 1
        pokemon_order = []
        # S' assurer que les Pokémon sont remis à leur état initial pour chaque bataille
        for pokemon in all_pokemon:
            pokemon.pv = pokemon.pvmax
        
        # Re-trier Pokémon en fonction de leur vitesse pour chaque nouvelle bataille
        all_pokemon.sort(key=lambda x: x.vitesse, reverse=True)
        
        battle_loop(all_pokemon)
        
        winner = [pokemon for pokemon in all_pokemon if pokemon.est_vivant()]
        if len(winner) > 1:
            pass
        elif winner:
            pokemon_wins[winner[0].nom] += 1
    
    print(f"Nombre d'égalitées' : {impasses}")
    return pokemon_wins

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

if __name__ == '__main__':
    # Création des pokemons et ajout dans la liste
    Pikachu = Pokemon('Pikachu', 70, 70, 30, 90, 40, 'electrique')
    Carapuce = Pokemon('Carapuce', 50, 50, 25, 43, 45, 'eau')
    Salameche = Pokemon('Salameche', 65, 65, 25, 65, 43, 'feu')
    Bulbizarre = Pokemon('Bulbizarre', 50, 50, 31, 45, 40, 'plante')
    Chuchmur = Pokemon('Chuchmur', 60, 60, 19, 64, 45, 'normal')
    Obalie = Pokemon('Obalie', 70, 70, 28, 25, 40, 'glace')
    Meditikka = Pokemon('Meditikka', 60, 60, 24, 60, 30, 'combat')
    Papinox = Pokemon('Papinox', 85, 85, 15, 65, 65, 'poison')
    Chamallot = Pokemon('Chamallot', 60, 60, 25, 35, 35, 'sol')
    Tylton = Pokemon('Tylton', 70, 70, 15, 50, 40, 'vol')
    Tarsal = Pokemon('Tarsal', 45, 45, 39, 40, 35, 'psy')
    Munja = Pokemon('Munja', 1, 1, 50, 56, 30, 'insecte')
    Relicanth = Pokemon('Relicanth', 65, 65, 25, 55, 35, 'roche')
    Tenefix = Pokemon('Tenefix', 40, 40, 25, 50, 35, 'spectre')
    Draby = Pokemon('Draby', 65, 65, 24, 50, 45, 'dragon')
    Medhyena = Pokemon('Medhyena', 30, 30, 28, 35, 30, 'tenebres')
    Terhal = Pokemon('Terhal', 20, 20, 23, 30, 35, 'acier')
    Azurill = Pokemon('Azurill', 30, 30, 30, 25, 20, 'fee')
    Groudon = Pokemon('Groudon', 70, 70, 40, 90, 90, 'sol')

    pokemon_order = []
    all_pokemon = [Pikachu, Carapuce, Salameche, Bulbizarre, Chuchmur, Obalie, Meditikka, Papinox,
                   Chamallot, Tylton, Tarsal, Munja, Relicanth, Tenefix, Draby, Medhyena, Terhal, Azurill, Groudon ]
    all_pokemon.sort(key=lambda x: x.vitesse, reverse=True)
    a = len(all_pokemon)+1
    player = Joueur(choisir_pokemon())
    battle_loop(all_pokemon,player)

    '''
    num_battles = 1000  # nombre de batailles à simuler
    wins = simulate_battles(all_pokemon, num_battles)

    for pokemon, num_wins in wins.items():
        print(f"{pokemon} a remporté {num_wins} victoires sur {num_battles} batailles.")
    '''
        
    ##########################
    # a essayer hors du site #
    #   Pour des raisons de  #
    #        Couleurs        #
    # et de Choix d'attaques #
    ##########################