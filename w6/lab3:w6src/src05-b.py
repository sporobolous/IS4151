# import the GPIO and time package
import RPi.GPIO as GPIO
import time



# Pin  Definitions
ledRedPin = 11
ledGreenPin = 13
ledBluePin = 15
butRedPin = 12
butGreenPin = 16
butBluePin = 18

# Track LED states
ledRedState= False
ledGreenState = False
ledBlueState = False

# Track previous button states
prevRedButton= True
prevGreenButton = True
prevBlueButton = True

# Pin Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledRedPin, GPIO.OUT)
GPIO.setup(ledGreenPin, GPIO.OUT)
GPIO.setup(ledBluePin, GPIO.OUT)
GPIO.setup(butRedPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(butGreenPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(butBluePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)



print("Program running... Press CTRL+C to exit")

try:
    while True:
        # RED
        currentRedButton = GPIO.input(butRedPin)
        if prevRedButton and not currentRedButton:  # Button was released and now pressed
            ledRedState = not ledRedState
            GPIO.output(ledRedPin, ledRedState)
        prevRedButton = currentRedButton

        # GREEN
        currentGreenButton = GPIO.input(butGreenPin)
        if prevGreenButton and not currentGreenButton:
            ledGreenState = not ledGreenState
            GPIO.output(ledGreenPin, ledGreenState)
        prevGreenButton = currentGreenButton

        # BLUE
        currentBlueButton = GPIO.input(butBluePin)
        if prevBlueButton and not currentBlueButton:
            ledBlueState = not ledBlueState
            GPIO.output(ledBluePin, ledBlueState)
        prevBlueButton = currentBlueButton
        
        time.sleep(0.1)
	
except KeyboardInterrupt:	
	print("Program terminated!")

finally:
    GPIO.cleanup()
