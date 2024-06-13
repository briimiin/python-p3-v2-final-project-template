from helpers import (
    add_dealership,
    add_car,
    record_sale,
    display_dealerships,
    search_car,
    display_all_cars
)

def main():
    while True:
        print("**NUNUAGARISIMZINGA DEALERSHIP***")
        print("Please Select a program")
        print("0. Exit the program")
        print("1. Add a dealership")
        print("2. Add a car")
        print("3. Record a sale")
        print("4. Display all dealerships")
        print("5. Search for a car")
        print("6. Display all cars")
        choice = input("> ")

        if choice == "0":
            break
        elif choice == "1":
            add_dealership()
        elif choice == "2":
            add_car()
        elif choice == "3":
            record_sale()
        elif choice == "4":
            display_dealerships()
        elif choice == "5":
            search_car()
        elif choice == "6":
            display_all_cars()
        else:
            print("Invalid option, please try again.")

        continue_choice = input("Do you want to continue? (y/n): ")
        if continue_choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()
