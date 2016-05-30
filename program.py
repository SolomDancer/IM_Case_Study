#!/usr/bin/python
import mysql.connector

city = input("Enter A CITY NAME: ") 
print ("City entered was: ", city)
# Setup MySQL Connection
# Pass viewer: *AAB3E285149C0135D51A520E1940DD3263DC008C
db = mysql.connector.connect(host="173.194.242.211", user="root", password="InfectiousTraining", db="IM_Task_2")
cursor = db.cursor()

queryword = city
query = ("SELECT ct.city_id,  c.country_id, c.name AS Country_Name,  c.alpha2, c.alpha3, ct.Region_Region_id, r.name AS Region_Name,  r.iso_code AS Region_ISO_Code,  ct.city_id, ct.name AS City_Name, ct.iso_code  AS City_ISO_Code, c.targetable  FROM IM_Task_2.City ct INNER JOIN IM_Task_2.Country c ON  ct.Country_country_id=c.country_id LEFT JOIN IM_Task_2.Region r ON  ct.Region_Region_id=r.Region_id WHERE ct.name = '"+queryword+"'")

query2 = ("SELECT COUNT(*) FROM IM_Task_2.City ct INNER JOIN IM_Task_2.Country c ON  ct.Country_country_id=c.country_id LEFT JOIN IM_Task_2.Region r ON  ct.Region_Region_id=r.Region_id WHERE ct.name = '"+queryword+"'")



cursor.execute(query)
results = cursor.fetchall()
cursor.execute(query2)
result=cursor.fetchone()
number_of_rows=result[0]
print (number_of_rows)
for row in results:
	if (number_of_rows > 0):
		print(row)
		print("Here are the details to the following city that you have entered:")
		print("	Country ID is : ",row[1],". The Country it belongs to is: ",row[2],". The 2 letter abrivation is: ",row[3],". The 3 letter abrivation is: ",row[4],".")
		print("		Region ID is: ",row[5],". The Region it belongs to is: ",row[6],". The ISO Code for the region is: ",row[7],".")
		print("				City ID: ",row[8]," The city: ",row[9],". The ISO Code for the city is: ",row[10],".")
		if(row[11]!= '0'):
			print("					This country is targetable.")
		else:
			print("					At the moment this country is not targetable.")
	else:
		print("No resultsfoundat thistime!")

#for (ct.city_id, ct.Region_Region_id, ct.Region_Country_country_id, ct.name, ct.iso_code, r.iso_code, r.name, c.alpha2, c.alpha3, c.name, c.targetable) in cursor:
#  print("{},{},{},{},{},{},{},{},{},{},{}".format(
#    ct.city_id, ct.Region_Region_id, ct.Region_Country_country_id, ct.name, ct.iso_code, r.iso_code, r.name, c.alpha2, c.alpha3, c.name, c.targetable))
	
#cursor.close()
#db.close()
