import pytest
import unittest

from squirrel_maze.resources import npc
from squirrel_maze.resources import actor

class TestNpc(unittest.TestCase):

    def test_get_goblin(self):
        test_gob = npc.get_goblin()

        self.assertTrue(isinstance(test_gob, actor.Actor))
        self.assertTrue(test_gob.name == "Goblin")
