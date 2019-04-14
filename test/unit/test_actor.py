from unittest.mock import patch, call

import helpers as test_helpers
from squirrel_maze.resources import actor


def test_initialize():
    actor_ham = test_helpers.get_single_actor()

    assert isinstance(actor_ham, actor.Actor) is True
    assert actor_ham.name == "ham"
    assert actor_ham.affiliation == "friendly"


def test_set_stats():
    actor_ham = test_helpers.get_single_actor()

    actor_ham.set_stats(1, 2, 3, 4, 5)

    assert actor_ham.max_hp == 1
    assert actor_ham.max_str == 2
    assert actor_ham.max_dex == 3
    assert actor_ham.max_sta == 4
    assert actor_ham.max_wil == 5


def test_modify_stat():
    actor_ham = test_helpers.get_single_actor()

    actor_ham.modify_stat("max_hp", 5)
    assert actor_ham.max_hp == 15

    actor_ham.modify_stat("max_hp", -3)
    assert actor_ham.max_hp == 12


def test_change_attribute():
    actor_ham = test_helpers.get_single_actor()

    actor_ham.change_attribute("max_hp", 2)
    assert actor_ham.max_hp == 2

    actor_ham.change_attribute("max_hp", 99)
    assert actor_ham.max_hp == 99


def test_restore_stat_to_max():
    actor_ham = test_helpers.get_single_actor()

    actor_ham.modify_stat("cur_hp", -5)
    actor_ham.restore_stat_to_max("hp")
    assert actor_ham.max_hp == 10

    actor_ham.change_attribute("cur_hp", 2)
    actor_ham.restore_stat_to_max("hp")
    assert actor_ham.max_hp == 10


@patch('squirrel_maze.resources.actor.Actor.restore_stat_to_max')
def test_restore_all_stats_to_max(mock_restore):
    calls = [
            call("hp"),
            call("str"),
            call("dex"),
            call("sta"),
            call("wil"),
            call("crit_hit_chance"),
            call("crit_fail_chance")
            ]
    actor_ham = test_helpers.get_single_actor()
    actor_ham.restore_all_stats_to_max()
    mock_restore.assert_has_calls(calls, any_order=True)


@patch('squirrel_maze.resources.actor.helpers.random.randint', return_value=6, autospec=True)
def test_get_atk_value(mock_rand):
    actor_ham = test_helpers.get_single_actor()
    atk_val = actor_ham.get_atk_value()
    assert atk_val == 26


@patch('squirrel_maze.resources.actor.helpers.random.randint', return_value=6, autospec=True)
def test_get_def_value(mock_rand):
    actor_ham = test_helpers.get_single_actor()
    atk_val = actor_ham.get_def_value()
    assert atk_val == 26


def test_get_friendly_actors():
    actor_ham = test_helpers.get_single_actor()
    actors = test_helpers.get_multiple_actors()

    friendlies = actor_ham.get_friendly_actors(actors)
    assert len(friendlies) == 4
    assert (
            all([x.affiliation == 'friendly' for x in friendlies])
    ) is True


def test_get_unfriendly_actors():
    actor_ham = test_helpers.get_single_actor()
    actors = test_helpers.get_multiple_actors()

    unfriendlies = actor_ham.get_unfriendly_actors(actors)
    assert len(unfriendlies) == 2
    assert (
            all([x.affiliation != actor_ham.affiliation for x in unfriendlies])
    ) is True
