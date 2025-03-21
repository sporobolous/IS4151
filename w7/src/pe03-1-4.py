# run this command first
# pip3 install adafruit-circuitpython-tcs34725



import time
import sys

import RPi.GPIO as GPIO
import board
import busio
import adafruit_tcs34725



ledPin = 18 # Not board mode



# Pin Setup
GPIO.setup(ledPin, GPIO.OUT)

# to run program normally with led on
# python pe03-1-4.py led=on
# to run program normally with led off
# python pe03-1-4.py led=off

if len(sys.argv) > 1:
	if sys.argv[1].split('=')[0] == 'led' and sys.argv[1].split('=')[1] == 'on':
		GPIO.output(ledPin, True)
	else:
		GPIO.output(ledPin, False)
else:
	GPIO.output(ledPin, False)

# to turn off led only
# python pe03-1-4.py led=off ledonly
if len(sys.argv) > 2:
	if sys.argv[2] == 'ledonly':
		sys.exit()


i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)



print('Program running... Press CTRL+C to exit')

try:	
		
	while True:
		
		print('Color: ({0}, {1}, {2})'.format(*sensor.color_rgb_bytes))
		print('Temperature: {0}K'.format(sensor.color_temperature))
		print('Lux: {0}'.format(sensor.lux))
		
		time.sleep(1)

except KeyboardInterrupt:	
	print('Program terminated!')

finally:
    GPIO.cleanup()
