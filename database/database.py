from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///database/dossier.db"

engine = create_engine(url=DATABASE_URL,
                       echo=True,
                       pool_size=5,
                       max_overflow=10)

SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)
