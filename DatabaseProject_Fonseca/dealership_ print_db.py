import sqlite3
 
conn = sqlite3.connect('dealership.sqlite')
cur = conn.cursor()
cur.execute('SELECT * FROM Dealership')
all_rows = cur.fetchall()
print("dealer_id  address              telno")
for row in all_rows:
    dealer_id = row[0]
    address = row[1]
    telno = row[2]
    print("%d\t   %s\t%d" % (dealer_id, address, telno))

cur.execute('SELECT * FROM Vehicle')
all_rows = cur.fetchall()
print("vehicle_id   dealer_id   make        model       vehicle_year  price")
for row in all_rows:
    vehicle_id = row[0]
    dealer_id = row[1]
    make = row[2]
    model = row[3]
    vehicle_year = row[4]
    price = row[5]
    
    print("%d\t      %d\t         %s\t     %s\t %d\t       %d\t" % (vehicle_id,dealer_id,make,model,vehicle_year,price))
 
print('End of data')
