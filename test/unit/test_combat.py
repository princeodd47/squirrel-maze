import pytest
import unittest

from unittest.mock import patch

from squirrel_maze.resources import actor
from squirrel_maze.resources import combat

class TestCombat(unittest.TestCase):

    #@patch('squirrel_maze.resources.helpers.random.randint', return_value = 6, autospec=True)
    def test_get_initiative_order(self):
        assert True
