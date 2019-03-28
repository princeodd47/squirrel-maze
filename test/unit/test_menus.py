import unittest

from unittest.mock import patch

from squirrel_maze.resources import menus


class TestMenus(unittest.TestCase):

    @patch('squirrel_maze.resources.menus.main_menu')
    def test_go_to_menu_main(self, mock_main):
        menus.go_to_menu('main')
        mock_main.assert_called_once()

    @patch('squirrel_maze.resources.menus.combat_menu')
    def test_go_to_menu_combat(self, mock_combat):
        menus.go_to_menu('combat')
        mock_combat.assert_called_once()
