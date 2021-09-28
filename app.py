#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello')  # this route is not working
@app.route('/hello/')
def hello_world():
    return 'Hello Worlds checking restriction after push 928!\n' # hi second push after updating branch protection rule

@app.route('/hello/<username>') # dynamic route
def hello_user(username):
    # show the user profile for that user
    return 'Why Hello onemoretime test %s!\n' % username

if __name__ == '__main__':
    app.run(host='0.0.0.0')  # open for everyone for now
