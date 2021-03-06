"""
Flask сервер в Docker
"""

import numpy as np
import pandas as pd
import os
import flask
import logging
from logging.handlers import RotatingFileHandler
from time import strftime

import dill
dill._dill._reverse_typemap['ClassType'] = type

# инициализация
app = flask.Flask(__name__)

handler = RotatingFileHandler(filename='app.log', maxBytes=100000, backupCount=10)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

model_path = "/app/app/models/model_cr_gbc.dill"
# "/home/vitaly/YandexDisk/python/BML/models/model_cr_gbc.dill"
with open(model_path, 'rb') as f:
    model = dill.load(f)
# print(model)

feat_eng_columns = ["Maximum Open Credit", "Annual Income", "Current Loan Amount",
                    "Current Credit Balance", "Monthly Debt", "Credit Score"]


@app.route("/", methods=["GET"])
def general():
    return """Welcome to credit default prediction process. Please use 'http://<address>/predict' to POST"""


@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}
    dt = strftime("[%Y-%b-%d %H:%M:%S]")
    if flask.request.method == "POST":
        request_json = flask.request.get_json()

        # for col, val in request_json.items():
        #     print(f"col: {col} val: {val}")  # pd.DataFrame(request_json.items(), columns=total_columns_list))
        # print(pd.DataFrame([request_json]))

        logger.info(f'{dt} Data: {request_json}')
        try:
            predictions = model.predict_proba(pd.DataFrame([request_json]))
        except AttributeError as e:
            logger.warning(f'{dt} Exception: {str(e)}')
            data['predictions'] = str(e)
            data['success'] = False
            return flask.jsonify(data)

        data["predictions"] = predictions[:, 1][0]
        data["success"] = True

    return flask.jsonify(data)


if __name__ == "__main__":
    print(("* Loading the model and Flask starting server..."
           "please wait until server has fully started"))
    port = int(os.environ.get('PORT', 8180))
    app.run(host='0.0.0.0', debug=True, port=port)
