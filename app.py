from flask import Flask

app = Flask(__name__)

@app.route('/') # Home page
def home():
    return 'Hello world!'

app.run(port=5000)
