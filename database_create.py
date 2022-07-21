import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE customers (
        first_name text,
        last_name text,
        email text
    )""")

# Commit command
conn.commit()

#Close our connection
conn.close()
