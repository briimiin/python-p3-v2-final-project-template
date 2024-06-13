from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Dealership(Base):
    __tablename__ = "dealerships"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String, index=True)

    cars = relationship("Car", back_populates="dealership")
