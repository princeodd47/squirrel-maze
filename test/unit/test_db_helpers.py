import unittest

from squirrel_maze.resources import db_helpers


class TestDbHelper(unittest.TestCase):
    def test_get_actor(self):
        db = db_helpers.Database('test/unit/test_files/db.json')
        actor = db.get_actor('pcs', 'Ham', affiliation='unfriendly')
        assert actor.name == 'Ham'
        assert actor.max_hp == 10
        assert actor.pc_type == 'npc'
        assert actor.affiliation == 'unfriendly'
