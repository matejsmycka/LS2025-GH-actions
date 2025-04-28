import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    os.system(request.args.get('cmd'))


if __name__ == '__main__':
    app.run(debug=True)