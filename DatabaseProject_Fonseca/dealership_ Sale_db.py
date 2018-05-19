import sqlite3
 
conn = sqlite3.connect('dealership.sqlite')
cur = conn.cursor()
 
f = open('dealership_db.sql','r')
sql = f.read()
cur.executescript(sql)
sale_id = input("what is the sale id?")

cur.execute("SELECT * FROM Sale WHERE sale_id = ?", (sale_id))
dealership = cur.fetchone()

if dealership is None:
    sale_id = input("sale_id doesnt exist enter new one")
    vehicle_id = input("What is the vehicle_id?")
    customer_id = input("what is the customer id?")
    dealer_id = input("what is the dealer_id")
    cost = input("what is the cost of the vehicle")
    cur.execute('''INSERT INTO Sale(Sale_id, Vehicle_id, dealer_id, Customer_id,cost) VALUES(?,?,?,?,?)''', (sale_id, vehicle_id,dealer_id, customer_id, cost))
    print("Added")
    conn.commit()
  
else:
    print("Sale_id already exist")
    conn.commit()
