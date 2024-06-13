## Car Dealership Management System
This is a CLI (Command Line Interface) application for managing car dealerships, cars, and sales records. The system is built using Python for database management.

# Features
Add Dealerships: Add new dealerships to the system with their name and location.
Add Cars: Add new cars to the system with details such as make, model, year, and dealership ID.
Record Sales: Record sales transactions including the car ID, sale date, sale price, and buyer name.
Display Dealerships and Cars: View a list of all dealerships and cars in the system.
Search for Cars: Search for a specific car by make, model, and year.
# Database Schema
dealerships: Stores dealership information such as ID, name, and location.
cars: Stores car information such as ID, make, model, year, and dealership ID.
sales_records: Stores sales record information such as car ID, sale date, price, and buyer name.
Relationships
One-to-many relationship between dealerships and cars.
One-to-many relationship between cars and sales_records.
Composite Key
The sales_records table uses a composite primary key consisting of car_id and sale_date.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

