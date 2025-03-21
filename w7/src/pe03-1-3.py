import time
import sys

import board
from adafruit_bme280 import basic as adafruit_bme280

import RPi.GPIO as GPIO



# Need to use logical pin numbering due to the Adafruit library
# The corresponding physical pin numbering will be 40, 38, 36 and 32
ledGreenPin = 21 # Physical pin number 40
ledRed1Pin = 20 # Physical pin number 38
ledRed2Pin = 16 # Physical pin number 36
ledRed3Pin = 12 # Physical pin number 32



# Pin Setup
GPIO.setup(ledGreenPin, GPIO.OUT)
GPIO.setup(ledRed1Pin, GPIO.OUT)
GPIO.setup(ledRed2Pin, GPIO.OUT)
GPIO.setup(ledRed3Pin, GPIO.OUT)



i2c = board.I2C()  # uses board.SCL and board.SDA
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)



print('Program running... Press CTRL+C to exit')

try:

	GPIO.output(ledGreenPin, False)
	GPIO.output(ledRed1Pin, False)
	GPIO.output(ledRed2Pin, False)
	GPIO.output(ledRed3Pin, False)
	
	time.sleep(1)
	
	GPIO.output(ledGreenPin, True)
	GPIO.output(ledRed1Pin, True)
	GPIO.output(ledRed2Pin, True)
	GPIO.output(ledRed3Pin, True)	

	time.sleep(1)
		
	GPIO.output(ledGreenPin, False)
	GPIO.output(ledRed1Pin, False)
	GPIO.output(ledRed2Pin, False)
	GPIO.output(ledRed3Pin, False)
		
	while True:		

		degrees = bme280.temperature
		
		print('Temperature = {0:0.3f} deg C'.format(bme280.temperature))
		print('Pressure    = {0:0.2f} hpa'.format(bme280.pressure))
		print('Humidity    = {0:0.2f} %'.format(bme280.humidity))
		print()
		
		if degrees <= 30:
			GPIO.output(ledGreenPin, True)
		else:
			GPIO.output(ledGreenPin, False)
		
		if degrees > 30:
			GPIO.output(ledRed1Pin, True)
		else:
			GPIO.output(ledRed1Pin, False)
		
		if degrees > 40:
			GPIO.output(ledRed2Pin, True)
		else:
			GPIO.output(ledRed2Pin, False)
		
		if degrees > 50:
			GPIO.output(ledRed3Pin, True)
		else:
			GPIO.output(ledRed3Pin, False)			
		
		time.sleep(0.1)

except KeyboardInterrupt:	
	print('Program terminated!')

finally:
    GPIO.cleanup()
