import unittest
import resources.action as action

class TestAction(unittest.TestCase):

    def test_is_critical_hit():
        #self.assertTrue(action.is_critical_hit(10, 10))
        pass

    def test_is_critical_hit():
        #self.assertFalse(action.is_critical_hit(1, 5))
        pass

    def test_is_critical_fail():
        #self.assertTrue(action.is_critical_fail(1, 1))
        pass

    def test_is_critical_fail():
        #self.assertFalse(action.is_critical_fail(5, 1))
        pass

    def test_get_crit_hit_bonus():
        pass

    def test_get_crit_fail_bonus():
        pass

if __name__ == '__main__':
    unittest.main()
