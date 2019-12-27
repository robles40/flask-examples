from flask import Flask, make_response, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', title='Welcome to Flask!')


@app.errorhandler(404)
def not_found(e):
    print(e)
    return render_template('404.html'), 404


@app.route('/fail')
def server_error():
    res = make_response(render_template('500.html'), 500)
    return res
