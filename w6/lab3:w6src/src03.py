# import the GPIO and time package
import RPi.GPIO as GPIO
import time



# Pin Definitions
butPin = 12



# Pin Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)



print("Program running... Press CTRL+C to exit")

try:
    while True:
        if GPIO.input(butPin):
            print("Button released!")
        else:
            print("Button pressed!")
        time.sleep(0.25)
	
except KeyboardInterrupt:
    print("Program terminated!")

finally:
    GPIO.cleanup()
