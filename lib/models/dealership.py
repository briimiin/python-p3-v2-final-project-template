from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Dealership(Base):
    __tablename__ = "dealerships"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)

    cars = relationship("Car", back_populates="dealership")
