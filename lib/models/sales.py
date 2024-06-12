from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class SalesRecord(Base):
    __tablename__ = "sales_records"

    car_id = Column(Integer, ForeignKey('cars.id'), primary_key=True)
    sale_date = Column(Date, primary_key=True)
    price = Column(Integer)
    buyer_name = Column(String)

    # Define the relationship with Car
    car = relationship("Car", back_populates="sales_records")
