# python -m flask --app src29-flask run

import numpy as np

import time

from flask import Flask
from flask import url_for



app = Flask(__name__)



@app.route('/')
def index():
    
    np.random.seed(int(round(time.time())))
    
    imageSrc = url_for('static', filename='temp.png')
    imageSrc = imageSrc + '?random=' + str(np.random.random())
    strHtml = '<html><head><script type="text/javascript">function init(){setTimeout(reload, 5000);}function reload(){location.reload(true);setTimeout(reload, 5000);}</script></head><body onload="init()"><img src="' + imageSrc + '?" /></body></html>'
    
    return strHtml
