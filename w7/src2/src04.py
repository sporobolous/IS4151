# demo temperature service



import time
from bluetooth import ble

import util
from bleuartlib import BleUartDevice



def addBleUartDevice(address, name):
	
	bleUartDevice = BleUartDevice(address)
	bleUartDevice.connect()
	
	bleUartDevices.append({'device':bleUartDevice, 'name':name})



def getTemperatureFromAllBleUartDevices():

	for bled in bleUartDevices:
		
		temp = bled['device'].readTemperature()
		print('{}\'s Temperature = {}'.format(bled['name'], temp))



def disconnectFromAllBleUartDevices():
	
	for bled in bleUartDevices:
		
		bled['device'].disconnect()
		bled['device'] = None



try:

	bleUartDevices = []

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
						
			print('Getting temperature from all micro:bit devices...')
			getTemperatureFromAllBleUartDevices()
			time.sleep(5)

except KeyboardInterrupt:
	
	print('********** END')
	
except:

	print('********** UNKNOWN ERROR')

finally:

	disconnectFromAllBleUartDevices()
	print('Disconnected from all micro:bit devices')
