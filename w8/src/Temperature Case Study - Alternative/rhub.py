import serial
import time
import sqlite3



def sendCommand(command):
		
	command = command + '\n'
	ser.write(str.encode(command))



def waitResponse():
	
	response = ser.readline()
	response = response.decode('utf-8').strip()
	
	return response



def saveData(temperatures):
	
	c = conn.cursor()
	
	for temperature in temperatures:
		
		data = temperature.split('=')		
		
		sql = "INSERT INTO temperature (devicename, temp, timestamp) VALUES('" + data[0] + "', " + data[1] + ", datetime('now', 'localtime'))"
		c.execute(sql)
	
	conn.commit()
	
	temperatures.clear()



try:

	print("Listening on /dev/ttyACM0... Press CTRL+C to exit")	
	ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=1)
	
	
	
	conn = sqlite3.connect('temperature.db')
	
	
	
	# Handshaking
	sendCommand('handshake')
	
	strMicrobitDevices = ''
	
	while strMicrobitDevices == None or len(strMicrobitDevices) <= 0:
		
		strMicrobitDevices = waitResponse()
		time.sleep(0.1)
	
	strMicrobitDevices = strMicrobitDevices.split('=')
	
	if len(strMicrobitDevices[1]) > 0:

		listMicrobitDevices = strMicrobitDevices[1].split(',')
		
		if len(listMicrobitDevices) > 0:
				
			for mb in listMicrobitDevices:
			
				print('Connected to micro:bit device {}...'.format(mb))
			
			while True:
				
				time.sleep(5)
				print('Sending command to all micro:bit devices...')
				
				commandToTx = 'sensor=temp'				
				sendCommand('cmd:' + commandToTx)
				print('Finished sending command to all micro:bit devices...')
				
				if commandToTx.startswith('sensor='):
					
					strSensorValues = ''

					while strSensorValues == None or len(strSensorValues) <= 0:
						
						strSensorValues = waitResponse()
						time.sleep(0.1)

					listSensorValues = strSensorValues.split(',')

					for sensorValue in listSensorValues:
						
						print(sensorValue)
					
					saveData(listSensorValues)
	
except KeyboardInterrupt:
		
	print("Program terminated!")

except:

	print('********** UNKNOWN ERROR')

finally:
	
	if ser.is_open:
		ser.close()
		
	conn.close()
