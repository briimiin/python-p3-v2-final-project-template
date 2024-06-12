from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, index=True)
    model = Column(String, index=True)
    year = Column(Integer, index=True)
    dealership_id = Column(Integer, ForeignKey('dealerships.id'))

    # Define the relationship with Dealership
    dealership = relationship("Dealership", back_populates="cars")
