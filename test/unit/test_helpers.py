import pytest
import unittest

from squirrel_maze.resources import helpers

class TestHelper(unittest.TestCase):

    def test_is_critical_hit(self):
        self.assertTrue(helpers.is_critical_hit(10, 10))

    def test_is_critical_hit_false(self):
        self.assertFalse(helpers.is_critical_hit(1, 10))
        self.assertFalse(helpers.is_critical_hit(5, 10))
        self.assertFalse(helpers.is_critical_hit(9, 10))

    def test_is_critical_fail(self):
        self.assertTrue(helpers.is_critical_fail(1, 1))

    def test_is_critical_fail_false(self):
        self.assertFalse(helpers.is_critical_fail(10, 1))
        self.assertFalse(helpers.is_critical_fail(4, 1))
        self.assertFalse(helpers.is_critical_fail(2, 1))

    def test_get_crit_hit_bonus(self):
        value = helpers.get_crit_hit_bonus() 
        self.assertTrue(value > 0)

    def test_get_crit_fail_bonus(self):
        value = helpers.get_crit_fail_bonus() 
        self.assertTrue(value < 0)

    def test_get_stat_list(self):
        test_stats = ["hp", "str", "dex", "sta",
                     "crit_hit_chance", "crit_fail_chance"]
        self.assertTrue(test_stats == helpers.get_stat_list())
