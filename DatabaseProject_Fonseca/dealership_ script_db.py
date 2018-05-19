import sqlite3
 
conn = sqlite3.connect('dealership.sqlite')
cur = conn.cursor()
 
cur.executescript('''
DROP TABLE IF EXISTS Dealership ;
DROP TABLE IF EXISTS Vehicle;
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Sale;
CREATE TABLE Dealership(
  dealer_id  INTEGER NOT NULL  PRIMARY KEY    AUTOINCREMENT,
  address   TEXT,
  tel_no  INTEGER
  
);

CREATE TABLE Vehicle
(
  vehicle_id    INTEGER NOT NULL PRIMARY KEY   AUTOINCREMENT,
  dealer_id 	INTEGER,
  make   TEXT,
  model  TEXT,
  vehicle_year  INTEGER,
  price			INTEGER,

  CONSTRAINT dealer_id_fk FOREIGN KEY(dealer_id) REFERENCES Dealership(dealer_id) 
  ON UPDATE CASCADE 
  ON DELETE NO ACTION
	
	
  
);

CREATE TABLE Customer
(
  Customer_id   INTEGER  NOT NULL  PRIMARY KEY       AUTOINCREMENT,
  name			TEXT
	
  
);

CREATE TABLE Sale
(
  Sale_id    INTEGER NOT NULL   PRIMARY KEY       AUTOINCREMENT,
  vehicle_id  INTEGER  ,
  dealer_id 	INTEGER	 ,
  Customer_id  INTEGER ,
  cost			DOUBLE,
  			
  
  CONSTRAINT dealer_id_fk FOREIGN KEY(dealer_id) REFERENCES dealership(dealer_id)
  ON UPDATE CASCADE 
  ON DELETE NO ACTION,
  
  CONSTRAINT vehicle_id_fk  FOREIGN KEY(vehicle_id)REFERENCES Vehicle(vehicle_id)
  ON UPDATE CASCADE 
  ON DELETE NO ACTION,
	
  CONSTRAINT customer_id_fk FOREIGN KEY(customer_id)REFERENCES Customer(Customer_id)
  ON UPDATE CASCADE 
  ON DELETE NO ACTION
	
	
  
);

CREATE INDEX Sale_cost ON Sale (cost);

INSERT INTO Dealership(dealer_id, address, tel_no) VALUES(1,"1234 W 2nd ST",232341232);
INSERT INTO Dealership(dealer_id, address, tel_no) VALUES(2,"4567 E 5th ST",232242665);
INSERT INTO Dealership(dealer_id, address, tel_no) VALUES(3,"2764 E 18th ST",235376679);
INSERT INTO Dealership(dealer_id, address, tel_no) VALUES(4,"8753 S 71st ST",234456275);
INSERT INTO Dealership(dealer_id, address, tel_no) VALUES(5,"1345 N Cook Dr",232356190);

INSERT INTO Vehicle(vehicle_id, dealer_id, make, model, vehicle_year, price) VALUES(123,1,"Mazda","Mazda3",2017, 19235);
INSERT INTO Vehicle(vehicle_id, dealer_id, make, model, vehicle_year, price) VALUES(234,1,"Mazda","CX7",2010, 15500);
INSERT INTO Vehicle(vehicle_id, dealer_id, make, model, vehicle_year, price) VALUES(223,3,"Honda","Civic",2012, 10255);
INSERT INTO Vehicle(vehicle_id, dealer_id, make, model, vehicle_year, price) VALUES(129,2,"Chevy","Camaro",2017, 32199);
INSERT INTO Vehicle(vehicle_id, dealer_id, make, model, vehicle_year, price) VALUES(769,4,"Doger","Charger",2017, 35990);

INSERT INTO Customer(Customer_id, name) VALUES(1, "John Smith");
INSERT INTO Customer(Customer_id, name) VALUES(2, "Joe Heyward");
INSERT INTO Customer(Customer_id, name) VALUES(3, "Ivan Fonseca");
INSERT INTO Customer(Customer_id, name) VALUES(4, "Eva Carver");
INSERT INTO Customer(Customer_id, name) VALUES(5, "Will Harvey");

INSERT INTO Sale(Sale_id, vehicle_id, dealer_id, Customer_id, cost) VALUES(1,123,1,1,22235);
INSERT INTO Sale(Sale_id, vehicle_id, dealer_id, Customer_id, cost) VALUES(2,223,3,2,11255);
INSERT INTO Sale(Sale_id, vehicle_id, dealer_id, Customer_id, cost) VALUES(3,234,1,3,17500);
INSERT INTO Sale(Sale_id, vehicle_id, dealer_id, Customer_id, cost) VALUES(4,129,2,5,36199);
INSERT INTO Sale(Sale_id, vehicle_id, dealer_id, Customer_id, cost) VALUES(5,769,4,4,38990);
''')
