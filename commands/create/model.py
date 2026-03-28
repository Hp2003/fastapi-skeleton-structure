from typing import Annotated
from lib.command import BaseCommand

class Command(BaseCommand) :
    command = "model"

    def __init__(self, name : str, type : str = BaseCommand.Option('', help='type of model')): 
        self.name = name
        self.type = type

    def run(self):
        print(f"Creating model {self.name}, with type {self.type}")