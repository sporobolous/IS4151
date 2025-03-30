import serial

try:
    # Replace COM port with the appropriate Linux serial port
    comPort = '/dev/ttyACM0'  # This is typical for micro:bit on Pi
    
    ser = serial.Serial(port=comPort, baudrate=115200, timeout=1)

    print(f'Listening on {comPort}... Press CTRL+C to exit')

    while True:
        msg = ser.readline()
        if msg:
            smsg = msg.decode('utf-8').strip()
            print(f'RX: {smsg}')

except serial.SerialException as err:
    print(f'SerialException: {err}')

except KeyboardInterrupt:
    print('Program terminated!')
