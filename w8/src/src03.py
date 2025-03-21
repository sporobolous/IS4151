from flask import Flask
from flask import request

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():

	if request.method == 'POST':
	
		return 'Hello POST!'
	
	else:
	
		return 'Hello GET!'
