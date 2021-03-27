#!/usr/bin/python
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/api/v1/type/", methods=['GET','POST','PATCH','DELETE'])
def obj_type():
    if 'GET' == request.method:
        if 'arg0' in request.args:
            result = request.args['arg0']
        elif 'arg1' in request.args:
            result = request.args['arg1']
        else:
            result = "This is a GET request"
        return jsonify(result)
    elif 'POST' == request.method:
        result = request.get_json()
        return jsonify(result)
    elif 'PATCH' == request.method:
        return "this is a PATCH request"
    elif 'DELETE' == request.method:
        return "this is a DELETE request"
    else:
        return "Error"

app.run()
