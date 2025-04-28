from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from pydantic import BaseModel, Field


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


class JSONDossier(BaseModel):
    """
    Model of json for pydantic
    """
    name: str = Field(alias='Name')
    gender: str = Field(alias='Gender')
    id: int = Field(alias='ID')
    date_of_birth: str = Field(alias='Date of Birth')
    birthplace: str = Field(alias='Birthplace')
    location_address: str = Field(alias='Location Address')
    driver_licence: str = Field(alias='Driver License')
    occupation: str = Field(alias='Occupation')
    education: str = Field(alias='Education')
    social_rating: int = Field(alias='Social Rating')
    social_rating_type: str = Field(alias='Social Rating Type')
