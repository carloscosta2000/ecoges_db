import sys
import mysql.connector
from datetime import datetime
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="seed",
  password="deesdees",
  database="ecoges"

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
sqlClient1 = "INSERT INTO Client (username, nome, password, morada) VALUES ('u1', 'n1', 'p1', 'm1')"
mycursor.execute(sqlClient1)
client1ID = mycursor.lastrowid

#CLIENT2
sqlClient2 = "INSERT INTO Client (username, nome, password, morada) VALUES ('u2', 'n2', 'p2', 'm2')"
mycursor.execute(sqlClient2)
client2ID = mycursor.lastrowid

#CLIENT3
sqlClient3 = "INSERT INTO Client (username, nome, password, morada) VALUES ('u3', 'n3', 'p3', 'm3')"
mycursor.execute(sqlClient3)
client3ID = mycursor.lastrowid

#CLIENT4
sqlClient4 = "INSERT INTO Client (username, nome, password, morada) VALUES ('u4', 'n4', 'p4', 'm4')"
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
sqlRoleSystemManager = "INSERT INTO Role (tipo) VALUES ('Team Manager')"
mycursor.execute(sqlRoleSystemManager)
systemManagerD = mycursor.lastrowid

#APPLIANCE1
sqlAppliance1 = "INSERT INTO Appliance (nome, maxConsumption, isProducing, contractID) VALUES ('Microondas', 5.0, FALSE, " + str(flatRateID) + ")"
mycursor.execute(sqlAppliance1)
appliance1 = mycursor.lastrowid

#APPLIANCE2
sqlAppliance2 = "INSERT INTO Appliance (nome, maxConsumption, isProducing, contractID) VALUES ('Frigorífico', 20.0, FALSE, " + str(biHourRateID) + ")"
mycursor.execute(sqlAppliance2)
appliance2 = mycursor.lastrowid

#APPLIANCE3
sqlAppliance3 = "INSERT INTO Appliance (nome, maxConsumption, isProducing, contractID) VALUES ('Painéis Solares', 40.0, TRUE, " + str(biHourRateID) + ")"
mycursor.execute(sqlAppliance3)
appliance3 = mycursor.lastrowid

#EMPLOYEE1
mycursor.execute("""INSERT INTO Employee (username, nome, password, roleID) VALUES (%s, %s, %s, %s)""",('une1', 'e1', 'p1', accountManagerID))
employee1 = mycursor.lastrowid

#EMPLOYEE2
mycursor.execute("""INSERT INTO Employee (username, nome, password, roleID) VALUES (%s, %s, %s, %s)""",('une2', 'e2', 'p2', technicalAssistantID))
employee2 = mycursor.lastrowid

#RATE1
mycursor.execute("""INSERT INTO Rates (rate, initial, finish, contractID) VALUES (%s, %s, %s, %s)""",(5.0, '1970-01-01 15:00:00', '1970-01-01 17:00:00', flatRateID))
employee2 = mycursor.lastrowid
mydb.commit()



#QUERY TO GET MAX CONSUMPTION
mycursor.execute("SELECT maxConsumption FROM Appliance WHERE id = " + str(appliance1))
maxConsumptionApp1 = float(mycursor.fetchone()[0])

#Appliance consumption
date_time_str = '2022-12-01 10:27:03'
for i in range(0,10):
  new_date_time_str = date_time_str.split(":")[0] + ":" + str(int(date_time_str.split(":")[1]) + i) + ":" + date_time_str.split(":")[2] 
  mycursor.execute("""INSERT into Appliance_consumption (applianceID, ts, consumption) values(%s,%s,%s)""",(str(appliance1), new_date_time_str, str(float(random.randint(0,int(maxConsumptionApp1))))))
mydb.commit()

