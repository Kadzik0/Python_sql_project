import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Delete records
c.execute("""DELETE from customers WHERE rowid = 5
        """)

# Commit command
conn.commit()

c.execute("Select rowid, * FROM customers")

items=c.fetchall()

for x in items:
    print(x)

#Close our connection
conn.close()
