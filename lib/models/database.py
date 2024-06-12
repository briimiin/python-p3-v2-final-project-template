from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base

DATABASE_URL = "sqlite:///./dealership.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    from .dealership import Dealership
    from .car import Car
    from .sales_record import SalesRecord
    Base.metadata.create_all(bind=engine)
