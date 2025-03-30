# demo temperature service

import time
from bluetooth import ble

import util
from bleuartlib import BleUartDevice



try:

	bleUartDevice1 = None
	found_microbit = False

	service = ble.DiscoveryService()
	devices = service.discover(2)

	print('********** Initiating device discovery......')

	for address,name in devices.items():

		found_microbit = False

		if address == 'E9:01:B2:1A:C5:4E':

			print('Found BBC micro:bit [vavet]: {}'.format(address))
			found_microbit = True
			break
	
	if found_microbit:

		bleUartDevice1 = BleUartDevice(address)
		bleUartDevice1.connect()
		print('Connected to micro:bit device')
	
		while True:				
				
			temp = bleUartDevice1.readTemperature()
			print('Temperature = {}'.format(temp))
			time.sleep(1)
			
except KeyboardInterrupt:
	
	print('********** END')
	
except:

	print('********** UNKNOWN ERROR')

finally:

	if bleUartDevice1 != None:
		
		bleUartDevice1.disconnect()
		bleUartDevice1 = None
		print('Disconnected from micro:bit device')
