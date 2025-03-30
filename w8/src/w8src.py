from flask import Flask

app = Flask(__name__)

@app.route("/") # src01
def hello():
    return "Hello World!"

# Routing

## variables rules
### <variable_name>
@app.route("/hello") # the /hello 
def greet(): #is binded to this method called greet()
    return "Hello from Flask"

@app.route('/greeting/<name>/<int:age>')
def greeting(name, age):

	print(type(name))
	print(type(age))
	return 'Hello {}! You are {} years old!'.format(name, age)

@app.route("/post/<int:post_id>") # specify type converters
def show_post(post_id):
    return f"Post ID: {post_id}"


@app.route("/submit", methods=["POST"])
def submit():
    return "Data submitted"

@app.route('/', methods=['GET', 'POST'])
def index():

	if request.method == 'POST':
	
		return 'Hello POST!' # curl -X POST http://localhost:5000/
	
	else:
	
		return 'Hello GET!' # curl http://localhost:5000

