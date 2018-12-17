import pytest
import unittest
from unittest.mock import MagicMock, patch, call

from squirrel_maze.resources import actor

class TestActor(unittest.TestCase):

    def test_initialize(self):
        actor_foo = actor.Actor()

        self.assertTrue(isinstance(actor_foo, actor.Actor))
        assert actor_foo.name == "unknown"

    def test_set_stats(self):
        actor_foo = actor.Actor()

        actor_foo.set_stats(1, 2, 3, 4, 5)

        assert actor_foo.max_hp == 1
        assert actor_foo.max_str == 2
        assert actor_foo.max_dex == 3
        assert actor_foo.max_sta == 4
        assert actor_foo.max_wil == 5

    def test_modify_stat(self):
        actor_foo = actor.Actor(max_hp = 10)

        actor_foo.modify_stat("max_hp", 5)
        assert actor_foo.max_hp == 15

        actor_foo.modify_stat("max_hp", -3)
        assert actor_foo.max_hp == 12

    def test_change_attribute(self):
        actor_foo = actor.Actor(max_hp = 10)

        actor_foo.change_attribute("max_hp", 2)
        assert actor_foo.max_hp == 2

        actor_foo.change_attribute("max_hp", 99)
        assert actor_foo.max_hp == 99

    def test_restore_stat_to_max(self):
        actor_foo = actor.Actor(max_hp = 10)

        actor_foo.modify_stat("cur_hp", -5)
        actor_foo.restore_stat_to_max("hp")
        assert actor_foo.max_hp == 10

        actor_foo.change_attribute("cur_hp", 2)
        actor_foo.restore_stat_to_max("hp")
        assert actor_foo.max_hp == 10

    @patch('squirrel_maze.resources.actor.Actor.restore_stat_to_max')
    def test_restore_all_stats_to_max(self, mock_restore):
        calls = [
                call("hp"),
                call("str"),
                call("dex"),
                call("sta"),
                call("wil"),
                call("crit_hit_chance"),
                call("crit_fail_chance")
                ]
        actor_foo = actor.Actor()
        actor_foo.restore_all_stats_to_max()
        mock_restore.assert_has_calls(calls, any_order=True)

    @patch('squirrel_maze.resources.actor.helpers.random.randint', return_value = 6, autospec=True)
    def test_get_atk_value(self, mock_rand):
        actor_foo = actor.Actor(max_str=10, max_dex=10)
        atk_val = actor_foo.get_atk_value()
        assert atk_val == 26

    @patch('squirrel_maze.resources.actor.helpers.random.randint', return_value = 6, autospec=True)
    def test_get_def_value(self, mock_rand):
        actor_foo = actor.Actor(max_sta=10, max_dex=10)
        atk_val = actor_foo.get_def_value()
        assert atk_val == 26

    # TODO: Add to integration tests
    #def test_restore_all_stats_to_max(self):
    #    actor_foo = actor.Actor(
    #            max_hp = 10, max_str = 10, max_dex = 10, max_sta = 10)
    #    actor_foo.modify_stat("cur_hp", -1)
    #    actor_foo.modify_stat("cur_str", -2)
    #    actor_foo.modify_stat("cur_dex", -3)
    #    actor_foo.modify_stat("cur_sta", -4)
    #    actor_foo.modify_stat("cur_crit_hit_chance", -5)
    #    actor_foo.modify_stat("cur_crit_fail_chance", 6)

    #    actor_foo.restore_all_stats_to_max()

    #    self.assertTrue(actor_foo.max_hp == 10)
    #    self.assertTrue(actor_foo.max_str == 10)
    #    self.assertTrue(actor_foo.max_dex == 10)
    #    self.assertTrue(actor_foo.max_sta == 10)
    #    self.assertTrue(actor_foo.max_crit_hit_chance == 10)
    #    self.assertTrue(actor_foo.max_crit_fail_chance == 1)


