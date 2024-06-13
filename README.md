##Car Dealership Management System
This is a CLI (Command Line Interface) application for managing car dealerships, cars, and sales records. The system is built using Python and SQLAlchemy for database management.

#Features
Add Dealerships: Add new dealerships to the system with their name and location.
Add Cars: Add new cars to the system with details such as make, model, year, and dealership ID.
Record Sales: Record sales transactions including the car ID, sale date, sale price, and buyer name.
Display Dealerships and Cars: View a list of all dealerships and cars in the system.
Search for Cars: Search for a specific car by make, model, and year.
Requirements
Python 3.6+
SQLAlchemy
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/car-dealership-management.git
Navigate to the project directory:

bash
Copy code
cd car-dealership-management
Install dependencies:

bash
Copy code
pipenv install
Set up the database:

bash
Copy code
pipenv run python lib/database.py
Usage
Run the CLI application:

bash
Copy code
pipenv run python lib/cli.py
Follow the on-screen instructions to perform various operations such as adding dealerships, cars, recording sales, and more.

Database Schema
The application uses SQLite as its database. The database schema includes the following tables:

dealerships: Stores dealership information such as ID, name, and location.
cars: Stores car information such as ID, make, model, year, and dealership ID.
sales_records: Stores sales record information such as car ID, sale date, price, and buyer name.
Relationships
One-to-many relationship between dealerships and cars.
One-to-many relationship between cars and sales_records.
Composite Key
The sales_records table uses a composite primary key consisting of car_id and sale_date.
Example CLI Commands
Add a dealership:

yaml
Copy code
Please select an option:
1. Add a dealership
Enter dealership name: Example Dealership
Enter dealership location: Example Location
Add a car:

yaml
Copy code
Please select an option:
2. Add a car
Enter car make: Toyota
Enter car model: Corolla
Enter car year: 2021
Enter dealership ID: 1
Record a sale:

mathematica
Copy code
Please select an option:
3. Record a sale
Enter car ID: 1
Enter sale date (YYYY-MM-DD): 2023-12-01
Enter sale price: 12000
Enter buyer name: John Doe
Display all dealerships:

sql
Copy code
Please select an option:
4. Display all dealerships
Search for a car:

yaml
Copy code
Please select an option:
5. Search for a car
Enter car make: Toyota
Enter car model: Corolla
Enter car year: 2021
Display all cars:

sql
Copy code
Please select an option:
6. Display all cars
Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

