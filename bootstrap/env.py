import os
from dotenv import load_dotenv

load_dotenv()

class Env :
    def __init__(self) -> None:
        pass

    def get(key : str) -> str | None:
        return os.getenv(key)