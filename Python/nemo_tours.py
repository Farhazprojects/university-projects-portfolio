# Author: Farhaz Khondoker
# Student ID: 12300016
# File: nemo_tours.py
# Date: 20/05/2025
# Description: Console-based menu-driven program for managing bookings at Nemo Reef Tours. It allows entering bookings, displaying all bookings, showing statistics, searching, saving, and reading from file.

import os.path

PASSENGER_CHARGE = 95.50

booking_names = []
booking_passengers = []
booking_count = 0

ENTER_BOOKING = 1
DISPLAY_BOOKINGS = 2
DISPLAY_STATISTICS = 3
SEARCH_BOOKINGS = 4
SAVE_BOOKINGS = 5
READ_BOOKINGS = 6
EXIT = 7

def print_heading():
    print("{:30s}{:11s}{:6s}".format("Booking name","Passengers", "Charge")) #The string sizes are given for adjustments

def get_menu_item():
    print("\nPlease select from the following")
    print(str(ENTER_BOOKING) + ". Enter booking name and number of passengers")
    print(str(DISPLAY_BOOKINGS) + ". Display all booking names, number of passengers and charges")
    print(str(DISPLAY_STATISTICS) + ". Display Statistics")
    print(str(SEARCH_BOOKINGS) + ". Search for booking")
    print(str(SAVE_BOOKINGS) + ". Save bookings to file")
    print(str(READ_BOOKINGS) + ". Read bookings from file")
    print(str(EXIT) + ". Exit the application")
    print("Enter choice==> ", end = " ")
    choice = input()
    while not choice.isdigit():
        print("Error - Menu selection name cannot be blank and must be numeric")
        print("Enter choice==> ", end = " ")
        choice = input()
    return int(choice)

def process_menu_item():
    choice = get_menu_item()
    while choice != EXIT:
        if choice == ENTER_BOOKING:
            enter_booking()
        elif choice == DISPLAY_BOOKINGS:
            display_bookings()
        elif choice == DISPLAY_STATISTICS:
            display_statistics()
        elif choice == SEARCH_BOOKINGS:
            search_bookings()
        elif choice == SAVE_BOOKINGS:
            save_bookings()
        elif choice == READ_BOOKINGS:
            read_bookings()
        choice = get_menu_item()
    print("Thank you for using the Nemo Reef Tours System. A Program written by Student ID: 12300016") #My student-ID Added

def enter_booking():
    global booking_count

    booking_name = input("Enter the booking name: ").strip() # Strip function will eliminate extra spaces
    while booking_name == "":
        print("Error - booking name cannot be blank.")
        booking_name = input("Enter the booking name: ").strip() # Strip function will eliminate extra spaces

    while True:
        try: # Try function is used because of eliminating complexity
            passengers = int(input("Enter number of passengers for " + booking_name + ": "))
            if passengers < 1:
                print("Error - number of passengers must be at least 1.")
            else:
                break
        except ValueError: # ValueError used for the values which are not integers
            print("Error - please enter a valid number.")

    booking_names.append(booking_name) # Append is used to update the list
    booking_passengers.append(passengers)
    booking_count += 1

    charge = calculate_charge(passengers)
    print_receipt(booking_name, passengers, charge)

def calculate_charge(passengers):
    if 3 <= passengers <= 5:
        discount = 0.10
    elif 6 <= passengers <= 10:
        discount = 0.15
    elif passengers > 10:
        discount = 0.20
    else:
        discount = 0.0
    total = passengers * PASSENGER_CHARGE
    return total * (1 - discount)

def print_receipt(name, passengers, charge):
    print("\nBooking Name:", name)
    print("Passengers:", passengers)
    print("Total Charge: $" + format(charge, ".2f"))

def display_bookings():
    if booking_count == 0:
        print("Error - no bookings entered yet.")
        return
    print_heading()
    for i in range(booking_count):
        charge = calculate_charge(booking_passengers[i])
        print("{:30s}{:<11d}${:4.2f}".format(booking_names[i], booking_passengers[i], charge)) # for adjustment
3
def display_statistics():
    if booking_count == 0:
        print("Error - no bookings entered yet.")
        return

    total_passengers = 0
    total_charges = 0.0
    min_passengers = 99999
    max_passengers = -1
    min_name = ""
    max_name = ""

    for i in range(booking_count):
        passengers = booking_passengers[i]
        name = booking_names[i]
        charge = calculate_charge(passengers)

        total_passengers += passengers
        total_charges += charge

        if passengers < min_passengers:
            min_passengers = passengers
            min_name = name
        if passengers > max_passengers:
            max_passengers = passengers
            max_name = name

    avg_passengers = total_passengers / booking_count
    print("Minimum passengers booked:", min_passengers, "by", min_name)
    print("Maximum passengers booked:", max_passengers, "by", max_name)
    print("Average passengers per booking: {:.2f}".format(avg_passengers))
    print("Total charges collected: ${:.2f}".format(total_charges))

def search_bookings():
    if booking_count == 0:
        print("Error - no bookings entered yet.")
        return

    search_name = input("Enter name to search for: ").strip().lower() # lower is used to convert all the words to lowercase to eliminate case senstivity
    found = False
    for i in range(booking_count):
        if booking_names[i].lower() == search_name:
            charge = calculate_charge(booking_passengers[i])
            print_receipt(booking_names[i], booking_passengers[i], charge)
            found = True
            break

    if not found:
        print("Booking not found.")

def save_bookings():
    try:
        with open("C:/Users/bookings.csv", "w") as file: # My own pcs directory
            for i in range(booking_count):
                file.write(f"{booking_names[i]},{booking_passengers[i]}\n")
        print("Data successfully saved to file.")
    except Exception as e:
        print("Error saving to file:", str(e))

def read_bookings():
    global booking_count
    file_path = "C:/Users/ASUS/Documents/bookings.csv"  #Own file path

    if not os.path.exists(file_path):
        print("Error – file does not exist.")
        return

    try:
        with open(file_path, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    booking_names.append(parts[0])
                    booking_passengers.append(int(parts[1]))
                    booking_count += 1
        print("Data successfully read from the file.")
    except Exception as e:
        print("Error reading file:", str(e))

print("Welcome to the Nemo Reef Tours Management System")
process_menu_item()

