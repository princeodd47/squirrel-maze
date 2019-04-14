import pytest

from squirrel_maze.resources import db_helpers


@pytest.fixture(scope='module')
def db_connection():
    db = db_helpers.Database('test/unit/test_files/db.json')
    yield db
    db.close()


@pytest.mark.usefixtures("db_connection")
def test_get_table_contents(db_connection):
    table_contents = db_connection.get_table_contents('next_index')
    assert table_contents == [{'npcs': 3, 'pcs': 5}]


def test_get_next_index(db_connection):
    assert db_connection.get_next_index('npcs') == 3
    assert db_connection.get_next_index('pcs') == 5


def test_get_actor(db_connection):
    actor = db_connection.get_actor('pcs', 0, affiliation='unfriendly')
    assert actor.name == 'Ham'
    assert actor.max_hp == 10
    assert actor.pc_type == 'npc'
    assert actor.affiliation == 'unfriendly'
