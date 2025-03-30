from flask import Flask

app = Flask(__name__)



@app.route('/')
def hello():
    return 'Hello World! IS4151/IS5451'

# use localhost:5000

# how to run? -> python3 -m flask --app src01 run

