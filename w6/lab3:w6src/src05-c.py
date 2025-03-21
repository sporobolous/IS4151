# import the GPIO and time package
import RPi.GPIO as GPIO
import time

# Pin Definitions
ledRedPin = 11
ledGreenPin = 13
ledBluePin = 15
butRedPin = 12
butGreenPin = 16
butBluePin = 18
butPatternPin = 22  # NEW: Fourth button

# Track LED states
ledRedState = False
ledGreenState = False
ledBlueState = False
patternMode = False  # NEW

# Track previous button states
prevRedButton = True
prevGreenButton = True
prevBlueButton = True
prevPatternButton = True  # NEW

# Pin Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledRedPin, GPIO.OUT)
GPIO.setup(ledGreenPin, GPIO.OUT)
GPIO.setup(ledBluePin, GPIO.OUT)
GPIO.setup(butRedPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(butGreenPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(butBluePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(butPatternPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # NEW

def turn_off_all_leds():
    GPIO.output(ledRedPin, False)
    GPIO.output(ledGreenPin, False)
    GPIO.output(ledBluePin, False)

def check_pattern_toggle():
    global patternMode, prevPatternButton
    patternButtonState = GPIO.input(butPatternPin)
    if prevPatternButton and not patternButtonState:
        patternMode = not patternMode
        if patternMode:
            print("Pattern mode activated.")
        else:
            print("Pattern mode deactivated. Returning to manual control.")
            turn_off_all_leds()
        time.sleep(0.2)  # Debounce delay
    prevPatternButton = patternButtonState

def pattern_step():
    # Step ii: Turn off all LEDs
    turn_off_all_leds()
    for _ in range(10):  # 1 second
        check_pattern_toggle()
        if not patternMode: return
        time.sleep(0.1)

    # Step iii: Red -> Green -> Blue
    GPIO.output(ledRedPin, True)
    for _ in range(10):
        check_pattern_toggle()
        if not patternMode: return
        time.sleep(0.1)
    GPIO.output(ledRedPin, False)

    GPIO.output(ledGreenPin, True)
    for _ in range(10):
        check_pattern_toggle()
        if not patternMode: return
        time.sleep(0.1)
    GPIO.output(ledGreenPin, False)

    GPIO.output(ledBluePin, True)
    for _ in range(10):
        check_pattern_toggle()
        if not patternMode: return
        time.sleep(0.1)
    GPIO.output(ledBluePin, False)

    # Step iv: Pause
    for _ in range(10):
        check_pattern_toggle()
        if not patternMode: return
        time.sleep(0.1)

    # Step v-vi: Blink 3 times
    for _ in range(3):
        GPIO.output(ledRedPin, True)
        GPIO.output(ledGreenPin, True)
        GPIO.output(ledBluePin, True)
        for _ in range(3):  # 0.3s
            check_pattern_toggle()
            if not patternMode: return
            time.sleep(0.1)

        turn_off_all_leds()
        for _ in range(3):  # 0.3s
            check_pattern_toggle()
            if not patternMode: return
            time.sleep(0.1)

print("Program running... Press CTRL+C to exit")

try:
    while True:
        check_pattern_toggle()

        if patternMode:
            pattern_step()
            continue

        # Manual LED toggle mode
        currentRedButton = GPIO.input(butRedPin)
        if prevRedButton and not currentRedButton:
            ledRedState = not ledRedState
            GPIO.output(ledRedPin, ledRedState)
        prevRedButton = currentRedButton

        currentGreenButton = GPIO.input(butGreenPin)
        if prevGreenButton and not currentGreenButton:
            ledGreenState = not ledGreenState
            GPIO.output(ledGreenPin, ledGreenState)
        prevGreenButton = currentGreenButton

        currentBlueButton = GPIO.input(butBluePin)
        if prevBlueButton and not currentBlueButton:
            ledBlueState = not ledBlueState
            GPIO.output(ledBluePin, ledBlueState)
        prevBlueButton = currentBlueButton

        time.sleep(0.05)

except KeyboardInterrupt:
    print("Program terminated!")

finally:
    GPIO.cleanup()
