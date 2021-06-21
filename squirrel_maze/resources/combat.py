from typing import Dict, List

from squirrel_maze.resources.actor import Actor
from squirrel_maze.resources import actor as sm_actor
from squirrel_maze.resources import action as sm_action
from squirrel_maze.resources import helpers as sm_helpers
from squirrel_maze.resources import menus as sm_menus


class Combat:
    def __init__(self, actors: List[Actor]):
        self.actors = actors
        self.get_teams()
        self.round = 0
        self.get_initiative_order()
        # self.turn_order = self.get_initiative_order()

    def battle(self) -> None:
        while sm_helpers.any_members_alive(self.actors, 'npc') and sm_helpers.any_members_alive(self.actors, 'pc'):
            self.battle_round()
        if sm_helpers.any_members_alive(self.actors, 'pc'):
            sm_menus.victory()
        else:
            sm_menus.defeat()

    def battle_round(self) -> None:
        for actor in self.actors:
            self.active_actor = actor
            if self.active_actor.cur_hp > 0:
                self.battle_turn()
        self.round += 1

    def battle_turn(self) -> None:
        if(self.active_actor.pc_type == 'npc'):
            self.npc_battle_turn()
        else:
            self.pc_battle_turn()

    def npc_battle_turn(self) -> None:
        unfriendlies = sm_helpers.get_affiliated_actors("unfriendly", self.actors)
        target_actor = unfriendlies[0]
        sm_action.fight(self.active_actor, target_actor)

    def pc_battle_turn(self) -> None:
        sm_menus.battle_menu(self.active_actor, self.actors)

    def combat_setup(self) -> None:
        raise NotImplementedError
        actors = []
        # actors.append(sm_npc.get_goblin("Fooblin"))
        char1 = sm_actor.Actor(pc_type="pc", name="Bar", level=1, max_hp=20,
                               max_str=10, max_dex=10, max_sta=10, max_wil=5)
        actors.append(char1)
        # print("{}({}) fights {}({})".format(actors[0].name, actors[0].pc_type, actors[1].name, actors[1].pc_type))
        Combat(actors)

    def get_initiative_order(self) -> None:
        self.actors = sm_helpers.get_actor_list_by_stat(self.actors, 'cur_dex', 'level')

    def get_teams(self) -> None:
        self.teams: Dict = {}
        for actor in self.actors:
            if actor.pc_type not in self.teams:
                self.teams.update(
                    {
                        actor.pc_type: []
                    }
                )
            self.teams[actor.pc_type].append(actor.name)
