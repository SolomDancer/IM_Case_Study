#!/usr/bin/python
import csv
import mysql.connector
import codecs

mydb = mysql.connector.connect(host="173.194.242.211", user="root", password="InfectiousTraining", db="IM_Task_2")
cursor = mydb.cursor()

csvfile = open('C:\python\\regions.csv', newline='\n',  encoding='utf-8')
spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
count = 0
errors = 0
for row in spamreader:
	
	if row[1] != "country_id":
		Squery = ("SELECT COUNT(*) from Country where country_id = '"+row[1]+"'")
		cursor.execute(Squery)
		result=cursor.fetchone()
		number_of_rows=result[0]
		if(number_of_rows > 0):
			print("Inserting:->",row[0]," ",row[1]," ",row[2]," ",row[3],"--",number_of_rows)
			Iquery = "INSERT IGNORE INTO IM_Task_2.Region (Region_id, Country_country_id, iso_code, name) VALUES (%s, %s, %s, %s)"
			cursor.execute(Iquery, (row[0],row[1],row[3],row[2]))
			count = count + 1
		else:
			print("Logging:->",row[0]," ",row[1]," ",row[2]," ",row[3])
			Lquery = "INSERT INTO IM_Task_2.error (Table_errored, Data) VALUES ('Regions', 'Region_ID: '%s' | country_id: '%s' | name: '%s' | iso_code: '%s' |')"
			cursor.execute(Lquery, (row[0],row[1],row[2],row[3]))
			count = count + 1
			errors = errors + 1
print("Total Number of rows: ", count)		
print("Total Number of errors: ", errors)		
#close the connection to the database. id,alpha2,alpha3,name,targetable
mydb.commit()
cursor.close()
print ("Done")