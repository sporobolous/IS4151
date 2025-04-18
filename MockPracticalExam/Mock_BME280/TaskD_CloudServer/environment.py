import sqlite3
from flask import make_response, abort

from joblib import dump, load



def read():
    
    readings = []
    
    conn = sqlite3.connect('/Users/eve_lappy/Developer/IS4151/MockPracticalExam/Mock_BME280/TaskD_CloudServer/environment.db')
    
    c = conn.cursor()
    c.execute('SELECT id, temp, humidity, pressure, timestamp FROM environment ORDER BY id ASC')
    results = c.fetchall()
    
    for result in results:
                
        readings.append({'id': result[0],'temp': result[1], 'humidity': result[2],'pressure': result[3],'timestamp': result[4] })
    
    conn.close()
    
    return readings



def create(environment):
    '''
    This function creates a new light record in the database
    based on the passed in light data
    :param globallight:  Global light record to create in the database
    :return:        200 on success
    '''
    temp = environment.get('temp', None)
    humidity = environment.get('humidity', None)
    pressure = environment.get('pressure', None)
    timestamp = environment.get('timestamp', None)

    
    conn = sqlite3.connect('/Users/eve_lappy/Developer/IS4151/MockPracticalExam/Mock_BME280/TaskD_CloudServer/environment.db')
    
    c = conn.cursor()    
    sql = "INSERT INTO environment (temp, humidity, pressure, timestamp) VALUES (?, ?, ?, ?)"
    print(sql)
    c.execute(sql, (temp, humidity, pressure, timestamp))  # ✅ This supplies 4 values

    conn.commit()
    conn.close()
    
    return make_response('Global environment record successfully created', 200)



def cluster(temp, humidity):
    try:
        kmeans = load('envcluster.joblib')
        newX = [[temp, humidity]]
        result = kmeans.predict(newX)
        print(f'Cluster result: temp={temp}, humidity={humidity} → cluster={result[0]}')
        return str(result[0])
    except Exception as error:
        print(f'Error: {error}')
        return 'Unknown'

