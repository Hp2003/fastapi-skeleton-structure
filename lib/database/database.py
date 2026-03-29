from lib.database.connect_to_db import DatabaseContext

class BaseModel(DatabaseContext) :

    def exec_query(self, query : str):
        self.db.execute(query)