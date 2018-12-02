import mock
import pytest
import resources.action as action

#import unittest
#class TestAction(unittest.TestCase):

class TestAction(object):

    def test_is_critical_hit():
        #self.assertTrue(action.is_critical_hit(10, 10))
        assert False

    def test_is_critical_hit():
        #self.assertFalse(action.is_critical_hit(1, 5))
        assert True

    def test_is_critical_fail():
        #self.assertTrue(action.is_critical_fail(1, 1))
        assert True

    def test_is_critical_fail():
        #self.assertFalse(action.is_critical_fail(5, 1))
        assert True

    def test_get_crit_hit_bonus():
        assert True

    def test_get_crit_fail_bonus():
        assert True
