from models.dealership import Dealership
from models.car import Car
from models.sales_record import SalesRecord
from models.database import SessionLocal
from datetime import datetime

def add_dealership():
    name = input("Enter dealership name: ")
    location = input("Enter dealership location: ")
    session = SessionLocal()
    dealership = Dealership(name=name, location=location)
    session.add(dealership)
    session.commit()
    session.close()
    print("Dealership added successfully.")

def add_car():
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = int(input("Enter car year: "))
    dealership_id = int(input("Enter dealership ID: "))
    session = SessionLocal()
    car = Car(make=make, model=model, year=year, dealership_id=dealership_id)
    session.add(car)
    session.commit()
    session.close()
    print("Car added successfully.")

def record_sale():
    car_id = int(input("Enter car ID: "))
    sale_date = input("Enter sale date (YYYY-MM-DD): ")
    price = int(input("Enter sale price: "))
    buyer_name = input("Enter buyer name: ")
    session = SessionLocal()
    sale_date_parsed = datetime.strptime(sale_date, '%Y-%m-%d')
    sale = SalesRecord(
        car_id=car_id,
        sale_date=sale_date_parsed,
        price=price,
        buyer_name=buyer_name
    )
    session.add(sale)
    session.commit()
    session.close()
    print("Sale recorded successfully.")
