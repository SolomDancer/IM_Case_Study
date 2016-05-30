#!/usr/bin/python
import csv
import mysql.connector
import codecs
import json

mydb = mysql.connector.connect(host="173.194.242.211", user="root", password="InfectiousTraining", db="IM_Task_2")
cursor = mydb.cursor()

count = 0
errors = 0

with open('cities', 'r', encoding=('utf-8')) as f:
	for line in f:
		d = json.loads(line)
		Squery = ("SELECT COUNT(*) from Country where country_id = '"+d.get('country_id')+"'")
		cursor.execute(Squery)
		result=cursor.fetchone()
		number_of_rows=result[0]
		if(number_of_rows > 0):
			if d.get('region_id'):
				Squery2 = ("SELECT COUNT(*) from Region where region_id = '"+d.get('region_id')+"'")
				cursor.execute(Squery2)
				result2=cursor.fetchone()
				number_of_rows2=result2[0]
				if(number_of_rows2 > 0):
					print("LOOP 1 INSERTING:-> ",d.get('id').encode('latin-1')," ",d.get('country_id').encode('latin-1')," ",d.get('iso_code').encode('latin-1')," ",d.get('region_id').encode('latin-1')," ",d.get('name').encode('latin-1'))
					Iquery = "INSERT IGNORE INTO IM_Task_2.City (city_id, name, iso_code, Region_Region_id, Country_country_id) VALUES (%s, %s, %s, %s, %s)"
					cursor.execute(Iquery, (d.get('id'),d.get('name'),d.get('iso_code'),d.get('region_id'),d.get('country_id')))
					count = count +1
					mydb.commit()
				else:
					print("LOOP 2 logging:-> ",d.get('id').encode('latin-1')," ",d.get('country_id').encode('latin-1')," ",d.get('iso_code').encode('latin-1')," ",d.get('region_id').encode('latin-1')," ",d.get('name').encode('latin-1'))
					Lquery = "INSERT INTO IM_Task_2.error (Table_errored, Data) VALUES ('City', 'City_ID: '%s' | Region_ID: '%s' | Country_id: '%s' | name: '%s' | iso_code: '%s' |')"
					cursor.execute(Lquery, (d.get('id')," ",d.get('country_id')," ",d.get('iso_code')," ",d.get('region_id')," ",d.get('name')))
					count = count +1
					errors = errors +1
					mydb.commit()
			else:
				print("LOOP 3 INSERTING:-> ",d.get('id').encode('latin-1')," ",d.get('country_id').encode('latin-1')," ",d.get('iso_code').encode('latin-1')," ",d.get('name').encode('latin-1'))
				Iquery = "INSERT IGNORE INTO IM_Task_2.City (city_id, name, iso_code, Country_country_id) VALUES (%s, %s, %s, %s)"
				cursor.execute(Iquery, (d.get('id'),d.get('name'),d.get('iso_code'),d.get('country_id')))
				count = count +1
				mydb.commit()
		else:
			print("LOOP 4 logging:-> ",d.get('id').encode('latin-1')," ",d.get('country_id').encode('latin-1')," ",d.get('iso_code').encode('latin-1')," ",d.get('name').encode('latin-1'))
			Lquery = "INSERT INTO IM_Task_2.error (Table_errored, Data) VALUES ('City', 'City_ID: '%s' | Country_id: '%s' | name: '%s' | iso_code: '%s' |')"
			cursor.execute(Lquery, (d.get('id')," ",d.get('country_id')," ",d.get('iso_code')," ",d.get('name')))
			count = count +1
			errors = errors +1
			mydb.commit()
		
#close the connection to the database. id,alpha2,alpha3,name,targetable
print("Total Number of rows: ", count)		
print("Total Number of errors: ", errors)	
mydb.commit()
cursor.close()
print ("Done")