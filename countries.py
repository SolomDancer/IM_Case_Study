#!/usr/bin/python
import csv
import mysql.connector

mydb = mysql.connector.connect(host="173.194.242.211", user="root", password="InfectiousTraining", db="IM_Task_2")
cursor = mydb.cursor()

csvfile = open('C:\python\\countries.csv', newline='\n',  encoding='utf-8')
spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
count = 0
errors = 0
for row in spamreader:
	if row[0] != "id" and row[1] != "alpha2" and row[2] != "alpha3" and row[3] != "name" and row[4] != "targetable":
		print("Inserting:->",row[0]," ",row[1]," ",row[2]," ",row[3]," ",row[4],"<-Into table Countries")
		query = "INSERT IGNORE INTO Country (country_id, alpha2, alpha3, name, targetable) VALUES (%s, %s, %s, %s, %s)"
		cursor.execute(query, (row[0],row[1],row[2],row[3],row[4]))
		count = count + 1
	else:
		print("Logging:->",row[0]," ",row[1]," ",row[2]," ",row[3]," ",row[4])
		Lquery = "INSERT INTO IM_Task_2.error (Table_errored, Data) VALUES ('Countries', 'Country_ID: '%s' | alpha2: '%s' | alpha3: '%s' | name: '%s' | iso_code: '%s' |')"
		cursor.execute(Lquery, (row[0],row[1],row[2],row[3],row[4]))
		count = count + 1
		errors = errors + 1
print("Total Number of rows: ", count)
print("Total Number of errors: ", errors)

#close the connection to the database. id,alpha2,alpha3,name,targetable
mydb.commit()
cursor.close()
print ("Done")

