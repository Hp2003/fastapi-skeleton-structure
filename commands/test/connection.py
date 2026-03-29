from lib.comamnds.command import BaseCommand
from lib.orm.basemodel import User

class Command(BaseCommand):
    command = "connection"

    def __init__(self) :
        pass

    def run(self) -> bool:
        user = User()
        user_mike = User() 

        user = user.find(2)
        print(user.name)
        user_mike=user_mike.find(1)
        print(user_mike.name)

        return True