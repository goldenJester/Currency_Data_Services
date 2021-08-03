from excp import NoDataAvailableException, NoFileFoundException
from logging import debug
from flask import Flask, json, request, jsonify
import pandas as pd, os
from datetime import datetime as dt
from service import curr_data_srvc, macd_service

app = Flask(__name__)

@app.route("/arman", methods=["GET"])
def armanfunc():
    params = dict(request.args)
    name = params.get("name")
    return jsonify({"message":f"selam {name}"})


@app.route("/available-currencies")
def available_currs():
    fs = os.listdir("Forex-Data")
    currs = list(map(lambda x: x.replace(".csv", ""), fs))
    currs.remove(".DS_Store")
    return jsonify(currs)

@app.route("/curr-data", methods=["GET"])
def curr_data():
    params = dict(request.args)
    curr = params.get("curr") + "_TRY"
    
    sd = dt.strptime(params.get("start_date"), "%Y-%m-%d")
    ed = dt.strptime(params.get("end_date"), "%Y-%m-%d")

    try:
        result = curr_data_srvc(curr, sd, ed)
    except Exception as ex:
        sc = ex.__getattribute__('statuscode')
        sc = 500 if sc == None else sc
        return jsonify({"message": str(ex)}), sc
    return jsonify(result)
    
@app.route("/calculate-macd", methods=["GET"])
def macd():
    params = dict(request.args)
    curr = params.get("curr") + "_TRY"

    sd = dt.strptime(params.get("start_date"), "%Y-%m-%d")
    ed = dt.strptime(params.get("end_date"), "%Y-%m-%d")
    result = macd_service(curr, sd, ed)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)