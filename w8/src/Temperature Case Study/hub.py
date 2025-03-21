import time
from bluetooth import ble

import sqlite3

import util
from bleuartlib import BleUartDevice



def bleUartReceiveCallback(data):
	dataParts = data.split('=')
	temperatures.append({'devicename':dataParts[0], 'temp':dataParts[2]})	
	
	print('Received data: Device Name = {}; Sensor Type = {}; Sensor Value = {}'.format(dataParts[0], dataParts[1], dataParts[2]))



def addBleUartDevice(address, name):
	
	bleUartDevice = BleUartDevice(address)
	bleUartDevice.connect()
	bleUartDevice.enable_uart_receive(bleUartReceiveCallback)
	
	bleUartDevices.append({'device':bleUartDevice, 'name':name})



def sendCommandToAllBleUartDevices(command):
	
	for bled in bleUartDevices:		
		
		bled['device'].send(command)



def disconnectFromAllBleUartDevices():
	
	for bled in bleUartDevices:
		
		bled['device'].disconnect()
		bled['device'] = None



def saveData():
	
	c = conn.cursor()
	
	for temperature in temperatures:
		
		devicename = '' + temperature['devicename']
		devicename = devicename.strip('\x00')
		temp = '' + temperature['temp']
		temp = temp.strip('\x00')
		
		sql = "INSERT INTO temperature (devicename, temp, timestamp) VALUES('" + devicename + "', " + temp + ", datetime('now', 'localtime'))"				
		c.execute(sql)
	
	conn.commit()
	
	temperatures.clear()


try:
	conn = sqlite3.connect('temperature.db')

	bleUartDevices = []
	temperatures = []

	service = ble.DiscoveryService()
	devices = service.discover(2)

	print('********** Initiating device discovery......')

	for address,name in devices.items():

		if address == 'E9:01:B2:1A:C5:4E':

			print('Found BBC micro:bit [vavet]: {}'.format(address))
			addBleUartDevice(address, 'vavet')
			
			print('Added micro:bit device...')
			
		elif address == 'C8:06:B1:B4:66:53':

			print('Found BBC micro:bit [tipov]: {}'.format(address))
			addBleUartDevice(address, 'tipov')
			
			print('Added micro:bit device...')
        
		elif address == 'DF:60:7F:9B:61:F6':

			print('Found BBC micro:bit [popap]: {}'.format(address))
			addBleUartDevice(address, 'popap')
			
			print('Added micro:bit device...')
	
	if len(bleUartDevices) > 0:	
		
		while True:
		
			time.sleep(5)
			print('Sending command to all micro:bit devices...')
			sendCommandToAllBleUartDevices('sensor=temp')
			print('Finished sending command to all micro:bit devices...')
			saveData()


except KeyboardInterrupt:
	
	print('********** END')
	
except:

	print('********** UNKNOWN ERROR')

finally:

	conn.close()
	disconnectFromAllBleUartDevices()
	print('Disconnected from micro:bit devices')
