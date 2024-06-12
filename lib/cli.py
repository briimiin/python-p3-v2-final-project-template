from helpers import (
    exit_program,
    add_dealership,
    add_car,
    record_sale
)
from models import init_db

def main():
    init_db()  # Initialize the database and create tables
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_dealership()
        elif choice == "2":
            add_car()
        elif choice == "3":
            record_sale()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add a dealership")
    print("2. Add a car")
    print("3. Record a sale")

if __name__ == "__main__":
    main()
