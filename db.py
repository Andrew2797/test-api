from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column


engine = create_engine("sqlite:///races.db")
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


def create_db():
    Base.metadata.create_all(bind=engine)


class Race(Base):
    __tablename__ = "races"

    id: Mapped[int] = mapped_column(primary_key=True)
    gp: Mapped[str] = mapped_column(String(100))
    laps: Mapped[str] = mapped_column(String())