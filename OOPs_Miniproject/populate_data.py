# populate_data.py

import psycopg2
from config import DATABASE

def populate_data():
    with psycopg2.connect(**DATABASE) as conn:
        cursor = conn.cursor()

        # Insert sample cars
        cars = [
            ("Model S", "Tesla", 2020, 100.0),
            ("Camry", "Toyota", 2018, 50.0),
            ("Civic", "Honda", 2019, 45.0),
            ("Mustang", "Ford", 2021, 150.0),
            ("Accord", "Honda", 2020, 60.0),
            ("Corolla", "Toyota", 2017, 40.0),
            ("3 Series", "BMW", 2019, 120.0),
            ("Altima", "Nissan", 2018, 55.0),
            ("A4", "Audi", 2020, 110.0),
            ("X5", "BMW", 2021, 180.0)
        ]
        cursor.executemany(
            "INSERT INTO cars (model, make, year, price_per_day) VALUES (%s, %s, %s, %s)",
            cars
        )

        # Insert sample customers
        customers = [
            ("Alice Johnson", "123-456-7890", "alice@example.com"),
            ("Bob Smith", "234-567-8901", "bob@example.com"),
            ("Charlie Brown", "345-678-9012", "charlie@example.com"),
            ("Daisy Thomas", "456-789-0123", "daisy@example.com"),
            ("Eve Adams", "567-890-1234", "eve@example.com"),
            ("Frank Miller", "678-901-2345", "frank@example.com"),
            ("Grace Lee", "789-012-3456", "grace@example.com"),
            ("Hank Green", "890-123-4567", "hank@example.com"),
            ("Ivy White", "901-234-5678", "ivy@example.com"),
            ("Jack Black", "012-345-6789", "jack@example.com")
        ]
        cursor.executemany(
            "INSERT INTO customers (name, phone, email) VALUES (%s, %s, %s)",
            customers
        )

        # Insert sample bookings
        bookings = [
            (1, 1, "2023-01-01", "2023-01-05", 400.0),
            (2, 2, "2023-02-10", "2023-02-15", 250.0),
            (3, 3, "2023-03-20", "2023-03-25", 225.0),
            (4, 4, "2023-04-05", "2023-04-10", 750.0),
            (5, 5, "2023-05-15", "2023-05-18", 180.0),
            (6, 6, "2023-06-25", "2023-06-28", 120.0),
            (7, 7, "2023-07-05", "2023-07-10", 600.0),
            (8, 8, "2023-08-15", "2023-08-17", 110.0),
            (9, 9, "2023-09-20", "2023-09-25", 550.0),
            (10, 10, "2023-10-05", "2023-10-09", 720.0)
        ]
        cursor.executemany(
            "INSERT INTO bookings (car_id, customer_id, start_date, end_date, total_price) VALUES (%s, %s, %s, %s, %s)",
            bookings
        )

        conn.commit()
        print("Data populated successfully.")

# Populate the data
populate_data()