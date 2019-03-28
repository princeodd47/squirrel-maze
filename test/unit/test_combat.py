import unittest

# from unittest.mock import patch

from squirrel_maze.resources import actor
from squirrel_maze.resources import combat


class TestCombat(unittest.TestCase):

    def get_multiple_actors(self):
        actors = []
        actors.append(actor.Actor(actor_id=0, name='spam', pc_type='pc', level=1, max_hp=10, max_str=10,
                      max_dex=10, max_sta=10))
        actors.append(actor.Actor(actor_id=1, name='eggs', pc_type='pc', level=1, max_hp=5, max_str=5,
                      max_dex=5, max_sta=5))
        actors.append(actor.Actor(actor_id=2, name='foo', pc_type='npc', level=1, max_hp=6, max_str=6,
                      max_dex=6, max_sta=6))
        actors.append(actor.Actor(actor_id=3, name='bar', pc_type='npc', level=1, max_hp=6, max_str=6,
                      max_dex=6, max_sta=6))
        actors.append(actor.Actor(actor_id=4, name='baz', pc_type='npc', level=1, max_hp=2, max_str=2,
                      max_dex=2, max_sta=2))
        return actors

    def test_initialize(self):
        combat_ham = combat.Combat(self.get_multiple_actors())

        assert isinstance(combat_ham, combat.Combat)
        assert combat_ham.round == 0

    def test_get_teams(self):
        combat_ham = combat.Combat(self.get_multiple_actors())
        combat_ham.get_teams()
        assert 'pc' in combat_ham.teams
        assert 'npc' in combat_ham.teams
        assert len(combat_ham.teams) == 2
        assert combat_ham.teams['pc'] == ['spam', 'eggs']
        assert combat_ham.teams['npc'] == ['foo', 'bar', 'baz']
