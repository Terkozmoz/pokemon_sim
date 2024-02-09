#abilities.py
import random as r

class Ability ():
    """Create an ability for a pokemon."""
    def __init__(self,name,description,trigger):
        self.name = name
        self.description = description
        self.trigger = trigger

    def __repr__(self):
        return f"{self.name} - {self.description} -- {self.trigger}"

# Create Abilities
Beast_Boost = Ability("Beast Boost","Boost Random Stat","Each Ko")
Blaze = Ability("Blaze","Power Up","Under 1/3 HP")
Corrosion = Ability("Corrosion","Poison Steel","Always")
Early_Bird = Ability("Early Bird","No Sleep","Always")
Flame_Body = Ability("Flame Body","Burn on Contact","Always")
Flare_Boost = Ability("Flare Boost","Power Up","Burned")
Galvanize = Ability("Galvanize","Normal to Electric","Always")
Guts = Ability("Guts","Power Up","Status")
Insomnia = Ability("Insomnia","No Sleep","Always")
Intimidate = Ability("Intimidate","Lower Opponent Attack","Always")
Levitate = Ability("Levitate","No Ground","Always")
Limber = Ability("Limber","No Paralysis","Always")
Magma_Armor = Ability("Magma Armor","No Freeze","Always")
Mold_Breaker = Ability("Mold Breaker","Ignores Abilities for Moves","Always")
Overgrow = Ability("Overgrow","Power Up","Under 1/3 HP")
Poison_Point = Ability("Poison Point","Poison on Contact","Always")
Swarm = Ability("Swarm","Power Up","Under 1/3 HP")
Torrent = Ability("Torrent","Power Up","Under 1/3 HP")

# Abilities for each type

# Normal
normal_abilities = [Guts,Mold_Breaker]

# Fire
fire_abilities = [Blaze,Flame_Body,Flare_Boost,Magma_Armor]

# Water
water_abilities = [Torrent,Mold_Breaker]

# Electric
electric_abilities = [Galvanize,Insomnia,Limber]

# Grass
grass_abilities = [Overgrow,Swarm]

# Ice
ice_abilities = [Magma_Armor,Levitate]

# Fighting
fighting_abilities = [Guts,Intimidate]

# Poison
poison_abilities = [Corrosion,Poison_Point]

# Ground
ground_abilities = [Magma_Armor,Mold_Breaker]

# Flying
flying_abilities = [Levitate,Early_Bird]

# Psychic
psychic_abilities = [Insomnia,Levitate,Beast_Boost]

# Bug
bug_abilities = [Swarm,Corrosion]

# Rock
rock_abilities = [Magma_Armor,Levitate]

# Ghost
ghost_abilities = [Insomnia,Levitate]

# Dragon
dragon_abilities = [Beast_Boost,Corrosion]

# Dark
dark_abilities = [Intimidate,Insomnia]

# Steel
steel_abilities = [Corrosion,Magma_Armor]

# Fairy
fairy_abilities = [Swarm,Corrosion]

# Typeless
typeless_abilities = [Mold_Breaker]

# Give Abilities

def give_abilities(pokemons):
    """Give abilities to pokemons based on their typing."""
    for pokemon in pokemons:
        if pokemon.type == "normal":
            pokemon.ability = r.choice(normal_abilities)
        elif pokemon.type == "fire":
            pokemon.ability = r.choice(fire_abilities)
        elif pokemon.type == "water":
            pokemon.ability = r.choice(water_abilities)
        elif pokemon.type == "electric":
            pokemon.ability = r.choice(electric_abilities)
        elif pokemon.type == "grass":
            pokemon.ability = r.choice(grass_abilities)
        elif pokemon.type == "ice":
            pokemon.ability = r.choice(ice_abilities)
        elif pokemon.type == "fighting":
            pokemon.ability = r.choice(fighting_abilities)
        elif pokemon.type == "poison":
            pokemon.ability = r.choice(poison_abilities)
        elif pokemon.type == "ground":
            pokemon.ability = r.choice(ground_abilities)
        elif pokemon.type == "flying":
            pokemon.ability = r.choice(flying_abilities)
        elif pokemon.type == "psychic":
            pokemon.ability = r.choice(psychic_abilities)
        elif pokemon.type == "bug":
            pokemon.ability = r.choice(bug_abilities)
        elif pokemon.type == "rock":
            pokemon.ability = r.choice(rock_abilities)
        elif pokemon.type == "ghost":
            pokemon.ability = r.choice(ghost_abilities)
        elif pokemon.type == "dragon":
            pokemon.ability = r.choice(dragon_abilities)
        elif pokemon.type == "dark":
            pokemon.ability = r.choice(dark_abilities)
        elif pokemon.type == "steel":
            pokemon.ability = r.choice(steel_abilities)
        elif pokemon.type == "fairy":
            pokemon.ability = r.choice(fairy_abilities)
        else:
            pokemon.ability = r.choice(typeless_abilities)