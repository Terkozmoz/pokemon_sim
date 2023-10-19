#pokemon_Att_Repertory.py
class Attaque:
    def __init__(self, nom, puissance, precision, type, effet = None, effet_proba = 0):
        self.nom = nom
        self.puissance = puissance
        self.precision = precision
        self.type = type
        self.effet = effet
        self.effet_proba = effet_proba

    def calculer_degats(self, attaquant, defenseur, efficacite):
        # Formule de calcul des dégâts sans considération du niveau
        A = attaquant.attaque
        D = defenseur.defense
        P = self.puissance
        E = efficacite
        degats = int(int((((100+A+(15*50))*P)/(D+50)))/20)*E
        return int(degats)

# Attaques pour le type "Electrique"
electric_attaques = [
    Attaque("Tonnerre", 90, 100, "electrique", "paralyse", 10),
    Attaque("Éclair", 40, 100, "electrique", "paralyse", 10),
    Attaque("Étincelle", 65, 100, "electrique", "paralyse", 30),
    Attaque("Cage-Éclair", 0, 90, "electrique", "paralyse", 100),
    Attaque("Éclair Fou", 120, 75, "electrique", "paralyse", 20),
    Attaque("Élecanon", 120, 50, "electrique", "paralyse", 100),
    Attaque("Rayon Chargé", 50, 90, "electrique", "attaque+", 70),
    Attaque("Coup d'Jus", 90, 85, "electrique", "paralyse", 30),
    Attaque("Abri", 0, 100, "normal", "abri", 100),
]

# Attaques pour le type "Feu"
fire_attaques = [
    Attaque("Lance-Flammes", 90, 100, "feu", "burn", 10),
    Attaque("Flammèche", 40, 100, "feu", "burn", 10),
    Attaque("Déflagration", 110, 85, "feu", "burn", 10),
    Attaque("Danseflamme", 35, 85, "feu", "burn", 50),
    Attaque("Canicule", 95, 90, "feu", "burn", 10),
    Attaque("Pied Brûleur", 85, 90, "feu", "burn", 10),
    Attaque("Feu d'Enfer", 100, 50, "feu", "burn", 100),
    Attaque("Nitrocharge", 50, 100, "feu", "vitesse+", 10),
    Attaque("Abri", 0, 100, "normal", "abri", 100),
]

# Attaques pour le type "Eau"
water_attaques = [
    Attaque("Surf", 90, 100, "eau"),
    Attaque("Pistolet à O", 40, 100, "eau"),
    Attaque("Hydrocanon", 110, 80, "eau"),
    Attaque("Bulles d'O", 65, 100, "eau"),
    Attaque("Aqua-Queue", 90, 90, "eau"),
    Attaque("Ébullition", 80, 100, "eau", "burn", 30),
    Attaque("Tourbillon", 35, 85, "eau"),
    Attaque("Saumure", 65, 100, "eau"),
    Attaque("Abri", 0, 100, "normal", "abri", 100),
]

# Attaques pour le type "Plante"
grass_attaques = [
    Attaque("Lance-Soleil", 120, 100, "plante"),
    Attaque("Tranch'Herbe", 55, 95, "plante"),
    Attaque("Fouet Lianes", 45, 100, "plante"),
    Attaque("Charge-Graine", 25, 100, "plante"),
    Attaque("Lame-Feuille", 90, 100, "plante"),
    Attaque("Bomb-Graine", 80, 100, "plante"),
    Attaque("Mégafouet", 120, 85, "plante"),
    Attaque("Giga-Sangsue", 80, 100, "plante"),
    Attaque("Abri", 0, 100, "normal", "abri", 100),
]

# Attaques pour le type "Normal"
normal_attaques = [
    Attaque("Charge", 40, 100, "normal"),
    Attaque("Coup d'Jus", 40, 100, "electrique", "paralyse", 30),
    Attaque("Ultralaser", 150, 90, "normal"),
    Attaque("Griffe", 40, 100, "normal"),
    Attaque("Plaquage", 85, 100, "normal", "paralyse", 30),
    Attaque("Coud'Krâne", 120, 100, "normal"),
    Attaque("Façade", 70, 100, "normal"),
    Attaque("Retour", 100, 100, "normal"),
    Attaque("Abri", 0, 100, "normal", "abri", 100),
]

# Attaques pour le type "Glace"
ice_attaques = [
    Attaque("Laser Glace", 90, 100, "glace", "freeze", 10),
    Attaque("Onde Boréale", 65, 100, "glace"),
    Attaque("Blizzard", 110, 70, "glace", "freeze", 10),
    Attaque("Vent Glace", 55, 95, "glace"),
    Attaque("Éclat Glace", 40, 100, "glace"),
    Attaque("Souffle Glacé", 60, 90, "glace", "freeze", 10),
    Attaque("Poing Glace", 75, 100, "glace"),
    Attaque("Lyophilisation", 70, 90, "glace", "freeze", 10),
    Attaque("Glaciation", 0, 30, "glace", "onehit", 100),
    Attaque("Abri", 0, 100, "normal", "abri", 100),
]

# Attaques pour le type "Combat"
fighting_attaques = [
    Attaque("Coup Karaté", 50, 100, "combat"),
    Attaque("Dynamopoing", 100, 50, "combat"),
    Attaque("Poing-Croix", 100, 80, "combat"),
    Attaque("Mach Punch", 40, 100, "combat"),
    Attaque("Close Combat", 120, 80, "combat"),
    Attaque("Surpuissance", 120, 90, "combat"),
    Attaque("Frappe Atlas", 150, 100, "combat"),
    Attaque("Abri", 0, 100, "normal", "abri", 100),
]

# Attaques pour le type "Poison"
poison_attaques = [
    Attaque("Bomb-Beurk", 90, 100, "poison", "poison", 10),
    Attaque("Toxik", 0, 85, "poison", "poison", 100),
    Attaque("Direct Toxik", 80, 100, "poison", "poison", 20),
    Attaque("Purédpois", 20, 70, "poison", "poison", 100),
    Attaque("Vampipoing", 65, 100, "combat"),
    Attaque("Poison-Croix", 70, 100, "poison"),
    Attaque("Pics Toxik", 20, 100, "poison"),
    Attaque("Giclé-Toxique", 120, 70, "poison"),
    Attaque("Abri", 0, 100, "normal", "abri", 100),
]

# Attaques pour le type "Sol"
ground_attaques = [
    Attaque("Séisme", 100, 100, "sol"),
    Attaque("Tunnel", 80, 100, "sol"),
    Attaque("Coud'boue", 20, 100, "sol"),
    Attaque("Fissure", 0, 30, "sol", "onehit", 100),
    Attaque("Tunnelier", 80, 95, "sol"),
    Attaque("Piétisol", 60, 100, "sol"),
    Attaque("Tourbi-Sable", 35, 85, "sol"),
    Attaque("Charge Magma", 95, 95, "feu", "burn", 30),
    Attaque("Abri", 0, 100, "normal", "abri", 100),
]

# Attaques pour le type "Vol"
flying_attaques = [
    Attaque("Aéropique", 60, 100, "vol"),
    Attaque("Vol", 90, 95, "vol"),
    Attaque("Vent Violent", 110, 70, "vol"),
    Attaque("Picpic", 35, 100, "vol"),
    Attaque("Piqué", 120, 100, "vol"),
    Attaque("Atterisage", 0, 100, "vol", "heal", 50),
    Attaque("Tranch'Air", 75, 95, "vol"),
    Attaque("Anti-Brume", 0, 100, "vol", "defense+", 100),
    Attaque("Abri", 0, 100, "normal", "abri", 100),
]

# Attaques pour le type "Psy"
psychic_attaques = [
    Attaque("Psychic", 90, 100, "psy"),
    Attaque("Confusion", 50, 100, "psy", "confus", 10),
    Attaque("Rafale Psy", 65, 100, "psy"),
    Attaque("Hypnose", 0, 60, "psy", "sleep", 100),
    Attaque("Dévorêve", 100, 100, "psy"),
    Attaque("Prescience", 120, 100, "psy"),
    Attaque("Coup d'Boule", 80, 90, "normal"),
    Attaque("Tranche-Psy", 70, 100, "psy"),
    Attaque("Abri", 0, 100, "normal", "abri", 100),
]

# Attaques pour le type "Insecte"
bug_attaques = [
    Attaque("Bourdon", 90, 100, "insecte"),
    Attaque("Dard-Nuée", 25, 95, "insecte"),
    Attaque("Plaie-Croix", 80, 100, "insecte"),
    Attaque("Toile", 0, 95, "insecte", "paralyse", 100),
    Attaque("Mégacorne", 120, 85, "insecte"),
    Attaque("Change Éclair", 70, 100, "insecte"),
    Attaque("Rayon Signal", 75, 100, "insecte"),
    Attaque("Piège de Venin", 20, 100, "insecte", "poison", 100),
    Attaque("Abri", 0, 100, "normal", "abri", 100),
]

# Attaques pour le type "Roche"
rock_attaques = [
    Attaque("Éboulement", 75, 90, "roche"),
    Attaque("Tranche Pierre", 100, 80, "roche"),
    Attaque("Jet-Pierres", 50, 90, "roche"),
    Attaque("Poliroche", 0, 100, "roche", "vitesse+", 100),
    Attaque("Frappe Atlas", 150, 80, "combat"),
    Attaque("Anti-Air", 50, 100, "roche"),
    Attaque("Roulade", 30, 90, "roche"),
    Attaque("Gyroballe", 80, 100, "acier", "vitesse-", 100),
    Attaque("Abri", 0, 100, "normal", "abri", 100),
]

# Attaques pour le type "Spectre"
ghost_attaques = [
    Attaque("Ball'Ombre", 80, 100, "spectre"),
    Attaque("Ombre Nocturne", 0, 100, "spectre", "sleep", 100),
    Attaque("Malédiction", 0, 100, "spectre", "maudis", 100),
    Attaque("Léchouille", 20, 100, "spectre", "paralyse", 30),
    Attaque("Châtiment", 65, 100, "spectre"),
    Attaque("Vent Mauvais", 60, 100, "poison"),
    Attaque("Hantise", 90, 100, "spectre"),
    Attaque("Poing Ombre", 60, 100, "spectre"),
    Attaque("Abri", 0, 100, "normal", "abri", 100),
]

# Attaques pour le type "Ténèbres"
dark_attaques = [
    Attaque("Vibrobscur", 80, 100, "tenebres"),
    Attaque("Poursuite", 40, 100, "tenebres"),
    Attaque("Dark Pulse", 95, 100, "tenebres"),
    Attaque("Vol-vie", 60, 100, "tenebres"),
    Attaque("Mâchouille", 80, 100, "tenebres","confus", 30),
    Attaque("Coup Bas", 70, 100, "tenebres"),
    Attaque("Hurlement", 55, 95, "tenebres", "vitesse-", 100),
    Attaque("Baston", 10, 100, "tenebres","defense+", 100),
    Attaque("Abri", 0, 100, "normal", "abri", 100),
]

# Attaques pour le type "Dragon"
dragon_attaques = [
    Attaque("Dracogriffe", 80, 100, "dragon"),
    Attaque("Dracosouffle", 40, 100, "dragon"),
    Attaque("Colère", 120, 100, "dragon", "attaque+", 50),
    Attaque("Dracosouffle", 60, 100, "dragon"),
    Attaque("Danse Draco", 0, 100, "dragon", "attaque+", 100),
    Attaque("Tornade", 40, 100, "dragon"),
    Attaque("Dracocharge", 100, 75, "dragon"),
    Attaque("Draco Météore", 130, 90, "dragon"),
    Attaque("Abri", 0, 100, "normal", "abri", 100),
]

# Attaques pour le type "Acier"
steel_attaques = [
    Attaque("Queue de Fer", 100, 75, "acier"),
    Attaque("Griffe Acier", 50, 95, "acier"),
    Attaque("Luminocanon", 80, 100, "acier"),
    Attaque("Tête de Fer", 80, 100, "acier"),
    Attaque("Aile d'Acier", 70, 90, "acier"),
    Attaque("Poliroche", 0, 100, "acier", "vitesse+", 100),
    Attaque("Gyroballe", 80, 100, "acier", "vitesse-", 100),
    Attaque("Éclat Magique", 90, 90, "acier"),
    Attaque("Abri", 0, 100, "normal", "abri", 100),
]

# Attaques pour le type "Fee"
fairy_attaques = [
    Attaque("Luminocanon", 95, 100, "fee"),
    Attaque("Éclat Magique", 80, 100, "fee"),
    Attaque("Charme", 90, 90, "fee"),
    Attaque("Vampibaiser", 50, 100, "fee"),
    Attaque("Vent Féerique", 40, 100, "fee"),
    Attaque("Voix Enjôleuse", 40, 100, "fee"),
    Attaque("Champ Brumeux", 0, 100, "fee", "attaque+", 100),
    Attaque("Berceuse", 0, 100, "normal", "sleep", 100),
    Attaque("Abri", 0, 100, "normal", "abri", 100),
]
