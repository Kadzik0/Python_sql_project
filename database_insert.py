import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

customer_list =[
                    ('Wes', 'Brown', 'wes@gmail.com'),
                    ('Steph', 'Kuewa', 'sk@gmail.com'), 
                    ('Harry', 'Potter', 'hp@hogwarts.edu.com'),
                    ('Konrad', 'Rajda', 'konradrajda98@gmail.com'),
                    ('Szymon', 'Zajda', 'szajda@gmail.com'),
                    ('Konrad', 'Pajda', 'kpajda@gmail.com'),
                    ('Konrad', 'Rajca', 'krajca@gmail.com'),
                ]

# Create a table
c.executemany("INSERT INTO customers VALUES (?, ?, ?)", customer_list)

print('insert commited succesfully')
# Commit command
conn.commit()

#Close our connection
conn.close()
