import sqlite3
 
conn = sqlite3.connect('dealership.sqlite')
cur = conn.cursor()
 
f = open('dealership_db.sql','r')
sql = f.read()
cur.executescript(sql)
customer_id = input("what is the customer id?")
cur.execute("SELECT * FROM Customer WHERE Customer_id = ?", (customer_id))
dealership = cur.fetchone()
if dealership is None:
    customer_id = input("Customer doesn't exsit enter new customer id?")
    name = input("What is the customer's name?")
    cur.execute('''INSERT INTO Customer(Customer_id,name) VALUES(?,?)''', (customer_id, name ))
    print("Added")
    conn.commit()
else:
    print("Customer already exists.")
    
