from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Urls(Base):
    __tablename__ = "URLS"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_url: Mapped[str]
    short_url: Mapped[str]