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

def display_dealerships():
    session = SessionLocal()
    dealerships = session.query(Dealership).all()
    if not dealerships:
        print("No dealerships available.")
    else:
        print("List of dealerships:")
        for dealership in dealerships:
            print(f"ID: {dealership.id}, Name: {dealership.name}, Location: {dealership.location}")
    session.close()

def search_car():
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = int(input("Enter car year: "))
    session = SessionLocal()
    car = session.query(Car).filter_by(make=make, model=model, year=year).first()
    if car:
        print(f"Car found: Make: {car.make}, Model: {car.model}, Year: {car.year}, Dealership ID: {car.dealership_id}")
    else:
        print("Car not found.")
    session.close()

def display_all_cars():
    session = SessionLocal()
    cars = session.query(Car).all()
    if not cars:
        print("No cars available.")
    else:
        print("List of cars:")
        for car in cars:
            print(f"ID: {car.id}, Make: {car.make}, Model: {car.model}, Year: {car.year}, Dealership ID: {car.dealership_id}")
    session.close()
