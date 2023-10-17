# pokemons.py
import pokemon_Att_Repertory as att
import random
class Pokemon:
    def __init__(self, nom, pvmax, Att, Vitesse,Def, Type):
        """
        Initialise un Pokemon avec des attributs de base.

        Args:
            nom (str): Le nom du Pokemon.
            pv (int): Les points de vie actuels du Pokemon.
            pvmax (int): Les points de vie maximum du Pokemon.
            Att (int) : L'attaque du Pokemon
            Vitesse (int): La vitesse du Pokemon.
            Def (int): La defense duokemon.
            Type (str): Le type du Pokemon.
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
        # statut du pokemon
        self.paralyse = False
        self.brule = False
        self.poison = False
        self.endormi = False
        self.confus = False
        self.maudit = False
        self.statut = False
        self.freeze = False
        self.abri = False

    def generer_attaques_aleatoires(self):
        # Selectionner 4 attaques aleatoires parmi les attaques du type du Pokemon
        attaques_disponibles = attaques_par_type.get(self.type, [])
        if len(attaques_disponibles) < 4:
            raise Exception("Pas assez d'attaques disponibles pour ce type de Pokemon.")
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
        Verifie si le Pokemon est en vie.

        Returns:
            bool: True si le Pokemon a des PV restants, False sinon.
        """
        if self.pv > 0:
            return True
        return False
    
    def BoitPotion(self, gain):
        """
        Fait boire une potion au Pokemon pour restaurer ses PV.

        Args:
            gain (int): Le nombre de PV restaures.

        Returns:
            int: Le nombre de PV actuels du Pokemon apres la restauration.
        """
        print(f"\x1b[32m{self.nom} boit une potion de {gain} PV\x1b[0m")
        if self.pv + gain > self.pvmax:
            self.pv = self.pvmax
        else:
            self.pv += gain
        print(f"{self.nom} a \x1b[34m{self.pv} PV\x1b[0m")
        return self.pv
    
    def choisir_attaque(self):
        attaque = random.choice(self.attaques)
        return attaque

    def BoitPotionMax(self):
        """
        Fait boire une potion max au Pokemon pour le soigner completement.

        Returns:
            int: Le nombre de PV actuels du Pokemon apres la restauration.
        """
        print(f" \x1b[34m {self.nom} boit une potion max et est completement soigne! \x1b[0m")
        self.pv = self.pvmax
        print(f"{self.nom} a \x1b[34m{self.pv} PV\x1b[0m")
        return self.pv

    def Typing(self, cible) -> int:
        """
        Calcule l'efficacite d'une attaque en fonction des types.

        Args:
            cible (Pokemon): Le Pokemon cible de l'attaque.

        Returns:
            int: Le facteur d'efficacite de l'attaque.
        """
        if self.type in self.TYPE_EFFECTIVENESS:
            if cible.type in self.TYPE_EFFECTIVENESS[self.type]:
                return self.TYPE_EFFECTIVENESS[self.type][cible.type]
        return 1
                
    def Attaque(self, cible, attaque):
        global place
        global pokemon_order
        if self.abri == True:
            self.abri = False
            print(f"L'abri de {self.nom} s'est éstompé!")
        if self.endormi == False:
            if self.confus == True:
                p = random.randint(0, 100)
                if p <= 50:
                    print(f"{self.nom} est confus et se blesse dans sa confusion!")
                    self.pv -= self.pvmax // 8
                    print(f"{self.nom} perd \x1b[31m{self.pvmax // 8} PV\x1b[0m.")
                    return
            if self.paralyse == True:
                p = random.randint(0, 100)
                if p <= 25:
                    print(f"{self.nom} est paralysé et ne peut pas attaquer!")
                    return
            print(f"{self.nom} attaque {cible.nom} avec {attaque.nom}.")
            if random.randint(0,100) <= attaque.precision:
                efficacite = self.Typing(cible)
                degats = attaque.calculer_degats(self, cible, efficacite)

                if cible.abri == True:
                    cible.abri = False
                    print(f"{cible.nom} a utilisé abri et a évité l'attaque!")
                    degats = 0
                    efficacite = 1

                if efficacite > 1:
                    efficacite_message = "\x1b[32mC'est super efficace!\x1b[0m"
                elif efficacite < 1 and efficacite > 0:
                    efficacite_message = "\x1b[mCe n'est pas très efficace...\x1b[0m"
                elif efficacite == 0:
                    efficacite_message = f"\x1b[31mÇa n'affecte pas {cible.nom}.\x1b[0m"
                else:
                    efficacite_message = ""

                print(f"{efficacite_message} {self.nom} inflige \x1b[31m{degats} \x1b[0m degâts à {cible.nom}.")

                # S'assurer que les PV de l'adversaire ne descendent pas en dessous de 0
                cible.pv = max(cible.pv - degats, 0)

                # Effet de l'attaque

                if attaque.effet:
                    # chance de l'effet
                    
                    a = random.randint(0, 100)
                    if a <= attaque.effet_proba:
                        if cible.statut == False:

                            # Negatif

                            if attaque.effet == "paralyse":
                                cible.paralyse = True
                                cible.statut = True
                                print(f"{cible.nom} est paralysé!")
                            
                            elif attaque.effet == "burn":
                                cible.brule = True
                                cible.statut = True
                                print(f"{cible.nom} est brulé!")
                            
                            elif attaque.effet == "poison":
                                cible.poison = True
                                cible.statut = True
                                print(f"{cible.nom} est empoisonné!")
                            
                            elif attaque.effet == "sleep":
                                cible.endormi = True
                                cible.statut = True
                                print(f"{cible.nom} s'endort!")
                            
                            elif attaque.effet == "confus":
                                cible.confus = True
                                cible.statut = True
                                print(f"{cible.nom} est confus!")

                            elif attaque.effet == "maudis":
                                cible.maudit = True
                                cible.statut = True
                                print(f"{cible.nom} est maudit!")

                            elif attaque.effet == "freeze":
                                cible.freeze = True
                                cible.statut = True
                                print(f"{cible.nom} est gelé!")
                        
                        if attaque.effet == "onehit":
                            cible.pv = 0
                            print(f"{cible.nom} est mis KO en un coup!")

                        # Positif

                        elif attaque.effet == "heal":
                            self.hp = self.hpmax
                            print(f"{self.nom} est soigné!")

                        elif attaque.effet == "abri":
                            self.abri = True
                            print(f"{self.nom} se protège!")

                        # Stats +

                        elif attaque.effet == "attaque+":
                            self.attaque += 1
                            print(f"{self.nom} a augmenté son attaque!")
                        
                        elif attaque.effet == "vitesse+":
                            self.vitesse += 1
                            print(f"{self.nom} a augmenté sa vitesse!")
                            all_pokemon.sort(key=lambda x: x.vitesse, reverse=True)

                        elif attaque.effet == "defense+":
                            self.defense += 1
                            print(f"{self.nom} a augmenté sa défense!")

                        # Stats -

                        elif attaque.effet == "attaque-":
                            cible.attaque -= 1
                            print(f"L'attaque de {cible.nom} a baissée!")

                        elif attaque.effet == "vitesse-":
                            cible.vitesse -= 1
                            print(f"La vitesse de {cible.nom} a baissée!")
                            all_pokemon.sort(key=lambda x: x.vitesse, reverse=True)

                        elif attaque.effet == "defense-":
                            cible.defense -= 1
                            print(f"La défense de {cible.nom} a baissée!")
        
            else:
                print("L'attaque a manqué sa cible...")

        if self.brule:
            self.pv -= self.pvmax // 16
            print(f"{self.nom} est brulé! Il perd \x1b[31m{self.pvmax // 16} PV\x1b[0m.")

        if self.poison:
            self.pv -= self.pvmax // 8
            print(f"{self.nom} est empoisonné! Il perd \x1b[31m{self.pvmax // 8} PV\x1b[0m.")

        if self.endormi:
            if random.randint(0, 100) <= 25:
                self.endormi = False
                print(f"{self.nom} s'est réveillé!")
            else:
                print(f"{self.nom} dort et ne peut pas attaquer!")

        if self.maudit:
            self.pv -= self.pvmax // 8
            print(f"{self.nom} est maudit! Il perd \x1b[31m{self.pvmax // 8} PV\x1b[0m.")

        if cible.pv == 0:
            print(f"\x1b[31m{cible.nom} est KO.\x1b[0m")
        else:
            print(f"Il reste \x1b[m{cible.pv} PV\x1b[0m à {cible.nom}.")
        
    def __add__(self, pvs):
        """
        Ajoute la valeur donnee à l'attribut `pv`.
        
        Parametres:
            pvs (int): La valeur à ajouter à `pv`.
        
        Renvoie:
            Aucun
        """
        self.pv += pvs
        
    def __sub__(self, pvs):
        """
        Soustrait la valeur de `pvs` à l'attribut `pv` actuel.
        
        Parametres :
            pvs (int) : La valeur à soustraire à `pv`.
        
        Renvoie :
            None
        """
        self.pv -= pvs

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
all_pokemon = [Pikachu, Carapuce, Salameche, Bulbizarre, Chuchmur, Obalie, Meditikka, Papinox, Chamallot, Tylton, Tarsal, Munja, Relicanth, Tenefix, Draby, Medhyena, Terhal, Azurill, Groudon, Raichu, Tortank, Dracaufeu, Florizarre, Ronflex, Lokhlass, Mackogneur, Nidoking, Rhinoferos, Ptera, Alakazam, Sarmuraï, Tyranocif, Metamorph, Flagadoss, Leuphorie, Rayquaza, Noctali, Registeel, Magicarpe, Aquali, Mew, Raikou, Artikodin]