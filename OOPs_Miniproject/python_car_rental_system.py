# car_rental_system.py

import psycopg2
from datetime import datetime
from config import DATABASE

def view_available_cars():
    with psycopg2.connect(**DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cars WHERE available=TRUE")
        cars = cursor.fetchall()
        
        if not cars:
            print("No cars available for rent.")
        else:
            print("Available Cars:")
            for car in cars:
                print(f"{car[0]}: {car[2]} {car[1]}, Year: {car[3]}, Price per day: ${car[4]}")

def rent_car():
    with psycopg2.connect(**DATABASE) as conn:
        cursor = conn.cursor()
        
        # Get car details
        car_id = int(input("Enter the Car ID to rent: "))
        cursor.execute("SELECT * FROM cars WHERE id=%s AND available=TRUE", (car_id,))
        car = cursor.fetchone()
        
        if car is None:
            print("Car not available or does not exist.")
            return
        
        # Get customer details
        customer_name = input("Enter your name: ")
        phone = input("Enter your phone: ")
        email = input("Enter your email: ")
        
        # Insert customer into database
        cursor.execute("INSERT INTO customers (name, phone, email) VALUES (%s, %s, %s) RETURNING id",
                       (customer_name, phone, email))
        customer_id = cursor.fetchone()[0]

        # Get rental period
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
        days = (end_date_obj - start_date_obj).days
        total_price = days * car[4]
        
        # Insert booking
        cursor.execute('''INSERT INTO bookings (car_id, customer_id, start_date, end_date, total_price) 
                          VALUES (%s, %s, %s, %s, %s)''', 
                       (car_id, customer_id, start_date, end_date, total_price))
        
        # Update car availability
        cursor.execute("UPDATE cars SET available=FALSE WHERE id=%s", (car_id,))
        conn.commit()
        
        print(f"Booking confirmed! Total price: ${total_price}")

def view_bookings():
    with psycopg2.connect(**DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT bookings.id, cars.make, cars.model, customers.name, 
                          bookings.start_date, bookings.end_date, bookings.total_price 
                          FROM bookings 
                          JOIN cars ON bookings.car_id = cars.id 
                          JOIN customers ON bookings.customer_id = customers.id''')
        bookings = cursor.fetchall()
        
        if not bookings:
            print("No bookings found.")
        else:
            print("Bookings:")
            for booking in bookings:
                print(f"Booking ID: {booking[0]}, Car: {booking[1]} {booking[2]}, Customer: {booking[3]}, "
                      f"From: {booking[4]}, To: {booking[5]}, Total Price: ${booking[6]}")

def main():
    while True:
        print("\n--- Car Rental System ---")
        print("1. View Available Cars")
        print("2. Rent a Car")
        print("3. View Bookings")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            view_available_cars()
        elif choice == '2':
            rent_car()
        elif choice == '3':
            view_bookings()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



