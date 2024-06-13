from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from .database import Base

class SalesRecord(Base):
    __tablename__ = "sales_records"
# foreign key
    car_id = Column(Integer, ForeignKey('cars.id'))
    sale_date = Column(Date, index=True)
    price = Column(Float, index=True)
    buyer_name = Column(String, index=True)

    __table_args__ = (
        # composite key
        PrimaryKeyConstraint('car_id', 'sale_date'),
    )

    car = relationship("Car", back_populates="sales_records")
