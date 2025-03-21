# import the GPIO and time package
import RPi.GPIO as GPIO
import time



# Pin  Definitions
ledPin = 11



# Pin Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)



print("Program running... Press CTRL+C to exit")

try:
    for i in range(50):                
        GPIO.output(ledPin, True)
        time.sleep(1)
        GPIO.output(ledPin, False)
        time.sleep(1)
	
except KeyboardInterrupt:
    print("Program terminated!")
    
finally:
    GPIO.cleanup()
