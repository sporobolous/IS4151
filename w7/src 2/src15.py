# import the GPIO and time package
import RPi.GPIO as GPIO
import time
from datetime import datetime
from picamera import PiCamera



# Pin  Definitions

ledRedPin = 40
ledGreenPin = 38
pirSensorPin = 12



# Pin Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledRedPin, GPIO.OUT)
GPIO.setup(ledGreenPin, GPIO.OUT)
GPIO.setup(pirSensorPin, GPIO.IN)



camera = PiCamera()



print("Program running... Press CTRL+C to exit")

try:
    
	while True:
		
		if GPIO.input(pirSensorPin):
		
			GPIO.output(ledRedPin, True)
			GPIO.output(ledGreenPin, False)
			print('Motion detected!')
			
			filePath = '/home/pi/Documents/is4151-is5451/lecture07'
			fileName =  datetime.now().strftime("%Y%m%d%H%M%S") + '.jpg'
			camera.capture(filePath + '/' + fileName)			
			
			time.sleep(3)
			
		else:
			
			GPIO.output(ledRedPin, False)
			GPIO.output(ledGreenPin, True)
		
		time.sleep(0.1)
	
except KeyboardInterrupt:    
	
    print("Program terminated!")

finally:
	
	GPIO.cleanup()
