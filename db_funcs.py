import sqlite3

# Show all records in table
def show_all():
    # Connect to db
    conn = sqlite3.connect('customer.db')

    # Create a cursor
    c = conn.cursor()

    # Query the db
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    print('ID|  NAME ' + '\t\t' + 'EMAIL\n----------------------------------')
    for x in items:
        print(str(x[0]) + ' | ' + x[1] + ' ' + x[2] + '\t' + x[3])

    # Commit command
    conn.commit()

    # Close connection
    conn.close()

# Add new record to table
def add_one(first_name, last_name, email):
    # Connect to db
    conn = sqlite3.connect('customer.db')

    # Create a cursor
    c = conn.cursor()

    # Add row the db
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first_name, last_name, email))

    # Commit command
    conn.commit()

    # Close connection
    conn.close()

# Delete record in table
def delete_one(id):
    # Connect to db
    conn = sqlite3.connect('customer.db')

    # Create a cursor
    c = conn.cursor()

    # Add row the db
    c.execute("DELETE from customers WHERE rowid = (?)", (id))

    # Commit command
    conn.commit()

    # Close connection
    conn.close()

# Lookup with WHERE
def email_lookup(email):
    # Connect to db
    conn = sqlite3.connect('customer.db')

    # Create a cursor
    c = conn.cursor()

    # Add row the db
    c.execute("SELECT first_name, last_name from customers WHERE email = (?)", (email,))
    items = c.fetchall()
    for item in items:
        print('Wlasciciel adresu to: ' + item[0] + ' ' + item[1])

    # Commit command
    conn.commit()

    # Close connection
    conn.close()