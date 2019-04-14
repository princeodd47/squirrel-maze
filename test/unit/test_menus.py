from unittest.mock import patch

from squirrel_maze.resources import menus


@patch('squirrel_maze.resources.menus.main_menu')
def test_go_to_menu_main(mock_main):
    menus.go_to_menu('main')
    mock_main.assert_called_once()


@patch('squirrel_maze.resources.menus.combat_menu')
def test_go_to_menu_combat(mock_combat):
    menus.go_to_menu('combat')
    mock_combat.assert_called_once()
