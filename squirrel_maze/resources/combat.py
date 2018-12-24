import sys

from squirrel_maze.resources import actor
from squirrel_maze.resources import action
from squirrel_maze.resources import helpers
from squirrel_maze.resources import menus
from squirrel_maze.resources import npc


class Combat:
    def __init__(self, actors):
        self.actors = actors
        self.get_teams()
        self.round = 0
        self.get_initiative_order()
        #self.turn_order = self.get_initiative_order()

    def battle(self):
        while helpers.any_members_active(self.actors, 'npc') and helpers.any_members_active(self.actors, 'pc'):
            self.battle_round()
        if helpers.any_members_active(self.actors, 'pc'):
            menus.victory()
        else:
            menus.defeat()

    def battle_round(self):
        for actor in self.actors:
            self.active_actor = actor
            if self.active_actor.cur_hp > 0:
                self.battle_turn()
        self.round += 1

    def battle_turn(self):
        if(self.active_actor.pc_type == 'npc'):
            self.npc_battle_turn()
        else:
            self.pc_battle_turn()

    # TODO: Add multiple actor support
    def npc_battle_turn(self):
        #self.active_actor.cur_hp -= 1
        unfriendlies = self.active_actor.get_unfriendly_actors(self.actors)
        target_actor = unfriendlies[0]
        action.fight(self.active_actor, target_actor)

    def pc_battle_turn(self):
        # TODO: menus.actor_menu()
        #unfriendlies = self.active_actor.get_unfriendly_actors(self.actors)
        #target_actor = unfriendlies[0]
        #action.fight(self.active_actor, target_actor)
        menus.battle_menu(self.active_actor, self.actors)

    def combat_setup(self):
        raise "notEmplementedException"
        actors = []
        actors.append(npc.get_goblin("Fooblin"))
        char1 = Actor(pc_type="pc", name="Bar", level=1, max_hp=20,
                      max_str=10, max_dex=10, max_sta=10, max_wil=5)
        actors.append(char1)
        #print("{}({}) fights {}({})".format(actors[0].name, actors[0].pc_type, actors[1].name, actors[1].pc_type))
        combat(actors)

    def get_initiative_order(self):
        self.actors = helpers.get_actor_list_by_stat(self.actors, 'cur_dex')
        #actor_list = []
        #for actor in helpers.get_actor_list_by_stat(self.actors, 'cur_dex'):
        #    actor_list.append()
        #return actor_list

    # TODO: add combatant list at the top
    #def print_battle_header(actors):
    #
    def get_teams(self):
        self.teams = {}
        for actor in self.actors:
            if actor.pc_type not in self.teams:
                self.teams.update(
                    {
                        actor.pc_type: []
                    }
                )
            self.teams[actor.pc_type].append(actor.name)
