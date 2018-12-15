import pytest
import unittest

from squirrel_maze.resources import actor

class TestActor(unittest.TestCase):

    def test_initialize(self):
        actor_foo = actor.Actor()
        self.assertTrue(isinstance(actor_foo, actor.Actor))
        self.assertTrue(actor_foo.name == "unknown")

    def test_set_stats(self):
        actor_foo = actor.Actor()
        actor_foo.set_stats(1, 2, 3, 4)
        self.assertTrue(actor_foo.max_hp == 1)
        self.assertTrue(actor_foo.max_str == 2)
        self.assertTrue(actor_foo.max_dex == 3)
        self.assertTrue(actor_foo.max_sta == 4)

    def test_modify_stat(self):
        actor_foo = actor.Actor(max_hp = 10)
        actor_foo.modify_stat("max_hp", 5)
        self.assertTrue(actor_foo.max_hp == 15)
        actor_foo.modify_stat("max_hp", -3)
        self.assertTrue(actor_foo.max_hp == 12)

    def test_change_attribute(self):
        actor_foo = actor.Actor(max_hp = 10)
        actor_foo.change_attribute("max_hp", 2)
        self.assertTrue(actor_foo.max_hp == 2)

