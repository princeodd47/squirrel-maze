import pytest
import unittest

from unittest.mock import patch

from squirrel_maze.resources import actor
from squirrel_maze.resources import combat

class TestCombat(unittest.TestCase):

    def test_initialize(self):
        test_actors = []
        test_actors.append(actor.Actor(name='foo'))
        test_actors.append(actor.Actor(name='bar'))
        test_actors.append(actor.Actor(name='baz'))
        combat_foo = combat.Combat(test_actors)

        self.assertTrue(isinstance(combat_foo, combat.Combat))
        assert combat_foo.round == 0

    #@patch('squirrel_maze.resources.helpers.random.randint', return_value = 6, autospec=True)
    #def test_get_initiative_order(self):
    #    assert True
