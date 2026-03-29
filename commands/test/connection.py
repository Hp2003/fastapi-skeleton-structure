from lib.comamnds.command import BaseCommand
from lib.orm.basemodel import User
import time

class Command(BaseCommand):
    command = "connection"

    def __init__(self) :
        pass

    def run(self) -> bool:
        while True :
            user = User()
            user = user.find(1)
            print(user.name)
            time.sleep(5)
        return True