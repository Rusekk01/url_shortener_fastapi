from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Urls(Base):
    __tablename__ = "URLS"

    short_url: Mapped[str] = mapped_column(primary_key=True)
    full_url: Mapped[str]