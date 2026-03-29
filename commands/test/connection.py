from lib.command import BaseCommand
from bootstrap.connect_to_db import DatabaseContext
from sqlalchemy import text

class Command(BaseCommand, DatabaseContext):
    command = "connection"

    def __init__(self) :
        pass

    def run(self) -> bool:
        self.exec_query("INSERT INTO users (id, name, email, password) VALUES (1, 'John Doe', 'john@example.com', 'password');")
        return True