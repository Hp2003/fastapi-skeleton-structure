from lib.command import BaseCommand
from lib.connect_to_db import DatabaseContext
from sqlalchemy import text

class Command(BaseCommand, DatabaseContext):
    command = "connection"

    def __init__(self) :
        pass

    def run(self) -> bool:
        response = self.exec_query("SELECT * FROM users;", fetch=False)
        print(response.one())
        return True