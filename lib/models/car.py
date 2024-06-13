from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, index=True)
    model = Column(String, index=True)
    year = Column(Integer, index=True)
    dealership_id = Column(Integer, ForeignKey('dealerships.id'))

    dealership = relationship("Dealership", back_populates="cars")
    sales_records = relationship("SalesRecord", back_populates="car")
