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
butPatternPin = 22



# Pin Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledRedPin, GPIO.OUT)
GPIO.setup(ledGreenPin, GPIO.OUT)
GPIO.setup(ledBluePin, GPIO.OUT)
GPIO.setup(butRedPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(butGreenPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(butBluePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(butPatternPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

ledRedState = False
ledGreenState = False
ledBlueState = False
patternMode = False
patternStep = 0
baseTime = 0
timeElapsed = 0

GPIO.output(ledRedPin, False)
GPIO.output(ledGreenPin, False)
GPIO.output(ledBluePin, False)



print('Program running... Press CTRL+C to exit')

try:
	while True:
	
		if not patternMode:
			
			if not GPIO.input(butRedPin):
				ledRedState = not ledRedState
				GPIO.output(ledRedPin, ledRedState)
				time.sleep(0.5)
			
			if not GPIO.input(butGreenPin):
				ledGreenState = not ledGreenState
				GPIO.output(ledGreenPin, ledGreenState)
				time.sleep(0.5)
			
			if not GPIO.input(butBluePin):
				ledBlueState = not ledBlueState
				GPIO.output(ledBluePin, ledBlueState)
				time.sleep(0.5)
			
		else:
			
			timeElapsed = time.time() - baseTime
			
			if timeElapsed >= 1:
			
				if patternStep == 1:
					
					GPIO.output(ledRedPin, True)
					GPIO.output(ledGreenPin, False)
					GPIO.output(ledBluePin, False)
					patternStep += 1
					baseTime = time.time()
				
				elif patternStep == 2:
					
					GPIO.output(ledRedPin, False)
					GPIO.output(ledGreenPin, True)
					GPIO.output(ledBluePin, False)
					patternStep += 1
					baseTime = time.time()
				
				elif patternStep == 3:
					
					GPIO.output(ledRedPin, False)
					GPIO.output(ledGreenPin, False)
					GPIO.output(ledBluePin, True)
					patternStep += 1
					baseTime = time.time()
				
				elif patternStep == 4:
					
					GPIO.output(ledRedPin, False)
					GPIO.output(ledGreenPin, False)
					GPIO.output(ledBluePin, False)
					patternStep += 1
					baseTime = time.time()
			
			elif timeElapsed >= 0.3:
				
				if patternStep in [6,8,10]:
					
					GPIO.output(ledRedPin, False)
					GPIO.output(ledGreenPin, False)
					GPIO.output(ledBluePin, False)
					patternStep += 1
					baseTime = time.time()
				
				elif patternStep in [5,7,9]:
					
					GPIO.output(ledRedPin, True)
					GPIO.output(ledGreenPin, True)
					GPIO.output(ledBluePin, True)
					patternStep += 1
					baseTime = time.time()
			
			if patternStep == 11:
			
				patternStep = 1
		
		if not GPIO.input(butPatternPin):
		
			patternMode = not patternMode
			
			ledRedState = False
			ledGreenState = False
			ledBlueState = False
			GPIO.output(ledRedPin, False)
			GPIO.output(ledGreenPin, False)
			GPIO.output(ledBluePin, False)
			
			time.sleep(0.5)
			
			if patternMode:
			
				print('Entering pattern mode at {}'.format(time.time()))
				patternStep = 1
				baseTime = time.time()
				
			else:
			
				print('Exiting pattern mode at {}'.format(time.time()))
		
		time.sleep(0.1)
	
except KeyboardInterrupt:

	print('Program terminated!')

finally:
	
    GPIO.cleanup()
