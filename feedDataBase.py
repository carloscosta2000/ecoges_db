import sys
import mysql.connector
from datetime import datetime
import random
import hashlib

mydb = mysql.connector.connect(
  host="localhost",
  user="sammy",
  password="password",
  database="remotedb"
)
mycursor = mydb.cursor()


#CONTRACT1
sqlContract = "INSERT INTO Contract (tipo) VALUES ('Flat Rate')"
mycursor.execute(sqlContract)
flatRateID = mycursor.lastrowid

#CONTRACT2
sqlContract = "INSERT INTO Contract (tipo) VALUES ('Bi-Hour Rate')"
mycursor.execute(sqlContract)
biHourRateID = mycursor.lastrowid

#CLIENT1
pass1 = hashlib.sha512("p1".encode("utf-8")).hexdigest()
sqlClient1 = "INSERT INTO Client (username, nome, password, morada, publickey) VALUES ('u1', 'n1', '" + str(pass1) + "', 'm1', 'pubkey')"
mycursor.execute(sqlClient1)
client1ID = mycursor.lastrowid

#CLIENT2
pass2 = hashlib.sha512("p2".encode("utf-8")).hexdigest()
sqlClient2 = "INSERT INTO Client (username, nome, password, morada, publickey) VALUES ('u2', 'n2', '" + str(pass2) + "', 'm2', 'pubkey')"
mycursor.execute(sqlClient2)
client2ID = mycursor.lastrowid

#CLIENT3
pass3 = hashlib.sha512("p3".encode("utf-8")).hexdigest()
sqlClient3 = "INSERT INTO Client (username, nome, password, morada, publickey) VALUES ('u3', 'n3', '" + str(pass3) + "', 'm3', 'pubkey')"
mycursor.execute(sqlClient3)
client3ID = mycursor.lastrowid

#CLIENT4
pass4 = hashlib.sha512("p4".encode("utf-8")).hexdigest()
sqlClient4 = "INSERT INTO Client (username, nome, password, morada, publickey) VALUES ('u4', 'n4', '" + str(pass4) + "', 'm4', 'pubkey')"
mycursor.execute(sqlClient4)
client4ID = mycursor.lastrowid

#ROLE1
sqlRoleMarketing = "INSERT INTO Role (tipo) VALUES ('Marketing')"
mycursor.execute(sqlRoleMarketing)
marketingID = mycursor.lastrowid

#ROLE2
sqlRoleAccountManager = "INSERT INTO Role (tipo) VALUES ('Account Manager')"
mycursor.execute(sqlRoleAccountManager)
accountManagerID = mycursor.lastrowid

#ROLE3
sqlRoleTechnicalAssistant = "INSERT INTO Role (tipo) VALUES ('Technical Assistant')"
mycursor.execute(sqlRoleTechnicalAssistant)
technicalAssistantID = mycursor.lastrowid

#ROLE4
sqlRoleSystemManager = "INSERT INTO Role (tipo) VALUES ('System Manager')"
mycursor.execute(sqlRoleSystemManager)
systemManagerD = mycursor.lastrowid

#APPLIANCE1
sqlAppliance1 = "INSERT INTO Appliance (nome, maxConsumption, isProducing, contractID, clientID) VALUES ('Microondas', 5.0, FALSE, " + str(flatRateID) + ", 1)"
mycursor.execute(sqlAppliance1)
appliance1 = mycursor.lastrowid

#APPLIANCE2
sqlAppliance2 = "INSERT INTO Appliance (nome, maxConsumption, isProducing, contractID, clientID) VALUES ('Frigorífico', 20.0, FALSE, " + str(biHourRateID) + ", 1)"
mycursor.execute(sqlAppliance2)
appliance2 = mycursor.lastrowid

#APPLIANCE3
sqlAppliance3 = "INSERT INTO Appliance (nome, maxConsumption, isProducing, contractID, clientID) VALUES ('Painéis Solares', 40.0, TRUE, " + str(biHourRateID) + ", 2)"
mycursor.execute(sqlAppliance3)
appliance3 = mycursor.lastrowid

#EMPLOYEE1
pass1 = hashlib.sha512("p1".encode("utf-8")).hexdigest()
mycursor.execute("""INSERT INTO Employee (username, nome, password, roleID) VALUES (%s, %s, %s, %s)""",('une1', 'e1', pass1, accountManagerID))
employee1 = mycursor.lastrowid

#EMPLOYEE2
pass2 = hashlib.sha512("p2".encode("utf-8")).hexdigest()
mycursor.execute("""INSERT INTO Employee (username, nome, password, roleID) VALUES (%s, %s, %s, %s)""",('une2', 'e2', pass2, technicalAssistantID))
employee2 = mycursor.lastrowid


#RATES
mycursor.execute("""INSERT INTO Bi_Hour_Rate (rate1, rate2, initial, finish, contractID) VALUES (%s, %s, %s, %s, %s)""", (5.0, 7.0, '1970-01-01 15:00:00', '1970-01-01 17:00:00', biHourRateID))
mycursor.execute("""INSERT INTO Flat_Rate (rate, contractID) VALUES (%s, %s)""", (4.0, flatRateID))

mydb.commit()




#Appliance consumption
date_time_str = input("Insert starting date for appliance consumption (YYYY-MM-DD HH:MM:SS):\n")
nr_entries = int(input("Insert number of entries: "))
#appliance_name = input("Insert appliance name: ")
#QUERY TO GET MAX CONSUMPTION
mycursor.execute("SELECT maxConsumption FROM Appliance WHERE id = " + str(appliance1))
maxConsumptionApp1 = float(mycursor.fetchone()[0])


for i in range(0,nr_entries):
  new_date_time_str = date_time_str.split(":")[0] + ":" + str(int(date_time_str.split(":")[1]) + i) + ":" + date_time_str.split(":")[2] 
  mycursor.execute("""INSERT into Appliance_consumption (applianceID, ts, consumption) values(%s,%s,%s)""",(str(appliance1), new_date_time_str, str(float(random.randint(0,int(maxConsumptionApp1))))))
mydb.commit()

mycursor.execute("""INSERT INTO Session_table (clientID, ts, rnd_hash) VALUES (%s, %s, %s)""",(str(client1ID), datetime.now().strftime("%Y-%m-%d %H:%M:%S"), hashlib.sha256(bytes(random.randint(0,100000))).hexdigest()))
session = mycursor.lastrowid
mydb.commit()