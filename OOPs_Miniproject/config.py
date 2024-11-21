# config.py

import psycopg2
from psycopg2 import sql

# Define your PostgreSQL connection details
DATABASE = {
    "dbname": "car_rental",
    "user": "postgres",
    "password": "kushagra2005@",
    "host": "localhost",
    "port": "5432"
}

def create_tables():
    with psycopg2.connect(**DATABASE) as conn:
        cursor = conn.cursor()

        # Create tables for cars, customers, and bookings
        cursor.execute('''CREATE TABLE IF NOT EXISTS cars (
                            id SERIAL PRIMARY KEY,
                            model VARCHAR(50) NOT NULL,
                            make VARCHAR(50) NOT NULL,
                            year INT NOT NULL,
                            price_per_day REAL NOT NULL,
                            available BOOLEAN DEFAULT TRUE)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(100) NOT NULL,
                            phone VARCHAR(20) NOT NULL,
                            email VARCHAR(100) NOT NULL)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                            id SERIAL PRIMARY KEY,
                            car_id INT REFERENCES cars(id),
                            customer_id INT REFERENCES customers(id),
                            start_date DATE,
                            end_date DATE,
                            total_price REAL)''')

        conn.commit()

# Initialize database tables
create_tables()