import pytest
from unittest.mock import patch

from squirrel_maze.resources import menus


@pytest.fixture(scope='function')
def location_menu_list():
    return [{'enemy_id': 0, 'name': 'Sweegy Forest - Goblin', 'value': 0}]


@pytest.fixture(scope='function')
def mock_actor():
    return {'name': 'Goblin', 'id': 0}


@pytest.fixture(scope='function')
def mock_location():
    return {'name': 'Sweegy Forest', 'id': 0, 'npcs': 0}


@patch('squirrel_maze.resources.menus.main_menu')
def test_go_to_menu_main(mock_main):
    menus.go_to_menu('main')
    mock_main.assert_called_once()


@patch('squirrel_maze.resources.menus.combat_menu')
def test_go_to_menu_combat(mock_combat):
    menus.go_to_menu('combat')
    mock_combat.assert_called_once()


@pytest.mark.usefixtures('mock_location')
@pytest.mark.usefixtures('mock_actor')
@pytest.mark.usefixtures('location_menu_list')
def test_format_location_item(mock_location, mock_actor, location_menu_list):
    location_item = menus.format_location_item(mock_location, mock_actor)
    assert location_item == location_menu_list[0]


@patch('squirrel_maze.resources.db_helpers')
@patch('squirrel_maze.resources.db_helpers.Database.get_table_contents',
       return_value=[{'name': 'Sweegy Forest', 'id': 0, 'npcs': 0}])
@pytest.mark.usefixtures("location_menu_list")
@pytest.mark.usefixtures("mock_actor")
def test_get_locaion_menu_list(mock_db_helpers, location_contents, location_menu_list, mock_actor):
    test_location_menu_list = menus.get_location_menu_list()
    #mock_db_helpers.Database().assert_called_once()
    mock_db_helpers.Database.get_table_contents().assert_called_once()
    # mock_db_helpers.get_table_contents().assert_called_with('location')
    # mock.db_helpers.close().assert_called_once()
    # assert test_location_menu_list == location_menu_list
    pass
