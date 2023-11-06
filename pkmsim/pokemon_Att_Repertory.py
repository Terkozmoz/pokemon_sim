# pokemon_attack_repertoire.py
class Attack:
    def __init__(self, name, power, accuracy, attack_type, effect=None, effect_probability=0):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.attack_type = attack_type
        self.effect = effect
        self.effect_probability = effect_probability

    def Calculate_damage(self, attacker, defender, effectiveness):
        # Damage calculation formula without considering the level
        A = attacker.attack
        D = defender.defense
        P = self.power
        E = effectiveness
        damage = int(int((((100 + A + (15 * 50)) * P) / (D + 50)) / 20) * E)
        return int(damage)

# Attacks for the "Electric" type
electric_attacks = [
    Attack("Thunder", 90, 100, "electric", "paralyze", 10),
    Attack("Spark", 40, 100, "electric", "paralyze", 10),
    Attack("Shock Wave", 65, 100, "electric", "paralyze", 30),
    Attack("Thunder Wave", 0, 90, "electric", "paralyze", 100),
    Attack("Wild Charge", 120, 75, "electric", "paralyze", 20),
    Attack("Thunderbolt", 120, 50, "electric", "paralyze", 100),
    Attack("Charge Beam", 50, 90, "electric", "attack+", 70),
    Attack("Discharge", 90, 85, "electric", "paralyze", 30),
    Attack("Protect", 0, 100, "normal", "protect", 100),
]

# Attacks for the "Fire" type
fire_attacks = [
    Attack("Flamethrower", 90, 100, "fire", "burn", 10),
    Attack("Ember", 40, 100, "fire", "burn", 10),
    Attack("Fire Blast", 110, 85, "fire", "burn", 10),
    Attack("Fire Spin", 35, 85, "fire", "burn", 50),
    Attack("Blaze Kick", 95, 90, "fire", "burn", 10),
    Attack("Flare Blitz", 85, 90, "fire", "burn", 10),
    Attack("Inferno", 100, 50, "fire", "burn", 100),
    Attack("Flame Charge", 50, 100, "fire", "speed+", 10),
    Attack("Protect", 0, 100, "normal", "protect", 100),
]

# Attacks for the "Water" type
water_attacks = [
    Attack("Surf", 90, 100, "water"),
    Attack("Water Gun", 40, 100, "water"),
    Attack("Hydro Pump", 110, 80, "water"),
    Attack("Bubble Beam", 65, 100, "water"),
    Attack("Aqua Tail", 90, 90, "water"),
    Attack("Scald", 80, 100, "water", "burn", 30),
    Attack("Whirlpool", 35, 85, "water"),
    Attack("Brine", 65, 100, "water"),
    Attack("Protect", 0, 100, "normal", "protect", 100),
]

# Attacks for the "Grass" type
grass_attacks = [
    Attack("Solar Beam", 120, 100, "grass"),
    Attack("Razor Leaf", 55, 95, "grass"),
    Attack("Vine Whip", 45, 100, "grass"),
    Attack("Seed Bomb", 25, 100, "grass"),
    Attack("Leaf Blade", 90, 100, "grass"),
    Attack("Bullet Seed", 80, 100, "grass"),
    Attack("Power Whip", 120, 85, "grass"),
    Attack("Giga Drain", 80, 100, "grass"),
    Attack("Protect", 0, 100, "normal", "protect", 100),
    Attack("Sleep Powder", 0, 75, "grass", "sleep", 100),
]

# Attacks for the "Normal" type
normal_attacks = [
    Attack("Tackle", 40, 100, "normal"),
    Attack("Thunder Shock", 40, 100, "electric", "paralyze", 30),
    Attack("Hyper Beam", 150, 90, "normal"),
    Attack("Scratch", 40, 100, "normal"),
    Attack("Take Down", 85, 100, "normal", "paralyze", 30),
    Attack("Skull Bash", 120, 100, "normal"),
    Attack("Facade", 70, 100, "normal"),
    Attack("Return", 100, 100, "normal"),
    Attack("Protect", 0, 100, "normal", "protect", 100),
]

# Attacks for the "Ice" type
ice_attacks = [
    Attack("Ice Beam", 90, 100, "ice", "freeze", 10),
    Attack("Aurora Beam", 65, 100, "ice"),
    Attack("Blizzard", 110, 70, "ice", "freeze", 10),
    Attack("Icy Wind", 55, 95, "ice"),
    Attack("Ice Shard", 40, 100, "ice"),
    Attack("Frost Breath", 60, 90, "ice", "freeze", 10),
    Attack("Ice Punch", 75, 100, "ice"),
    Attack("Freeze-Dry", 70, 90, "ice", "freeze", 10),
    Attack("Glaciate", 0, 30, "ice", "one-hit", 100),
    Attack("Protect", 0, 100, "normal", "protect", 100),
]

# Attacks for the "Fighting" type
fighting_attacks = [
    Attack("Karate Chop", 50, 100, "fighting"),
    Attack("Dynamic Punch", 100, 50, "fighting"),
    Attack("Cross Chop", 100, 80, "fighting"),
    Attack("Mach Punch", 40, 100, "fighting"),
    Attack("Close Combat", 120, 80, "fighting"),
    Attack("Superpower", 120, 90, "fighting"),
    Attack("Hammer Arm", 150, 100, "fighting"),
    Attack("Protect", 0, 100, "normal", "protect", 100),
]

# Attacks for the "Poison" type
poison_attacks = [
    Attack("Sludge Bomb", 90, 100, "poison", "poison", 10),
    Attack("Toxic", 0, 85, "poison", "poison", 100),
    Attack("Poison Jab", 80, 100, "poison", "poison", 20),
    Attack("Sludge", 20, 70, "poison", "poison", 100),
    Attack("Drain Punch", 65, 100, "fighting"),
    Attack("Poison Sting", 70, 100, "poison"),
    Attack("Toxic Spikes", 20, 100, "poison"),
    Attack("Gunk Shot", 120, 70, "poison"),
    Attack("Protect", 0, 100, "normal", "protect", 100),
]

# Attacks for the "Ground" type
ground_attacks = [
    Attack("Earthquake", 100, 100, "ground"),
    Attack("Dig", 80, 100, "ground"),
    Attack("Mud-Slap", 20, 100, "ground"),
    Attack("Fissure", 0, 30, "ground", "one-hit", 100),
    Attack("Drill Run", 80, 95, "ground"),
    Attack("Mud Shot", 60, 100, "ground"),
    Attack("Sand Tomb", 35, 85, "ground"),
    Attack("Lava Plume", 95, 95, "fire", "burn", 30),
    Attack("Protect", 0, 100, "normal", "protect", 100),
]

# Attacks for the "Flying" type
flying_attacks = [
    Attack("Air Slash", 60, 100, "flying"),
    Attack("Fly", 90, 95, "flying"),
    Attack("Hurricane", 110, 70, "flying"),
    Attack("Peck", 35, 100, "flying"),
    Attack("Brave Bird", 120, 100, "flying"),
    Attack("Roost", 0, 100, "flying", "heal", 50),
    Attack("Aerial Ace", 75, 95, "flying"),
    Attack("Defog", 0, 100, "flying", "defense+", 100),
    Attack("Protect", 0, 100, "normal", "protect", 100),
]

# Attacks for the "Psychic" type
psychic_attacks = [
    Attack("Psychic", 90, 100, "psychic"),
    Attack("Confusion", 50, 100, "psychic", "confuse", 10),
    Attack("Psybeam", 65, 100, "psychic"),
    Attack("Hypnosis", 0, 60, "psychic", "sleep", 100),
    Attack("Dream Eater", 100, 100, "psychic"),
    Attack("Foresight", 120, 100, "psychic"),
    Attack("Headbutt", 80, 90, "normal"),
    Attack("Psycho Cut", 70, 100, "psychic"),
    Attack("Protect", 0, 100, "normal", "protect", 100),
]

# Attacks for the "Bug" type
bug_attacks = [
    Attack("Bug Buzz", 90, 100, "bug"),
    Attack("Fury Cutter", 25, 95, "bug"),
    Attack("X-Scissor", 80, 100, "bug"),
    Attack("Spider Web", 0, 95, "bug", "paralyze", 100),
    Attack("Megahorn", 120, 85, "bug"),
    Attack("U-turn", 70, 100, "bug"),
    Attack("Signal Beam", 75, 100, "bug"),
    Attack("Toxic Spikes", 20, 100, "bug", "poison", 100),
    Attack("Protect", 0, 100, "normal", "protect", 100),
]

# Attacks for the "Rock" type
rock_attacks = [
    Attack("Rock Slide", 75, 90, "rock"),
    Attack("Stone Edge", 100, 80, "rock"),
    Attack("Rock Throw", 50, 90, "rock"),
    Attack("Rock Polish", 0, 100, "rock", "speed+", 100),
    Attack("Hammer Arm", 150, 80, "fighting"),
    Attack("Smack Down", 50, 100, "rock"),
    Attack("Rollout", 30, 90, "rock"),
    Attack("Gyro Ball", 80, 100, "steel", "speed-", 100),
    Attack("Protect", 0, 100, "normal", "protect", 100),
]

# Attacks for the "Ghost" type
ghost_attacks = [
    Attack("Shadow Ball", 80, 100, "ghost"),
    Attack("Night Shade", 0, 100, "ghost", "sleep", 100),
    Attack("Curse", 0, 100, "ghost", "curse", 100),
    Attack("Lick", 20, 100, "ghost", "paralyze", 30),
    Attack("Hex", 65, 100, "ghost"),
    Attack("Venoshock", 60, 100, "poison"),
    Attack("Ominous Wind", 90, 100, "ghost"),
    Attack("Shadow Punch", 60, 100, "ghost"),
    Attack("Protect", 0, 100, "normal", "protect", 100),
]

# Attacks for the "Dark" type
dark_attacks = [
    Attack("Dark Pulse", 80, 100, "dark"),
    Attack("Pursuit", 40, 100, "dark"),
    Attack("Foul Play", 95, 100, "dark"),
    Attack("Sucker Punch", 60, 100, "dark", "confuse", 30),
    Attack("Crunch", 80, 100, "dark"),
    Attack("Low Sweep", 70, 100, "dark", "speed-", 100),
    Attack("Howl", 55, 95, "dark", "speed-", 100),
    Attack("Foul Play", 80, 100, "dark", "defense+", 100),
    Attack("Protect", 0, 100, "normal", "protect", 100),
]

# Attacks for the "Dragon" type
dragon_attacks = [
    Attack("Dragon Claw", 80, 100, "dragon"),
    Attack("Dragon Breath", 40, 100, "dragon"),
    Attack("Outrage", 120, 100, "dragon", "attack+", 50),
    Attack("Dragon Rage", 60, 100, "dragon"),
    Attack("Dragon Dance", 0, 100, "dragon", "attack+", 100),
    Attack("Dragon Tail", 40, 100, "dragon"),
    Attack("Draco Meteor", 130, 90, "dragon"),
    Attack("Protect", 0, 100, "normal", "protect", 100),
]

# Attacks for the "Steel" type
steel_attacks = [
    Attack("Iron Tail", 100, 75, "steel"),
    Attack("Steel Claw", 50, 95, "steel"),
    Attack("Flash Cannon", 80, 100, "steel"),
    Attack("Iron Head", 80, 100, "steel"),
    Attack("Steel Wing", 70, 90, "steel"),
    Attack("Rock Polish", 0, 100, "steel", "speed+", 100),
    Attack("Gyro Ball", 80, 100, "steel", "speed-", 100),
    Attack("Dazzling Gleam", 90, 90, "steel"),
    Attack("Protect", 0, 100, "normal", "protect", 100),
]

# Attacks for the "Fairy" type
fairy_attacks = [
    Attack("Flash Cannon", 95, 100, "fairy"),
    Attack("Dazzling Gleam", 80, 100, "fairy"),
    Attack("Charm", 90, 90, "fairy"),
    Attack("Draining Kiss", 50, 100, "fairy"),
    Attack("Fairy Wind", 40, 100, "fairy"),
    Attack("Enchanting Voice", 40, 100, "fairy"),
    Attack("Misty Terrain", 0, 100, "fairy", "attack+", 100),
    Attack("Lullaby", 0, 100, "normal", "sleep", 100),
    Attack("Protect", 0, 100, "normal", "protect", 100),
]
