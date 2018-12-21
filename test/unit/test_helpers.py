import pytest
import unittest

from unittest.mock import patch

from squirrel_maze.resources import helpers
from squirrel_maze.resources import actor

class TestHelper(unittest.TestCase):

    @patch('squirrel_maze.resources.helpers.random.randint', return_value = 6, autospec=True)
    def test_get_rand_val(self, mock_rand):
        test_rand_num = helpers.get_rand_val(1, 10)
        assert test_rand_num == 6
        mock_rand.assert_called_with(1, 10)

    def test_is_critical_hit_true(self):
        assert helpers.is_critical_hit(10, 10) is True

    def test_is_critical_hit_false(self):
        assert helpers.is_critical_hit(1, 10) is False
        assert helpers.is_critical_hit(5, 10) is False
        assert helpers.is_critical_hit(9, 10) is False

    def test_is_critical_fail_true(self):
        assert helpers.is_critical_fail(1, 1) is True

    def test_is_critical_fail_false(self):
        assert helpers.is_critical_fail(10, 1) is False
        assert helpers.is_critical_fail(4, 1) is False
        assert helpers.is_critical_fail(2, 1) is False

    @patch('squirrel_maze.resources.helpers.random.randint', return_value = 6, autospec=True)
    def test_get_crit_hit_bonus(self, mock_rand):
        value = helpers.get_crit_hit_bonus() 

        assert value == 3
        mock_rand.assert_called_with(1, 10)

    @patch('squirrel_maze.resources.helpers.random.randint', return_value = 6, autospec=True)
    def test_get_crit_fail_bonus(self, mock_rand):
        value = helpers.get_crit_fail_bonus() 

        assert value == -3
        mock_rand.assert_called_with(1, 10)

    def test_get_stat_list(self):
        test_stats = ["hp", "str", "dex", "sta", "wil",
                     "crit_hit_chance", "crit_fail_chance"]

        assert test_stats == helpers.get_stat_list()

    def test_calc_magic_defense(self):
        source_actor = actor.Actor(level=10, max_wil=5)
        target_actor = actor.Actor(level=10, max_wil=8)

        md = helpers.calc_magic_defense(source_actor, target_actor)

        assert md == -3

    def test_any_members_active(self):
        actors = []
        actors.append(actor.Actor(max_hp=10, pc_type="pc"))
        actors.append(actor.Actor(max_hp=0, pc_type="pc"))
        actors.append(actor.Actor(max_hp=0, pc_type="npc"))

        assert helpers.any_members_active(actors, "pc") == True

    def test_get_max_stat_from_actor_list(self):
        actors = []
        actors.append(actor.Actor(name='foo', level=1, max_dex=10))
        actors.append(actor.Actor(name='bar', level=2, max_dex=5))
        actors.append(actor.Actor(name='baz', level=1, max_dex=15))

        max_val = helpers.get_max_stat_from_actor_list(actors, 'cur_dex')
        assert max_val == 15

    # TODO: write a test with tie
    def test_get_actor_list_by_stat_no_tie(self):
        actors = []
        actors.append(actor.Actor(name='foo', level=1, max_dex=10))
        actors.append(actor.Actor(name='bar', level=2, max_dex=5))
        actors.append(actor.Actor(name='baz', level=1, max_dex=15))

        sorted_actors = helpers.get_actor_list_by_stat(actors, "cur_dex")

        assert sorted_actors[0].name == 'baz'

    # TODO: write a test where levels are same, random solves ties
    def test_break_tie_between_actors_different_levels(self):
        actors = []
        actors.append(actor.Actor(name='bar', level=1, max_dex=15))
        actors.append(actor.Actor(name='baz', level=4, max_dex=15))
        actors.append(actor.Actor(name='red', level=2, max_dex=15))

        sorted_actors = helpers.break_tie_between_actors(actors, "cur_dex")

        assert sorted_actors[0].name == 'baz'
