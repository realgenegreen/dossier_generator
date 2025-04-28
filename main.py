import json

from sqlalchemy.orm import Session
from generator import dossier
from database.database import SessionLocal, engine
from database.models import Base, Dossier

Base.metadata.create_all(bind=engine)


def update_table(data):
    db: Session = SessionLocal()
    try:
        item = Dossier(
            id=data['ID'],
            name=data['Name'],
            gender=data['Gender'],
            date_of_birth=data['Date of Birth'],
            birthplace=data['Birthplace'],
            location_address=data['Location Address'],
            driver_licence=data['Driver License'],
            occupation=data['Occupation'],
            education=data['Education'],
            social_rating=data['Social Rating'],
            social_rating_type = data['Social Rating Type']
        )

        db.add(item)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error saving data: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    person = json.loads(dossier())
    print(person)
    update_table(person)
