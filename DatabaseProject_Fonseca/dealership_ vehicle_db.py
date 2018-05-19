import sqlite3
 
conn = sqlite3.connect('dealership.sqlite')
cur = conn.cursor()
 
f = open('dealership_db.sql','r')
sql = f.read()
cur.executescript(sql)
dealer_id = input("What is the Vehicle_id")
cur.execute("SELECT * FROM Vehicle WHERE Vehicle_id = ?", (dealer_id))
dealership = cur.fetchone()
if dealership is None:
    dealer_id = input("Enter id of dealership")
    vehicle_id = input("What is the vehicle id number?")
    make = input("What is the make of vehicle")
    year = input("What is the year of the vehicle")
    price = input("What is the price of the vehicle")
    model = input("What is the model of the vehicle")
    cur.execute('''INSERT INTO Vehicle(vehicle_id,dealer_id,make,model,vehicle_year,price) VALUES(?,?,?,?,?,?)''', (vehicle_id,dealer_id,make, model,year,price ))
    print("Added")
    conn.commit()
else:
    print("Vechile id already exists")
    
