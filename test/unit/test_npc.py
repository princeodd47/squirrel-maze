import unittest

from squirrel_maze.resources import npc
from squirrel_maze.resources import actor


class TestNpc(unittest.TestCase):

    def test_get_goblin_defaults(self):
        test_gob = npc.get_goblin()

        assert isinstance(test_gob, actor.Actor)
        assert test_gob.name == 'Goblin'
        assert test_gob.pc_type == 'npc'
        assert test_gob.affiliation == 'unfriendly'

    def test_get_big_goblin_not_defaults(self):
        test_gob = npc.get_big_goblin(name='Fooblin', pc_type='pc', affiliation='friendly')

        assert isinstance(test_gob, actor.Actor)
        assert test_gob.name == 'Fooblin'
        assert test_gob.pc_type == 'pc'
        assert test_gob.affiliation == 'friendly'
