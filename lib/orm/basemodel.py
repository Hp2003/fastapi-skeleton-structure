from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped as AlchemyMapped
from lib.database.connect_to_db import DatabaseContext
from sqlalchemy.orm import mapped_column as alchemy_mapped_column
from sqlalchemy import String
from sqlalchemy import select

def mapped_column(*args, **kwargs) :
    return alchemy_mapped_column(*args, **kwargs)

class Mapped(AlchemyMapped):
    pass

class Base(DeclarativeBase, DatabaseContext):

    def __del__(self) :
        # self.db.close()
        pass
        
    def find(self, id : int) :
        stmt = select(User).where(User.id == id)
        self.__qs = self.exec_query(stmt, fetch=True)
        return self.__qs.scalar()

class User(Base) :
    __tablename__ = "users"

    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(255))
    email : Mapped[str] = mapped_column(String(255))
    password : Mapped[str] = mapped_column(String(255))