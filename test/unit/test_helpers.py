import pytest
from unittest.mock import patch

from squirrel_maze.resources import actor
from squirrel_maze.resources import helpers
from . import helpers as test_helpers


@patch('squirrel_maze.resources.helpers.random.randint', return_value=6, autospec=True)
def test_get_rand_val(mock_rand):
    test_rand_num = helpers.get_rand_val(1, 10)
    assert test_rand_num == 6
    mock_rand.assert_called_with(1, 10)


def test_is_critical_hit_true():
    assert helpers.is_critical_hit(10, 10) is True


def test_is_critical_hit_false():
    assert helpers.is_critical_hit(1, 10) is False
    assert helpers.is_critical_hit(5, 10) is False
    assert helpers.is_critical_hit(9, 10) is False


def test_is_critical_fail_true():
    assert helpers.is_critical_fail(1, 1) is True


def test_is_critical_fail_false():
    assert helpers.is_critical_fail(10, 1) is False
    assert helpers.is_critical_fail(4, 1) is False
    assert helpers.is_critical_fail(2, 1) is False


@patch('squirrel_maze.resources.helpers.random.randint', return_value=6, autospec=True)
def test_get_crit_hit_bonus(mock_rand):
    value = helpers.get_crit_hit_bonus()

    assert value == 3
    mock_rand.assert_called_with(1, 10)


@patch('squirrel_maze.resources.helpers.random.randint', return_value=6, autospec=True)
def test_get_crit_fail_bonus(mock_rand):
    value = helpers.get_crit_fail_bonus()

    assert value == -3
    mock_rand.assert_called_with(1, 10)


def test_get_stat_list():
    test_stats = ['hp', 'str', 'dex', 'sta', 'wil',
                  'crit_hit_chance', 'crit_fail_chance']

    assert test_stats == helpers.get_stat_list()


def test_calc_magic_defense():
    source_actor = actor.Actor(stats={'level': 10, 'max_str': 0, 'max_dex': 0, 'max_sta': 0, 'max_wil': 5, 'max_hp': 0})
    target_actor = actor.Actor(stats={'level': 10, 'max_str': 0, 'max_dex': 0, 'max_sta': 0, 'max_wil': 8, 'max_hp': 0})

    assert helpers.calc_magic_defense(source_actor, target_actor) == -3


def test_any_members_alive():
    actors = []
    actors.append(actor.Actor(stats={'level': 10, 'max_str': 0, 'max_dex': 0, 'max_sta': 0, 'max_wil': 5, 'max_hp': 10},
                  pc_type='pc'))
    actors.append(actor.Actor(stats={'level': 10, 'max_str': 0, 'max_dex': 0, 'max_sta': 0, 'max_wil': 5, 'max_hp': 0},
                  pc_type='pc'))
    actors.append(actor.Actor(stats={'level': 10, 'max_str': 0, 'max_dex': 0, 'max_sta': 0, 'max_wil': 5, 'max_hp': 0},
                  pc_type='npc'))

    assert helpers.any_members_alive(actors, 'pc') is True


def test_any_members_alive_false():
    actors = []
    actors.append(actor.Actor(stats={'level': 10, 'max_str': 0, 'max_dex': 0, 'max_sta': 0, 'max_wil': 5, 'max_hp': 0},
                  pc_type='pc'))
    actors.append(actor.Actor(stats={'level': 10, 'max_str': 0, 'max_dex': 0, 'max_sta': 0, 'max_wil': 5, 'max_hp': 0},
                  pc_type='pc'))
    actors.append(actor.Actor(stats={'level': 10, 'max_str': 0, 'max_dex': 0, 'max_sta': 0, 'max_wil': 5, 'max_hp': 0},
                  pc_type='npc'))

    assert helpers.any_members_alive(actors, 'pc') is False
    assert helpers.any_members_alive(actors, 'npc') is False


def test_get_max_stat_from_actor_list():
    actors = []
    actors.append(actor.Actor(stats={'level': 10, 'max_str': 0, 'max_dex': 10, 'max_sta': 0, 'max_wil': 5, 'max_hp': 0},
                  pc_type='pc', name='foo'))
    actors.append(actor.Actor(stats={'level': 10, 'max_str': 0, 'max_dex': 5, 'max_sta': 0, 'max_wil': 5, 'max_hp': 0},
                  pc_type='pc', name='bar'))
    actors.append(actor.Actor(stats={'level': 10, 'max_str': 0, 'max_dex': 15, 'max_sta': 0, 'max_wil': 5, 'max_hp': 0},
                  pc_type='pc', name='bar'))

    assert helpers.get_max_stat_from_actor_list(actors, 'cur_dex') == 15


def test_get_actor_list_by_stat():
    actors = []
    actors.append(actor.Actor(name='foo', stats={'level': 1, 'max_dex': 10}))
    actors.append(actor.Actor(name='bar', stats={'level': 2, 'max_dex': 5}))
    actors.append(actor.Actor(name='baz', stats={'level': 3, 'max_dex': 15}))
    actors.append(actor.Actor(name='ham', stats={'level': 1, 'max_dex': 15}))

    sorted_actors = helpers.get_actor_list_by_stat(actors, 'cur_dex', 'level')

    assert sorted_actors[0].name == 'baz'

@pytest.mark.parametrize('affiliation, expected_count', [('friendly', 4),('unfriendly', 2)])
def test_get_friendly_actors(affiliation, expected_count):
    actor_ham = test_helpers.get_single_actor()
    actors = test_helpers.get_multiple_actors()

    affiliation_count = helpers.get_affiliated_actors(affiliation, actors)
    assert len(affiliation_count) == expected_count
    assert (
            all([x.affiliation == affiliation for x in affiliation_count])
    ) is True
