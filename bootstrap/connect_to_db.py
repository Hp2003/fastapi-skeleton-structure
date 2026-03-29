from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from bootstrap.env import Env
from sqlalchemy.engine.cursor import CursorResult

class DatabaseManager:
    _engine = None
    _SessionLocal = None

    @classmethod
    def get_session_factory(cls):
        if cls._engine is None:
            # Build connection string ONCE
            connection_type = Env.get('DB_CONNECTION')
            parser = ConnectionParser(
                db_name=Env.get('DB_NAME'),
                user=Env.get('DB_USER'),
                password=Env.get('DB_PASSWORD'),
                host=Env.get('DB_HOST'),
                port=Env.get('DB_PORT')
            )
            
            if connection_type == 'postgresql':
                url = parser.get_postgres_connection()
            elif connection_type == 'mysql':
                url = parser.get_mysql_connection()
            else:
                url = parser.get_sqlite_connection()

            # Create ONE engine for the whole app
            cls._engine = create_engine(url, pool_size=10, max_overflow=20)
            cls._SessionLocal = sessionmaker(bind=cls._engine)
            
        return cls._SessionLocal

class DatabaseContext:

    def __enter__(self):
        # Grab the existing shared factory
        session_factory = DatabaseManager.get_session_factory()
        self.db = session_factory()
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        try :
            if exc_type:
                self.db.rollback()
            else:
                self.db.commit()
        finally :
            self.db.close()

    def exec_query(self, query : str, fetch : bool = False) -> CursorResult | list:
        with self as db_session :
            response = db_session.execute(text(query))
            if fetch :
                return response.fetchall()
            return response
        
        return None

class ConnectionParser :
    def __init__(
     self, 
     user : str | None = None,
     password : str | None = None,
     host : str | None = None,
     port : int | None = None,
     db_name : str | None = None
     ) -> None:
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db_name = db_name

    def get_postgres_connection(self) :
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"

    def get_mysql_connection(self) :
        return f"mysql+mysqlconnector://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"

    def get_sqlite_connection(self) :
        return f"sqlite:///{self.db_name}"