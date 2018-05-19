import sqlite3
 
conn = sqlite3.connect('dealership.sqlite')
cur = conn.cursor()
 
f = open('dealership_db.sql','r')
sql = f.read()
cur.executescript(sql)


dealer = input("Enter dealer id")
cur.execute("SELECT * FROM Dealership WHERE dealer_id = ?", (dealer))
dealership = cur.fetchone()
if dealership is None:
    dealer_id = input("Enter new dealer id")
    address = input("Enter address of dealership")
    telno = input("Enter Telephone of dealership")
    cur.execute('''INSERT INTO Dealership(dealer_id, address, tel_no) VALUES(?,?,?)''', (dealer_id, address, telno))
    print("Added")
    conn.commit()
else:
    print("Dealership already exists")
