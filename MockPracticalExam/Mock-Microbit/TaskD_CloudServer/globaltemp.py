import sqlite3
from flask import make_response, abort

from joblib import dump, load

import numpy as np
from flask import jsonify


def read():
    
    temps = []
    
    conn = sqlite3.connect('temp.db')
    
    c = conn.cursor()
    c.execute('SELECT id, devicename, temp, timestamp FROM temp ORDER BY id ASC')
    results = c.fetchall()
    
    for result in results:
                
        temps.append({'id':result[0],'devicename':result[1],'temp':result[2],'timestamp':result[3]})
    
    conn.close()
    
    return temps



def create(globaltemp):
    '''
    This function creates a new temp record in the database
    based on the passed in temp data
    :param globaltemp:  Global temp record to create in the database
    :return:        200 on success
    '''
    devicename = globaltemp.get('devicename', None)
    temp = globaltemp.get('temp', None)
    timestamp = globaltemp.get('timestamp', None)
    
    conn = sqlite3.connect('temp.db')
    
    c = conn.cursor()    
    sql = "INSERT INTO temp (devicename, temp, timestamp) VALUES('" + devicename + "', " + str(temp) + ", '" + timestamp + "')"
    print(sql)
    c.execute(sql)
    conn.commit()
    conn.close()
    
    return make_response('Global temp record successfully created', 200)



def cluster(temp):
    try:
        temp = float(temp)
        kmeans = load('/Users/eve_lappy/Developer/IS4151/MockPracticalExam/Mock-Microbit/TaskE_MLModel/tempcluster.joblib')

        newX = [[temp]]
        result = kmeans.predict(newX)

        # Label assignment
        cluster_mean = kmeans.cluster_centers_.flatten()
        normal_cluster = int(np.argmin(cluster_mean))
        alert_cluster = int(np.argmax(cluster_mean))

        label = "Normal" if result[0] == normal_cluster else "Alert"

        print(f"🌡️ temp={temp} → cluster={result[0]} ({label})")

        return jsonify({
            "temp": temp,
            "cluster": int(result[0]),
            "label": label
        })

    except Exception as error:
        print(f"❌ Error: {error}")
        return jsonify({"error": str(error), "cluster": "Unknown"})

