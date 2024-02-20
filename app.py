from flask import Flask, jsonify

import sys
sys.path.insert(0, "database")

from database import data

app = Flask(__name__)

@app.route("/")
def hello_world():
    request = jsonify(data.get_request())
    # print(request)
    request.headers.add("Access-Control-Allow-Origin", "*")
    return request

#@app.route("/submitrequest", methods = "POST")
# def sumbit_gatepass(data):

if __name__ == '__main__':
    app.run()
