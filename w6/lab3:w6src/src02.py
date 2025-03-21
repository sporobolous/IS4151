# import the GPIO and time package
import RPi.GPIO as GPIO
import time



# Pin  Definitions
ledPin = 11



# Pin Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)



print("Program running... Press CTRL+C to exit")

ledStatus = True
GPIO.output(ledPin, ledStatus)

try:
    while True:
        time.sleep(1)
        ledStatus = not ledStatus
        GPIO.output(ledPin, ledStatus)
	
except KeyboardInterrupt:
    print("Program terminated!")

finally:
    GPIO.cleanup()
