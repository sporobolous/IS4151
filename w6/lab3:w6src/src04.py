# import the GPIO and time package
import RPi.GPIO as GPIO
import time



# Pin  Definitions
ledPin = 11
butPin = 12



# Pin Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)



print("Program running... Press CTRL+C to exit")

try:
    while True:
        if GPIO.input(butPin):
			# button is released
            GPIO.output(ledPin, False)			
        else:
			# button is pressed
            GPIO.output(ledPin, True)
        time.sleep(0.1)
	
except KeyboardInterrupt:
    print("Program terminated!")

finally:
    GPIO.cleanup()
