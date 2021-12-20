#!/usr/bin/env python3

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method != 'POST':
        return "I'm only postable\n", 222

    try:
        data = int(request.form["test"])
    except:
        return "Non integer data passed in request form\n", 501

    if data < 0:
        return "Value is too small\n", 500

    if data > 10:
        return "Value is too large\n", 502

    return "Ok"


if __name__ == "__main__":
    app.run(debug=True)
