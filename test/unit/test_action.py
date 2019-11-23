from unittest.mock import patch, call

from squirrel_maze.resources import action
from squirrel_maze.resources import actor


@patch('squirrel_maze.resources.actor.Actor.get_atk_value', return_value=24, autospec=True)
@patch('squirrel_maze.resources.actor.Actor.get_def_value', return_value=15, autospec=True)
def test_fight(mock_atk, mock_def):
    source_actor = actor.Actor()
    target_actor = actor.Actor(stats={'max_hp': 20})
    action.fight(source_actor, target_actor)
    assert target_actor.cur_hp == 11


@patch('squirrel_maze.resources.actor.Actor.get_atk_value', return_value=10, autospec=True)
@patch('squirrel_maze.resources.actor.Actor.get_def_value', return_value=15, autospec=True)
def test_fight_min_damage(mock_atk, mock_def):
    source_actor = actor.Actor()
    target_actor = actor.Actor(stats={'max_hp': 20})
    action.fight(source_actor, target_actor)
    assert target_actor.cur_hp == 19


@patch('squirrel_maze.resources.action.fight')
def test_fight_all(mock_fight):
    source_actor = actor.Actor()
    target = actor.Actor(stats={'max_hp': 20})
    targets = [
        target,
        target,
        target,
    ]
    action.fight_all(source_actor, targets)
    mock_fight.assert_has_calls([
        call(source_actor, target),
        call(source_actor, target),
        call(source_actor, target)
    ])


@patch('squirrel_maze.resources.action.helpers.random.randint', return_value=2, autospec=True)
@patch('squirrel_maze.resources.action.helpers.calc_magic_defense', return_value=-1, autospec=True)
def test_fire_bolt(mock_rand, mock_md):
    source_actor = actor.Actor(level=10, stats={'max_wil': 5})
    target_actor = actor.Actor(level=10, stats={'max_wil': 6})

    dmg = action.fire_bolt(source_actor, target_actor)
    assert dmg[0]['element'] == "fire"
    assert dmg[0]['damage'] == 11
