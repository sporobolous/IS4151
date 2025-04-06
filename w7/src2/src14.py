# import the GPIO and time package
import RPi.GPIO as GPIO
import time



# Pin  Definitions
pirSensorPin = 12



# Pin Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pirSensorPin, GPIO.IN)



print("Program running... Press CTRL+C to exit")

try:
    
	while True:
		
		if GPIO.input(pirSensorPin):
		
			print('Motion detected!')
			
		else:
			
			print('No motion detected...')
		
		time.sleep(0.1)
	
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program terminated!")
