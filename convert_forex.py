from flask import Flask
from flask.json import jsonify
from werkzeug.wrappers import request
import pandas as pd
import numpy as np

month_dict = {
    "01": "Jan",
    "02": "Feb",
    "03": "Mar",
    "04": "Apr",
    "05": "May",
    "06": "Jun",
    "07": "Jul",
    "08": "Aug",
    "09": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec"
}

app = Flask(__name__)

@app.route('/curr-convert', methods=['GET'])
def redirect():
    params = dict(request.args)
    src = params.get("src")
    dest = params.get("dest")
    yr, mth, day = params.get("date").split("-")
    amount = params.get("amount")
    date = month_dict[mth] + " " + day + ", " + yr


    try:
        data = pd.read_csv(f"Forex-Data/{src}_{dest}.csv")
        df = pd.DataFrame(data, columns=['Date', 'Open'])
        idx = np.where(df['Date'] == date)



    except Exception:
        return jsonify({"error": "no file found"}), 404

    return jsonify(df.to_dict())

if __name__ == "__main__":
    app.run(debug=True)