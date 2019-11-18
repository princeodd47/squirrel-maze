from . import helpers as test_helpers
from squirrel_maze.resources import combat


def test_initialize():
    combat_ham = combat.Combat(test_helpers.get_multiple_actors())

    assert isinstance(combat_ham, combat.Combat)
    assert combat_ham.round == 0


def test_get_teams():
    combat_ham = combat.Combat(test_helpers.get_multiple_actors())
    combat_ham.get_teams()
    assert 'pc' in combat_ham.teams
    assert 'npc' in combat_ham.teams
    assert len(combat_ham.teams) == 2
    assert combat_ham.teams['pc'] == ['ham', 'spam', 'eggs']
    assert combat_ham.teams['npc'] == ['foo', 'bar', 'baz']
