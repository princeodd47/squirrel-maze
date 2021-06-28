from tinydb import TinyDB, Query

from squirrel_maze.resources.actor import Actor


class Database:
    def __init__(self, db_file: str):
        self.db = TinyDB(db_file)

    def close(self) -> None:
        self.db.close()

    def get_table(self, table_name: str):  # type: ignore
        return self.db.table(table_name)

    def get_table_contents(self, table_name):  # type: ignore
        return self.db.table(table_name).all()

    def get_next_index(self, key):  # type: ignore
        index_contents = self.get_table_contents('next_index')
        return index_contents[0][key]

    def get_actor(self, actor_id: int, pc_type: str = 'npc', affiliation: str = 'friendly') -> Actor:
        db_actor = self.get_actor_by_id(actor_id)
        return Actor(name=db_actor['name'], stats={'level': db_actor['attributes']['level'],
                     'max_str': db_actor['attributes']['str'], 'max_dex': db_actor['attributes']['dex'],
                     'max_sta': db_actor['attributes']['sta'], 'max_hp': db_actor['attributes']['hp']},
                     pc_type=pc_type, affiliation=affiliation, actor_id=actor_id)

    def get_actor_by_id(self, actor_id: int) -> dict:
        actor_table = self.get_table('actors')
        ActorQuery = Query()
        actor = actor_table.search(ActorQuery.id == actor_id)
        return actor[0]

    def get_location(self, location_id: int) -> dict:
        location_table = self.get_table('locations')
        LocationQuery = Query()
        return location_table.search(LocationQuery.id == location_id)
