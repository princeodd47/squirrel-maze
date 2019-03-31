from tinydb import TinyDB, Query

from squirrel_maze.resources import actor as sm_actor


class Database:
    def __init__(self, db_file):
        self.db = TinyDB(db_file)

    def get_table(self, table_name):
        return self.db.table(table_name)

    def get_actor(self, table_name, actor_name, pc_type='npc', affiliation='friendly', actor_id=0):
        actor_table = self.get_table(table_name)
        ActorQuery = Query()
        db_actor = actor_table.search(ActorQuery.name == actor_name)
        return sm_actor.Actor(name=db_actor[0]['name'], level=db_actor[0]['attributes']['level'],
                              max_str=db_actor[0]['attributes']['str'], max_dex=db_actor[0]['attributes']['dex'],
                              max_sta=db_actor[0]['attributes']['sta'], max_hp=db_actor[0]['attributes']['hp'],
                              pc_type=pc_type, affiliation=affiliation, actor_id=actor_id)
