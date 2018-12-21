import pytest
import unittest
from unittest.mock import MagicMock, patch, call

from squirrel_maze.resources import actor

class TestActor(unittest.TestCase):

    def get_single_actor(self):
        return actor.Actor(name='ham',pc_type='pc',level=1,max_hp=10,max_str=10,max_dex=10,max_sta=10)

    def get_multiple_actors(self):
        actors = []
        actors.append(actor.Actor(name='spam',pc_type='pc',level=1,max_hp=10,max_str=10,max_dex=10,max_sta=10))
        actors.append(actor.Actor(name='eggs',pc_type='pc',level=1,max_hp=5,max_str=5,max_dex=5,max_sta=5))
        actors.append(actor.Actor(name='foo',pc_type='npc',level=1,max_hp=6,max_str=6,max_dex=6,max_sta=6))
        actors.append(actor.Actor(name='bar',pc_type='npc',level=1,max_hp=6,max_str=6,max_dex=6,max_sta=6))
        actors.append(actor.Actor(name='baz',pc_type='npc',level=1,max_hp=2,max_str=2,max_dex=2,max_sta=2))
        return actors

    def test_initialize(self):
        actor_ham = self.get_single_actor()

        self.assertTrue(isinstance(actor_ham, actor.Actor))
        assert actor_ham.name == "ham"

    def test_set_stats(self):
        actor_ham = self.get_single_actor()

        actor_ham.set_stats(1, 2, 3, 4, 5)

        assert actor_ham.max_hp == 1
        assert actor_ham.max_str == 2
        assert actor_ham.max_dex == 3
        assert actor_ham.max_sta == 4
        assert actor_ham.max_wil == 5

    def test_modify_stat(self):
        actor_ham = self.get_single_actor()

        actor_ham.modify_stat("max_hp", 5)
        assert actor_ham.max_hp == 15

        actor_ham.modify_stat("max_hp", -3)
        assert actor_ham.max_hp == 12

    def test_change_attribute(self):
        actor_ham = self.get_single_actor()

        actor_ham.change_attribute("max_hp", 2)
        assert actor_ham.max_hp == 2

        actor_ham.change_attribute("max_hp", 99)
        assert actor_ham.max_hp == 99

    def test_restore_stat_to_max(self):
        actor_ham = self.get_single_actor()

        actor_ham.modify_stat("cur_hp", -5)
        actor_ham.restore_stat_to_max("hp")
        assert actor_ham.max_hp == 10

        actor_ham.change_attribute("cur_hp", 2)
        actor_ham.restore_stat_to_max("hp")
        assert actor_ham.max_hp == 10

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
        actor_ham = self.get_single_actor()
        actor_ham.restore_all_stats_to_max()
        mock_restore.assert_has_calls(calls, any_order=True)

    @patch('squirrel_maze.resources.actor.helpers.random.randint', return_value = 6, autospec=True)
    def test_get_atk_value(self, mock_rand):
        actor_ham = self.get_single_actor()
        atk_val = actor_ham.get_atk_value()
        assert atk_val == 26

    @patch('squirrel_maze.resources.actor.helpers.random.randint', return_value = 6, autospec=True)
    def test_get_def_value(self, mock_rand):
        actor_ham = self.get_single_actor()
        atk_val = actor_ham.get_def_value()
        assert atk_val == 26

    def test_get_friendly_actors(self):
        actor_ham = self.get_single_actor()
        actors = self.get_multiple_actors()

        friendlies = actor_ham.get_friendly_actors(actors)
        assert len(friendlies) == 2
        assert (
                all([x.pc_type is 'pc' for x in friendlies])
        ) is True

    def test_get_unfriendly_actors(self):
        actor_ham = self.get_single_actor()
        actors = self.get_multiple_actors()

        unfriendlies = actor_ham.get_unfriendly_actors(actors)
        assert len(unfriendlies) == 3
        assert (
                all([x.pc_type is not 'pc' for x in unfriendlies])
        ) is True

    # TODO: Add to integration tests
    #def test_restore_all_stats_to_max(self):
    #    actor_ham = actor.Actor(
    #            max_hp = 10, max_str = 10, max_dex = 10, max_sta = 10)
    #    actor_ham.modify_stat("cur_hp", -1)
    #    actor_ham.modify_stat("cur_str", -2)
    #    actor_ham.modify_stat("cur_dex", -3)
    #    actor_ham.modify_stat("cur_sta", -4)
    #    actor_ham.modify_stat("cur_crit_hit_chance", -5)
    #    actor_ham.modify_stat("cur_crit_fail_chance", 6)

    #    actor_ham.restore_all_stats_to_max()

    #    self.assertTrue(actor_ham.max_hp == 10)
    #    self.assertTrue(actor_ham.max_str == 10)
    #    self.assertTrue(actor_ham.max_dex == 10)
    #    self.assertTrue(actor_ham.max_sta == 10)
    #    self.assertTrue(actor_ham.max_crit_hit_chance == 10)
    #    self.assertTrue(actor_ham.max_crit_fail_chance == 1)


