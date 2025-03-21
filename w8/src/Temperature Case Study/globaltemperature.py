import mysql.connector
from flask import make_response, abort



def read():
	
	temperatures = []
	
	conn = mysql.connector.connect(
		host='localhost',
		user='root',
		passwd='password',
		database='temperature'
	)
	
	c = conn.cursor()
	c.execute('SELECT devicename, AVG(temp) AS averagetemp FROM temperature GROUP BY devicename ORDER BY devicename ASC')
	results = c.fetchall()
	
	for result in results:
				
		temperatures.append({'devicename':result[0],'averagetemp':result[1]})
	
	conn.close()
	
	return temperatures



def create(globaltemperature):
	'''
	This function creates a new temperature record in the database
	based on the passed in temperature data
	:param globaltemperature:  Global temperature record to create in the database
	:return:        200 on success
	'''
	devicename = globaltemperature.get('devicename', None)
	temp = globaltemperature.get('temp', None)
	timestamp = globaltemperature.get('timestamp', None)
	
	conn = mysql.connector.connect(
		host='localhost',
		user='root',
		passwd='password',
		database='temperature'
	)
	
	c = conn.cursor()	
	sql = "INSERT INTO temperature (devicename, temp, timestamp) VALUES('" + devicename + "', " + str(temp) + ", '" + timestamp + "')"
	print(sql)
	c.execute(sql)
	conn.commit()
	conn.close()
	
	return make_response('Global temperature record successfully created', 200)
