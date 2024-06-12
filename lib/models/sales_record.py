from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from .base import Base

class SalesRecord(Base):
    __tablename__ = "sales_records"

    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey('cars.id'))
    sale_date = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    buyer_name = Column(String, nullable=False)

    car = relationship("Car", back_populates="sales_records")
