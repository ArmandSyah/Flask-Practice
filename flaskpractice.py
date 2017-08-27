from flask import Flask
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user/<name>', methods=['GET'])
def user(name):
    return '<h1> Hello, {}!'.format(name)

if __name__ == '__main__':
    app.run()
