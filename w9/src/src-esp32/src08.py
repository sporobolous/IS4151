import connexion

import sqlite3



app = connexion.App(__name__, specification_dir='./')
app.add_api('src08.yml')



@app.route('/')
def index():
    
    html = '<html><head><title>DHT11 Sensor REST web service</title></head><body><h1>DHT11 Sensor REST web service</h1><p>For demonstration purpose only...</p></body></html>'       

    return html



# If we're running in stand alone mode, run the application
if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
