import sys
import random
import time

import requests

import paho.mqtt.client as mqtt



def main():
    
    n = len(sys.argv)
    
    if n > 1:
        
        arg = sys.argv[1]
        print('Temp to cluster: ' + arg)
        
        base_uri = 'http://localhost:5050/'
        # http://localhost:5050/api/ui/#/Get%20cluster%20label%20of%20temp
        tempcluster_uri = base_uri + 'api/tempcluster'        
        req = requests.get(tempcluster_uri, params={'temp': arg})
        cluster_label = str(req.text).replace('"', '')
        cluster_label = cluster_label.strip()
        print('Cluster Label: ' + cluster_label)
        
        smartlight = 'off'
        
        if cluster_label == '0':       
        
            smartlight = 'on'
                
        broker = 'broker.emqx.io'
        port = 1883
        topic = "/is4151-is5451/mockpe/smarttemp"
        client_id = f'python-mqtt-{random.randint(0, 10000)}'
        username = 'emqx'
        password = 'public'        
        client = mqtt.Client()
        client.username_pw_set(username, password)
        client.connect(broker, port)
        client.publish(topic, smartlight)
        client.disconnect()
        
        print('Smartlight command published: ' + smartlight)


if __name__ == '__main__':
    
    main()