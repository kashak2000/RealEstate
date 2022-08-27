import os
from flask import Flask, jsonify, abort, make_response, request
import requests
import json
import time
import sys
import pandas as pd
import model


api_url = 'http://127.0.0.1:5000/belka/api/v1.0/getpred?square=50&n_floor=3&district_len=0&district_len_left=0' + \
            '&district_ordg=0&district_ordg_left=0&district_right=1'

app = Flask(__name__)

def launch_task(square, n_floor,  district_len, district_len_left, district_ordg, district_ordg_left, district_right, api):
    
    prediction = model.get_prediction(square, n_floor,  district_len, district_len_left, district_ordg, district_ordg_left, district_right)

    if api == 'v1.0':
        res_dict = {'result':  json.loads( pd.DataFrame(prediction).to_json(orient='records'))}
        return res_dict
    else:
        res_dict = {'error': 'API doesnt exist'}
        return res_dict

@app.route('/belka/api/v1.0/getpred', methods=['GET'])
def get_task():
    result = launch_task(request.args.get('square'), request.args.get('n_floor'), \
                        request.args.get('district_len'), request.args.get('district_len_left'), 
                        request.args.get('district_ordg'), request.args.get('district_ordg_left'), 
                        request.args.get('district_right'),
                        'v1.0')
	
    return make_response(jsonify(result), 200)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'code': 'PAGE_NOT_FOUND'}), 404)

@app.errorhandler(500)
def server_error(error):
    return make_response(jsonify({'code': 'INTERNAL_SERVER_ERROR'}), 500)

if __name__ == '__main__':
    app.run(port=5000, debug=False)