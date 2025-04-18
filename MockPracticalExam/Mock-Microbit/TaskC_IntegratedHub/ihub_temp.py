import time
import random

import serial
import RPi.GPIO as GPIO

import sqlite3
import requests
import json

import paho.mqtt.client as mqtt

import _thread as thread



def sendCommand(command):
    command = command + '\n'
    ser.write(str.encode(command))




def waitResponse():
    
    response = ser.readline()
    response = response.decode('utf-8').strip()
    
    return response




def saveData(temps):
    
    conn = sqlite3.connect('temp.db')
    c = conn.cursor()
    
    for temp in temps:
        
        data = temp.split('=')        
        
        sql = "INSERT INTO temp (devicename, temp, timestamp) VALUES('" + data[0] + "', " + data[1] + ", datetime('now', 'localtime'))"
        c.execute(sql)
    
    conn.commit()
    conn.close()
    
    temps.clear()




def rhub():
        
    global ser
    ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=1)
    print('rhub: Listening on /dev/ttyACM0... Press CTRL+C to exit')
    
    # Handshaking
    sendCommand('handshake')
    
    strMicrobitDevices = ''
    
    while strMicrobitDevices == None or len(strMicrobitDevices) <= 0:
        
        strMicrobitDevices = waitResponse()        
        
        print('rhub handshake: ' + strMicrobitDevices)
        
        time.sleep(0.1)
    
    strMicrobitDevices = strMicrobitDevices.split('=')
    
    if len(strMicrobitDevices[1]) > 0:

        listMicrobitDevices = strMicrobitDevices[1].split(',')
        
        if len(listMicrobitDevices) > 0:
                
            for mb in listMicrobitDevices:
            
                print('rhub: Connected to micro:bit device {}...'.format(mb))
            
            while True:
                
                time.sleep(1)                    
                
                commandToTx = 'sensor=temp'                
                sendCommand('cmd:' + commandToTx)                    
                
                if commandToTx.startswith('sensor='):
                    
                    strSensorValues = ''

                    while strSensorValues == None or len(strSensorValues) <= 0:
                        
                        strSensorValues = waitResponse()
                        time.sleep(0.1)

                    listSensorValues = strSensorValues.split(',')

                    for sensorValue in listSensorValues:
                        
                        print('rhub: {}'.format(sensorValue))
                    
                    saveData(listSensorValues)



def cloudrelay():
    
    conn = sqlite3.connect('temp.db')
    ## IF FAIL TEST WITH THIS curl http://192.168.1.253:5050/api/globaltemp

    base_uri = 'http://192.168.1.253:5000/'
    globaltemp_uri = base_uri + 'api/globaltemp'
    headers = {'content-type': 'application/json'}
    
    
    
    while True:
    
        time.sleep(10)
        
        print('Relaying data to cloud server...')
                
        c = conn.cursor()
        c.execute('SELECT id, devicename, temp, timestamp FROM temp WHERE tocloud = 0')
        results = c.fetchall()
        c = conn.cursor()
                
        for result in results:
                    
            print('Relaying id={}; devicename={}; temp={}; timestamp={}'.format(result[0], result[1], result[2], result[3]))
            
            gtemp = {
                'devicename':result[1],
                'temp':result[2],
                'timestamp':result[3]
            }
            req = requests.put(globaltemp_uri, headers = headers, data = json.dumps(gtemp))
            
            c.execute('UPDATE temp SET tocloud = 1 WHERE id = ' + str(result[0]))
        
        conn.commit()



def on_message(client, userdata, msg):
    
    smarttemp = str(msg.payload.decode())
    print('Smarttemp command subscribed: ' + smarttemp)
    
    if smarttemp == 'on':
        
        GPIO.output(redLedPin, True)
        
    else:
    
        GPIO.output(redLedPin, False)



def smarttemp():        
    
    broker = 'broker.emqx.io'
    port = 1883
    topic = "/is4151-is5451/mockpe/smarttemp"
    client_id = f'python-mqtt-{random.randint(0, 10000)}'
    username = 'emqx'
    password = 'public'
    client = mqtt.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)    
    client.subscribe(topic)
    client.on_message = on_message
    client.loop_forever()



def init():    

    GPIO.setmode(GPIO.BOARD)
    
    global redLedPin
    redLedPin = 11
    GPIO.setup(redLedPin, GPIO.OUT)
    GPIO.output(redLedPin, False)



def main():
    
    init()
    
    thread.start_new_thread(rhub, ())
    thread.start_new_thread(cloudrelay, ())
    thread.start_new_thread(smarttemp, ())
    
    print('Program running... Press CTRL+C to exit')
    
    while True:

        try:                       
                        
            time.sleep(0.1)
            
        except RuntimeError as error:
            
            print('Error: {}'.format(error.args[0]))
        
        except Exception as error:
            
            print('Error: {}'.format(error.args[0]))
            
        except KeyboardInterrupt:                  
        
            if ser.is_open:
            
                ser.close()                           
        
            GPIO.cleanup()
            
            print('Program terminating...')
            
            break
    

    print('Program exited...')



if __name__ == '__main__':
    
    main()
