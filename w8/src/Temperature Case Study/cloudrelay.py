import time
import sqlite3
import requests
import json



try:
	conn = sqlite3.connect('temperature.db')
	
	base_uri = 'http://169.254.78.152:5000/'
	globaltemperature_uri = base_uri + 'api/globaltemperature'
	headers = {'content-type': 'application/json'}
	
	
	
	while True:
	
		time.sleep(10)
		
		print('Relaying data to cloud server...')
				
		c = conn.cursor()
		c.execute('SELECT id, devicename, temp, timestamp FROM temperature WHERE tocloud = 0')
		results = c.fetchall()
		c = conn.cursor()
				
		for result in results:
					
			print('Relaying id={}; devicename={}; temp={}; timestamp={}'.format(result[0], result[1], result[2], result[3]))
			
			gtemp = {
				'devicename':result[1],
				'temp':result[2],
				'timestamp':result[3]
			}
			req = requests.put(globaltemperature_uri, headers = headers, data = json.dumps(gtemp))
			
			c.execute('UPDATE temperature SET tocloud = 1 WHERE id = ' + str(result[0]))
		
		conn.commit()



except KeyboardInterrupt:
	
	print('********** END')
	
except Error as err:

	print('********** ERROR: {}'.format(err))

finally:

	conn.close()
