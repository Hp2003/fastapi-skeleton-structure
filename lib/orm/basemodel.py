from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped as AlchemyMapped
from lib.database.connect_to_db import DatabaseContext
from sqlalchemy.orm import mapped_column as alchemy_mapped_column
from sqlalchemy import String
from sqlalchemy import select
from sqlalchemy.dialects import postgresql

def mapped_column(*args, **kwargs) :
    return alchemy_mapped_column(*args, **kwargs)

class Mapped(AlchemyMapped):
    pass

class Base(DeclarativeBase, DatabaseContext):

    def find(self, id : int) :
        stmt = select(User).where(User.id == id)
        compiled = stmt.compile(
            dialect=postgresql.dialect(),
            compile_kwargs={"literal_binds": True}
        )
        self.__qs = str(compiled)
        response = self.exec_query(self.__qs, id)
        
        return response.first()

class User(Base) :
    __tablename__ = "users"

    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(255))
    email : Mapped[str] = mapped_column(String(255))
    password : Mapped[str] = mapped_column(String(255))