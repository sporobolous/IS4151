import time
import random
import serial
import sqlite3
import requests
import json
import paho.mqtt.client as mqtt
from joblib import load
from adafruit_bme280 import basic as adafruit_bme280
import board
import _thread as thread

# ===== GPIO & Sensor Init =====
def init():


    # BME280
    global bme280
    i2c = board.I2C()
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# ===== Serial Comm Utilities =====
def sendCommand(command):
    command = command + '\n'
    ser.write(str.encode(command))

def waitResponse():
    response = ser.readline().decode('utf-8').strip()
    return response

# ===== SQLite Save Function =====
def saveData(temp, humidity, pressure):
    conn = sqlite3.connect('environment.db')
    c = conn.cursor()
    sql = "INSERT INTO environment (temp, humidity, pressure, timestamp) VALUES (?, ?, ?, datetime('now', 'localtime'))"
    c.execute(sql, (temp, humidity, pressure))
    conn.commit()
    conn.close()

# ===== Radio Hub Communication =====
def rhub():
    global ser
    ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=1)
    print('rhub: Listening on /dev/ttyACM0... Press CTRL+C to exit')

    # Handshake
    sendCommand('handshake')
    strMicrobitDevices = ''
    while not strMicrobitDevices:
        strMicrobitDevices = waitResponse()
        print('rhub handshake: ' + strMicrobitDevices)
        time.sleep(0.1)

    # Continuous Sensor Loop
    while True:
        time.sleep(1)

        temp = round(bme280.temperature, 2)
        humidity = round(bme280.humidity, 2)
        pressure = round(bme280.pressure, 2)
        print(f"BME280: T={temp}°C, H={humidity}%, P={pressure}hPa")

        # Save locally
        saveData(temp, humidity, pressure)

        # Every 10 seconds: send humidity via serial
        if int(time.time()) % 10 == 0:
            sendCommand(f"radio:humidity={humidity}")

# ===== Cloud Relay (Optional) =====
def cloudrelay():
    conn = sqlite3.connect('environment.db')
    base_uri = 'http://192.168.1.253:5050/'  # UPDATE TO YOUR CLOUD IP
    endpoint = base_uri + 'api/environment'
    headers = {'content-type': 'application/json'}

    while True:
        time.sleep(10)
        print('Relaying data to cloud server...')

        c = conn.cursor()
        c.execute('SELECT id, temp, humidity, pressure, timestamp FROM environment WHERE tocloud = 0')
        results = c.fetchall()
        c = conn.cursor()

        for result in results:
            payload = {
                'temp': result[1],
                'humidity': result[2],
                'pressure': result[3],
                'timestamp': result[4]
            }
            try:
                req = requests.put(endpoint, headers=headers, data=json.dumps(payload))
                c.execute('UPDATE environment SET tocloud = 1 WHERE id = ?', (result[0],))
            except Exception as e:
                print(f"Cloud relay error: {e}")

        conn.commit()

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"[MQTT] Received smartlight command: {message}")

    # Send to bController via serial (formatted as expected)
    if message in ["on", "off"]:
        rain_command = "radio:rain=yes" if message == "on" else "radio:rain=no"
        sendCommand(rain_command)
        print(f"[SERIAL] Sent to bController: {rain_command}")

def smartlight():
    broker = 'broker.emqx.io'
    port = 1883
    topic = "/is4151-is5451/mockpe/smartlight"
    client_id = f'python-mqtt-{random.randint(0, 10000)}'
    username = 'emqx'
    password = 'public'

    client = mqtt.Client(callback_api_version=mqtt.MQTTv311)

    client.username_pw_set(username, password)
    client.on_message = on_message

    print("[MQTT] Connecting to broker...")
    client.connect(broker, port)
    client.subscribe(topic)

    print(f"[MQTT] Subscribed to topic: {topic}")
    client.loop_forever()


# ===== Main Loop =====
def main():
    init()
    thread.start_new_thread(rhub, ())
    thread.start_new_thread(cloudrelay, ())
    thread.start_new_thread(smartlight, ())

    print('Program running... Press CTRL+C to exit')

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        if ser.is_open:
            ser.close()
       
        print('Program terminating...')

if __name__ == '__main__':
    main()