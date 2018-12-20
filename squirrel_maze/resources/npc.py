from squirrel_maze.resources.actor import Actor

def get_goblin(name="Goblin"):
    return Actor("npc", name, level=1, max_hp=5, max_str=3, max_dex=2, max_sta=2)
def get_big_goblin(name="Big Goblin"):
    return Actor("npc", name, level=3, max_hp=20, max_str=10, max_dex=10, max_sta=10)
