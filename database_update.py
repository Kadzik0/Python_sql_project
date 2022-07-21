import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Create a table
c.execute("""UPDATE customers SET first_name = 'pozdro'
            WHERE rowid = 1
        """)

# Commit command
conn.commit()

c.execute("Select * FROM customers")

items=c.fetchall()

for x in items:
    print(x)

#Close our connection
conn.close()
