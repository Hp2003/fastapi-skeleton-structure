import os
from dotenv import load_dotenv

class LoadEnv :
    env = {}

    @staticmethod
    def scan_env_file(path : str = os.path.join(os.getcwd(), ".env")) -> None:
        if not LoadEnv.env :
            print("Loading environment variables...")
            if os.path.exists(path) :
                load_dotenv(path)
            else :
                raise Exception(f'Env file not found at {path}')
            LoadEnv.env = dict(os.environ)

class Env:

    LoadEnv.scan_env_file()
    
    @staticmethod
    def get(key: str, default: str | None = None) -> str:
        return LoadEnv.env.get(key, default)

    @staticmethod
    def get_int(key: str, default: int = 0) -> int:
        value = LoadEnv.env.get(key)
        return int(value) if value is not None else default

    @staticmethod
    def get_bool(key: str, default: bool = False) -> bool:
        value = LoadEnv.env.get(key, str(default)).lower()
        return value in ("true", "1", "yes", "on")

    @staticmethod
    def required(key: str) -> str:
        value = LoadEnv.env.get(key)
        if value is None:
            raise KeyError(f"Critical Environment Variable Missing: {key}")
        return value