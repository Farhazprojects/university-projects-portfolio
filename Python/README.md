# Nemo Reef Tours Booking System

A Python console application to manage tour bookings at **Nemo Reef Tours**.  
It supports entering bookings, applying group discounts, displaying statistics, searching, and saving/loading data from CSV.

---

## Project Overview

- **Purpose:** Manage customer bookings via a menu-driven CLI with validated inputs and formatted outputs.
- **Core data model:** Parallel lists for names and passenger counts; per-passenger base charge with tiered discounts.
- **Scope:** Input validation, discount calculation, statistics, search, CSV persistence, and basic error handling.

---

## Features

-  **Validated inputs:** Non-empty booking names and integer passenger counts ≥ 1  
-  **Tiered discounts:** Auto-applied based on group size  
-  **Formatted listing:** Aligned columns for name, passengers, and charge  
-  **Statistics:** Minimum, maximum, average passengers, and total charges  
-  **Search:** Case-insensitive booking name lookup  
-  **CSV save/load:** Error-checked file I/O with existence checks  

---

## Discount Rules

| Group size | Discount |
|------------|----------|
| 1–2        | 0%       |
| 3–5        | 10%      |
| 6–10       | 15%      |
| >10        | 20%      |

---

## Usage

### Run the program
- **Prerequisites:** Python 3.x  
- **Start:** Run `python nemo_tours.py` from your terminal  

### Menu options
**1: Enter booking** → Add a booking name and passenger count. Prints a receipt with the discounted total.  
**2: Display bookings** → Shows all bookings in aligned columns with calculated charges.  
**3: Display statistics** → Prints min/max/average passengers and total charges collected.  
**4: Search bookings** → Case-insensitive lookup by booking name; prints the matching receipt.  
**5: Save bookings to file** → Writes bookings to CSV with basic error handling.  
**6: Read bookings from file** → Loads bookings from CSV, checking if the file exists first.  
**7: Exit** → Quits the application with a closing message.  

> **Tip:** The current code uses a hardcoded path `bookings.csv`.  
Update this path to a suitable location on your machine (e.g., your Documents folder) for portability.

---

## File I/O

- **Save path:** `C:/Users/ASUS/Documents/bookings.csv`  
- **Format:** Each line is `name,passengers`  
- **Existence check:** Read operation verifies the file exists before loading  

---

## Testing Scenarios

- **Valid booking:** Name “Farhaz Khondoker”, passengers 8 → expects 15% discount  
- **Blank name:** Prompts error and retry  
- **Zero passengers:** Prompts error and retry  
- **Display all:** Shows formatted table with computed charges  
- **Statistics:** Shows correct min, max, average, totals  
- **Search:** Case-insensitive match returns the correct booking  
- **Save to file:** Confirmation message on success  
- **Read from file:** Confirmation and bookings appended  

---

## Project Structure

- **nemo_tours.py** → Main application  
- **bookings.csv** → CSV data file (created after Save)  

---

## Code Highlights

```python
PASSENGER_CHARGE = 95.50

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

def print_heading():
    print("{:30s}{:11s}{:6s}".format("Booking name", "Passengers", "Charge"))

def print_receipt(name, passengers, charge):
    print("\nBooking Name:", name)
    print("Passengers:", passengers)
    print("Total Charge: $" + format(charge, ".2f"))
