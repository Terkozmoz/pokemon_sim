#pyramid.py

import random
import pokemons as p
import battle as b
import pygame as pg
all_pkms = p.all_pokemon
music = "assets\\theme\\Regis_Trio.mp3"
music_on = False

def items(id):
    ids = {
        1: "red shard",     #1%
        2: "blue shard",    #1%
        3: "yellow shard",  #1%
        4: "green shard",   #1%
        5: "white shard",   #1%
        20: "pokeball",     #15%
        70: "potion",       #50%
        90: "super potion", #20%
        100: "max potion"   #10%
    }
    if p.quest != None and p.quest.type == "collect":
        print(f"Looking for {p.quest.target} ...")
    for i in ids:
        if id <= i:
            print(f"You found a {ids[i]}!")
            if ids[i] == "pokeball":
                b.bonus_pball += 1
            elif ids[i] == "red shard":
                b.r_shards += 1
            elif ids[i] == "blue shard":
                b.b_shards += 1
            elif ids[i] == "yellow shard":
                b.y_shards += 1
            elif ids[i] == "green shard":
                b.g_shards += 1
            elif ids[i] == "white shard":
                b.w_shards += 1
            elif ids[i] == "potion":
                b.bonus_potion += 1
            elif ids[i] == "super potion":
                b.bonus_superpotion += 1
            elif ids[i] == "max potion":
                b.bonus_potionmax += 1
            
            if p.quest != None:
                if p.quest.type == "collect":
                    if ids[i] == p.quest.target:
                        p.quest.update_progress(1)
            break

def start_battle():
    print("You encountered an enemy!")
    b.start(all_pkms)
    print("End of the encounter!")
    # shows leveled up pokemons
    for mon in p.leveled_ups:
        print(f"{mon[0]} leveled up to level {mon[1]}!")
        p.leveled_ups.remove(mon)
    # Updates music, if any
    if pg.mixer.music.get_busy() and music != None:
        pg.mixer.music.stop()
        pg.mixer.music.load(music)
        pg.mixer.music.play(-1)
    # Back to the board

class TreeNode:
    def __init__(self, value, left=None, right=None, up=None):
        self.value = value
        self.left = left
        self.right = right
        self.up = up
        self.visited = False

def generate_tree(height, parent=None):
    """
    Generates a binary tree with the specified height.

    Parameters:
    height (int): The height of the tree.
    parent (TreeNode, optional): The parent node of the current node. Defaults to None.

    Returns:
    TreeNode: The root node of the generated tree.
    """
    if height == 0:
        return None
    value = random.choice(["Nothing", "Item", "Encounter"])
    node = TreeNode(value)
    node.up = parent
    node.left  = generate_tree(height - 1, node) if random.random() < 0.8 else None  # 80% chance to have a left  child 
    node.right = generate_tree(height - 1, node) if random.random() < 0.8 else None  # 80% chance to have a right child
    return node

def find_random_leaf(node):

    "Finds a random leaf node in the tree."

    if node is None:
        return None
    if node.left is None and node.right is None:
        return node
    left_leaf = find_random_leaf(node.left)
    right_leaf = find_random_leaf(node.right)
    if left_leaf and right_leaf:
        return random.choice([left_leaf, right_leaf])
    elif left_leaf:
        return left_leaf
    else:
        return right_leaf

def explore(node, visited_nodes):
    """
    Explores the pyramid starting from the given node.

    Args:
        node (Node): The starting node.
        visited_nodes (list): A list of visited nodes.

    Returns:
        None
    """
    if node.up == None:
        print("You are at the top of the pyramid.")
    if node.left is None and node.right is None:  # Leaf node
        print("You are at a leaf node.")
    if node.value == "Encounter":
        if not node.visited:
            print("Oh no! You encountered an enemy!")
            start_battle()
            if music_on == True:
                pg.mixer.music.stop()
                pg.mixer.music.load(music)
                pg.mixer.music.play(-1)
        else:
            print("You already defeated the enemy here.")
    elif node.value == "Item":
        if not node.visited:
            print("You found an item!")
            items(random.randint(1, 100))
        else:
            print("You already took the item here.")
    node.visited = True
    print("You can go:")
    if node.left:
        print("l - left")
    if node.right:
        print("r - right")
    if node.up:
        print("u - up")
    if node.left is None and node.right is None:  # Leaf node
        print("e - exit")
    direction = input("Which direction do you want to go? ").lower()
    if direction == "l" and node.left:
        explore(node.left, visited_nodes)
    elif direction == "r" and node.right:
        explore(node.right, visited_nodes)
    elif direction == "u" and node.up:
        explore(node.up, visited_nodes)
    elif direction == "e" and node.left is None and node.right is None:
        return
    else:
        print("Invalid choice. Try again.")
        explore(node, visited_nodes)

def main():
    global music_on
    if pg.mixer.music.get_busy() and music != None:
        music_on = True
        pg.mixer.music.stop()
        pg.mixer.music.load(music)
        pg.mixer.music.play(-1)
    height = random.randint(3, 4)
    tree = generate_tree(height)
    leaf_node = find_random_leaf(tree)
    print("You entered the pyramid!")
    visited_nodes = []
    explore(leaf_node, visited_nodes)
    print("Exiting the pyramid.")
    # Back to the board (end of file)

if __name__ == "__main__":
    main()