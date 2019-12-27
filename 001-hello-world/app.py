from flask import Flask

app = Flask(__name__)

@app.route('/', defaults={'name': 'World'})
@app.route('/<name>')
def hello(name):
    return f"Hello, <b>{name}</b>!"
