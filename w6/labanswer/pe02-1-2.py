import serial



try:
	comPort = 'COM14' # this is for windows
	# use ls /dev/cu.* | grep usbmodem
	# to find the port for mac then change the comPort to '/dev/cu.usbmodem14202' for example
	
	ser = serial.Serial(port=comPort, baudrate=115200)
	
	print('Listening on {}... Press CTRL+C to exit'.format(comPort))
	
	while True:			
		
		# Read newline terminated data
		msg = ser.readline()
		smsg = msg.decode('utf-8').strip()
		print('RX:{}'.format(smsg))
	
except serial.SerialException as err:
	
	print('SerialException: {}'.format(err))

except KeyboardInterrupt:
	
	print('Program terminated!')
