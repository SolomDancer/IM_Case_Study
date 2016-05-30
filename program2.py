#!/usr/bin/python
import csv
import mysql.connector

mydb = mysql.connector.connect(host="173.194.242.211", user="root", password="InfectiousTraining", db="IM_Task_2")
cursor = mydb.cursor()

csvfile = open('C:\python\\countries.csv', newline='\n',  encoding='utf-8')
spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
for row in spamreader:

    query = "INSERT INTO Country (country_id, alpha2, alpha3, name, targetable) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (row[0],row[1],row[2],row[3],row[4]))
#close the connection to the database.
mydb.commit()
cursor.close()
print ("Done")

