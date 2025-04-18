import sys
import random
import time
import requests
import paho.mqtt.client as mqtt

def main():
    n = len(sys.argv)
    
    if n > 2:
        temp = float(sys.argv[1])
        humidity = float(sys.argv[2])
        print(f'Temp to cluster: {temp}')
        print(f'Humidity to cluster: {humidity}')
        
        # REST API request
        base_uri = 'http://localhost:5050/'
        env_uri = base_uri + 'api/envcluster'
        req = requests.get(env_uri, params={'temp': temp, 'humidity': humidity})

        cluster_label = str(req.text).replace('"', '').strip()
        print('Cluster Label: ' + cluster_label)
        
        # Decide smart control command
        smartlight = 'off'
        if cluster_label == '0':
            smartlight = 'on'
        
        # MQTT Configuration
        broker = 'broker.emqx.io'
        port = 1883
        topic = "/is4151-is5451/mockpe/smartlight"
        client_id = f'python-mqtt-{random.randint(0, 10000)}'
        username = 'emqx'
        password = 'public'        

        # Publish command
        client = mqtt.Client()
        client.username_pw_set(username, password)
        client.connect(broker, port)
        client.publish(topic, smartlight)
        client.disconnect()

        print(f'Smartlight command published: {smartlight}')

    else:
        print("❌ Please provide both temp and humidity as command-line arguments.")
        print("✅ Example: python3 smartcontrol.py 31.2 64.5")

if __name__ == '__main__':
    main()
