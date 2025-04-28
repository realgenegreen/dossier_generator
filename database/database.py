from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base, Dossier, JSONDossier

DATABASE_URL = "sqlite:///database/dossier.db"

engine = create_engine(url=DATABASE_URL,
                       echo=True,
                       pool_size=5,
                       max_overflow=10)

SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)

Base.metadata.create_all(bind=engine)


def update_table(data) -> None:
    """Function that parses JSON and collects data to DB"""
    dossier = JSONDossier(**data)
    db: Session = SessionLocal()
    try:
        item = Dossier(
            id=dossier.id,
            name=dossier.name,
            gender=dossier.gender,
            date_of_birth=dossier.date_of_birth,
            birthplace=dossier.birthplace,
            location_address=dossier.location_address,
            driver_licence=dossier.driver_licence,
            occupation=dossier.occupation,
            education=dossier.education,
            social_rating=dossier.social_rating,
            social_rating_type=dossier.social_rating_type
        )

        db.add(item)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error saving data: {e}")
    finally:
        db.close()
