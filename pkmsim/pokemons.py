# pokemons.py
import pokemon_Att_Repertory as att
import random
import pygame

class Pokemon:
    def __init__(self, name, max_hp, Att, speed,Def, Type, Type2=None):
        """
        Init a Pokemon with its name, hp, attack, defense, speed and type.

        Args:
            name (str): Pokemon's name.
            max_hp (int): Pokemon's max hp.
            Att (int) : Pokemon's attack.
            speed (int): Pokemon's speed.
            Def (int): Pokemon's defense.
            Type (str): Pokemon's type(One or Two).
        """
        self.name = name
        self.base = max_hp
        self.attack = Att
        self.defense = Def
        self.speed = speed
        self.type = Type
        self.type2 = Type2
        self.hp = self.calculate_hp()
        self.max_hp = self.hp
        self.attacks = self.random_attacks()
        self.status = None
        self.attack_pp = [0, 0, 0, 0]
        for i in range(len(self.attacks)):
            self.attack_pp[i] = self.attacks[i].pp

    def random_attacks(self):
        if self.type2 == None:
            # Select 4 random attacks from the list of attacks available for this type of Pokemon
            attacks_disponibles = attacks_by_type.get(self.type, [])
            if len(attacks_disponibles) < 4:
                raise Exception("Not enough attacks available for this type of Pokemon")
            return random.sample(attacks_disponibles, 4)
        else:
            # Select 4 random attacks from the list of attacks available for this type of Pokemon
            attacks_disponibles = attacks_by_type.get(self.type, []) + attacks_by_type.get(self.type2, [])
            if len(attacks_disponibles) < 4:
                raise Exception("Not enough attacks available for this type of Pokemon")
            return random.sample(attacks_disponibles, 4)

    def calculate_hp(self):
        if self.name != 'Munja':
            return int(0.01 * (2 * self.base) * 50 + 50 + 10)
        return self.base
    
    TYPE_EFFECTIVENESS = {
        'electric': {'water': 2, 'flying': 2, 'grass': 0.5, 'dragon': 0.5, 'ground': 0},
        'fire': {'grass': 2, 'insect': 2, 'steel': 2, 'ice': 2, 'water': 0.5, 'rock': 0.5, 'dragon': 0.5},
        'water': {'fire': 2, 'rock': 2, 'ground': 2, 'grass': 0.5, 'dragon': 0.5},
        'grass': {'water': 2, 'ground': 2, 'rock': 2, 'fire': 0.5, 'poison': 0.5, 'flying': 0.5, 'insect': 0.5, 'dragon': 0.5, 'steel': 0.5},
        'normal': {'ghost': 0, 'rock': 0.5, 'steel': 0.5},
        'ice': {'grass': 2, 'ground': 2, 'flying': 2, 'dragon': 2, 'fire': 0.5, 'water': 0.5, 'steel': 0.5},
        'fighting': {'normal': 2, 'ice': 2, 'rock': 2, 'steel': 2, 'dark': 2, 'poison': 0.5, 'flying': 0.5, 'psychic': 0.5, 'insect': 0.5, 'fairy': 0.5, 'ghost': 0},
        'poison': {'grass': 2, 'fairy': 2, 'ground': 0.5, 'rock': 0.5, 'ghost': 0.5, 'steel': 0},
        'ground': {'fire': 2, 'electric': 2, 'poison': 2, 'rock': 2, 'steel': 2, 'grass': 0.5, 'insect': 0.5, 'flying': 0},
        'flying': {'grass': 2, 'fighting': 2, 'insect': 2, 'electric': 0.5, 'rock': 0.5, 'steel': 0.5},
        'psychic': {'fighting': 2, 'poison': 2, 'steel': 0.5, 'dark': 0, 'ghost': 2},
        'insect': {'insect': 2, 'psychic': 2, 'dark': 2, 'fire': 0.5, 'fighting': 0.5, 'poison': 0.5, 'flying': 0.5, 'ghost': 0.5, 'steel': 0.5, 'fairy': 0.5},
        'rock': {'fire': 2, 'ice': 2, 'flying': 2, 'insect': 2, 'fighting': 0.5, 'ground': 0.5, 'steel': 0.5},
        'ghost': {'psychic': 2, 'dark': 0.5, 'normal': 0},
        'dragon': {'dragon': 2, 'steel': 0.5, 'fairy': 0},
        'dark': {'psychic': 2, 'ghost': 0.5, 'fighting': 0.5, 'fairy': 0.5},
        'steel': {'ice': 2, 'rock': 2, 'fairy': 2, 'fire': 0.5, 'water': 0.5, 'electric': 0.5},
        'fairy': {'fighting': 2, 'dragon': 2, 'dark': 0.5, 'fire': 0.5, 'poison': 0.5, 'steel': 0.5}
    }
        
    def Learn_attack(self, attack):
        if len(self.attacks) < 4 and attack not in self.attacks:
            self.attacks.append(attack)
            print(f"{self.name} has learned {attack.name}!")
        else:
            print(f"{self.name} can't learn {attack.name}!")

    def Learn_struggle(self):
        self.attacks.append(att.Struggle)
        self.attack_pp.append(-1)

    def Zero_pp(self):
        for attack in self.attacks:
            if self.attack_pp[self.attacks.index(attack)] != 0:
                return False
        self.Learn_struggle()
        return True
    
    def Is_alive(self):
        """
        Check if the Pokemon is alive.

        Returns:
            bool: True if the Pokemon is alive, False otherwise.
        """
        if self.hp > 0:
            return True
        return False
    
    def DrinkPotion(self, gain):
        """
        Make the Pokemon drink a potion to restore its HP.

        Args:
            gain (int): The number of HP restored by the potion.

        Returns:
            int: The Pokemon's current HP after the restoration.
        """
        print(f"\x1b[32m{self.name} drinks a potion and restores {gain} HP.\x1b[0m")
        if self.hp + gain > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += gain
        print(f"{self.name} has \x1b[32m{self.hp} HP\x1b[0m.")
        return self.hp
    
    def Choose_attack(self):
        i = random.randint(0, 3)
        attack = self.attacks[i]
        if self.attack_pp[i] == 0:
            self.Zero_pp()
            return self.Choose_attack()
        return attack

    def DrinkPotionMax(self):
        """
        Make the Pokemon drink a max potion to restore its HP to the max.

        Returns:
            int: The Pokemon's current HP after the restoration.
        """
        print(f" \x1b[34m {self.name} drinks a max potion and restores all its HP.\x1b[0m")
        self.hp = self.max_hp
        print(f"{self.name} a \x1b[34m{self.hp} hp\x1b[0m")
        return self.hp

    def Typing(self, attack, target) -> int:
        """
        Calculating the effectiveness of an attack.

        Args:
            target (Pokemon): The Pokemon that is attacked.

        Returns:
            int: The effectiveness of the attack.
        """
        b = 1
        a = 1
        if attack.attack_type in self.TYPE_EFFECTIVENESS:
            if target.type in self.TYPE_EFFECTIVENESS[attack.attack_type]:
                a = self.TYPE_EFFECTIVENESS[attack.attack_type][target.type]
            if target.type2 in self.TYPE_EFFECTIVENESS:
                if target.type2 in self.TYPE_EFFECTIVENESS[attack.attack_type]:
                    b = self.TYPE_EFFECTIVENESS[attack.attack_type][target.type2]
        return a * b
                
    def Attack(self, target, attack):
        global place
        global pokemon_order
        self.staring_hp = self.hp
        if self.status == "protect":
            self.protect = False
            print(f"{self.name}'s protection has disappeared!")
        if self.status != "asleep":
            if self.status != "frozen":

                if self.status == "confused":
                    print(f"{self.name} is confused...")
                    p = random.randint(0, 100)
                    if p <= 50:
                        print(f"{self.name} attacks itself!")
                        self.hp -= self.max_hp // 8
                        print(f"{self.name} loses \x1b[31m{self.max_hp // 8} HP\x1b[0m.")
                        return
                if self.status == "paralyzed":
                    print(f"{self.name} is paralyzed...")
                    p = random.randint(0, 100)
                    if p <= 25:
                        print(f"{self.name} can't attack!")
                        return
                print(f"{self.name} attacks {target.name} with {attack.name}!")
                self.attack_pp[self.attacks.index(attack)] -= 1
                if random.randint(0,100) <= attack.accuracy:
                    efficiency = self.Typing(attack, target)
                    degats = attack.Calculate_damage(self, target, efficiency)

                    if target.status == "protect":
                        target.status = False
                        print(f"{target.name} used its protection and avoided the attack!")
                        degats = 0
                        efficiency = 1

                    if efficiency > 1:
                        efficiency_message = "\x1b[32mIt's super effective!\x1b[0m"
                    elif efficiency < 1 and efficiency > 0:
                        efficiency_message = "\x1b[mIt's not very effective...\x1b[0m"
                    elif efficiency == 0:
                        efficiency_message = f"\x1b[31mIt doesn't affect {target.name}...\x1b[0m"
                    else:
                        efficiency_message = ""

                    print(f"{efficiency_message} {self.name} deals \x1b[31m{degats} HP\x1b[0m to {target.name}.")

                    target.hp -= degats

                    # Applies the effect of the attack

                    if attack.effect and efficiency != 0:
                        # Checks if the effect is triggered
                        
                        a = random.randint(0, 100)
                        if a <= attack.effect_probability:
                            if target.status == None:
                                print(f"{target.name} is affected by {attack.effect}!")

                                # Negatives

                                if attack.effect == "paralyze":
                                    target.status = "paralyzed"
                                    print(f"\x1b[33m{target.name} is paralyzed!\x1b[0m")
                                
                                elif attack.effect == "burn":
                                    target.status = "burned"
                                    print(f"\x1b[31m{target.name} is burned!\x1b[0m")
                                
                                elif attack.effect == "poison":
                                    target.status = "poisoned"
                                    print(f"\x1b[35m{target.name} is poisoned!\x1b[0m")
                                
                                elif attack.effect == "sleep":
                                    target.status = "asleep"
                                    print(f"\x1b[34m{target.name} is asleep!\x1b[0m")
                                
                                elif attack.effect == "confuse":
                                    target.status = "confused"
                                    print(f"\x1b[33m{target.name} is confused!\x1b[0m")

                                elif attack.effect == "curse":
                                    target.status = "cursed"
                                    print(f"\x1b[31m{target.name} is cursed!\x1b[0m")

                                elif attack.effect == "freeze":
                                    target.status = "frozen"
                                    print(f"\x1b[36m{target.name} is frozen!\x1b[0m")

                                elif attack.effect == "recoil":
                                    self.hp -= degats // 3
                                    print(f"{self.name} loses \x1b[31m{degats // 3} HP because of the recoil\x1b[0m.")
                            
                            if attack.effect == "one-hit":
                                target.hp = 0
                                print(f"{target.name} is knocked out in one hit!")

                            # Positif

                            elif attack.effect == "heal":
                                self.hp = self.max_hp
                                print(f"{self.name} is healed!")

                            elif attack.effect == "protect":
                                self.status = "protect"
                                print(f"{self.name} protects itself!")

                            # Stats +

                            elif attack.effect == "attack+":
                                self.attack += 10
                                print(f"{self.name}'s attack has increased!")
                            
                            elif attack.effect == "speed+":
                                self.speed += 3
                                print(f"{self.name}'s speed has increased!")
                                all_pokemon.sort(key=lambda x: x.speed, reverse=True)

                            elif attack.effect == "defense+":
                                self.defense += 10
                                print(f"{self.name}'s defense has increased!")

                            # Stats -

                            elif attack.effect == "attack-":
                                target.attack -= 10
                                print(f"{target.name}'s attack has decreased!")

                            elif attack.effect == "speed-":
                                target.speed -= 3
                                print(f"{target.name}'s speed has decreased!")
                                all_pokemon.sort(key=lambda x: x.speed, reverse=True)

                            elif attack.effect == "defense-":
                                target.defense -= 10
                                print(f"{target.name}'s defense has decreased!")
        
            else:
                print("The attack missed!")

        if self.status == "burned":
            self.hp -= self.max_hp // 8
            print(f"{self.name} is burned! It loses \x1b[31m{self.max_hp // 8} HP\x1b[0m.")
            if random.randint(0, 100) <= 25:
                self.status = None
                print(f"{self.name} is no longer burned!")

        if self.status == "poisoned":
            self.hp -= self.max_hp // 8
            print(f"{self.name} is poisoned! It loses \x1b[31m{self.max_hp // 8} HP\x1b[0m.")
            if random.randint(0, 100) <= 25:
                self.poison = False
                self.status = None
                print(f"{self.name} is no longer poisoned!")

        if self.status == "asleep":
            if random.randint(0, 100) <= 25:
                self.status = None
                print(f"{self.name} woke up!")
            else:
                print(f"{self.name} is asleep and can't attack!")

        if self.status == "frozen":
            if random.randint(0, 100) <= 25:
                self.status = None
                print(f"{self.name} is no longer frozen!")
            else:
                print(f"{self.name} is frozen and can't attack!")

        if self.status == "cursed":
            self.hp -= self.max_hp // 16
            print(f"{self.name} is cursed! It loses \x1b[31m{self.max_hp // 16} HP\x1b[0m.")

        if self.hp != self.staring_hp:
        
            if self.hp <= 0:
                print(f"\x1b[31m{self.name} is knocked out!\x1b[0m")
            else:
                print(f"{self.name} have \x1b[31m{self.hp} HP\x1b[0m.")

        if target.hp <= 0:
            print(f"\x1b[31m{target.name} is knocked out!\x1b[0m")
        else:
            print(f"{target.name} has \x1b[31m{target.hp} HP left\x1b[0m.")
        
    def __add__(self, hps):
        """
        adds the value of `hps` to the current `hp` attribute.
        
        takes:
            hps (int): the value to add to `hp`.
        
        Returns :
            None
        """
        self.hp += hps
        
    def __sub__(self, hps):
        """
        subtracts the value of `hps` to the current `hp` attribute.
        
        takes :
            hps (int) : the value to subtract to `hp`.
        
        Returns :
            None
        """
        self.hp -= hps
        if self.hp <= 0:
            self.hp = 0

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
        print("You found a secret music! (yeah, just because you said yes instead of y)")
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

attacks_by_type = {
    "electric": att.electric_attacks,
    "fire": att.fire_attacks,
    "water": att.water_attacks,
    "grass": att.grass_attacks,
    "normal": att.normal_attacks,
    "ice": att.ice_attacks,
    "fighting": att.fighting_attacks,
    "poison": att.poison_attacks,
    "ground": att.ground_attacks,
    "flying": att.flying_attacks,
    "psychic": att.psychic_attacks,
    "insect": att.bug_attacks,
    "rock": att.rock_attacks,
    "ghost": att.ghost_attacks,
    "dark": att.dark_attacks,
    "dragon": att.dragon_attacks,
    "steel": att.steel_attacks,
    "fairy": att.fairy_attacks,
    None : att.normal_attacks
}

Pikachu = Pokemon('Pikachu', 70, 30, 90, 40, 'electric')
Squirtle = Pokemon('Squirtle', 50, 25, 43, 45, 'water')
Charmander = Pokemon('Charmander', 65, 25, 65, 43, 'fire')
Bulbasaur = Pokemon('Bulbasaur', 50, 31, 45, 40, 'grass')
Charmur = Pokemon('Charmur', 60, 19, 64, 45, 'normal')
Seel = Pokemon('Seel', 70, 28, 25, 40, 'water')
Meditite = Pokemon('Meditite', 60, 24, 60, 30, 'fighting')
Gloom = Pokemon('Gloom', 85, 15, 65, 65, 'poison')
Dugtrio = Pokemon('Dugtrio', 60, 25, 35, 35, 'ground')
Pidgey = Pokemon('Pidgey', 70, 15, 50, 40, 'flying')
Abra = Pokemon('Abra', 45, 39, 40, 35, 'psychic')
Wurmple = Pokemon('Wurmple', 1, 50, 56, 30, 'insect')
Relicanth = Pokemon('Relicanth', 65, 25, 55, 35, 'rock', 'water')
Shuppet = Pokemon('Shuppet', 40, 25, 50, 35, 'ghost')
Bagon = Pokemon('Bagon', 65, 24, 50, 45, 'dragon')
Poochyena = Pokemon('Poochyena', 30, 28, 35, 30, 'dark')
Aron = Pokemon('Aron', 20, 23, 30, 35, 'steel')
Marill = Pokemon('Marill', 30, 30, 25, 20, 'fairy','normal')
Groudon = Pokemon('Groudon', 70, 40, 90, 90, 'ground')
Raichu = Pokemon('Raichu', 60, 40, 110, 35, 'electric')
Blastoise = Pokemon('Blastoise', 75, 40, 78, 100, 'water')
Charizard = Pokemon('Charizard', 78, 40, 100, 85, 'fire', 'flying')
Venusaur = Pokemon('Venusaur', 80, 35, 70, 83, 'grass', 'poison')
Snorlax = Pokemon('Snorlax', 160, 50, 30, 65, 'normal')
Lapras = Pokemon('Lapras', 130, 45, 60, 70, 'ice', 'water')
Machamp = Pokemon('Machamp', 90, 80, 45, 65, 'fighting')
Nidoking = Pokemon('Nidoking', 81, 47, 85, 77, 'poison', 'ground')
Rhydon = Pokemon('Rhydon', 80, 45, 40, 95, 'ground', 'rock')
Aerodactyl = Pokemon('Aerodactyl', 80, 61, 110, 45, 'flying', 'rock')
Alakazam = Pokemon('Alakazam', 55, 50, 120, 45, 'psychic')
Samurott = Pokemon('Samurott', 70, 85, 60, 100, 'water')
Tyranitar = Pokemon('Tyranitar', 100, 70, 61, 110, 'rock', 'dark')
Ditto = Pokemon('Ditto', 48, 48, 48, 48, 'normal')
Slowbro = Pokemon('Slowbro', 95, 45, 30, 55, 'psychic')
Blissey = Pokemon('Blissey', 250, 10, 55, 10, 'fairy', 'normal')
Rayquaza = Pokemon('Rayquaza', 105, 70, 95, 90, 'dragon', 'flying')
Umbreon = Pokemon('Umbreon', 95, 65, 65, 110, 'dark')
Registeel = Pokemon('Registeel', 80, 75, 50, 150, 'steel')
Magikarp = Pokemon('Magikarp', 20, 10, 80, 55, 'water')
Vaporeon = Pokemon('Vaporeon', 130, 65, 65, 60, 'water')
Mew = Pokemon('Mew', 100, 100, 100, 100, 'psychic')
Raikou = Pokemon('Raikou', 90, 85, 115, 75, 'electric')
Articuno = Pokemon('Articuno', 90, 85, 85, 100, 'ice', 'flying')
Moltres = Pokemon('Moltres', 90, 85, 85, 75, 'fire', 'flying')
Zapdos = Pokemon('Zapdos', 90, 90, 100, 85, 'electric', 'flying')
Dialga = Pokemon('Dialga', 100, 120, 90, 120, 'dragon', 'steel')
Palkia = Pokemon('Palkia', 90, 120, 100, 100, 'dragon', 'water')
Giratina = Pokemon('Giratina', 150, 100, 90, 120, 'ghost', 'dragon')
Deoxys = Pokemon('Deoxys', 50, 150, 150, 150, 'psychic')
Arceus = Pokemon('Arceus', 120, 120, 120, 120, 'normal')
Arcanine = Pokemon('Arcanine', 90, 110, 95, 80, 'fire')
Arbok = Pokemon('Arbok', 60, 85, 80, 69, 'poison')
Beedrill = Pokemon('Beedrill', 65, 90, 75, 40, 'insect', 'poison')
Bellossom = Pokemon('Bellossom', 75, 80, 50, 95, 'grass')
Regirock = Pokemon('Regirock', 80, 100, 50, 200, 'rock')
Regice = Pokemon('Regice', 80, 50, 100, 200, 'ice')
Regigiagas = Pokemon('Regigiagas', 110, 160, 100, 110, 'normal')
Regieleki = Pokemon('Regieleki', 80, 100, 200, 50, 'electric')
Regidraco = Pokemon('Regidraco', 80, 100, 50, 200, 'dragon')
Darkrai = Pokemon('Darkrai', 70, 90, 125, 90, 'dark')
Cresselia = Pokemon('Cresselia', 120, 70, 85, 120, 'psychic')
Uxie = Pokemon('Uxie', 75, 75, 130, 75, 'psychic')
Mesprit = Pokemon('Mesprit', 80, 80, 80, 80, 'psychic')
Azelf = Pokemon('Azelf', 75, 125, 70, 115, 'psychic')
Lugia = Pokemon('Lugia', 106, 90, 110, 130, 'psychic', 'flying')
HoOh = Pokemon('Ho-Oh', 106, 130, 90, 110, 'fire', 'flying')
Celebi = Pokemon('Celebi', 100, 100, 100, 100, 'psychic', 'grass')
Heatran = Pokemon('Heatran', 91, 90, 77, 106, 'fire', 'steel')
Victini = Pokemon('Victini', 100, 100, 100, 100, 'fire', 'psychic')
Suicune = Pokemon('Suicune', 100, 75, 85, 115, 'water')
Entei = Pokemon('Entei', 115, 115, 85, 100, 'fire')

Mewthree = Pokemon('Mewthree', 500, 500, 500, 500, None)

all_pokemon = [Pikachu, Squirtle, Charmander, Bulbasaur, Charmur, Seel, Meditite, Gloom, Dugtrio, Pidgey, Abra, Wurmple, Relicanth,
               Shuppet, Bagon, Poochyena, Aron, Marill, Groudon, Raichu, Blastoise, Charizard, Venusaur, Snorlax, Lapras, Machamp,
               Nidoking, Rhydon, Aerodactyl, Alakazam, Samurott, Tyranitar, Ditto, Slowbro, Blissey, Rayquaza, Umbreon, Registeel,
               Magikarp, Vaporeon, Mew, Raikou, Articuno, Moltres, Zapdos, Dialga, Palkia, Giratina, Deoxys, Arceus, Arcanine, Arbok,
               Beedrill, Bellossom, Regirock, Regice, Regigiagas, Regieleki, Regidraco, Darkrai, Cresselia, Uxie, Mesprit, Azelf, Lugia,
               HoOh, Celebi, Heatran, Victini, Suicune, Entei]
