from models import init_db, SessionLocal
from models.dealership import Dealership
from models.car import Car
from models.sales import SalesRecord
from datetime import datetime

def add_dealership():
    name = input("Enter dealership name: ")
    location = input("Enter dealership location: ")
    
    session = SessionLocal()
    dealership = Dealership(name=name, location=location)
    session.add(dealership)
    session.commit()
    session.close()
    print(f"Added dealership {name} at {location}.")

def add_car():
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = input("Enter car year: ")
    dealership_id = input("Enter dealership ID: ")
    
    session = SessionLocal()
    car = Car(make=make, model=model, year=year, dealership_id=dealership_id)
    session.add(car)
    session.commit()
    session.close()
    print(f"Added car {make} {model} ({year}) to dealership {dealership_id}.")

def record_sale():
    car_id = input("Enter car ID: ")
    sale_date = input("Enter sale date (YYYY-MM-DD): ")
    
    try:
        sale_date_parsed = datetime.strptime(sale_date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    
    price = input("Enter sale price: ")
    buyer_name = input("Enter buyer name: ")
    
    session = SessionLocal()
    sale = SalesRecord(car_id=car_id, sale_date=sale_date_parsed, price=price, buyer_name=buyer_name)
    session.add(sale)
    session.commit()
    session.close()
    print(f"Recorded sale of car ID {car_id} on {sale_date} for ${price} to {buyer_name}.")

def exit_program():
    print("Goodbye!")
    exit()
