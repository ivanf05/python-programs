import sqlite3
 
conn = sqlite3.connect('dealership.sqlite')
conn.row_factory = sqlite3.Row
cur = conn.cursor()
 
cur.execute('SELECT  make, model, vehicle_year|| " " || cost as cost FROM Vehicle JOIN Sale on Sale.vehicle_id = Vehicle.Vehicle_id')
print("\nSales")
print()
print("Make\tModel\tYear TotalCost")
print("-"*43)
for row in cur:
    cols = len(row)
    for col in range(cols):
        print(row[col], end='\t');
    print()
