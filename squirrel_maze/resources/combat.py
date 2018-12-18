import sys

from squirrel_maze.resources.actor import Actor
from squirrel_maze.resources import helpers
from squirrel_maze.resources import menus
from squirrel_maze.resources import npc

def combat_setup(foo):
    actors = []
    actors.append(npc.get_goblin("Fooblin"))
    char1 = Actor(pc_type="pc", name="Bar", level=1, max_hp=20,
                  max_str=10, max_dex=10, max_sta=10, max_wil=5)
    actors.append(char1)
    #print("{}({}) fights {}({})".format(actors[0].name, actors[0].pc_type, actors[1].name, actors[1].pc_type))
    combat(actors)

def combat(actors):
    for actor in actors:
        print("{}({})".format(actor.name, actor.pc_type))
    while helpers.any_members_active(actors, 'npc') and helpers.any_members_active(actors, 'pc'):
        # TODO: combat
        print('Combat happens here')
        menus.go_to_menu('combat')
    menus.go_to_menu('combat')

def get_initiative_order(actors):
    raise "notEmplementedException"
