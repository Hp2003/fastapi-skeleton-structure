from typing import Any

class Registery :

    __instances = {}

    def __init__(self) -> None:
        pass

    def register(self, key : str, value : Any) -> None:
        self.__instances[key] = value

    def get(self, key : str) -> Any | None:
        return self.__instances.get(key)

    def __str__(self) -> str:
        return str(self.__instances)
