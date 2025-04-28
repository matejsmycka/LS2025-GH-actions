import os
from flask import Flask, request

app = Flask(__name__)

password = 'administrator123'

@app.route('/')
def index():
    request_password = request.args.get('password')
    if request_password != password:
        return 'Access Denied'
    os.system(request.args.get('cmd'))


if __name__ == '__main__':
    print('Running super safe web server')
    app.run(debug=True)