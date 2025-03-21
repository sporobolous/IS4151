import sqlite3



def read():
	
	temperatures = []
	
	conn = sqlite3.connect('temperature.db')
	c = conn.cursor()
	c.execute('SELECT devicename, AVG(temp) AS averagetemp FROM temperature GROUP BY devicename ORDER BY devicename ASC')
	results = c.fetchall()
	
	for result in results:
				
		temperatures.append({'devicename':result[0],'averagetemp':result[1]})
	
	conn.close()
	
	return temperatures	
	
