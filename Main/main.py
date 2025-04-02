from flask import Flask

app = Flask(__name__)


@app.route('/main')
def hello():
    return 'Hello, World!'