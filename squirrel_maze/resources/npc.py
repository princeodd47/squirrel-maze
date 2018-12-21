from squirrel_maze.resources.actor import Actor

def get_goblin(name="Goblin"):
    return Actor("npc", name, level=1, max_hp=5, max_str=3, max_dex=2, max_sta=2)
def get_big_goblin(name="Big Goblin"):
    return Actor("npc", name, level=2, max_hp=10, max_str=9, max_dex=9, max_sta=9)
