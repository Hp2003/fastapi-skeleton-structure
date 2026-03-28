from abc import ABC, abstractmethod

class BaseCommand(ABC):
    command = ""

    class Option:
        def __init__(self, default=None, **kwargs):
            self.default = default
            self.metadata = kwargs

    @abstractmethod
    def run(self):
        pass
