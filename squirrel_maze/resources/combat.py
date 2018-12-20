import sys

from squirrel_maze.resources.actor import Actor
from squirrel_maze.resources import helpers
from squirrel_maze.resources import menus
from squirrel_maze.resources import npc


class Combat:
    def __init__(self, actors):
        self.actors = actors
        self.round = 0
        self.get_initiative_order()

    def battle(self):
        while helpers.any_members_active(actors, 'npc') and helpers.any_members_active(actors, 'pc'):
            for actor in self.actors:
                self.active_actor = actor
                battle_round()
        menus.go_to_menu('combat')


    def battle_round(self):
        for actor in self.actors if actor.cur_hp > 0:
            battle_turn()

    def battle_turn(self):
        if(self.active_actor.pc_type == 'npc'):
            npc_battle_turn()
        else:
            pc_battle_turn()

    def npc_battle_turn(self):
        print("{}'s turn".format(self.active_actor.name))

    def pc_battle_turn(self):
        print("{}'s turn".format(self.active_actor.name))
        # TODO: menus.actor_menu()

    def combat_setup(self):
        raise "notEmplementedException"
        actors = []
        actors.append(npc.get_goblin("Fooblin"))
        char1 = Actor(pc_type="pc", name="Bar", level=1, max_hp=20,
                      max_str=10, max_dex=10, max_sta=10, max_wil=5)
        actors.append(char1)
        #print("{}({}) fights {}({})".format(actors[0].name, actors[0].pc_type, actors[1].name, actors[1].pc_type))
        combat(actors)

    def get_initiative_order():
        self.actors = helpers.get_actor_list_by_stat(self.actors, 'cur_dex')

