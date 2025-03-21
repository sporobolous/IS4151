from flask import Flask
from flask import request

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():

	if request.method == 'GET':
				
		strHtml = '<form method="post" action="/">'
		strHtml = strHtml + '<label for="email">Email</label> <input type="text" id="email" name="email" /><br/>'
		strHtml = strHtml + '<label for="password">Password</label> <input type="password" id="password" name="password" /><br/>'
		strHtml = strHtml + '<input type="reset" /> <input type="submit" />'
		strHtml = strHtml + '</form>'
		
		return strHtml
		
	elif request.method == 'POST':
		
		print('Login: email={}, password={}'.format(request.form['email'], request.form['password']))
		
		return 'Login successfully!'
	
	else:
		
		# we won't see this because the other methods are not defined in @app.route
		return 'Unsupported HTTP Method'
