import sqlite3

def db_call():
    # Create a table
    c.execute("SELECT rowid, * FROM customers")
    items=c.fetchall()

    print('ID|  NAME ' + '\t\t' + 'EMAIL\n----------------------------------')
    for x in items:
        print(str(x[0]) + ' | ' + x[1] + ' ' + x[2] + '\t' + x[3])
    # Commit command
    conn.commit()

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

db_call()

#Close our connection
conn.close()
