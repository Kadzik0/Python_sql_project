import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

c.execute("DROP TABLE customers")

items=c.fetchall()

for x in items:
    print(x)

#Close our connection
conn.close()
