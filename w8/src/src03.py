from flask import Flask
from flask import request

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():

	if request.method == 'POST':
	
		return 'Hello POST!' 
        # curl -X POST http://localhost:5000/
	else:
	
		return 'Hello GET!'
        # curl http://localhost:5000