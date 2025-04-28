from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Dossier(Base):
    """
    Model of dossier block
    """
    __tablename__ = 'dossier'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    gender: Mapped[str]
    date_of_birth: Mapped[str]
    birthplace: Mapped[str]
    location_address: Mapped[str]
    driver_licence: Mapped[str]
    occupation: Mapped[str]
    education: Mapped[str]
    social_rating: Mapped[int]
    social_rating_type: Mapped[str]
