import unittest

from unittest.mock import patch

from squirrel_maze.resources import action
from squirrel_maze.resources import actor


class TestAction(unittest.TestCase):

    @patch('squirrel_maze.resources.actor.Actor.get_atk_value', return_value=24, autospec=True)
    @patch('squirrel_maze.resources.actor.Actor.get_def_value', return_value=15, autospec=True)
    def test_fight(self, mock_atk, mock_def):
        source_actor = actor.Actor()
        target_actor = actor.Actor(max_hp=20)
        action.fight(source_actor, target_actor)
        assert target_actor.cur_hp == 11

    @patch('squirrel_maze.resources.action.helpers.random.randint', return_value=2, autospec=True)
    @patch('squirrel_maze.resources.action.helpers.calc_magic_defense', return_value=-1, autospec=True)
    def test_fire_bolt(self, mock_rand, mock_md):
        source_actor = actor.Actor(level=10, max_wil=5)
        target_actor = actor.Actor(level=10, max_wil=6)

        dmg = action.fire_bolt(source_actor, target_actor)
        assert dmg[0]['element'] == "fire"
        assert dmg[0]['damage'] == 11
