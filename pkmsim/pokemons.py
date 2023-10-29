# pokemons.py
import pokemon_Att_Repertory as att
import random
import pygame
class Pokemon:
    def __init__(self, nom, pvmax, Att, Vitesse,Def, Type):
        """
        Init a Pokemon with its name, hp, attack, defense, speed and type.

        Args:
            nom (str): Pokemon's name.
            pvmax (int): Pokemon's max hp.
            Att (int) : Pokemon's attack.
            Vitesse (int): Pokemon's speed.
            Def (int): Pokemon's defense.
            Type (str): Pokemon's type(Max one).
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
        self.statut = None

    def generer_attaques_aleatoires(self):
        # Select 4 random attacks from the list of attacks available for this type of Pokemon
        attaques_disponibles = attaques_par_type.get(self.type, [])
        if len(attaques_disponibles) < 4:
            raise Exception("Not enough attacks available for this type of Pokemon")
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
        
    def Learn_attack(self, attack):
        if len(self.attaques) < 4 and attack not in self.attaques:
            self.attaques.append(attack)
            print(f"{self.nom} has learned {attack.nom}!")
        else:
            print(f"{self.nom} can't learn {attack.nom}!")
    
    def Est_vivant(self):
        """
        Check if the Pokemon is alive.

        Returns:
            bool: True if the Pokemon is alive, False otherwise.
        """
        if self.pv > 0:
            return True
        return False
    
    def BoitPotion(self, gain):
        """
        Make the Pokemon drink a potion to restore its HP.

        Args:
            gain (int): The number of HP restored by the potion.

        Returns:
            int: The Pokemon's current HP after the restoration.
        """
        print(f"\x1b[32m{self.nom} drinks a potion and restores {gain} HP.\x1b[0m")
        if self.pv + gain > self.pvmax:
            self.pv = self.pvmax
        else:
            self.pv += gain
        print(f"{self.nom} has \x1b[32m{self.pv} HP\x1b[0m.")
        return self.pv
    
    def Choisir_attaque(self):
        attaque = random.choice(self.attaques)
        return attaque

    def BoitPotionMax(self):
        """
        Make the Pokemon drink a max potion to restore its HP to the max.

        Returns:
            int: The Pokemon's current HP after the restoration.
        """
        print(f" \x1b[34m {self.nom} drinks a max potion and restores all its HP.\x1b[0m")
        self.pv = self.pvmax
        print(f"{self.nom} a \x1b[34m{self.pv} PV\x1b[0m")
        return self.pv

    def Typing(self, cible) -> int:
        """
        Calculating the effectiveness of an attack.

        Args:
            cible (Pokemon): The Pokemon that is attacked.

        Returns:
            int: The effectiveness of the attack.
        """
        if self.type in self.TYPE_EFFECTIVENESS:
            if cible.type in self.TYPE_EFFECTIVENESS[self.type]:
                return self.TYPE_EFFECTIVENESS[self.type][cible.type]
        return 1
                
    def Attaque(self, cible, attaque):
        global place
        global pokemon_order
        if self.statut == "abri":
            self.abri = False
            print(f"{self.nom}'s protection has disappeared!")
        if self.statut != "asleep":
            if self.statut != "frozen":

                if self.statut == "confused":
                    print(f"{self.nom} is confused...")
                    p = random.randint(0, 100)
                    if p <= 50:
                        print(f"{self.nom} attacks itself!")
                        self.pv -= self.pvmax // 8
                        print(f"{self.nom} loses \x1b[31m{self.pvmax // 8} HP\x1b[0m.")
                        return
                if self.statut == "paralyzed":
                    print(f"{self.nom} is paralyzed...")
                    p = random.randint(0, 100)
                    if p <= 25:
                        print(f"{self.nom} can't attack!")
                        return
                print(f"{self.nom} attacks {cible.nom} with {attaque.nom}!")
                if random.randint(0,100) <= attaque.precision:
                    efficacite = self.Typing(cible)
                    degats = attaque.calculer_degats(self, cible, efficacite)

                    if cible.statut == "abri":
                        cible.statut = False
                        print(f"{cible.nom} used its protection and avoided the attack!")
                        degats = 0
                        efficacite = 1

                    if efficacite > 1:
                        efficacite_message = "\x1b[32mIt's super effective!\x1b[0m"
                    elif efficacite < 1 and efficacite > 0:
                        efficacite_message = "\x1b[mIt's not very effective...\x1b[0m"
                    elif efficacite == 0:
                        efficacite_message = f"\x1b[31mIt doesn't affect {cible.nom}...\x1b[0m"
                    else:
                        efficacite_message = ""

                    print(f"{efficacite_message} {self.nom} deals \x1b[31m{degats} HP\x1b[0m to {cible.nom}.")

                    cible.pv -= degats

                    # Applies the effect of the attack

                    if attaque.effet:
                        # Checks if the effect is triggered
                        
                        a = random.randint(0, 100)
                        if a <= attaque.effet_proba:
                            if cible.statut == None:

                                # Negatives

                                if attaque.effet == "paralyse":
                                    cible.statut = "paralyzed"
                                    #print "a" in yellow
                                    print(f"\x1b[33m{cible.nom} is paralyzed!\x1b[0m")
                                
                                elif attaque.effet == "burn":
                                    cible.statut = "burned"
                                    print(f"\x1b[31m{cible.nom} is burned!\x1b[0m")
                                
                                elif attaque.effet == "poison":
                                    cible.statut = "poisoned"
                                    print(f"\x1b[35m{cible.nom} is poisoned!\x1b[0m")
                                
                                elif attaque.effet == "sleep":
                                    cible.statut = "asleep"
                                    print(f"\x1b[34m{cible.nom} is asleep!\x1b[0m")
                                
                                elif attaque.effet == "confus":
                                    cible.statut = "confused"
                                    print(f"\x1b[33m{cible.nom} is confused!\x1b[0m")

                                elif attaque.effet == "maudis":
                                    cible.statut = "cursed"
                                    print(f"\x1b[31m{cible.nom} is cursed!\x1b[0m")

                                elif attaque.effet == "freeze":
                                    cible.statut = "frozen"
                                    print(f"\x1b[36m{cible.nom} is frozen!\x1b[0m")
                            
                            if attaque.effet == "onehit":
                                cible.pv = 0
                                print(f"{cible.nom} is knocked out in one hit!")

                            # Positif

                            elif attaque.effet == "heal":
                                self.pv = self.pvmax
                                print(f"{self.nom} is healed!")

                            elif attaque.effet == "abri":
                                self.effet = "abri"
                                print(f"{self.nom} protects itself!")

                            # Stats +

                            elif attaque.effet == "attaque+":
                                self.attaque += 10
                                print(f"{self.nom}'s attack has increased!")
                                print(self.attaque)
                            
                            elif attaque.effet == "vitesse+":
                                self.vitesse += 3
                                print(f"{self.nom}'s speed has increased!")
                                all_pokemon.sort(key=lambda x: x.vitesse, reverse=True)

                            elif attaque.effet == "defense+":
                                self.defense += 10
                                print(f"{self.nom}'s defense has increased!")

                            # Stats -

                            elif attaque.effet == "attaque-":
                                cible.attaque -= 10
                                print(f"{cible.nom}'s attack has decreased!")

                            elif attaque.effet == "vitesse-":
                                cible.vitesse -= 3
                                print(f"{cible.nom}'s speed has decreased!")
                                all_pokemon.sort(key=lambda x: x.vitesse, reverse=True)

                            elif attaque.effet == "defense-":
                                cible.defense -= 10
                                print(f"{cible.nom}'s defense has decreased!")
        
            else:
                print("The attack missed!")

        if self.statut == "burned":
            self.pv -= self.pvmax // 8
            print(f"{self.nom} is burned! It loses \x1b[31m{self.pvmax // 8} HP\x1b[0m.")
            if random.randint(0, 100) <= 25:
                self.statut = None
                print(f"{self.nom} is no longer burned!")

        if self.statut == "poisoned":
            self.pv -= self.pvmax // 8
            print(f"{self.nom} is poisoned! It loses \x1b[31m{self.pvmax // 8} HP\x1b[0m.")
            if random.randint(0, 100) <= 25:
                self.poison = False
                self.statut = None
                print(f"{self.nom} is no longer poisoned!")

        if self.statut == "asleep":
            if random.randint(0, 100) <= 25:
                self.statut = None
                print(f"{self.nom} woke up!")
            else:
                print(f"{self.nom} is asleep and can't attack!")

        if self.statut == "frozen":
            if random.randint(0, 100) <= 25:
                self.statut = None
                print(f"{self.nom} is no longer frozen!")
            else:
                print(f"{self.nom} is frozen and can't attack!")

        if self.statut == "cursed":
            self.pv -= self.pvmax // 16
            print(f"{self.nom} is cursed! It loses \x1b[31m{self.pvmax // 16} HP\x1b[0m.")

        if self.statut:
        
            if self.pv <= 0:
                print(f"\x1b[31m{self.nom} is knocked out!\x1b[0m")
            else:
                print(f"{self.nom} have \x1b[31m{self.pv} HP\x1b[0m.")

        if cible.pv <= 0:
            print(f"\x1b[31m{cible.nom} is knocked out!\x1b[0m")
        else:
            print(f"{cible.nom} has \x1b[31m{cible.pv} HP left\x1b[0m.")
        
    def __add__(self, pvs):
        """
        adds the value of `pvs` to the current `pv` attribute.
        
        takes:
            pvs (int): the value to add to `pv`.
        
        Returns :
            None
        """
        self.pv += pvs
        
    def __sub__(self, pvs):
        """
        subtracts the value of `pvs` to the current `pv` attribute.
        
        takes :
            pvs (int) : the value to subtract to `pv`.
        
        Returns :
            None
        """
        self.pv -= pvs
        if self.pv <= 0:
            self.pv = 0

def play_music(i=0):
    choix = input("Do you want to play music? (y/n) ")
    if choix == "y":
        pygame.mixer.music.play(-1)
    elif choix == "maybe":
        print("You're not very decisive, are you?")
        play_music(i+1)
    elif choix == "secret":
        print("You found a secret! You can now choose the music you want to play!")
        choix = input("Enter the path of the music you want to play: ")
        pygame.mixer.music.load(choix)
    elif choix == "n":
        print("You're no fun...")
    elif choix == "yes":
        print("You found a secret music!")
        pygame.mixer.music.load("assets\\theme\\battle_theme_alt.mp3")
        play_music(i+1)
    elif i == 10:
        print("are you really gonna keep trying?")
        play_music(i+1)
    elif i == 20:
        print("You're really stubborn, aren't you?")
        play_music(i+1)
    elif i == 30:
        print("You're not gonna give up, are you?")
        play_music(i+1)
    elif i == 40:
        print("You're really persistent...")
        play_music(i+1)
    elif i == 50:
        print("just play the game already...")
        play_music(i+1)
    elif i == 60:
        print("You're really annoying...")
        print("I'm gonna stop you right there")
        exit()
    else:
        print("invalid choice. Try again.")
        play_music(i+1)

attaques_par_type = {
    "electrique": att.electric_attaques,
    "feu": att.fire_attaques,
    "eau": att.water_attaques,
    "plante": att.grass_attaques,
    "normal": att.normal_attaques,
    "glace": att.ice_attaques,
    "combat": att.fighting_attaques,
    "poison": att.poison_attaques,
    "sol": att.ground_attaques,
    "vol": att.flying_attaques,
    "psy": att.psychic_attaques,
    "insecte": att.bug_attaques,
    "roche": att.rock_attaques,
    "spectre": att.ghost_attaques,
    "tenebres": att.dark_attaques,
    "dragon": att.dragon_attaques,
    "acier": att.steel_attaques,
    "fee": att.fairy_attaques,
}

Pikachu = Pokemon('Pikachu', 70, 30, 90, 40, 'electrique')
Carapuce = Pokemon('Carapuce', 50, 25, 43, 45, 'eau')
Salameche = Pokemon('Salameche', 65, 25, 65, 43, 'feu')
Bulbizarre = Pokemon('Bulbizarre', 50, 31, 45, 40, 'plante')
Chuchmur = Pokemon('Chuchmur', 60, 19, 64, 45, 'normal')
Obalie = Pokemon('Obalie', 70, 28, 25, 40, 'glace')
Meditikka = Pokemon('Meditikka', 60, 24, 60, 30, 'combat')
Papinox = Pokemon('Papinox', 85, 15, 65, 65, 'poison')
Chamallot = Pokemon('Chamallot', 60, 25, 35, 35, 'sol')
Tylton = Pokemon('Tylton', 70, 15, 50, 40, 'vol')
Tarsal = Pokemon('Tarsal', 45, 39, 40, 35, 'psy')
Munja = Pokemon('Munja', 1, 50, 56, 30, 'insecte')
Relicanth = Pokemon('Relicanth', 65, 25, 55, 35, 'roche')
Tenefix = Pokemon('Tenefix', 40, 25, 50, 35, 'spectre')
Draby = Pokemon('Draby', 65, 24, 50, 45, 'dragon')
Medhyena = Pokemon('Medhyena', 30, 28, 35, 30, 'tenebres')
Terhal = Pokemon('Terhal', 20, 23, 30, 35, 'acier')
Azurill = Pokemon('Azurill', 30, 30, 25, 20, 'fee')
Groudon = Pokemon('Groudon', 70, 40, 90, 90, 'sol')
Raichu = Pokemon('Raichu', 60, 40, 110, 35, 'electrique')
Tortank = Pokemon('Tortank', 75, 40, 78, 100, 'eau')
Dracaufeu = Pokemon('Dracaufeu', 78, 40, 100, 85, 'feu')
Florizarre = Pokemon('Florizarre', 80, 35, 70, 83, 'plante')
Ronflex = Pokemon('Ronflex', 160, 50, 30, 65, 'normal')
Lokhlass = Pokemon('Lokhlass', 130, 45, 60, 70, 'glace')
Mackogneur = Pokemon('Mackogneur', 90, 80, 45, 65, 'combat')
Nidoking = Pokemon('Nidoking', 81, 47, 85, 77, 'poison')
Rhinoferos = Pokemon('Rhinoferos', 80, 45, 40, 95, 'sol')
Ptera = Pokemon('Ptera', 80, 61, 110, 45, 'vol')
Alakazam = Pokemon('Alakazam', 55, 50, 120, 45, 'psy')
Sarmuraï = Pokemon('Sarmuraï', 70, 85, 60, 100, 'eau')
Tyranocif = Pokemon('Tyranocif', 100, 70, 61, 110, 'roche')
Metamorph = Pokemon('Metamorph', 48, 48, 48, 48, 'normal')
Flagadoss = Pokemon('Flagadoss', 95, 45, 30, 55, 'psy')
Leuphorie = Pokemon('Leuphorie', 250, 10, 55, 10, 'fee')
Rayquaza = Pokemon('Rayquaza', 105, 70, 95, 90, 'dragon')
Noctali = Pokemon('Noctali', 95, 65, 65, 110, 'tenebres')
Registeel = Pokemon('Registeel', 80, 75, 50, 150, 'acier')
Magicarpe = Pokemon('Magicarpe', 20, 10, 80, 55, 'eau')
Aquali = Pokemon('Aquali', 130, 65, 65, 60, 'eau')
Mew = Pokemon('Mew', 100, 100, 100, 100, 'psy')
Raikou = Pokemon('Raikou', 90, 85, 115, 75, 'electrique')
Artikodin = Pokemon('Artikodin', 90, 85, 85, 100, 'glace')
Sulfura = Pokemon('Sulfura', 90, 85, 85, 75, 'feu')
all_pokemon = [Pikachu, Carapuce, Salameche, Bulbizarre, Chuchmur, Obalie, Meditikka, Papinox, Chamallot, Tylton, Tarsal, Munja, Relicanth,
                Tenefix, Draby, Medhyena, Terhal, Azurill, Groudon, Raichu, Tortank, Dracaufeu, Florizarre, Ronflex, Lokhlass, Mackogneur,
                  Nidoking, Rhinoferos, Ptera, Alakazam, Sarmuraï, Tyranocif, Metamorph, Flagadoss, Leuphorie, Rayquaza, Noctali, Registeel,
                    Magicarpe, Aquali, Mew, Raikou, Artikodin, Sulfura ]
