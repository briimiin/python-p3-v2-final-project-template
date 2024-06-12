from helpers import (
    add_dealership,
    add_car,
    record_sale
)

def main():
    while True:
        print("Please select an option:")
        print("0. Exit the program")
        print("1. Add a dealership")
        print("2. Add a car")
        print("3. Record a sale")
        choice = input("> ")
        
        if choice == "0":
            break
        elif choice == "1":
            add_dealership()
        elif choice == "2":
            add_car()
        elif choice == "3":
            record_sale()
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
